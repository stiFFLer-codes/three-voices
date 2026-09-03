# STATE.md — project state & handoff

Read this at the start of every session. Update it at the end (phase, status,
next step) and **append** to the Decision Log — never edit or delete an
existing entry; supersede it with a new dated one.

_Last updated: 2026-09-03_

## Current phase

**P5 manuscript COMPLETE.** All eight sections plus back matter are written:
Abstract, Introduction, Related Work, Data & Vehicle, Three Tiers,
Evaluation, Limitations, Reproducibility. Title, authors, ORCID, CRediT and
the Zenodo concept DOI are in place. `paper/refs.bib` holds 31 entries, all
cited, every identifier resolved in-session. Body is 5968 words (~9.9 pp)
with the Introduction, plus a 235-word abstract and one table. Pushed to
`origin/main` at 77fda14.

**Two things stand between this and a readable PDF.** Figure 1 is currently
the clinician panel alone and must become the three-tier composite the figure
budget always specified (#39). And nothing has ever been through LaTeX —
there is no local toolchain, so the first build is untested and may surface
float placement problems for Figure 1 and Table 1.

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
  Standing result after the P3 fixes and the Decision Log #15 Devanagari
  fix: **29 Pass / 12 Partial / 1 Fail / 6 Deferred**; the one Fail is
  clinician 1.4.5 (images of text), the six
  Deferred are operability + robustness, which a static artifact cannot
  exercise. No human subjects.
- **P5 — manuscript — DRAFTING DONE, unreviewed and uncompiled.**
  `paper/main.tex` + nine `paper/sections/*.tex` + `paper/refs.bib` (31
  entries). Every section drafted. Not compiled — no local LaTeX toolchain;
  the first build is a P6 / Overleaf step and may surface layout problems
  this repo cannot see, particularly float placement for Figure 1 and
  Table 1.
- P6 cold-run/submit — not started.

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

## Next step — P5, continued

The manuscript is written. Next, in order:

1. **Figure 1 composite** (#39). Build the `boundary_mid` three-tier figure
   from the three PNGs already on disk, add it to `src/render.py` so it
   regenerates with everything else, and swap it into `three_tiers.tex`.
   This is the paper's money figure and it does not exist yet.
2. **First LaTeX build**, on Overleaf or any TeX install. Nothing here has
   ever been compiled; expect float placement and line-break fixes, not
   content changes.
3. **Author's end-to-end read** of the resulting PDF.
4. **P6**: cold run from a fresh environment (clearing `results/audio/`
   first, per #19), tagged release, arXiv submission to cs.HC.

Standing items before submission: pull Mamun et al. 2025 (#23); decide on
Clark et al. (#24b), still quarantined; and the `failure_mode` triptych
stays cut (#33, reaffirmed as #38).

Standing items before submission, unchanged: pull Mamun et al. 2025 (#23),
answer calibration in one sentence (#24a), and decide on Clark et al. (#24b),
which is still quarantined.

### Reference material P4 hands the remaining sections:

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
- **2026-09-02 #12 — The dedup penalty is measured, not asserted.**
  `duplicate_leakage_check()` in `src/model.py` scores the final model
  (RF/none, same 5-fold CV) twice: duplicates dropped vs. kept. Dropped:
  macro-recall 0.580±0.027, accuracy 0.641±0.025, n=451. Kept: 0.859±0.026,
  0.854±0.026, n=1012. Keeping the 562 exact duplicates reproduces the
  published 83–88% band, so those numbers are recoverable only when
  identical rows straddle the train/test split. Written to
  `results/tables/p1_duplicate_leakage.csv`. Consequence for the paper: our
  lower headline metric is explained by hygiene, not by a weak vehicle, and
  the comparison is stated up front rather than defended in Limitations.
  `p1_model_metrics.csv` is unchanged by this addition (verified
  byte-identical), so P1's existing artifacts are untouched.
- **2026-09-02 #13 — P5 framing locked.** Headline claim is Decision Log #7,
  uncertainty-aware down-ranking: a knife-edge prediction must not reach the
  least-powerful stakeholder as an alarm. Deterministic LLM-free templating
  (#5) and the in-role defect-finding (#11) are listed contributions, not the
  thesis. Target is a standalone arXiv preprint (cs.HC), not a waypoint to a
  peer-reviewed venue — so the heuristic evaluation IS the evaluation, and
  user studies stay in Future Work. Consequence: the low macro-recall is
  reframed as the paper's premise (explanation design must degrade gracefully
  under model uncertainty), with #12 supplying the reason it is low.
- **2026-09-03 #14 — The Hindi is collaborator-authored and clinically
  reviewed.** The three band strings in `MOTHER_HI` were written and reviewed
  by the project's clinical collaborator, an MBBS physician and native Hindi
  speaker; the synthesised audio was checked against them by the author. They
  are not machine-translated and not author-invented. This is a strength and
  the manuscript states it plainly: the non-English health messaging in the
  tier that depends on it was authored and clinically reviewed by a
  native-speaking medical collaborator. Consequence for P4: the mother tier's
  3.1.1/3.1.2 rationale now cites provenance rather than only the `lang='hi'`
  setting.
- **2026-09-03 #15 — 'ANM' respelled phonetically in Devanagari.** The AMBER
  string embedded the Latin-script acronym `ANM` inside Devanagari, which a
  Hindi TTS engine voices unpredictably — a gTTS artifact, not a translation
  error, and the exact wrinkle P4 flagged at 3.1.1/3.1.2. The source string
  now reads `ए-एन-एम`. Both AMBER cases (`boundary_mid`, `failure_mode`) were
  re-rendered and re-voiced. Consequence: mother 3.1.1/3.1.2 moves Partial →
  Pass, and the matrix is now 29 Pass / 12 Partial / 1 Fail / 6 Deferred.
- **2026-09-03 #16 — The evaluation's grade-inflation guard was moved once,
  deliberately.** `_selfcheck` asserts the Pass rate stays below a threshold,
  so an author rating their own artifacts cannot drift upward unnoticed. The
  #15 fix took the rate to 0.604 and tripped the 0.60 bound. The upgrade is
  legitimate — the string is now wholly Devanagari, so there is no
  language-of-parts defect left to rate Partial — so the bound moved to 0.65,
  with a comment in `src/evaluate.py` recording the date, the reason, and the
  instruction that any FURTHER upgrade tripping it be read as drift rather
  than as licence to raise it again. Recorded here because silently loosening
  an honesty guard is precisely what the guard exists to catch.
- **2026-09-03 #17 — Per-tier language rationale replaces the blanket
  'non-English' claim.** The ASHA card stays English. The README's
  "low-resource, non-English deployment contexts" over-claimed, so it is
  replaced by a per-tier account: the mother tier substitutes **modality and
  language** (a non-reading user leaves no text channel, so language is
  central and is demonstrated), while the ASHA tier substitutes **detail for
  one action** — its contribution is cognitive-load reduction and its
  language is incidental, since every string is a fixed template constant and
  localisation is string substitution deferred to deployment. Umbrella claim:
  *modality- and literacy-calibrated rendering, with language localisation
  demonstrated in the tier where it is most essential — the non-reading
  mother.* Rejected: localising the ASHA card, which would spend effort on a
  string-substitution exercise that demonstrates nothing new. Consequence:
  the English ASHA card is a scoped exposition choice, not a contradiction;
  README, the P4 ASHA 3.1.1/3.1.2 rationale and the corresponding GAPS entry
  are aligned to it. P4 keeps that cell at Partial — a Hindi-first ASHA still
  cannot read the card today, and the framing does not make that untrue.
- **2026-09-03 #18 — gTTS is an illustrative stand-in; Bhashini/AI4Bharat is
  the stated path.** Recorded in README's reproducibility note and as a sixth
  entry in the P4 inherent-limitations list. gTTS is general-purpose, not
  tuned for Indian-language health speech, handles acronyms unpredictably
  (the reason #15 was needed), needs the network, and is not reliably
  byte-reproducible. This supersedes nothing in #10 but sharpens it: across
  the 2026-09-03 re-runs, `confident_low` came back byte-identical while the
  two AMBER cases produced different bytes from each other on identical input
  — so the honest statement is "not reliably reproducible", not "always
  different". The deterministic record remains the Hindi source string in
  `results/tables/tier_mother_<case>_hi.txt`.
- **2026-09-03 #19 — Re-rendering over an existing MP3 can silently keep the
  stale file.** After the #15 string change, `python -m src.render` reported
  success, printed the path and updated the mtime, yet
  `tier_mother_boundary_mid_hi.mp3` still hashed to the pre-fix blob;
  deleting the file first and re-rendering produced the corrected audio. All
  four MP3s were regenerated from an empty `results/audio/` to be certain.
  Consequence for **P6**: the cold run must clear `results/audio/` before
  re-rendering, or it can certify audio it did not actually regenerate. Not
  fixed in code — the renderer is not the bug and the fix is one `rm` in the
  cold-run script.
- **2026-09-03 #20 — `failure_mode`'s low maternal age is kept and framed,
  not filtered.** The case is a 13-year-old whose 101°F BodyTemp drives a
  true-low row to a predicted-high flip. The low ages are real: the source
  population is rural Bangladesh and adolescent pregnancy is documented
  there. Excluding a group the system would actually encounter is itself a
  harm, so the rows stay. Paper-ready wording, to appear at the case's FIRST
  appearance: *"The dataset contains very low maternal ages, reflecting
  adolescent pregnancy in the source population. We retain rather than filter
  these rows: excluding a group the system would encounter is itself a harm.
  This case shows the model over-weighting a demographic feature, which is
  precisely why final judgment stays with a human. All data is public (UCI
  Maternal Health Risk); no real patient or child record is exposed."* The
  public-data point is stated once, not repeated per figure.
- **2026-09-03 #21 — No preeclampsia framing survives into the manuscript.**
  The dataset carries no preeclampsia label and none of its markers — no
  proteinuria, no oedema, no obstetric history — and the top global driver is
  glycemic (BS). All language stays generic "maternal-health risk". A repo
  grep for preeclampsia / pre-eclampsia / proteinuria returns nothing today;
  it must keep returning nothing through P5 and P6.

- **2026-09-03 #22 — Related-work review done; two close-prior papers found,
  and the leakage claim is downgraded.** `paper/related_work.md`, two axes,
  every DOI verified against Crossref in-session. Three consequences the
  manuscript must absorb. (a) **Suresh et al. (CHI 2021) argues against
  role-based tiering** — it deliberately decouples stakeholder knowledge from
  role labels. Our tiers are named by role, so the paper re-grounds them in
  what each reader lacks (modality, literacy, decision authority) per #17 and
  concedes the point explicitly rather than waiting for a reviewer to make it.
  (b) **Two papers do XAI for community health workers in India** — Okolo et
  al. (CSCW 2024, a neonatal-jaundice design probe with real CHWs) and
  Solano-Kamaiko et al. (CHI 2024). They must be cited and distinguished in
  Related Work, not a footnote. The honest distinction is single-tier and
  empirical vs. three-tier and architectural, and the asymmetry is stated
  plainly: they have users, we do not. (c) **Bhatt et al. (AIES 2021) is the
  nearest ancestor of #7** — it already treats uncertainty display as
  audience-aware. Our delta is that we make *suppression* audience-aware: the
  mother does not receive the uncertainty in a gentler format, she receives a
  different assertion. That sentence is the novelty claim, and it is narrower
  than "we propose audience-specific uncertainty communication".
- **2026-09-03 #23 — Leakage claim downgraded from discovery to
  quantification.** No published documentation of the duplicate-row problem in
  UCI id=863 was found: prior papers report n=1014 and describe preprocessing
  only as normalisation / "removal of inconsistencies", and the UCI page
  carries no data-quality note. But absence of evidence is weak here — Kaggle
  notebooks were not retrievable in-session and would not be indexed as
  literature anyway. So the manuscript claims the measurement, not the
  discovery: "We do not claim to be the first to notice these duplicates. We
  report what they cost." The #12 numbers are ours and reproducible either
  way, and the wording survives a reviewer who says everyone already knew.
  **Open item before submission:** Mamun et al. 2025, Engineering Reports
  (10.1002/eng2.70491), uses this dataset with SHAP; paywalled and UNVERIFIED
  in-session. It is simultaneously the closest novelty check on Axis 1 and the
  best leakage check. Pull it.
- **2026-09-03 #24 — Two open items the review created.** (a) Calibration is
  unaddressed: the #7 gate thresholds a margin between random-forest class
  probabilities, which are uncalibrated votes. Guo et al. (ICML 2017) makes
  "are these calibrated?" a foreseeable question — answer it in one honest
  sentence (the threshold is a design constant, not a probability statement;
  calibration is future work) rather than leaving it implicit. (b) Cite
  Clark et al. (BJGP 2022) against ourselves: the NICE traffic light system
  did not accurately detect seriously ill children. A traffic light being
  comprehensible is not the same as it being safe, which is precisely why the
  tier caps at an action (#6) and derates under uncertainty (#7).

## Paper-ready framing decided 2026-09-03

Fixed wording P5 should use rather than re-deriving. Full rationale in the
Decision Log entries named.

- **Umbrella claim (#17).** Modality- and literacy-calibrated rendering, with
  language localisation demonstrated in the tier where it is most essential —
  the non-reading mother. NOT "non-English deployment" as a blanket claim.
- **Per-tier contribution (#17).** Mother: modality + language substitution.
  ASHA: cognitive-load reduction; language incidental, localisation deferred.
  Clinician: full decomposition for a trained reader.
- **Hindi provenance (#14).** Authored and clinically reviewed by a
  native-speaking MBBS collaborator. State it; it is a strength.
- **TTS (#18).** gTTS is an illustrative stand-in; AI4Bharat / Bhashini is the
  deployment path. The deterministic record is the Hindi source text.
- **`failure_mode` adolescent framing (#20).** Verbatim paragraph in that
  entry, at the case's first appearance.
- **Terminology (#21).** Generic "maternal-health risk" throughout. No
  preeclampsia framing, no condition named in any tier.
- **Figure budget.** Three: `boundary_mid` three-tier composite, one global
  SHAP, one `failure_mode` triptych in Limitations. The other 14 renders stay
  in the repo and are cited.
- **Related work (#22).** Novelty sentence: audience-aware *suppression*, not
  audience-aware display. Cite and distinguish Okolo 2024 + Solano-Kamaiko
  2024; concede Suresh 2021 on role-based tiering.
- **Leakage wording (#23).** Claim the quantification, not the discovery.

- **2026-09-03 #25 — P5 skeleton laid down; two sections drafted, Intro and
  Abstract deliberately last.** `paper/main.tex` (single-column arXiv-style
  article) `\input`s eight section files under `paper/sections/`. Three
  comment blocks at the top of `main.tex` are the session-to-session
  contract and must not be deleted: the **outline map** (each section names
  its SOURCE, so no section is ever written from memory), the **contribution
  stack** (exactly three claims, plus the three occupied territories named
  as explicitly NOT claimed), and the **oversell firewall** (banned phrase,
  no clinical-validity claim, generic maternal-risk only, formative framing,
  numbers traceable, citations DOI-resolved). Drafted this session:
  `sections/related_work.tex` (five subsections, each folding in its
  concession) and `sections/data_and_vehicle.tex`. The other six are stubs
  that carry only their source map — the outline is visible without any
  prose being invented ahead of its evidence. No LaTeX toolchain is
  installed locally; compilation is a P6 / Overleaf step and was not
  attempted. A structural check (balanced braces, matched environments,
  every `\input` target present, every `\cite` key defined) passes.

- **2026-09-03 #26 — refs.bib is Crossref-generated, and three citations
  were dropped rather than guessed.** All 29 entries were resolved against
  `api.crossref.org/works/<doi>` and their BibTeX bodies emitted by
  Crossref's own transform endpoint, so no author list, year or venue is
  typed by hand. Two years moved against `related_work.md` §6 and the paper
  follows Crossref: **Kim et al. is 2024**, not 2023 (IJHCS,
  10.1016/j.ijhcs.2023.103160), and **Hendrickx et al. is 2024**, not 2021
  (Machine Learning, 10.1007/s10994-024-06534-x — the 2021 date was the
  preprint). **Dropped for want of any Crossref record, and flagged rather
  than invented:** Arya et al. 2019 (AIX360, arXiv only) — §3.1's canonical
  "one explanation does not fit all" anchor, whose role is now carried by
  Imrie 2023 and Kim 2024; Mozannar & Sontag 2020 (PMLR only) — the
  learning-to-defer lineage, now carried by the Hendrickx reject-option
  survey; and Franc et al. 2021 (JMLR only), which was optional depth. The
  §7 quarantine holds: Liao 2020, Clark 2022 and the Kilkari/mMitra
  references are cited nowhere, and the reason is recorded in the refs.bib
  header — resolving a DOI is necessary but not sufficient, §7 also requires
  the paper to have been read.

- **2026-09-03 #27 — two files named `related_work.md` exist and only one is
  the P5 source.** `./related_work.md` (root) is the Consensus-based sweep
  with the §1–§8 numbering the P5 brief refers to; **it is canonical for the
  manuscript** and is what `sections/related_work.tex` was drafted from.
  `paper/related_work.md` is an earlier web-search sweep with different
  numbering; its DOIs are sound and it is kept for provenance, but it is not
  the section's source. Not merged or deleted this session — flagged so the
  duplication is a known state rather than a trap for the next reader.

- **2026-09-03 #28 — citation gate broadened; Arya and Mozannar restored.**
  Crossref-only was the wrong bar for a CS venue: it excludes arXiv-first
  and proceedings-only work that the field treats as canonical. A citation
  is now admissible once its identifier is resolved in-session against a
  **Crossref DOI, an arXiv ID, or a PMLR / JMLR / ACL / DBLP record** —
  resolved meaning the record was fetched and its title, authors and year
  read off it. Restored under the new bar, both verified this session:
  **Arya et al. 2019** (arXiv:1909.03012, resolved via the arXiv API — v2,
  20 authors, title confirmed) back into §3.1, where it is the canonical
  "one explanation does not fit all" anchor; **Mozannar & Sontag 2020**
  (PMLR v119, pp. 7076–7087, BibTeX taken verbatim from the PMLR record
  page) back into §3.2, where learning-to-defer strengthens the "we claim
  none of the mechanism" concession. Franc 2021 stays out — optional depth,
  not pursued. The §7 quarantine is untouched: Liao 2020, Clark 2022 and
  Kilkari/mMitra are still uncited, because a resolved identifier is
  necessary and not sufficient, and §7 also requires the paper to be read.
  Supersedes the drop decision in #26. Recorded in CLAUDE.md as
  non-negotiable #9 so the bar does not drift again.

- **2026-09-03 #29 — /anti-ai is a standing gate on manuscript prose.**
  CLAUDE.md non-negotiable #8: all prose under `paper/`, and README prose,
  passes the `/anti-ai` skill before commit. Academic register is that
  skill's use case 3.1 — justified statistical hedging and methods passive
  voice stay; the targets are AI vocabulary, unjustified vagueness, flat
  sentence rhythm and significance inflation. Both sections drafted this
  session were audited: no vocabulary tells, no formulaic connectives, no
  trailing participial tails, no negative parallelism, and sentence-length
  spread is wide (Three Tiers stdev 9.2 over 4–37 words; Evaluation stdev
  10.1 over 7–53), which is the opposite of the flat 15–25 band the skill
  flags. **Not applied retroactively:** `related_work.tex` and
  `data_and_vehicle.tex` were committed before this rule and reviewed as
  they stand. They should get an audit pass before P6.

- **2026-09-03 #30 — title, authorship and archive fixed.** Title is
  *"A Coin Flip Is Not a Red Light: Grading a Maternal-Health Risk Alarm for
  Mothers, Community Health Workers, and Clinicians."* The hook is literal
  rather than decorative — the hero case is a 0.012 top-2 margin — and "red
  light" was chosen over "emergency" because it names what the gate actually
  withholds and cannot be misread as "so relax". Authors: Maitreya Sapariya
  (Independent Researcher, ORCID 0009-0003-9346-3775, corresponding) and
  Aditi Patil (Smt. B. K. Shah Medical Institute & Research Centre,
  Sumandeep Vidyapeeth), with a CRediT statement in
  `sections/backmatter.tex`. Archive is the Zenodo **concept** DOI
  **10.5281/zenodo.22252076**, confirmed against the Zenodo API; the v1.0.0
  version DOI 10.5281/zenodo.22252077 is deliberately NOT cited, so the
  reference follows later releases. Also in README.

- **2026-09-03 #31 — `paper/related_work.md` deleted.** The earlier
  web-search sweep, superseded by the root `related_work.md` (the §1–§8
  Consensus sweep) which is canonical and is what the manuscript is drafted
  from. Removed rather than kept alongside, because two files of the same
  name with different section numbering is a trap for the next reader.
  Recoverable from git history at commit cdb52b4. Supersedes #27, which
  flagged the duplication without resolving it.

- **2026-09-03 #32 — the 8 pp body line is breached, and the overrun is in
  the first two sections.** Measured at roughly 600 words per page for this
  class and these margins: Related Work 1669 w (~2.8 pp against 1.5
  allowed), Data & Vehicle 1467 w (~2.4 against 1.5), Three Tiers 919 w plus
  a full-width figure (~1.9 against 2.0), Evaluation 609 w (~1.0 against
  1.0), Limitations 672 w (~1.1), Reproducibility 505 w (~0.85). Body total
  5841 w, about 9.7 pp, before Intro and Abstract exist. Two sections drafted
  this session are close to allowance; the two drafted first are not.
  **Reproducibility's allowance was raised deliberately** from 0.25 to ~0.85
  pp: five named gates, a stated determinism guarantee and one honest
  exception are a differentiator, and compressing that to a boilerplate
  sentence would discard the strongest evidence the paper has that its
  numbers are checkable. **Not cut this session.** Trimming reviewed prose is
  a review decision, not a drafting one, so the arithmetic is recorded in the
  `main.tex` budget block and handed back rather than acted on.

- **2026-09-03 #33 — the third planned figure was not placed, on the
  accountability test.** The figure budget set on 2026-09-03 called for three
  figures, the third being a `failure_mode` triptych in Limitations. Applying
  this session's test — what breaks if this is removed? — the answer was
  nothing: the case is already carried numerically in Data & Vehicle (13-year
  old, 101°F body temperature, true-low predicted high, blood sugar and
  systolic pressure both arguing against the flip), and a triptych would
  restate it visually without adding evidence. Given #32 it would also cost
  roughly a third of a page the paper does not have. Left unplaced rather
  than dropped: if the trim in #32 frees space and a reader wants to see the
  model be wrong rather than read that it was, Limitations is still its home.

- **2026-09-03 #34 — Limitations and Reproducibility drafted; collection and
  receipts only, no new claim.** Limitations groups every logged limitation
  into five clusters — no users (which carries comprehension, the 0.15
  constant, the magnitude omission and role-as-proxy as its four
  dependents), what one public dataset supports (including calibration per
  #24a and the 35 conflicting vectors), who the renderings still exclude,
  the TTS stand-in, and nothing deployed. Each is stated once with its
  resolution named; none is new, and the three citations it uses were
  already in `refs.bib` and already cited in Related Work. Reproducibility
  names the five gates by exact command, states the seed/pins/cache
  guarantee, and gives the one honest exception. Precision check made this
  session: `src/data.py` contains no random component at all, so the text
  says the seed is applied in each script that touches randomness rather
  than claiming the loader calls `set_seeds()` — it does not. Decision Log
  #19 is stated in the section itself, because a cold run that certifies
  audio it did not regenerate is exactly the failure a reproducibility
  section exists to prevent.

- **2026-09-03 #35 — voice pass and compression done together on the two
  earliest sections.** `related_work.tex` and `data_and_vehicle.tex` predated
  the /anti-ai gate and read differently from the four newer sections. Both
  now match. Em-dashes went 16 to 2 in Related Work, keeping only the pair
  that frames *One Explanation Does Not Fit All*, which is correct usage, and
  13 to 0 in Data & Vehicle. Rhetorical triples softened; genuine lists (the
  six features, the model names, the three contributions) left alone.
  Compression in the same pass: 1602 to 1424 words and 1373 to 1244, about
  526 words or 0.9 pp across the body, which now stands at 5315 w (~8.9 pp).
  **Verified mechanically that nothing was lost:** the cited-key set is
  identical to the previous commit (31 keys, none added, none removed), and a
  multiset diff of every numeric token in both sections shows no number
  dropped. That check earned its keep — a first pass had silently swallowed
  the sentence carrying the leakage claim itself ("recoverable only when
  identical rows are allowed to straddle the split"), which the number diff
  caught and which was restored. Compression stops here: further cuts start
  removing content that earns its place, so the residual overrun is accepted
  rather than squeezed.

- **2026-09-03 #36 — cohort counts are now a committed artifact.**
  `prepare_modeling_frame()` already computed the row counts, the duplicate
  count and the 35 conflicting vectors but only printed them. It now also
  records age min, age max and the count under 18, and `run()` writes the
  whole preparation report to `results/tables/p1_cohort_summary.csv`. Reason:
  the Reproducibility section promises any number in the paper can be checked
  against the file that produced it, and the adolescent-age counts in Data &
  Vehicle (95 under 18, minimum 10) were the one claim with no committed file
  behind it. The new table also backs 1014, 2, 561, 451, the 233/106/112 class
  split and the 35 conflicting vectors, so every cohort number in the
  manuscript is now checkable. Verified that `p1_model_metrics.csv` and
  `p1_duplicate_leakage.csv` come back byte-identical after the change, so no
  existing P1 artifact moved. The Reproducibility gate list was updated to
  name the new file — the only edit made outside the two sections in scope,
  made because leaving it unnamed would have made that section describe its
  own gate inaccurately.

- **2026-09-03 #37 — stale citation-gate comment in `related_work.tex`
  fixed.** Its header still said Arya 2019 and Mozannar & Sontag 2020 had
  been dropped for want of a Crossref DOI. Both were restored under the
  broadened gate in #28 and are cited in the body. The comment now states the
  broadened gate and records that both identifiers were resolved in-session,
  so a future session cannot re-drop them by trusting the comment over the
  text.

- **2026-09-03 #38 — Intro and Abstract drafted last, to a frozen body; the
  third figure stays cut.** Both were written only after the six body
  sections were stable, so that every capability either states is one the
  body actually delivers. Abstract is 235 words and opens on the failure
  rather than on the contribution: a model at 0.487 against 0.499, a
  clinician who can discount that margin, a mother who cannot. Introduction
  is 770 words (~1.3 pp) and puts the honest frame in its own subsection
  BEFORE the reader reaches Limitations: nobody in the three groups has used
  the system, the evaluation is a formative critique of our own artifact, and
  user studies are gated on ethics. The three claims and the three
  disclaimers sit in the same passage, as required, so a skimming reader
  cannot pick up the claims without the bounds. **Verified mechanically:** no
  citation appears in Intro or Abstract that the body does not already use
  (31 keys, unchanged), and no numeric token appears in either that is not
  already in a body section. The abstract runs 235 words against a 150–200
  target; the overrun is accepted deliberately, because hitting 200 required
  dropping either the derate direction or one of the four disclaimers, and
  arXiv imposes no abstract limit. **Figure #33 decision: stays cut.** The
  `failure_mode` triptych carries no claim the prose does not — the case is
  given numerically in Data & Vehicle and its wrongness is the closing beat
  of Three Tiers — and it would cost ~0.35 pp on a paper already at ~9.9.
  It remains rendered, archived and cited in the repository.

- **2026-09-03 #39 — Figure 1 must be the three-tier composite, and is not
  one yet.** The figure budget fixed earlier today specified a `boundary_mid`
  three-tier composite as the paper's first figure. What is actually in
  `three_tiers.tex` is `tier_clinician_boundary_mid.png` alone, with the
  other two tiers named in the caption as separate files. That
  under-delivers the paper's central claim at exactly the point a reader
  looks for it: the argument is that ONE prediction becomes THREE renderings,
  and the figure shows one. A reader who looks only at the figures never sees
  the ASHA card or the mother's lamp. **Decision: build the composite** —
  three panels for the same case, clinician / community health worker /
  mother, labelled by tier, so the derate is visible as a single image.
  Constraints for whoever builds it: (a) it is generated by `src/render.py`
  so it regenerates with every other artifact and stays inside the
  determinism guarantee, not assembled by hand in an image editor; (b) the
  three source PNGs already exist on disk
  (`tier_{clinician,asha,mother}_boundary_mid.png`), so this is composition,
  not re-rendering, and no SHAP or model code is touched; (c) the caption
  must not introduce a claim — the numbers stay as Three Tiers already
  states them; (d) Reproducibility's gate list gains the new output file, the
  same way it did for `p1_cohort_summary.csv` in #36. This is separate from
  #33: the `failure_mode` triptych stays cut, and this entry does not reopen
  it. Figure count for the paper remains small on purpose.
