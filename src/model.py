"""Phase 1 — the model vehicle.

Trains Logistic Regression / Random Forest / XGBoost on the UCI Maternal
Health Risk dataset and reports honest, leak-free cross-validated metrics.

The model is a VEHICLE for the three-tier explanation architecture, not the
contribution. We do NOT tune for accuracy; we establish a clean baseline.

Leakage discipline (the thing reviewers check first)
----------------------------------------------------
* Fixed-rule cleaning that learns NO statistics from the data — dropping exact
  duplicate rows and physiologically impossible HeartRate values — happens
  ONCE, before any split. It cannot leak: it uses neither the label/feature
  relationship nor the held-out fold.
* Everything that LEARNS from the data — SMOTE oversampling and feature
  scaling — is fit INSIDE each training fold only, via an imblearn Pipeline,
  and never sees the validation fold.

Why dedup BEFORE the split, not after
-------------------------------------
55% of rows are exact duplicates. If copies of one row sit in both train and
test, the model is scored on rows it memorised and every metric inflates —
macro-recall included. Removing duplicates up front guarantees no identical
row can straddle the split. (The alternative — keep duplicates but force all
copies into the same fold with group-aware CV — preserves the raw
distribution but adds complexity a vehicle model does not need.)

Run:
    python -m src.model
"""
from __future__ import annotations

import sys

import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler

from src import config
from src.data import load_dataset

try:
    from xgboost import XGBClassifier
    _HAS_XGB = True
except ImportError:  # pragma: no cover
    _HAS_XGB = False

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SEED = config.RANDOM_SEED
N_SPLITS = 5
MIN_PLAUSIBLE_HR = 20  # bpm; anything below is a data-entry error
FEATURES = config.FEATURE_COLUMNS
TARGET = config.TARGET_COLUMN
CLASSES = [0, 1, 2]  # low, mid, high
CLASS_NAMES = [config.INT_TO_RISK[i] for i in CLASSES]

# Final model for the paper + the saved artifact. RF tied RF/SMOTE on
# macro-recall (0.580) with tighter variance and the best high-risk recall,
# and SMOTE bought nothing measurable at this imbalance. Hardcoded on purpose
# — not a 4th-decimal argmax tie-break.
FINAL_MODEL = ("random_forest", False)  # (name, use_smote)


# ---------------------------------------------------------------------------
# Data preparation  (fixed-rule, pre-split — leak-safe by construction)
# ---------------------------------------------------------------------------
def prepare_modeling_frame(X: pd.DataFrame, y: pd.Series, dedup: bool = True):
    """Return (X_clean, y_clean, report) after fixed-rule cleaning.

    Steps, in order, each recorded in ``report``:
      1. drop physiologically impossible HeartRate (< 20 bpm)
      2. drop exact duplicate rows (identical across ALL columns incl. label)

    Also reports how many distinct feature vectors survive with MORE THAN ONE
    label (irreducible ambiguity — kept, not "fixed").
    """
    df = X.copy()
    df[TARGET] = y.to_numpy()
    report: dict = {"n_start": int(len(df))}

    # 1) impossible HeartRate
    hr_bad = int((df["HeartRate"] < MIN_PLAUSIBLE_HR).sum())
    df = df[df["HeartRate"] >= MIN_PLAUSIBLE_HR].copy()
    report["dropped_impossible_heartrate"] = hr_bad

    # 2) exact duplicate rows (dedup=False only for the leakage check below)
    n_before_dedup = len(df)
    if dedup:
        df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    report["dropped_exact_duplicates"] = int(n_before_dedup - len(df))

    # diagnostic: same features, conflicting label (kept — genuine ambiguity)
    label_counts = df.groupby(FEATURES, sort=False)[TARGET].nunique()
    report["conflicting_label_feature_vectors"] = int((label_counts > 1).sum())

    report["n_clean"] = int(len(df))
    report["class_distribution_clean"] = {
        config.INT_TO_RISK[k]: int(v)
        for k, v in df[TARGET].value_counts().sort_index().items()
    }

    # Cohort composition. Reported because the manuscript cites these counts:
    # adolescent rows are RETAINED, not filtered (Decision Log #20), so the
    # reader needs the number to check the claim rather than take it on trust.
    report["age_min"] = int(df["Age"].min())
    report["age_max"] = int(df["Age"].max())
    report["n_age_under_18"] = int((df["Age"] < 18).sum())

    X_clean = df[FEATURES].reset_index(drop=True)
    y_clean = df[TARGET].reset_index(drop=True)
    return X_clean, y_clean, report


# ---------------------------------------------------------------------------
# Model factories  (modest, sensible defaults — NO accuracy chasing)
# ---------------------------------------------------------------------------
def _model_factories() -> dict:
    factories = {
        "logreg": {
            "needs_scaling": True,
            "make": lambda: LogisticRegression(max_iter=2000, random_state=SEED),
        },
        "random_forest": {
            "needs_scaling": False,
            "make": lambda: RandomForestClassifier(
                n_estimators=300, random_state=SEED, n_jobs=-1
            ),
        },
    }
    if _HAS_XGB:
        factories["xgboost"] = {
            "needs_scaling": False,
            "make": lambda: XGBClassifier(
                n_estimators=300,
                max_depth=4,
                learning_rate=0.1,
                subsample=0.9,
                colsample_bytree=0.9,
                objective="multi:softprob",
                num_class=3,
                tree_method="hist",
                eval_metric="mlogloss",
                random_state=SEED,
                n_jobs=-1,
            ),
        }
    return factories


def _build_pipeline(spec: dict, use_smote: bool) -> ImbPipeline:
    steps = []
    if spec["needs_scaling"]:
        steps.append(("scale", StandardScaler()))
    if use_smote:
        steps.append(("smote", SMOTE(random_state=SEED)))
    steps.append(("clf", spec["make"]()))
    return ImbPipeline(steps)


# ---------------------------------------------------------------------------
# Cross-validated evaluation
# ---------------------------------------------------------------------------
def evaluate(spec: dict, X: pd.DataFrame, y: pd.Series, use_smote: bool):
    """Stratified k-fold. Returns (metrics dict of mean/std, summed CM)."""
    skf = StratifiedKFold(n_splits=N_SPLITS, shuffle=True, random_state=SEED)
    rows = {"macro_recall": [], "macro_f1": [], "accuracy": [], "roc_auc_ovr": []}
    per_class_recall = []
    cm_total = np.zeros((3, 3), dtype=int)

    for tr, te in skf.split(X, y):
        X_tr, X_te = X.iloc[tr], X.iloc[te]
        y_tr, y_te = y.iloc[tr], y.iloc[te]

        pipe = _build_pipeline(spec, use_smote)
        pipe.fit(X_tr, y_tr)
        pred = pipe.predict(X_te)
        proba = pipe.predict_proba(X_te)

        rows["macro_recall"].append(recall_score(y_te, pred, average="macro"))
        rows["macro_f1"].append(f1_score(y_te, pred, average="macro"))
        rows["accuracy"].append(accuracy_score(y_te, pred))
        rows["roc_auc_ovr"].append(
            roc_auc_score(y_te, proba, multi_class="ovr", average="macro", labels=CLASSES)
        )
        per_class_recall.append(
            recall_score(y_te, pred, average=None, labels=CLASSES)
        )
        cm_total += confusion_matrix(y_te, pred, labels=CLASSES)

    metrics = {k: (float(np.mean(v)), float(np.std(v))) for k, v in rows.items()}
    pcr = np.array(per_class_recall)
    metrics["recall_per_class"] = {
        CLASS_NAMES[i]: (float(pcr[:, i].mean()), float(pcr[:, i].std()))
        for i in range(3)
    }
    return metrics, cm_total


# ---------------------------------------------------------------------------
# Reporting helpers
# ---------------------------------------------------------------------------
def _fmt(mean_std) -> str:
    m, s = mean_std
    return f"{m:.3f}±{s:.3f}"


def run() -> pd.DataFrame:
    config.set_seeds()
    X_raw, y_raw = load_dataset()
    X, y, prep = prepare_modeling_frame(X_raw, y_raw)

    print("Phase 1 — model vehicle")
    print("=" * 60)
    print("Data preparation (fixed-rule, pre-split):")
    for k, v in prep.items():
        print(f"  {k}: {v}")
    print("=" * 60)

    # Persist the preparation report so every cohort number the manuscript
    # quotes has a committed file behind it, not just stdout.
    config.TABLES_DIR.mkdir(parents=True, exist_ok=True)
    cohort_rows = []
    for k, v in prep.items():
        if isinstance(v, dict):
            cohort_rows += [{"field": f"{k}.{ik}", "value": iv} for ik, iv in v.items()]
        else:
            cohort_rows.append({"field": k, "value": v})
    cohort_csv = config.TABLES_DIR / "p1_cohort_summary.csv"
    pd.DataFrame(cohort_rows).to_csv(cohort_csv, index=False)
    print(f"cohort summary -> {cohort_csv}")

    factories = _model_factories()
    if not _HAS_XGB:
        print("  [warn] xgboost not installed — skipping that model.\n")

    records = []
    cms = {}  # (name, use_smote) -> summed confusion matrix
    best = None  # (macro_recall_mean, name, resample, spec, use_smote)
    for name, spec in factories.items():
        for use_smote in (False, True):
            metrics, cm = evaluate(spec, X, y, use_smote)
            tag = "SMOTE" if use_smote else "none"
            cms[(name, use_smote)] = cm
            mr_mean = metrics["macro_recall"][0]
            records.append(
                {
                    "model": name,
                    "resample": tag,
                    "macro_recall": _fmt(metrics["macro_recall"]),
                    "macro_f1": _fmt(metrics["macro_f1"]),
                    "accuracy": _fmt(metrics["accuracy"]),
                    "roc_auc_ovr": _fmt(metrics["roc_auc_ovr"]),
                    "recall_low": _fmt(metrics["recall_per_class"][CLASS_NAMES[0]]),
                    "recall_mid": _fmt(metrics["recall_per_class"][CLASS_NAMES[1]]),
                    "recall_high": _fmt(metrics["recall_per_class"][CLASS_NAMES[2]]),
                }
            )
            if best is None or mr_mean > best[0]:
                best = (mr_mean, name, tag, spec, use_smote, cm)

    table = pd.DataFrame.from_records(records)
    config.TABLES_DIR.mkdir(parents=True, exist_ok=True)
    out_csv = config.TABLES_DIR / "p1_model_metrics.csv"
    table.to_csv(out_csv, index=False)

    print("Cross-validated metrics (mean±std over %d folds):" % N_SPLITS)
    print(table.to_string(index=False))
    print("-" * 60)
    print(f"metrics table -> {out_csv}")

    # ----- report the argmax winner (transparency), then refit + save the
    #       deliberately hardcoded final model (see FINAL_MODEL) --------------
    _, arg_name, arg_tag, _, _, _ = best
    print(f"\nArgmax macro-recall winner: {arg_name} / {arg_tag}")

    final_name, final_smote = FINAL_MODEL
    final_tag = "SMOTE" if final_smote else "none"
    final_cm = cms[(final_name, final_smote)]
    print(f"Final model (hardcoded for the paper): {final_name} / {final_tag}")
    print("Summed confusion matrix (rows=true, cols=pred; order low/mid/high):")
    print(pd.DataFrame(final_cm, index=CLASS_NAMES, columns=CLASS_NAMES).to_string())

    final = _build_pipeline(factories[final_name], final_smote)
    final.fit(X, y)
    config.MODELS_DIR.mkdir(parents=True, exist_ok=True)
    model_path = config.MODELS_DIR / "model.joblib"
    try:
        import joblib

        joblib.dump(
            {"pipeline": final, "features": FEATURES, "classes": CLASS_NAMES,
             "selection": {"model": final_name, "resample": final_tag}},
            model_path,
        )
        print(f"\nsaved model -> {model_path}")
    except ImportError:  # pragma: no cover
        print("\n[warn] joblib not available — model not saved.")

    duplicate_leakage_check()

    print("OK")
    return table


def duplicate_leakage_check() -> pd.DataFrame:
    """Score FINAL_MODEL twice: duplicates dropped vs. kept.

    55% of the raw rows are exact duplicates. Keeping them lets identical rows
    land in both the train and test fold of the same split, so the classifier
    is scored partly on rows it memorised. This quantifies that inflation and
    is the reason our headline numbers sit below the published 83-88%.
    """
    config.set_seeds()
    X_raw, y_raw = load_dataset()
    spec = _model_factories()[FINAL_MODEL[0]]

    records = []
    for dedup in (True, False):
        X, y, prep = prepare_modeling_frame(X_raw, y_raw, dedup=dedup)
        metrics, _ = evaluate(spec, X, y, FINAL_MODEL[1])
        records.append({
            "duplicates": "dropped" if dedup else "kept",
            "n_rows": prep["n_clean"],
            "macro_recall": _fmt(metrics["macro_recall"]),
            "macro_f1": _fmt(metrics["macro_f1"]),
            "accuracy": _fmt(metrics["accuracy"]),
            "recall_high": _fmt(metrics["recall_per_class"][CLASS_NAMES[2]]),
        })

    table = pd.DataFrame.from_records(records)
    out_csv = config.TABLES_DIR / "p1_duplicate_leakage.csv"
    table.to_csv(out_csv, index=False)
    tag = "SMOTE" if FINAL_MODEL[1] else "none"
    print()
    print(f"Duplicate-leakage check ({FINAL_MODEL[0]} / {tag}):")
    print(table.to_string(index=False))
    print(f"leakage table -> {out_csv}")
    return table


if __name__ == "__main__":
    run()
    sys.exit(0)
