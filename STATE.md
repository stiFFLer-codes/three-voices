# STATE.md — project state & handoff

Read this at the start of every session. Update it at the end (phase, status,
next step) and **append** to the Decision Log — never edit or delete an
existing entry; supersede it with a new dated one.

_Last updated: 2026-09-02_

## Current phase

**P4 done (and fed back into P3); P5 next (manuscript).**

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
- **P3 — three-tier renderer — DONE, then revised by P4.** `python -m
  src.render [--case <tag>|all]` (default `boundary_mid`). Reads the saved P2
  CSVs — does NOT re-run SHAP. Renders all four cases across three tiers; see
  "Artifacts on disk". Five defects found by P4 are fixed in it (Decision Log
  #11). Re-run verified 2026-09-02: all PNG and TXT outputs are
  byte-identical; the gTTS MP3s are NOT (same length, different bytes — see
  Decision Log #10).
- **P4 — heuristic evaluation — DONE.** `python -m src.evaluate`: 16 criteria
  (WCAG 2.1 POUR + Nielsen) x 3 tiers = 48 cells, authored as data, each cell
  grounded in a named artifact detail. Contrast ratios are computed at run
  time from the palette in `src/render.py`. Outputs
  `results/tables/heuristic_matrix.csv` and `heuristic_evaluation.md`.
  Standing result after the P3 fixes: **28 Pass / 13 Partial / 1 Fail /
  6 Deferred**; the one Fail is clinician 1.4.5 (images of text), the six
  Deferred are operability + robustness, which a static artifact cannot
  exercise. No human subjects.
- P5 manuscript, P6 cold-run/submit — not started.

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
- **P4:** `results/tables/heuristic_matrix.csv` (48 rows, criterion x tier)
  and `results/tables/heuristic_evaluation.md` (matrix, cell-by-cell
  findings, defects-corrected list, inherent limitations, synthesis, and the
  verbatim method-and-limitations note).
- `results/figures/`: `shap_global_high.png`, `shap_case_confident_low.png`,
  `shap_case_confident_high.png`, `shap_case_boundary_mid.png`,
  `shap_case_failure_mode.png`.
- `models/model.joblib` — gitignored; `{pipeline, features, classes,
  selection}`.
- **P3, per case tag** `<c>` ∈ {boundary_mid, confident_low, confident_high,
  failure_mode}:
  - `results/figures/tier_clinician_<c>.png` — SHAP waterfall + probability
    bar + raw feature table.
  - `results/figures/tier_asha_<c>.png` + `results/tables/tier_asha_<c>.txt`.
  - `results/figures/tier_mother_<c>.png` (traffic light),
    `results/tables/tier_mother_<c>_hi.txt`,
    `results/audio/tier_mother_<c>_hi.mp3`.

## P3 mother-tier bands (as rendered)

| case | predicted | top-2 margin | band |
|---|---|---|---|
| confident_low | low | 1.000 | GREEN |
| confident_high | high | 1.000 | RED |
| boundary_mid | high | 0.012 | AMBER |
| failure_mode | high | 0.002 | AMBER |

Since Decision Log #11 the SAME band also drives the ASHA card header —
GREEN → "LOW — routine care", AMBER → "ELEVATED — needs follow-up",
RED → "HIGH — needs follow-up".

## Next step — P5

Manuscript. The three sections P4 hands it, ready to use:

- **Evaluation section** — the matrix and synthesis in
  `results/tables/heuristic_evaluation.md`. Frame it as formative and
  single-evaluator, in the words of the verbatim method note in that file.
- **Limitations** — the five inherent gaps in that file's "Inherent
  limitations" section (mother-tier colour reliance, no rendered text
  alternative for a deaf reader, clinician chart/English literacy, images of
  text, ASHA tier English-only), plus the 35 conflicting-label rows, the
  0.15 RED threshold as a stated design choice, and Decision Log #10 on gTTS
  reproducibility.
- **The design-process argument** — five defects were found by reading the
  artifacts as their users, not from any model metric, and were fixed; the
  "Defects found and corrected" section is the evidence.

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
- **2026-09-02 #6 — Mother tier caps at an ACTION, never a number.** Tier 3
  shows a three-lamp traffic light and speaks one templated Hindi sentence.
  No probability, no percentage, no disease name, no text required to read
  it. The tier's job is "what do I do next", not "how likely is X".
- **2026-09-02 #7 — Uncertainty-aware AMBER down-ranking.** Band rule:
  GREEN if predicted low; RED only if predicted high AND top-2 probability
  margin ≥ 0.15; AMBER otherwise. A knife-edge call must not reach a mother
  as a red alarm. Consequence: `boundary_mid` (margin 0.012) and
  `failure_mode` (margin 0.002) both light AMBER, not RED — the model's
  own uncertainty is rendered as caution rather than alarm. The 0.15
  threshold is a stated design choice, not an empirical one.
- **2026-09-02 #8 — ASHA card uses LOCAL drivers, not global ones.** Top-2
  features by |SHAP| for THIS case's predicted class, through a fixed
  feature→phrase map, with "raised"/"low" from the reading vs. the dataset
  median. Rejected: naming the global top-2 (BS, SystolicBP) on every card —
  it would be constant text, explaining nothing about the individual.
  The next-step sentence is deliberately generic (no medical timeframe).
- **2026-09-02 #9 — `src/render.py` reads CSVs, not the model.** Everything
  the three tiers need (probabilities, per-feature SHAP, raw values) is
  already in the P2 tables; the waterfall's base value is recovered as
  `p_pred − Σ SHAP` (TreeExplainer is additive in probability space). So P3
  loads no `model.joblib` — one less artifact to keep in sync. The clean
  frame is still loaded, but only for the six feature medians.
- **2026-09-02 #10 — gTTS output is not byte-reproducible.** A clean re-run
  of `python -m src.render` regenerates every PNG and TXT byte-identically,
  but `tier_mother_*_hi.mp3` comes back the same length with different
  bytes: gTTS is a remote service, so the audio is outside our seed control.
  Consequence: the tracked MP3s dirty the working tree on every re-run. They
  stay tracked — a reader without network still gets the artifact, and the
  Hindi source string in `results/tables/tier_mother_*_hi.txt` IS
  deterministic and is the reproducible record. Non-negotiable #6
  (determinism) is scoped to our pipeline, not to a third-party TTS
  endpoint; say so in the manuscript's reproducibility note.
- **2026-09-02 #11 — P4 evaluated the artifacts, found five P3 defects, and
  they were fixed rather than reported.** The first run of `src.evaluate`
  against the original P3 outputs returned four Fails, three of them in the
  ASHA tier. All are now corrected in `src/render.py`, the tiers re-rendered,
  and the matrix re-rated against the corrected artifacts — the defects and
  their fixes are recorded in the "Defects found and corrected" section of
  `heuristic_evaluation.md` so the finding survives its own repair. What
  changed: (a) **sign-blind driver list** — `top_drivers` ranked by |SHAP|
  and could print a feature arguing AGAINST the prediction as a flag
  (`failure_mode` listed blood sugar at −0.085); it now keeps only positive
  contributions to the predicted class, and a predicted-low card lists none
  at all and says so. This **supersedes Decision Log #8's** "top-2 by |SHAP|"
  rule — the local-not-global principle in #8 stands, the ranking does not.
  (b) **cross-tier colour** — `band_for` is computed once per case and drives
  both the card header and the lamp, so a case can no longer be amber in one
  tier and red in the next. (c) **header contrast** — white-on-amber measured
  2.12:1; `text_on()` now picks ink or paper per band by measured contrast
  (worst case 5.14:1) and a self-check asserts AA. (d) **direction-word
  deadband** — "raised"/"low" attach only outside 0.25 IQR of the clean-set
  median, so BS 7.7 against a 7.5 median is no longer worded as a concern;
  still median-relative, NOT clinical. (e) **mother provenance** — the
  transcript file now carries case, band and the disclaimer under an explicit
  "written, not spoken" rule; the spoken line is unchanged, because appending
  provenance to every message would bury the one action the tier exists to
  deliver. Two later label refinements: Age carries its own direction pair
  ("young"/"older", not "low"/"raised"), and each band's header states its
  level in words ("LOW — routine care" / "ELEVATED — needs follow-up" /
  "HIGH — needs follow-up") with the separate band-word line removed, so the
  three states are distinguishable in text alone and hue is purely redundant
  (WCAG 1.4.1). Neither refinement moved a rating.
  **Preserved as Limitations, not fixed:** the mother tier leans on colour
  (position and the lit/unlit luminance step are real redundancies, but a
  colour-blind AND deaf reader has position alone); the voice-first mother
  visual has no rendered text alternative (1.1.1) for a deaf reader; the
  clinician tier assumes chart and English literacy; all tiers ship as images
  of text; the ASHA tier is English-only. These are properties of the design,
  and each trades against what makes its tier work — they go in the paper's
  Limitations section, and closing them needs the user studies that are gated
  on ethics clearance.
