"""Phase 2 — the SHAP engine.

Explains the Phase-1 model vehicle. The final model is **Random Forest with NO
resampling (RF/none)**: at P1 it tied RF/SMOTE on macro-recall (0.580) with
tighter variance and the best high-risk recall, and SMOTE bought nothing
measurable at this imbalance. We hardcode that deliberate pick here rather than
trust a 4th-decimal argmax.

Everything below is reproducible and saved as DATA so Phase 3's three tiers can
consume it without re-running SHAP:

  results/tables/shap_global_mean_abs.csv   global mean |SHAP| per feature/class
  results/tables/shap_case_summary.csv      per-case prediction + probabilities
  results/tables/shap_case_contributions.csv  per-feature SHAP for each case
  results/figures/shap_global_high.png      global beeswarm, high-risk class
  results/figures/shap_case_<tag>.png       local waterfall per case

Global SHAP is the FINAL model fitted on all 451 rows. The four cases are
scored OUT OF FOLD (Decision Log #61): probabilities and local SHAP come from
the fold model that held the row out (``src.model.out_of_fold``), and the
criteria below pick the cases from those scores. Each criterion is what
reproduces; the rows it resolves to are recorded in STATE.md (#62) and move
if the data or model changes. See ``select_cases`` for the full definitions.
  * confident_low   — highest P(low risk)
  * confident_high  — highest P(high risk)
  * boundary_mid    — true-mid, smallest top-2 margin, #1 SHAP driver is
                      BS or SystolicBP. The paper's central teaching case.
  * failure_mode    — true-low but predicted-high, smallest top-2 margin.

Run:
    python -m src.explain
"""
from __future__ import annotations

import json
import sys

import matplotlib

matplotlib.use("Agg")  # headless, deterministic figure output
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap

from src import config
from src.data import load_dataset
from src.model import (
    CLASS_NAMES,
    FEATURES,
    _model_factories,
    out_of_fold,
    prepare_modeling_frame,
)

# The deliberate P1 pick (documented above). RF/none => no scaler, no SMOTE,
# so SHAP runs directly on the six raw clinical features. That is exactly what
# the three tiers want: contributions in interpretable feature units.
FINAL_MODEL_NAME = "random_forest"


def fit_final_model(X: pd.DataFrame, y: pd.Series):
    """Fit RF/none on the full clean set (mirrors src.model's final fit)."""
    clf = _model_factories()[FINAL_MODEL_NAME]["make"]()
    clf.fit(X, y)
    return clf


def select_cases(
    proba: np.ndarray, pred: np.ndarray, y: pd.Series, values: np.ndarray
) -> dict:
    """Return {tag: row_index}, each resolved from a defensible criterion.

    confident_low / confident_high
        Unchanged: the rows with the highest P(low risk) / P(high risk).

    boundary_mid  (the paper's central teaching case)
        Among rows whose TRUE label is mid risk, the one with the smallest
        top-2 predicted-probability margin whose #1 SHAP driver (by |value|)
        for the predicted class is BS or SystolicBP. This isolates a case
        where the ground truth is the hard middle class, the model is
        genuinely on the fence, AND the reason is a core clinical driver
        rather than an outlier feature (e.g. a lone BodyTemp spike). The
        CRITERION is what is reproducible; the index moves if the data or
        model changes.

    failure_mode
        Among rows whose true label is low risk but whose predicted label is
        high risk, the one with the smallest top-2 margin — the narrowest
        call on which the model flipped a genuinely low-risk mother all the
        way to high risk.

    ``proba``, ``pred`` and ``values`` are whatever scoring the caller
    passes; since #61 run() passes out-of-fold scores.
    """
    p_sorted = np.sort(proba, axis=1)
    margin = p_sorted[:, -1] - p_sorted[:, -2]
    y_arr = y.to_numpy()

    def top_driver(i: int) -> str:
        c = int(pred[i])
        return FEATURES[int(np.argmax(np.abs(values[i, :, c])))]

    mid_core = [
        i for i in np.where(y_arr == 1)[0]
        if top_driver(int(i)) in ("BS", "SystolicBP")
    ]
    lo_to_hi = np.where((y_arr == 0) & (pred == 2))[0]

    return {
        "confident_low": int(np.argmax(proba[:, 0])),
        "confident_high": int(np.argmax(proba[:, 2])),
        "boundary_mid": int(min(mid_core, key=lambda i: margin[i])),
        "failure_mode": int(min(lo_to_hi, key=lambda i: margin[i])),
    }


def run() -> None:
    config.set_seeds()
    X_raw, y_raw = load_dataset()
    X, y, _ = prepare_modeling_frame(X_raw, y_raw)

    # Global SHAP only: the final model fitted on all 451 rows. The cases are
    # NOT scored with it — see the out-of-fold block below (Decision Log #61).
    model = fit_final_model(X, y)

    print("Phase 2 — SHAP engine")
    print("=" * 60)
    print(f"global SHAP: final model {FINAL_MODEL_NAME} / none, fitted on all {len(X)} rows")
    print("cases: scored out of fold, by the fold model that held each row out")

    # ----- SHAP values (Explanation shape: n_samples x n_features x n_classes)
    explainer = shap.TreeExplainer(model)
    expl = explainer(X)
    values = expl.values  # (n, feat, classes)

    config.FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    config.TABLES_DIR.mkdir(parents=True, exist_ok=True)

    # ----- GLOBAL: mean |SHAP| per feature per class ------------------------
    mean_abs = np.abs(values).mean(axis=0)  # (feat, classes)
    global_tbl = pd.DataFrame(mean_abs, index=FEATURES, columns=CLASS_NAMES)
    global_tbl.index.name = "feature"
    global_csv = config.TABLES_DIR / "shap_global_mean_abs.csv"
    global_tbl.to_csv(global_csv)
    print("-" * 60)
    print("Global mean |SHAP| (per feature, per class):")
    print(global_tbl.round(4).to_string())

    # global beeswarm for the clinically salient class (high risk = index 2)
    plt.figure()
    shap.plots.beeswarm(expl[:, :, 2], show=False)
    plt.title("Global SHAP — high-risk class")
    fig_global = config.FIGURES_DIR / "shap_global_high.png"
    plt.savefig(fig_global, dpi=150, bbox_inches="tight")
    plt.close()

    # ----- LOCAL: four cases, scored OUT OF FOLD (Decision Log #61) ---------
    # Probabilities and SHAP come from the fold model that held each row out,
    # through the same helper src.model uses for p1_oof_predictions.csv.
    oof = out_of_fold(X, y)
    proba, values = oof["proba"], oof["values"]
    pred = proba.argmax(axis=1)
    cases = select_cases(proba, pred, y, values)

    # Fail loudly if a case is not scored exactly as p1_oof_predictions.csv
    # scores the same row (round_trip: compare the floats the CSV holds).
    committed = pd.read_csv(config.TABLES_DIR / "p1_oof_predictions.csv",
                            float_precision="round_trip").set_index("row_index")
    for tag, i in cases.items():
        assert (committed.loc[i, ["p_low", "p_mid", "p_high"]].to_numpy(float)
                == proba[i]).all(), (
            f"{tag} (row {i}) does not match p1_oof_predictions.csv — rerun "
            "python -m src.model, or find what diverged (Decision Log #61)")

    summary_rows = []
    contrib_rows = []
    for tag, i in cases.items():
        c = int(pred[i])
        fold = int(oof["fold"][i])
        summary_rows.append(
            {
                "case": tag,
                "row_index": i,
                "true": CLASS_NAMES[int(y.iloc[i])],
                "predicted": CLASS_NAMES[c],
                "p_low": float(proba[i, 0]),
                "p_mid": float(proba[i, 1]),
                "p_high": float(proba[i, 2]),
                "scoring": "out_of_fold",
                "fold": fold,
            }
        )
        for f_idx, feat in enumerate(FEATURES):
            contrib_rows.append(
                {
                    "case": tag,
                    "feature": feat,
                    "feature_value": float(X.iloc[i, f_idx]),
                    "shap_pred_class": float(values[i, f_idx, c]),
                    "pred_class": CLASS_NAMES[c],
                    "scoring": "out_of_fold",
                    "fold": fold,
                }
            )

        # local waterfall for the predicted class, from the same fold model
        plt.figure()
        shap.plots.waterfall(shap.Explanation(
            values=values[i, :, c], base_values=oof["base"][i, c],
            data=X.iloc[i].to_numpy(), feature_names=FEATURES,
        ), show=False)
        plt.title(f"{tag} — pred {CLASS_NAMES[c]}")
        fig_case = config.FIGURES_DIR / f"shap_case_{tag}.png"
        plt.savefig(fig_case, dpi=150, bbox_inches="tight")
        plt.close()

    summary = pd.DataFrame(summary_rows)
    contrib = pd.DataFrame(contrib_rows)
    summary_csv = config.TABLES_DIR / "shap_case_summary.csv"
    contrib_csv = config.TABLES_DIR / "shap_case_contributions.csv"
    summary.to_csv(summary_csv, index=False)
    contrib.to_csv(contrib_csv, index=False)

    print("-" * 60)
    print("Representative cases:")
    print(summary.round(3).to_string(index=False))
    print("-" * 60)
    print("Saved:")
    for p in (global_csv, summary_csv, contrib_csv, fig_global):
        print(f"  {p}")
    for tag in cases:
        print(f"  {config.FIGURES_DIR / f'shap_case_{tag}.png'}")
    print("OK")


if __name__ == "__main__":
    run()
    sys.exit(0)
