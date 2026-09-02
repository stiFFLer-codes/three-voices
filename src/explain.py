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

Four cases, each chosen by a stated CRITERION (not a hardcoded index — the
criterion is what reproduces; the row it resolves to will move if the data
or model changes). See ``select_cases`` for the full definitions.
  * confident_low   — highest P(low risk)
  * confident_high  — highest P(high risk)
  * boundary_mid    — true-mid, smallest top-2 margin, #1 SHAP driver is
                      BS or SystolicBP. The paper's central teaching case.
                      Resolves to row 66 on the current clean set.
  * failure_mode    — true-low but predicted-high, smallest top-2 margin.
                      The "confidently wrong" case for the Limitations
                      section, not the main figures. Resolves to row 382.

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
from src.model import CLASS_NAMES, FEATURES, prepare_modeling_frame, _model_factories

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
        rather than an outlier feature (e.g. a lone BodyTemp spike). On the
        current clean set this resolves to row 66 — true mid, sitting on the
        mid<->high boundary (0.487 / 0.499), BS-led. The CRITERION is what
        is reproducible; the index moves if the data or model changes.

    failure_mode  (Limitations section, not the main figures)
        Among rows whose true label is low risk but whose predicted label is
        high risk, the one with the smallest top-2 margin — the narrowest
        call on which the model flipped a genuinely low-risk mother all the
        way to high risk. On the current clean set this resolves to row 382
        (true low, predicted high at 0.451 / 0.453; a BodyTemp 101F reading
        in a 13-year-old drives the flip).

        On that age: the dataset contains very low maternal ages, reflecting
        adolescent pregnancy in the source population (rural Bangladesh). We
        retain rather than filter those rows — excluding a group the system
        would encounter is itself a harm — and this case shows the model
        over-weighting a demographic feature, which is precisely why final
        judgment stays with a human. All data is public (UCI Maternal Health
        Risk); no real patient or child record is exposed. Decision Log #20
        carries the wording the manuscript uses.
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

    model = fit_final_model(X, y)
    proba = model.predict_proba(X)
    pred = proba.argmax(axis=1)

    print("Phase 2 — SHAP engine")
    print("=" * 60)
    print(f"final model: {FINAL_MODEL_NAME} / none   (n={len(X)})")

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

    # ----- LOCAL: three representative cases --------------------------------
    cases = select_cases(proba, pred, y, values)
    summary_rows = []
    contrib_rows = []
    for tag, i in cases.items():
        c = int(pred[i])
        summary_rows.append(
            {
                "case": tag,
                "row_index": i,
                "true": CLASS_NAMES[int(y.iloc[i])],
                "predicted": CLASS_NAMES[c],
                "p_low": float(proba[i, 0]),
                "p_mid": float(proba[i, 1]),
                "p_high": float(proba[i, 2]),
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
                }
            )

        # local waterfall for the predicted class
        plt.figure()
        shap.plots.waterfall(expl[i, :, c], show=False)
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
