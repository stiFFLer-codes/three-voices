# STATE.md — project state & handoff

Read this at the start of every session. Update it at the end (phase, status,
next step) and **append** to the Decision Log — never edit or delete an
existing entry; supersede it with a new dated one.

_Last updated: 2026-09-02_

## Current phase

**P2 complete. Next: P3 (three-tier renderer).**

## Status by phase

- **P0 — reproducibility spine — DONE.** `python -m src.data` pulls, caches
  (`data/raw/maternal_health_risk.csv`, gitignored), reports, byte-identical
  across runs.
- **P1 — model vehicle — DONE.** `python -m src.model`: LR / RF / XGBoost,
  5-fold stratified CV, SMOTE + scaling in-fold via imblearn Pipeline.
  Metrics table at `results/tables/p1_model_metrics.csv`. Final model
  hardcoded (see Decision Log 2026-09-02 #3), saved to `models/model.joblib`
  (gitignored — regenerate with the script).
- **P2 — SHAP engine — DONE.** `python -m src.explain`: global mean|SHAP|
  per feature/class + four criterion-selected cases, values saved as data,
  five figures. Tables in `results/tables/shap_*.csv`, figures in
  `results/figures/shap_*.png`.
- **P3 — three-tier renderer — NOT STARTED.**
- P4 heuristic eval, P5 manuscript, P6 cold-run/submit — not started.

## Key data facts (UCI Maternal Health Risk, id=863)

- Raw: 1014 rows, 6 features, 3 classes. 562 exact-duplicate rows, 2
  impossible HeartRate (<20 bpm).
- Clean modelling set (drop impossible HR, then exact dedup): **n = 451** —
  low 233 / mid 106 / high 112. Imbalance ~2.2:1 (low:mid).
- **35 conflicting-label feature vectors** in the clean set: identical
  6-feature rows with >1 risk label. Irreducible ambiguity — kept, not
  "fixed". This is the Limitations-section number.

## Model

- **Final: Random Forest, no resampling (RF/none).** `n_estimators=300`,
  `random_state=42`. No scaler, no SMOTE — SHAP runs on the six raw clinical
  features in interpretable units.
- CV macro-recall 0.580±0.027; high-risk recall 0.723; summed CM high row
  [14, 17, 81] (true-high → pred low / mid / high).
- Argmax over macro-recall tied RF/SMOTE; RF/none chosen deliberately for
  tighter variance + best high-risk recall + no SMOTE dependence.

## SHAP results

- **Top global drivers:** BS (blood sugar) #1 for every class (high-risk
  mean|SHAP| 0.156), SystolicBP #2 (0.087). DiastolicBP is near-noise
  (~0.035, tied with HeartRate); BodyTemp mid-pack. Paper language: "BS and
  systolic BP", not "the BP features".
- **Four cases** (`src/explain.py::select_cases` — criteria reproduce, row
  indices will move if data/model change):
  - `confident_low` — highest P(low). Row 196.
  - `confident_high` — highest P(high). Row 16.
  - `boundary_mid` — true-mid, smallest top-2 margin whose #1 predicted-class
    SHAP driver is BS or SystolicBP. **Row 66** (mid↔high boundary
    0.487/0.499, BS +0.204 drives it). The paper's central teaching case.
  - `failure_mode` — true-low but predicted-high, smallest top-2 margin.
    **Row 382** (0.451/0.453; BodyTemp 101°F in a 13-year-old drives the
    flip; BS and SystolicBP argue against high). For the Limitations
    section, not the main figures.

## Artifacts on disk

- `results/tables/`: `p1_model_metrics.csv`, `shap_global_mean_abs.csv`,
  `shap_case_summary.csv` (4 rows), `shap_case_contributions.csv`.
- `results/figures/`: `shap_global_high.png`, `shap_case_confident_low.png`,
  `shap_case_confident_high.png`, `shap_case_boundary_mid.png`,
  `shap_case_failure_mode.png`.
- `models/model.joblib` — gitignored; `{pipeline, features, classes,
  selection}`.

## Next step — P3

One case → clinician dashboard PNG + ASHA plain-language card + Hindi MP3 +
mother-to-be visual. Consume the saved P2 data (`shap_case_*.csv`), do not
re-run SHAP. ASHA layer is deterministic template-over-SHAP — no LLM at
inference. Likely start with `boundary_mid` (row 66) as the worked example.

## Decision Log (append-only)

- **2026-09-02 #1 — Dedup before the split.** 55% of raw rows are exact
  duplicates. Drop them (and impossible HeartRate) once, pre-split, as a
  fixed rule that learns no statistics. Rejected: keep dupes + group-aware
  CV (adds complexity a vehicle model doesn't need). Consequence: n 1014 →
  451, imbalance shifts to ~2.2:1.
- **2026-09-02 #2 — Primary metric is macro-recall.** With macro-F1,
  per-class recall, ROC-AUC (OvR), and the confusion matrix as support.
  Rationale: missing a high-risk mother dominates the cost; headline
  accuracy is misleading on imbalanced risk data.
- **2026-09-02 #3 — Final model hardcoded to RF/none.** Argmax macro-recall
  tied RF/none and RF/SMOTE at 0.580. Picked RF/none: tighter variance
  (±0.027 vs ±0.040), best high-risk recall (0.723), no SMOTE dependence,
  SHAP on raw features. `FINAL_MODEL` constant in `src/model.py`;
  `src/model.py` still prints the argmax winner for transparency.
- **2026-09-02 #4 — SHAP cases chosen by criterion, not index.**
  `boundary_mid` and `failure_mode` are defined by stated rules (see above).
  The rule is what reproduces; the resolved row index is a current-data
  fact and may move.
- **2026-09-02 #5 — AI commit attribution disabled repo-wide.** No
  Co-Authored-By / "Generated with Claude Code" / Claude-Session trailers.
  Enforced three ways: `.claude/settings.json`, CLAUDE.md non-negotiable #7,
  `.git/hooks/commit-msg` (local, untracked — re-add on fresh clones).
