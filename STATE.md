# STATE.md — project state & handoff

Read this at the start of every session. Update it at the end (phase, status,
next step) and **append** to the Decision Log — never edit or delete an
existing entry; supersede it with a new dated one.

_Last updated: 2026-10-09_

## Current phase

**2026-10-09: out-of-fold gate analysis done (#59 pre-registered, #60
results).** `python -m src.model` now also writes `p1_oof_predictions.csv` and
`p1_gate_summary.csv`. The paper's case probabilities are in-sample; the
out-of-fold numbers are in #60. No paper prose or figure has been changed in
response, and that is an open author decision ahead of Gate A.

**P5 CLOSED 2026-09-03. Now in P6 — pre-submission pass.** Branch
`revision/sncs-framing`, unmerged, carries a journal-alignment framing pass
(#47, #48), an **arXiv moderation repositioning (#49)** — new title naming the
artifact, three-paragraph abstract, ADIT affiliation, and `%` comments
stripped from the upload but not the repo — and now a **consolidated edit pass
(#56)**. What remains is reading, verifying and packaging. See "Next step" for
the ordered gate list, and #43 for what closing P5 does and does not assert.

**#56 changed content, unlike #47-#49.** It added a **Section 7 Conclusion**
(so Reproducibility is now Section 8), a **Section 4.4** on the row-382 case,
**Table 2** (model comparison) and **Table 3** (the 48-cell heuristic matrix),
a first statement of **mid-risk recall 0.227**, and a disclosure that the
**uncertainty gate is one-sided**: it guards the high boundary and leaves
GREEN ungated, which Section 3.4's own asymmetry argument says is the wrong
side to leave open. Section 2 was re-textured so every subsection opens on the
work rather than the literature. **Now 20 pp**, clean build, no locked number
changed, Section 6 duplication deliberately untouched. Not committed.

**THAT BLOCKER IS CLOSED (#57, 2026-09-15).** `paper/ARXIV_SUBMISSION.md` is
regenerated — sixteen upload files including `sections/conclusion.tex`, 20 pp,
36 bibitems, and a corrected Comments field (it had said "1 table"; the paper
has three). `arxiv/` itself had drifted the same way and is regenerated too;
packaging is now scripted off `main.tex`'s own `\input` lines rather than
hand-copied, so the file list cannot drift again.

**REPOSITIONING PASS LANDED (#57).** Section 6 is now Section 7 "Limitations
and Future Work" and owns every forward-looking claim; the three scattered
`is future work` tails are consolidated into one subsection 7.5, and the
section still came out one word shorter than before. The invented self-label
"This is a design and feasibility artifact" is **gone from all four sites** —
the Introduction now names the contribution types in HCI's own vocabulary
(Wobbrock & Kientz 2016, resolved against Crossref; `refs.bib` 35 -> 36), and
the abstract no longer ends on a disclaimer. No limitation was removed, no
number and no claim changed.

**OPEN against #49 — now partly closed by #57.** `sections/intro.tex` had
never been repositioned; the three intro diffs the earlier session called for
were lost when it cleared. #57 rewrote 1.1's contribution opener and
compressed 1.2, so the Introduction has now had a repositioning pass, though
not the specific lost one. **The #53 position-paper risk turned out to be
already closed** — the flagged phrases ("entitled to be told",
"vulnerability", "least power") are not in the file; #56's compression had
removed them. See #57(d), which also records why that risk was worse than #53
knew: since 2025-10-31 a cs.* position paper must already have completed peer
review or is likely to be **declined**, not held.

**GATE B IS CLOSED (#55, 2026-09-11).** The cold run has been done: fresh
clone, fresh venv, pinned deps, audio purged first. 33 of 33 non-audio
artifacts byte-identical; all four MP3s the right length, three of them
byte-identical. Every headline number regenerated, so Table 1 is verified
rather than asserted. It found two real defects, both now fixed: the pins
require Python 3.12 and nothing said so, and the abstract and Introduction
attributed 561 duplicates to the raw file, which actually holds 562 (561 is
the post-filter count the body always reported). Endorsement is confirmed to
cover **cs.HC**. **GATE A IS THE ONLY THING LEFT BLOCKING THE TAG** — the
author's end-to-end read has still never happened, and Patil's read is out
but not back.

**Gate C packaging is done (#45):** the arXiv `\graphicspath` blocker is
closed, the 15-file upload compiles standalone with `pdflatex` alone and zero
errors, References now opens on its own page, and `paper/ARXIV_SUBMISSION.md`
holds every field the arXiv form asks for. (The 17 pp figure in this paragraph
was #45's; the manuscript is **19 pp** as of #49 and was re-verified cold at
19 pp in #55.) **Gate B is now CLOSED (#55). Gate A (author read) remains
untouched and is the last thing blocking the v1.0.0 tag.**

**P5 manuscript COMPLETE.** All eight sections plus back matter are written:
Abstract, Introduction, Related Work, Data & Vehicle, Three Tiers,
Evaluation, Limitations, Reproducibility. Title, authors, ORCID, CRediT and
the Zenodo concept DOI are in place. `paper/refs.bib` holds **35** entries (31
at P5 close; #47 added the two Nielsen heuristics papers and the WCAG 2.1
Recommendation; #55 added Yesmin et al.), all cited, every identifier
re-resolved in-session on 2026-09-11. Body is 5968 words (~9.9 pp)
with the Introduction, plus a 235-word abstract and one table. Pushed to
`origin/main` at 77fda14.

**Both remaining blockers are cleared.** Figure 1 is now the three-tier
composite, built LaTeX-native from the three committed PNGs (#40), and the
manuscript has compiled: **17 pages**, zero errors, zero undefined citations
or references, zero overfull boxes. A local MiKTeX toolchain now exists on
the author's machine (#41). A cosmetic pass then reclaimed Figure 1's float
page and added front-matter polish (#42). Still 17 pages, still a clean log.
Figure 1 is a top float on page 9 with Section 4.4 flowing beneath it; Table 1
sits at the top of page 6 with its reference below it on the same page.

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
- **P5 — manuscript — DONE (closed 2026-09-03, #43). Compiles clean;
  unread on the page.**
  `paper/main.tex` + nine `paper/sections/*.tex` + `paper/refs.bib` (31
  entries, all 31 cited, all 31 resolving in the bibliography). Builds to
  `paper/main.pdf`, 17 pages: 13 pp body and front matter, 4 pp references.
  Clean log — no errors, no undefined refs, no overfull boxes. Four underfull
  hboxes remain (loose lines in `\texttt{}`-heavy list items); cosmetic,
  deliberately deferred. Front matter carries a bold title, a keywords line
  under the abstract, and a two-line CRediT statement (#42). **Not yet read
  end to end by either author — that is the first P6 gate, not a P5
  leftover.**
- **P6 — cold-run + submit — IN PROGRESS (entered 2026-09-03).** Gate C's
  packaging items are done ahead of Gates A and B, deliberately: they are
  mechanical, they touch no prose, and #44 was a live blocker worth closing
  before it could bite. See #45. **Gate A (the author read) and Gate B (the
  cold run) are still untouched and still blocking the tag.** The gate list is
  under "Next step".

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

## Next step — P6, the pre-submission pass

Three gates, in order. **Do not start a later gate before an earlier one
closes** — a cold run against prose that is still moving wastes the run, and
tagging before the cold run tags something unverified.

### Gate A — read and settle the content (nothing here is layout)

1. **Author's end-to-end read of `paper/main.pdf`** (now **20 pp**, #56).
   Never done. No part of this manuscript has been read on the page by a
   human. Blocking: every later gate assumes the prose is final. **#56 raised
   the stakes on this item** — it added a Section 7 Conclusion, a Section 4.4,
   and two tables, none of which any human has read, and it disclosed a
   one-sided gate that a reader should check against Section 4.2 and 6.2 with
   their own eyes.
1a. **Re-run Gate B (cold run) after Gate A closes.** #55 closed it against a
   19 pp manuscript with one table. #56 changed content, so that run no longer
   describes what would be tagged. Nothing in #56 touched `src/`, so the
   artifacts should be unchanged, but the claim "verified cold" now needs a
   fresh run to be true.
1b. **Regenerate `paper/ARXIV_SUBMISSION.md`** — **DONE 2026-09-15 (#57).**
   Sixteen upload files including `sections/conclusion.tex`, 20 pp, 36
   bibitems, abstract block re-derived mechanically (1824 chars / 284 words),
   Comments field corrected to "20 pages, 1 figure, 3 tables". `arxiv/` was
   stale in the same way and is regenerated; packaging is scripted now.
2. **Co-author read (Patil).** Specifically: the Hindi strings and their
   clinical framing (#14), the ASHA-tier card wording, and her own CRediT
   role list — of her four roles only *Validation* is an official CRediT
   term (#42), and whether to keep the three custom descriptors is hers to
   decide, not a layout call.
3. **Pull Mamun et al. 2025** (Engineering Reports, 10.1002/eng2.70491) —
   #23. Paywalled and still unread; it is cited from resolved Crossref
   metadata only. It is simultaneously the closest novelty check on Axis 1
   and the best external leakage check. If it documents the duplicate rows,
   the leakage framing in Data & Vehicle needs a sentence, not a rewrite.
4. **Decide Clark et al. (BJGP 2022)** — #24b, still quarantined. Cite it
   against ourselves (NICE traffic light comprehensible but not accurate) or
   drop it and say so. If cited, `refs.bib` goes 31 -> 32 and the citation
   gate applies in full: §7 of `related_work.md` requires the paper to have
   been READ, not merely resolved.
5. #24a **calibration is CLOSED** — `limitations.tex` carries the honest
   sentence ("vote fractions rather than calibrated posteriors... a design
   constant on an ordering, not a statement about probability"). Do not
   reopen it.
6. The `failure_mode` triptych **stays cut** (#33, reaffirmed #38). Do not
   reopen it either.

### Gate B — cold run — **DONE 2026-09-11 (#55). PASSED.**

Items 7-11 below were all executed and all passed; they are kept for the
record and as the recipe if the pipeline ever changes. Re-run only if `src/`
moves.

7. Fresh clone into a clean directory, fresh virtualenv, pinned deps. The
   point is to catch what only works because this machine has been running
   the pipeline for days.
8. **`rm -rf results/audio/*` FIRST** (#19). Re-rendering over an existing
   MP3 reports success, updates the mtime and can leave the stale blob in
   place. Skipping this certifies audio that was never regenerated.
9. Run the five gates in order: `python -m src.{data,model,explain,render,
   evaluate}`.
10. Verify every PNG, CSV and TXT is byte-identical to what is committed.
    The MP3s are the one documented exception (#10, #18) — same length,
    different bytes. Expect that; do not "fix" it.
11. **Rebuild the PDF from the regenerated figures** and confirm it is still
    17 pp with a clean log. The three tier PNGs feed Figure 1 directly, so a
    changed renderer is a changed figure.

### Gate C — package, release, submit

12. **arXiv packaging blocker — CLOSED 2026-09-03 (#45).** `main.tex` now sets
    `\graphicspath{{./}{../results/figures/}}`, so the archive root matches
    before the `../` entry is ever consulted and the upload needs no source
    edit. The repo is unrestructured and the PNGs are not re-rendered, per
    #44. Packaging is now a pure copy; the commands are in
    `paper/ARXIV_SUBMISSION.md`. **Re-run the standalone compile after the
    Gate B cold run**, since a re-rendered PNG is a changed figure.
13. Ship `main.bbl` in the upload — DONE and verified in the standalone
    compile (#45). arXiv runs LaTeX but not BibTeX, so the `.bbl` is the
    bibliography. It is already tracked for this reason.
14. Final firewall grep before upload — **run 2026-09-03 (#45), clean**: no
    "novel framework", no clinical-validity claim, no named condition (#21),
    31/31/31 citations with zero orphans, every numeric token in the abstract
    and introduction present in a body section. Re-run if any prose moves in
    Gate A.
15. Tag `v1.0.0`, push the tag, confirm Zenodo minted the version under the
    concept DOI 10.5281/zenodo.22252076 (the concept DOI is what the paper
    cites, deliberately, so it tracks later releases).
16. Submit to arXiv, **cs.HC**.

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

- **2026-09-11 #55 — GATE B CLOSED (cold run passed), plus an external-review
  response pass.** Branch `revision/sncs-framing`, still **not merged to
  `main`, still no PR.** Two external moderation reviews were run by the
  author between #54 and this entry. This entry records what they got right,
  what they got wrong, and what was actually changed.

  **GATE B — THE COLD RUN, RUN AND PASSED. This was never done before.**
  Fresh `git clone` into an empty directory, fresh venv, pinned deps,
  `rm -rf results/audio/*` first per #19, then the five gates in order.
  *Result:* **33 of 33 non-audio artifacts byte-identical** to what is
  committed — every PNG, CSV, TXT and MD. Zero differing, zero missing. All
  four MP3s identical in length; three byte-identical and one not, which is
  exactly the behaviour #10/#18 documents and predicts. Every headline number
  regenerated from scratch: 561 duplicates, n_clean 451, macro-recall
  0.580 +/- 0.027 -> 0.859 +/- 0.026, accuracy 0.641 -> 0.854, recall_high
  0.723 -> 0.908, 35 conflicting vectors, the boundary case at
  0.013/0.487/0.499 with a 0.012 margin, and the 48-cell evaluation at 29 pass
  / 12 partial / 1 fail / 6 deferred. **Table 1 is now verified rather than
  asserted.**

  **The cold run found a real reproducibility defect, which is what it was
  for.** The pins require **Python 3.12** and nothing said so. numpy 1.26.4
  and scikit-learn 1.5.1 ship no wheels for 3.13+, and the system default is
  now 3.14, so a reader following the README could not install the pinned set
  at all. Stated now in `reproducibility.tex`, `requirements.txt` and
  `README.md`. The paper claimed pinned determinism while omitting the one
  fact that makes the pins installable.

  **A second defect, found by the consistency sweep: 561 versus 562.** The raw
  file holds **562** exact duplicates; **561** is the count *after* the
  documented two-row plausibility filter. Section 3.2 always said this
  correctly ("561 of the 1012 rows"), but the abstract and the Introduction
  attributed 561 to the dataset as distributed. A reader running
  `drop_duplicates()` on the download gets 562 and a mismatch against the
  paper's headline measurement. Both sites now say "of the 1012 rows that
  survive a two-row plausibility filter". Same class of error as #54 — a claim
  that did not match the artifact — caught this time before submission.

  **Claim-vs-renderer sweep: CLEAN.** Every mechanism claim in the prose was
  read against `src/render.py` rather than against the tables, which is the
  check #54 said the firewall lacked. `band_for` returns RED only for high
  risk at margin >= 0.15 and AMBER otherwise, never GREEN except on predicted
  low risk; `BAND_LABEL` gives AMBER "ELEVATED — needs follow-up". The
  abstract, Section 1, Sections 4.1 and 4.2 and the Figure 1 caption all
  match. The cold run then rendered the boundary case's ASHA header as
  "ELEVATED — needs follow-up" live, confirming #54's fix in a clean clone.
  Also verified: no language model anywhere at inference — gTTS is the only
  network call and it synthesises a committed string.

  **WHAT THE TWO EXTERNAL REVIEWS GOT WRONG.** Recorded so no future session
  re-does this work.
  (a) *"Maisoon et al. [17] could not be confirmed."* FALSE POSITIVE. It
  resolves cleanly against Crossref (10.1109/access.2026.3710610): exact
  title, all three authors, IEEE Access, 2026, vol. 14, pp. 102905-102919.
  (b) *"Novelty-undercutting comments sit in the raw .tex and arXiv publishes
  source."* ALREADY CLOSED by #49 — the upload set carries 0 comment lines.
  This was the most damaging item either review raised and it was already
  handled.
  (c) *"Move the leakage audit up / make it co-equal in the abstract."*
  ALREADY TRUE — abstract paragraph 3 was the leakage audit and Section 1.2
  already labelled it MEASUREMENT alongside MECHANISM and ARTIFACT.
  (d) *"The disclaimer appears at least five times."* It appears three times —
  abstract, 1.2, 6.1 — which is standard placement.
  (e) *"55-65% chance of passing."* No basis; ignore the number.
  (f) One review urged framing the audit as "a correction to the published
  record". **Rejected — that is an oversell-firewall breach**; the paper's "a
  cost we quantify, not a fault we claim to have found first" stands.

  **WHAT THEY GOT RIGHT, AND WHAT CHANGED.**
  (a) *Front-loaded negatives.* Both reviews, run independently, said the
  stacked caveats on page one cause a 60-second triage to over-weight them.
  **Abstract paragraphs 2 and 3 SWAPPED** — leakage measurement now second,
  caveats third. Verified as a pure block swap: the transcription measured
  1760 characters before and after. **This SUPERSEDES #49's ORDERING RULE**
  ("the caveats stay EARLY, in paragraph 2"), and the supersession is recorded
  in `abstract.tex`'s own header. **All eight checklist items survive verbatim
  and were re-verified item by item after the swap.** Nothing was dropped,
  softened or compressed — the caveats sit ~100 words later in the same
  abstract, not deferred to a section.
  (b) *Advocacy register in the Introduction* — the risk #53 logged as (i) and
  left alone. The three phrases are now descriptive: "what is each reader
  *entitled to be told*" -> "which assertion should each channel carry";
  "abstention graded by stakeholder vulnerability" -> "graded across
  stakeholder channels"; "the reader with the least power to interrogate the
  system" -> "the channel that exposes least of the model's output". The
  research question is unchanged; only the register is. The parallel sentence
  at `related_work.tex:85` was aligned to the same wording so the two cannot
  drift. **"stakeholder vulnerability" at `related_work.tex:87` was
  deliberately KEPT** — it is the novelty-boundary sentence ("that
  intersection, and only that intersection, is what we claim"), which is the
  most research-shaped sentence in the paper, and it sits deep in Section 2.2
  where triage does not reach.
  (c) *Two Limitations headings renamed.* "Nobody has used this" ->
  "Evaluation without users"; "Nothing is deployed" -> "Evaluated on a
  workstation". Two of five headings read as an incompleteness confession at
  ToC skim. **Not one sentence of body text moved.** ("Bench conditions, not
  field conditions" was drafted and rejected: it is the "X, not Y" pattern the
  paper already spends well elsewhere, and a fourth instance is a tell.)
  (d) *Yesmin et al. cited* — `refs.bib` 34 -> 35. arXiv:2601.07866v1
  [cs.AI], 10 Jan 2026, three authors, resolved in-session against the arXiv
  API, and the dataset confirmed from the full HTML text: "We utilized the UCI
  Maternal Health Risk Dataset (N=1,014)", six clinical features plus a
  **synthetic** regional access score, and **no mention of duplicates or
  deduplication anywhere**. Cited twice: in Section 3.3 as a third
  undeduplicated n=1014 report at 88.67% — flagged explicitly as **not**
  like-for-like because of the synthetic feature — and in Section 5.5 as the
  closest contemporaneous neighbour, separated on both mechanism (nothing in
  their pipeline withholds an assertion) and audience (their fourteen
  clinicians sit on the one tier our gate leaves untouched).

  **Yesmin is a calibration point worth keeping.** Five pages, cs.AI primary,
  a WCCI submission, no released artifact and no reproducibility package — and
  it cleared moderation in January 2026. This manuscript is 19 pp with an
  archived artifact and a verified cold run.

  **`/anti-ai` run on every sentence written this session.** Four tells found
  and fixed in the new prose: a vague "most of whom" where 71.4% was
  available; an empty transition ("The separation is clean in both
  directions"); the "X, not Y" heading above; and "pinned" three times in one
  sentence. The pre-existing prose was not touched.

  **Firewall re-run in full (Gate C item 14), clean.** No banned phrase. The
  four clinical-validity greps hit only sentences that *deny* the claim.
  Citations **35 cited / 35 in refs.bib / 35 bibitem, zero orphans in either
  direction**, and **all 35 identifiers mechanically re-resolved this
  session**: 33 against Crossref or the arXiv API, plus PMLR v119 (Mozannar)
  and the W3C WCAG 2.1 Recommendation, both HTTP 200. Every one of the 14
  distinct numbers in the abstract and Introduction appears in a body section.
  `refs.bib` comments are now stripped from the upload too — they documented
  the citation gate and read as diligence, but arXiv never runs BibTeX, so
  they are inert surface. The repo keeps them.

  **Verified, cold rather than asserted.** Package rebuilt, extracted into an
  empty directory, `pdflatex` three passes, no BibTeX: **15 files, 0 leaked
  comment lines, 0 dot-prefixed entries, 19 pp, 0 errors, 0 overfull boxes, 0
  undefined citations or references, 0 LaTeX warnings.** In-repo `main.pdf`
  is content-identical to the cold build (same byte length; 68 bytes differ,
  all in the trailing timestamp/ID region). Abstract transcription regenerated
  from source, not retyped: **1827 characters against the 1920 ceiling, 289
  words.**

  **Endorsement confirmed by the author this session: covers cs.HC.** #51(b)
  is therefore closed for this submission; #51(a) (prior-decline scrutiny)
  still stands and is not fixable, only compensated for.

  **STILL OPEN, and still blocking the v1.0.0 tag: Gate A.** The author's
  end-to-end read of the 19 pp PDF has not happened, and the co-author read
  (Patil) was sent this session but has not returned. Mamun et al. is
  **deliberately deferred to the journal round** (#23 downgraded): the paper
  claims no priority on the duplicates, so nothing breaks if Mamun documented
  them first, and Yesmin now supplies the external undeduplicated-band
  corroboration Mamun was wanted for. Clark et al. (#24b) is **dropped**.


- **2026-09-15 #56 — CONSOLIDATED EDIT PASS: body sections 1-6, plus a new
  Section 7 Conclusion.** Branch `revision/sncs-framing`, still **not merged
  to `main`, still no PR, not committed.** Driven by an editorial read that
  found the paper arguing in places where it could show, and reading as a
  survey in Section 2 because every subsection opened on the literature rather
  than on us. Sizes before: Related Work 1594 prose words against Three Tiers
  1056, so the literature outweighed the contribution by half again.

  **The gate's missing side, and the reason this entry exists (ADDITION 1).**
  Section 4.2's band rule fires RED on predicted-high AND margin >= 0.15, but
  GREEN follows the argmax with NO margin test at all. Section 3.4 states the
  opposite principle in the paper's own words: "the costs are asymmetric:
  failing to flag a high-risk mother is the error that matters". The paper
  shipped the principle in Section 3 and the rule that does not implement it in
  Section 4, two sections apart, and named the gap nowhere. A near-tie
  resolving to low risk renders an unqualified GREEN all-clear to the mother
  and no derate exists for it. **Now named in one paragraph in 4.2 and one
  entry in 6.2, both framed as UNHANDLED**: the gate is one-sided, the low
  boundary is unprotected, the symmetric extension (derating an ungated
  near-tie GREEN down to AMBER, mirroring red-to-amber) is future work, and
  this version does not do it. **No code changed.** `band_for` is untouched;
  this is a disclosure, not a fix. Same class as the #55 breach: a claim read
  against the tables but never against the rule.

  **Row 382 promoted to its own subsection 4.4 (ADDITION 2).** The paper's
  strongest single design case survived only as a passing mention in 3.5 and a
  defect illustration in Section 5. It is true LOW, predicted HIGH, at
  `0.451 / 0.097 / 0.453` with a top-two margin of `0.002` — a 13-year-old
  whose 101 F body temperature drives the call — and the gate withheld a red
  lamp and an urgent spoken message from her. `heuristic_evaluation.md` already
  called it "the strongest single design decision in the three tiers".
  Figure 1 stays on row 66: it is referenced in five places and the 0.487/0.499
  split is the cleaner coin-flip illustration. **The honesty sentences are
  load-bearing and must survive any future edit:** amber on a true-low record
  is still a false referral, and the gate made the error smaller, not correct.
  Subsection title is "Derating a false alarm", not "When the gate prevents a
  false alarm" — the gate derated it, it did not prevent it.

  **Mid-risk recall stated for the first time (ADDITION 3).** `0.227 +/- 0.057`
  for the selected model, no higher than `0.302` in any of the six
  configurations, against `0.790` low and `0.723` high. Tied to the 35
  conflicting feature vectors already in 3.2. This turns "a model that was
  right 99% of the time would not need the machinery we describe" from a
  general remark into a measurement: the mid class is the one the vehicle
  cannot resolve, so mid-high near-ties are a structural property of this data,
  not an occasional accident. A worse number that strengthens the design
  argument and costs nothing on the firewall.

  **Two committed tables typeset for the first time (ADDITION 4).** Before this
  pass the entire body carried one table and one figure while citing five
  committed CSVs. **Table 2** is the six-configuration model comparison from
  `p1_model_metrics.csv`; **Table 3** is the 16 x 3 heuristic matrix from
  `heuristic_matrix.csv`, symbols only, rationales left in the CSV. The
  abstract already named that matrix as archived and the paper had never shown
  it. Both verified cell-by-cell against their source CSVs by script, not by
  eye. This also closes a self-containment gap: Section 5's result no longer
  lives only in the repository.

  **Section 7 Conclusion added (ADDITION 5).** Two short paragraphs, landing on
  row 382. Reason is ToC shape: the paper trailed into Limitations /
  Reproducibility / Declarations, and #55's external reviews had already shown
  that a ToC skim reads as an incompleteness signal (the same evidence that
  renamed two Section 6 headings on 2026-09-11). **Deliberately NOT a recap:**
  no future-work list, no section-by-section summary, no new claim, and the
  user-study point appears in one clause pointing at Section 6. Reproducibility
  stays at Section 8, before Declarations.

  **Section 2 re-textured, the single highest-leverage move against the survey
  read (RELOCATION + TONE).** (a) The opener now names the split it always had:
  TWO literatures we claim between (tiering, selective prediction) and THREE we
  are answerable to (CHW comprehension, risk communication, this dataset). It
  previously promised "two mature literatures" and then ran five subsections;
  `intro.tex` repeated the undercount. (b) All five subsections now open on
  what we do, with the literature positioned as what we build past. Same
  citations, same bolded disclaimers, opposite genre signal. (c) 2.4's
  entitlement defence (an icon array communicates a magnitude the sender is
  entitled to assert; at 0.487 against 0.499 the model is not so entitled)
  MOVED to Section 4 beside the mother tier it defends, seventy lines closer to
  the thing being defended; 2.4 keeps the literature, the tension and one
  pointer. (d) Concession-announcements deleted, boundaries kept verbatim:
  "and both weaken us", "evidence of a weaker kind", "forced by the field
  rather than chosen out of modesty". **"This paper has none" (re: users)
  stays, stated once and plainly — it is load-bearing.** 2.5 now reads as
  deliberate use of a standardised vehicle, and does NOT claim to have
  evaluated whether the rendering helps anyone.

  **Compression funded the additions.** Intro 1.2's two paragraphs merged (they
  made one point twice); the "gated on ethics clearance" repeat inside the
  intro removed; throat-clearing cut ("The disclaimers belong in the same
  breath", "Here is the standard we ask to be held to", "We are careful about
  what this licenses us to say", "stating the assumption is what makes the gap
  findable", "which is how a design claim gets tested before anyone is asked to
  rely on it"); the local pile-up of five negative constructions in thirteen
  lines of the disclaimer paragraph thinned, with the global count of
  contrastive constructions left alone because contrast is the right instrument
  for boundary-drawing; the Figure 1 caption cut to what the figure needs; the
  abstention sentence, the vehicle line and the saturation claim now point back
  instead of restating with the same cites.

  **SECTION 6 WAS NOT TOUCHED for duplication.** It is a declared collection
  point and its repetition is load-bearing. The only changes there are the new
  one-sided-gate entry in 6.2 and one trimmed framing sentence in 6.3.

  **Two precision fixes.** (a) `evaluation.tex` said "four failures" and then
  listed five defects; `intro.tex` and `abstract.tex` said five. BOTH numbers
  were right and referred to different things — four Fail RATINGS on the first
  pass, arising from five distinct DEFECTS (C1-C5). "Four" was NOT changed to
  "five"; a clause now says which is which. (b) The intro compared macro-recall
  `0.859` to an accuracy band; the like-for-like comparator against the
  published figures (83.74 / 99.51 / 88.67, all accuracies) is accuracy
  `0.854`, which 3.3 already had. Fixed in both places, and 3.3's "the inflated
  figure" now names which figure.

  **Verified.** Data spine recomputed independently from `data/raw/`, not read
  off prose: 1014 / 2 at HR=7 / 1012 / 561 / 451 (233 low, 106 mid, 112 high) /
  35 conflicting vectors / 95 under 18 / min age 10 — all match. Every numeric
  token in body prose extracted and checked; no locked number changed. Tables 2
  and 3 script-verified against their CSVs. Clean build: **20 pp, 0 errors,
  0 overfull boxes, 0 undefined citations or references**, 35 citations against
  35 bibitems. The stripped-comment upload variant was rebuilt cold from an
  empty directory with the shipped `.bbl` and no BibTeX run: identical 20 pp,
  identical byte length, 0 leaked comment lines.

  **`paper/ARXIV_SUBMISSION.md` IS NOW STALE AND MUST BE REGENERATED BEFORE
  UPLOAD.** It names fifteen upload files and omits `sections/conclusion.tex`;
  it says nine input targets (now ten), 19 pp (now 20), 609826 bytes (now
  679581), and 34 bibitems against 34 cite keys (now 35 — that one was already
  stale before this pass). The build recipe itself is fine: it globs
  `paper/sections/*.tex`, so the new file is picked up automatically, and the
  comment-strip `sed` catches every new header line. Not fixed here because the
  pass was scoped to `paper/sections/`.

  **Gate A still blocks the v1.0.0 tag and this pass does not touch it.** The
  author's end-to-end read has still not happened, and this pass added a new
  section and two new tables that no human has read.

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

- **2026-09-03 #40 — Figure 1 composite is LaTeX-native, superseding #39(a).**
  #39 required the composite to be generated by `src/render.py` so it would
  regenerate with every other artifact. Built instead with the `subcaption`
  package: three `\subcaptionbox` panels (clinician spanning the width above,
  ASHA card and mother's lamp scaled to a common 52 mm height below), one
  shared `\caption` and one `\label{fig:tiers}`, reading the three committed
  PNGs through the existing `\graphicspath`. Rationale: #39's real
  requirements were determinism, composition rather than re-rendering, and no
  new claim. LaTeX composition satisfies all three and is *more* deterministic
  than a generated PNG — it produces no new artifact, so #39(d) is moot and
  Reproducibility's gate list is unchanged, and it touches no SHAP, model or
  renderer code. The three source PNGs are byte-unchanged. The panels' aspect
  ratios (clinician 1.64, ASHA 1.50, mother 0.44) cooperate with a 2-up
  layout, so the fallback stitching script #39 anticipated was not needed.
  Caption states row 66, true mid-risk, 0.487/0.499, the full split to the
  clinician and the red withheld from the mother's channel and no other; it
  introduces no number the Three Tiers prose did not already state. Passed
  `/anti-ai`, which caught the first draft cloning the body paragraph
  verbatim; rewritten to carry the same facts in its own words.

- **2026-09-03 #41 — Local MiKTeX toolchain; three preamble fixes to make the
  first build clean.** MiKTeX 25.12 installed per-user via winget, so the
  paper no longer depends on Overleaf to compile (`winget uninstall
  MiKTeX.MiKTeX` reverses it). Three preamble additions, all layout-only,
  no prose touched: (a) `lmodern` — MiKTeX basic under `[T1]{fontenc}` falls
  back to bitmap EC fonts, which `microtype` cannot expand; this was a fatal
  error, not a warning, and bitmap fonts would also have failed arXiv;
  (b) `emergencystretch=3em` — cleared all three overfull hboxes, which were
  unbreakable `\texttt{}` filenames spilling up to 61 pt into the margin,
  at the cost of four cosmetic underfull lines; (c) raised `\topfraction`
  to 0.92 and pinned `\@fptop` to 0 pt — Figure 1 fills ~85% of the text
  block so it takes a float page, and the stock centred float page opened a
  dead band above it. Also corrected eight non-standard month macros in
  `refs.bib` (`June`/`July`/`Sept` are undefined in BibTeX; `Jun`/`Jul`/`Sep`
  are the defined ones). This is a metadata field only — no key, title,
  author, year or DOI changed, and the file stays at 31 entries.

- **2026-09-03 #42 — Cosmetic/layout pass; no claim, number or citation
  touched.** Five items, all verified against the rendered PDF rather than
  the log alone. (a) Figure 1 moved from `[tbp]` to `[t!]`. It fills ~85% of
  the text block, which exceeds `\floatpagefraction`, so LaTeX had been
  giving it a page of its own with the lower third blank; `!` overrides the
  placement fractions and makes it a top float with Section 4.4 flowing
  beneath. Kept — the reclaimed space is real and the figure did not shrink
  or split. (b) Title set `\bfseries`, size left at the class default; three
  bold lines read solid, not heavy, so no compensating change was made.
  (c) CRediT reformatted to one line per author with CRediT capitalization.
  NOTE for the authors: of Aditi Patil's four roles only *Validation* is an
  official CRediT term; *Clinical domain expertise*, *Hindi authoring and
  review* and *ASHA-tier design input* are custom descriptors. Left exactly
  as the authors worded them — a co-author's attribution is not a layout
  decision. (d) Keywords line added inside the `abstract` environment so it
  keeps the abstract's measure; `article` has no keyword hook, so it is a
  bold run-in label. Six terms, each tracing to a real section. Passed
  `/anti-ai`, clean, no rewrite needed. (e) `microtype` was ALREADY in the
  preamble and had been since the first draft, so there was nothing to add
  and the four underfull hboxes are its output, not its absence — the count
  is unchanged at four and this line supersedes any expectation that loading
  it would drop them. Page count unchanged at 17; log still shows zero
  errors, zero warnings, zero overfull boxes.

- **2026-09-03 #43 — P5 closed; P6 pre-submission pass opened.** Closing P5
  asserts exactly this: every section is drafted, the manuscript compiles
  clean (17 pp, no errors, no warnings, no undefined references, no overfull
  boxes), Figure 1 is the three-tier composite it was always specified to be,
  all 31 citations resolve, and the whole thing is pushed. It asserts nothing
  about quality, because **no human has yet read the rendered PDF end to
  end** — that is deliberately the first P6 gate rather than a P5 leftover,
  so it cannot be skipped on the way to a tag. P6 is ordered into three gates
  (content, cold run, packaging) with a rule that a later gate does not open
  before an earlier one closes; the reasons are that a cold run against
  moving prose is wasted and a tag before a cold run tags something
  unverified. Two standing items were confirmed CLOSED and should not be
  reopened: #24a calibration, answered in `limitations.tex`, and the
  `failure_mode` triptych, cut at #33 and reaffirmed at #38. Two remain open
  and are now numbered gates: #23 (pull Mamun et al., the novelty and leakage
  check) and #24b (decide Clark et al., which would take `refs.bib` to 32 and
  requires the paper to have been read, not merely resolved). The duplicated
  "standing items" paragraphs that had accumulated in this file were
  consolidated into that gate list; no item was dropped in the merge.

- **2026-09-03 #44 — arXiv packaging blocker recorded before it bites.**
  `main.tex` sets `\graphicspath{{../results/figures/}}` so the manuscript can
  read the renderer's committed output in place, which is right for this repo
  and keeps Figure 1 pointing at the real artifacts rather than a duplicated
  copy. It does not survive arXiv, which builds from a self-contained upload
  where a `../` path escapes the submission root. Decision: fix at PACKAGING
  time, not in the repo — copy the three committed PNGs beside the sources in
  the upload and drop or repoint `\graphicspath` there. Rejected: restructuring
  the repo so `paper/` holds its own copies of the figures, which would create
  a second copy that can drift from the renderer's output and would weaken the
  determinism guarantee the Reproducibility section makes. The source PNGs are
  not re-rendered for this. Recorded now because it is invisible until an
  upload fails and easy to misdiagnose as a missing-figure error.

- **2026-09-03 #45 — #44 closed by graphicspath ORDER, not by a packaging-time
  edit; arXiv package verified by standalone compile.** `main.tex` now sets
  `\graphicspath{{./}{../results/figures/}}`. Both of #44's constraints hold and
  the packaging step gets simpler than #44 anticipated. In the repository `./`
  (= `paper/`) holds no PNGs, so the figures still resolve from the renderer's
  committed output and no second copy is tracked — the determinism guarantee is
  untouched and #44's rejection of restructuring stands. In an arXiv upload the
  three PNGs sit beside the sources, `./` matches first, and the `../` entry is
  never consulted, so nothing escapes the submission root. **Consequence: the
  upload needs no source edit at all**, superseding #44's "drop or repoint
  `\graphicspath` there" instruction while leaving its decision intact.
  Rejected: committing the PNGs under `paper/`, for exactly #44's reason.
  **Verified, not asserted.** The twelve tracked sources plus the three PNGs,
  fifteen files, were copied into an empty directory holding no `.aux`, `.log`, `.out` or
  `.pdf`, and compiled with `pdflatex` alone, three passes, no BibTeX run —
  what arXiv actually does. Result: 17 pp, 0 errors, 0 overfull boxes, no LaTeX
  warnings, all 31 citations resolving from the shipped `.bbl`, and a PDF
  byte-size identical to the in-repo build. Also this session: `\clearpage`
  before the bibliography, so References opens at the top of p14 instead of at
  the foot of p13 — still 17 pp, so the page came free. `main.bbl` was NOT
  rebuilt; a BibTeX run returned it byte-identical, because no citation moved.
  `refs.bib` stays at 31 entries and the three source PNGs are byte-unchanged.
  Sweeps run and clean: 31 cite keys = 31 `refs.bib` entries = 31 `\bibitem`,
  zero orphans either way; no absolute path in any `.tex`; no `\input` outside
  `paper/`; eleven packages, all standard TeX Live; every numeric token in
  `abstract.tex` and `intro.tex` also present in a body section; the oversell
  grep returns only the two known false positives. `paper/ARXIV_SUBMISSION.md`
  written — categories, licence, plain-text title/authors/abstract, file list,
  build commands and the known-warnings note. Its abstract is a de-LaTeX'd
  transcription, verified word-for-word identical to `sections/abstract.tex`
  after stripping `$` and `\emph{}`, and pure ASCII with straight quotes. The
  Zenodo concept DOI is deliberately kept OUT of the arXiv DOI field, which is
  for a journal DOI of this same article; it stays in the back matter. The file
  passed `/anti-ai` (five negative-parallel constructions cut to one, prose
  em-dashes to zero, and one overclaim about arXiv's TeX Live narrowed to what
  the compile actually proved). **This closes no other P6 gate.** Nobody has
  read the PDF end to end (Gate A) and no cold run has happened (Gate B); both
  still block the v1.0.0 tag.

- **2026-09-04 #46 — repo made public-ready; CLAUDE.md untracked, STATE.md
  deliberately kept.** The repository goes public alongside the arXiv
  submission, so the tree was sorted into what a public reader needs, what is
  provenance, and what is working scaffolding.
  **STATE.md stays tracked, and this is the load-bearing decision.** It is the
  design-decision record the paper's honesty rests on: it is where the leakage
  measurement, the 0.15 threshold's status as a design constant, the once-moved
  grade-inflation guard (#16) and the five in-role defects (#11) are recorded
  with their rejected alternatives. A reader who wants to know whether a number
  was reasoned into place or reverse-engineered has to be able to read it, so
  the new README points at it by name and frames it as provenance.
  **CLAUDE.md untracked and gitignored**, history retained. It is the operating
  contract for the assistant rather than something a public reader needs, and
  every constraint in it that bears on the paper is already restated in
  STATE.md or in the `main.tex` header blocks. Untracked rather than deleted:
  `git log` still shows the rules the work was done under, so the process stays
  auditable. **`.claude/commands/anti-ai.md` and `.claude/settings.json` stay
  tracked by author decision** — `settings.json` is one of the three
  enforcement points for #5 (no AI-attribution trailers) and `anti-ai.md` is
  the gate CLAUDE.md #8 ran prose through, so both are mechanism behind a
  process the paper describes.
  **`related_work.md` (root) stays tracked, and this is no longer a judgment
  call.** `main.tex` names it by section number in six comment lines, including
  the outline map #25 forbids deleting, and four section files cite it as their
  SOURCE. It is cited by the paper, so the no-removal guardrail settles it.
  #31 already deleted the duplicate that used to sit in `paper/`.
  Also removed: four zero-byte `.gitkeep` placeholders made redundant by
  tracked content in their directories, and an empty untracked `agents/`.
  `models/.gitkeep` was KEPT — `models/*.joblib` is gitignored, so it is the
  only thing holding that directory. `.gitignore` broadened to cover editor and
  OS junk and to replace the single scaffold filename with `*.zip` / `*.tar.gz`,
  which also catches the arXiv upload tarball.
  **README rewritten** for a reader arriving from the preprint: the thesis in
  the paper's own terms, the four disclaimers up front, links (paper, an
  explicit `arXiv:XXXX.XXXXX` placeholder to fill after submission, the Zenodo
  concept DOI, the dataset), the five gates with the determinism guarantee and
  the gTTS exception, a repo map, CRediT roles and licences. The old Roadmap
  table was dropped: P0–P6 is internal project structure and STATE.md carries
  it in more detail. Passed `/anti-ai` — eight negative-parallel constructions
  cut to the two that encode real technical distinctions, three prose em-dashes
  removed, one sermonising closer trimmed; the firewall grep returns zero hits
  and every number traces to a committed table. The README states no count of
  Decision Log entries, deliberately, because such a count invalidates itself
  on the next entry.
  **Nothing cited by the paper was touched:** zero content diff across
  `paper/main.tex`, `refs.bib`, `main.bbl`, `main.pdf`, `paper/sections/` and
  all of `results/`. The clean-checkout arXiv build was re-run after the
  cleanup and still passes — 15 files, `pdflatex` alone, 17 pp, 0 errors, 0
  overfull boxes, 0 warnings, PDF byte-size unchanged. Tracked files 73 -> 68.
  **This closes no P6 gate.** Gate A (the author read) and Gate B (the cold
  run) remain untouched and still block the v1.0.0 tag.


- **2026-09-08 #47 — Journal-alignment framing pass, on branch
  `revision/sncs-framing`. Emphasis only.** The manuscript is being prepared
  for **SN Computer Science** (Springer Nature) alongside the arXiv posting.
  One source serves both: no publisher template, no reference-style
  conversion, no bibliography reordering. Those belong to a later phase and
  doing them now would break the arXiv build for no gain.
  **The load-bearing line first: no number changed, no result changed, no file
  under `src/` or `results/` was touched, and no disclaimer was removed.**
  Verified mechanically rather than asserted. A numeric-token multiset diff of
  every section against `main` returns **zero tokens lost**; the cite-key diff
  returns **zero keys removed**; and `limitations.tex`, `three_tiers.tex`,
  `related_work.tex` and `reproducibility.tex` are **byte-identical to
  `main`**, which is where the honest caveats live.
  **What changed, and why.** The target journal reviews "from a sound science
  perspective", so this pass makes the contribution land as hard as the
  caveats already did, without laundering either into the other.
  (a) **Abstract restructured** to Purpose / Methods / Results / Conclusion
  and held at exactly **250 words**, the ceiling of the journal's 150–250
  band. The caveats moved *earlier*, into Methods and Results beside the
  things they bound, and the abstract now closes on what the artifact
  delivers. All eight disclaimers survive, and `abstract.tex` carries the
  checklist as a comment so a later edit cannot quietly drop one. Supersedes
  #38's 235-word count; it still opens on the failure, now inside Purpose.
  (b) **The Introduction's three claims are a labelled Contributions list** —
  MECHANISM, ARTIFACT, MEASUREMENT — so a computer-science reader can see
  what kind of object each one is. The claims are unchanged in substance and
  the disclaimer paragraph still sits in the same passage as them.
  (c) **The leakage audit reads as a peer of the abstention rule**, tied to
  the reproducibility literature the body already cites (Kapoor and
  Narayanan; Rosenblatt et al.), and its subsection heading now names it:
  "A leakage-aware re-benchmark". The pinned contribution stack is unchanged,
  item 1 is still the thesis and the title, and the claim is still **the
  measurement and never the discovery** (#23 stands).
  (d) **Section 1.2 states an explicit evaluation contract**: a design and
  measurement contribution, an artifact validated by formative inspection, a
  leakage effect quantified, and efficacy out of scope and ethics-gated.
  (e) **Section 5's two instruments carry citations for the first time.** The
  section named WCAG 2.1 and Nielsen's heuristics and cited neither, leaving
  a methods claim standing on nothing, which is the first thing a
  sound-science reviewer pushes on. `refs.bib` goes **31 -> 34**. The added
  paragraph gives the METHOD standing and does not upgrade what the method
  proves: the "not user testing and it is not validation" paragraph is
  untouched, and the `evaluation.tex` diff has **zero deleted lines**.
  **Citation gate extended visibly rather than quietly.** Nielsen and Molich
  1990 (10.1145/97243.97281) and Nielsen 1994 (10.1145/191666.191729) were
  resolved against Crossref and their BibTeX emitted by Crossref's transform
  endpoint, exactly as the other 29 were. Nielsen 1994 is the right second
  entry because `src/evaluate.py` rates against the refined **ten**
  heuristics, checked in the source this session rather than assumed.
  **WCAG 2.1 fits none of #28's three schemes**, because it is a standard and
  not a paper. It is admitted on a stricter basis than the gate asks for: the
  W3C Recommendation IS the primary record, and it was fetched in-session
  from `w3.org/TR/WCAG21/` with its status, its date (06 May 2025) and its
  editor list read off the document. Also recorded in the `refs.bib` header.
  **Declarations added**, where Springer requires them, before the reference
  list. Funding (none received), Competing Interests (none), Ethics Approval
  (no human participants, public CC BY 4.0 dataset, approval not required and
  not sought), Consent (not applicable). The two pre-existing statements,
  Data and Code Availability and the CRediT contributions, are **unchanged in
  wording** and now sit as subsections under the same `Declarations` heading.
  #42's note stands: three of Aditi Patil's four CRediT roles are custom
  descriptors and remain the authors' call, not a formatting decision.
  **Generative-AI-in-writing declaration: disclosed, and it stays.** Springer
  Nature exempts only AI-assisted *copy editing* from disclosure. Drafting is
  not copy editing, and this repository's own record (#25, #34, #38) shows
  sections drafted in assisted sessions, so a statement that the prose is
  unassisted would have been false. An undisclosed assistance that surfaces
  later is a far worse problem than a disclosed one, which Springer does not
  treat as a ground for rejection. The declaration's closing sentence is
  load-bearing for a separate reason: it stops a reader conflating how the
  PAPER was written with what the SYSTEM does, and the system's
  no-model-at-inference property is one of the three contributions.
  **Do not "clean this up" in a later session.** This is orthogonal to #5,
  which bans AI *commit trailers*; #5 is untouched and no trailer was added.
  **Consequences to absorb.** The paper is **18 pp, up from 17**, from the
  added prose and the Declarations block. No page cap applies: SN Computer
  Science sets none and neither does arXiv. `paper/main.bbl` and
  `paper/main.pdf` were regenerated because `refs.bib` moved, since shipping
  a stale `.bbl` would give the arXiv build three undefined citations.
  `paper/ARXIV_SUBMISSION.md` was refreshed: its abstract transcription, its
  page count and its 31/31/31 citation line all went stale the moment the
  abstract changed, and leaving them would have put the OLD abstract on the
  arXiv form. Its abstract block is again a mechanical de-LaTeX of
  `sections/abstract.tex`, pure ASCII, verified word-for-word.
  **Verified this session rather than asserted.** The in-repo build and a
  15-file fresh-directory build with `pdflatex` alone against the shipped
  `.bbl`, which is what arXiv actually does, both give **18 pp, 0 errors, 0
  overfull boxes, 0 undefined citations or references and 0 LaTeX
  warnings**, with the same four cosmetic underfull hboxes #41 documented.
  34 cite keys = 34 `refs.bib` entries = 34 `\bibitem`, no orphans either
  way. The oversell firewall grep is clean: no banned phrase, no named
  condition, and the only "clinically validated" hit is `limitations.tex`
  saying there is none. `/anti-ai` was run over every new passage: a
  near-verbatim echo of Related Work's "fluency and coverage" line was cut,
  along with a doubled word, a number-agreement slip and two negative-parallel
  constructions. The three surviving "X, not Y" constructions in the abstract
  are each a required disclaimer and are kept on #46's precedent.
  Sentence-length spread stays wide, which is the opposite of what the gate
  flags: intro stdev 10.8 over 7 to 42 words, evaluation 11.4 over 4 to 57.
  **This closes no P6 gate.** Gate A (the author read) and Gate B (the cold
  run) remain untouched and still block the v1.0.0 tag, and the read is now
  against an 18 pp PDF rather than the 17 pp one #43 described. **Branch not
  merged and not pushed**, by instruction.

- **2026-09-08 #48 — Title page completed and abstract trimmed for margin.
  Two compliance items and one safety cut, on `revision/sncs-framing`.**
  **No result number changed and no file under `src/` or `results/` was
  touched.** Verified the same way #47 was: a numeric-token multiset diff of
  every section against the previous commit (21979ae) returns **zero tokens
  lost and zero gained**. All eight abstract disclaimers survive, checked
  item by item against the checklist pinned in `abstract.tex`.
  **(a) Title page.** SN Computer Science requires city and country on every
  affiliation and an active e-mail plus ORCID clearly bound to the
  corresponding author; a submission missing either is returned as incomplete,
  so this is compliance rather than polish. Maitreya Sapariya is now
  *Independent Researcher, Surat, India*, with the e-mail added to the
  existing corresponding-author `\thanks` footnote alongside the ORCID that
  was already there, which keeps both bound to the right author.
  **Aditi Patil's location is `Vadodara, Gujarat, India`, CONFIRMED by the
  co-author on 2026-09-08** — the phase brief had asked for a
  `% TODO CONFIRM` marker pending her sign-off, and that marker was
  deliberately **not** added because the confirmation arrived in the same
  instruction. Leaving a "pending" comment in the source against a fact the
  co-author had already settled would have been inaccurate, and a stale TODO
  is worse than none. The confirmation and its date are recorded as a source
  comment above the author block instead. Her institution string is otherwise
  untouched. Nothing publisher-specific is used: both are ordinary title-page
  facts and the arXiv build is unaffected.
  **(b) Abstract trimmed 250 -> 237 words.** 250 sat exactly on the journal's
  ceiling, where a word-counter that counts the four run-in labels or splits a
  hyphenated term could bounce it. The Purpose / Methods / Results /
  Conclusion structure is unchanged and every number stays. Three cuts, all
  redundant connective phrasing rather than content: the second *no language
  model at inference*, which is kept in Conclusion where it is the
  contribution instead of a restatement of the mechanism; *of an uncertain
  prediction*, which the two preceding sentences already establish; and a
  second *our own*, which Methods already carries. Passed `/anti-ai`, which
  caught the one real defect the trim introduced — dropping *of an uncertain
  prediction* left "each reader" with no antecedent, Purpose having named a
  clinician and a mother rather than readers of anything, so the sentence now
  reads *what each of them is entitled to be told*. Sentence-length spread
  stays wide at stdev 6.4 over 7 to 30 words, against the flat 15-25 band the
  gate flags.
  **Verified this session rather than asserted.** In-repo build and a 15-file
  fresh-directory build with `pdflatex` alone against the shipped `.bbl` both
  give **18 pp, 0 errors, 0 overfull boxes, 0 undefined citations or
  references and 0 LaTeX warnings**, with the same four cosmetic underfull
  hboxes #41 documented. `main.bbl` is unchanged because no citation moved;
  only `main.tex`, `sections/abstract.tex` and the regenerated `main.pdf`
  differ. `refs.bib` stays at 34 entries.
  **This closes no P6 gate.** Gate A (the author read) and Gate B (the cold
  run) remain untouched and still block the v1.0.0 tag. Remaining SN Computer
  Science work is the template phase — `sn-jnl.cls`, the Springer reference
  style, editable source files — and is deliberately not started, so the
  manuscript stays arXiv-clean until then.

- **2026-09-09 #49 — arXiv moderation repositioning.** Prompted by the
  ADS-Cascade desk-reject and by an observed acceptance (Naisha, cs.CR): arXiv
  triage reads the shopfront, not Section 6. Emphasis, title page and
  packaging only. **No claim, number or citation changed.** `refs.bib` stays
  at 34 entries and `main.bbl` is untouched.
  **(a) Title names the artifact.** *A Coin Flip Is Not a Red Light: Grading a
  Maternal-Health Risk Alarm...* becomes *Three Voices: Uncertainty-Gated
  Rendering of a Maternal-Health Risk Alarm for Mothers, Community Health
  Workers, and Clinicians*. 127 characters, pure ASCII, no macro, not
  all-caps, which is what `prep.html` asks of the title field. The coin-flip
  framing already lives in the Introduction's third paragraph and stays there.
  **(b) Abstract restructured to three unlabelled paragraphs.** Artifact and
  mechanism first, scope limits second, leakage measurement last. This
  SUPERSEDES #47/#48's Purpose / Methods / Results / Conclusion labelling,
  which SN Computer Science requires and arXiv does not; the labelled 237-word
  version is recoverable from commit 6993541 and is restored before the
  journal submission. Two deliberate changes beyond the reframing: the
  novelty-boundary sentence moved from the end of paragraph 1 to the end of
  paragraph 2, because arXiv's moderation page names *originality, novelty,
  significance* as a decline ground and the last line of the opening paragraph
  is where a moderator skimming for what is new will land; and one sentence
  was ADDED naming the archived, regenerable artifact, which is the paper's
  primary-research evidence and had no place in the abstract before. All eight
  disclaimers on abstract.tex's checklist survive, verified item by item.
  **(c) `/anti-ai` caught a firewall breach, not just a style tell.** The
  proposed abstract dropped *gated on ethics* from the user-studies sentence,
  which is checklist item (4). Restored. The gate also fixed a stacked triplet
  (the deposit holds four things, so it now names four), a 45-word single-
  sentence paragraph split into three, *the benchmark we use* named as the UCI
  Maternal Health Risk benchmark, and *a critique that found and fixed five
  defects*, which credited the instrument with the repair.
  **(d) Affiliation updated.** Maitreya Sapariya moves from *Independent
  Researcher, Surat* to *Department of Information Technology, A. D. Patel
  Institute of Technology (ADIT), Charutar Vidya Mandal (CVM) University, New
  Vallabh Vidyanagar, Anand, Gujarat, India*, corresponding e-mail
  `12202120601029@adit.ac.in`. Changed in `main.tex`, `ARXIV_SUBMISSION.md`
  and `README.md`. Aditi Patil's affiliation is untouched.
  **(e) `%` comments are stripped from the UPLOAD, not from the repo.** arXiv
  publishes raw `.tex` source, and 155 of `main.tex`'s 216 lines are working
  notes containing, in these words, `EXPLICITLY NOT CLAIMED AS NOVEL`, `There
  is no ML novelty here`, `Do not claim the mechanism` and `OVERSELL
  FIREWALL`. Those notes are why the manuscript is honest and they stay in the
  repository, but publishing the authors' own internal case against their
  novelty, to a moderator who declines on that exact ground, is a needless
  loss. `ARXIV_SUBMISSION.md`'s packaging block gains one line-oriented `sed`
  that deletes only lines whose first non-space character is `%`, so the
  line-joining `%` at the end of three_tiers.tex's `\subcaptionbox` lines
  survives.
  **(f) Three stale claims in `ARXIV_SUBMISSION.md` corrected.** It asserted
  *arXiv runs LaTeX but not BibTeX*; `submit_tex.html`, fetched 2026-09-09,
  says arXiv "provides support for bib file processing using various
  processors like `biblatex`... and `bibtex`" and blocks a submission carrying
  neither a `.bbl` nor the `.bib` it needs. Shipping the `.bbl` stays right;
  the reason given was wrong. The same page requires the `.bbl` to be named
  for the main `.tex`, which `main.bbl` satisfies. Second, the sheet's
  "verified word-for-word identical" abstract transcription still carried
  #47's 250-word text after #48 trimmed the source to 237 — it had been false
  since 2026-09-08. It is now generated from `sections/abstract.tex` rather
  than retyped. Third, the page count.
  **Verified this session rather than asserted.** All 34 citation identifiers
  re-resolved: 31 against the Crossref API with title, first author and year
  read off each record, plus arXiv 1909.03012, PMLR `v119/mozannar20b` and the
  W3C WCAG 2.1 Recommendation. 34 `\bibitem` against 34 `\cite` keys against
  34 `refs.bib` entries, no orphans — note that a line-oriented grep
  undercounts to 32, because `evaluation.tex` cites the two Nielsen keys in a
  `\citep` that spans a line break. Fresh 15-file directory, `pdflatex` three
  passes, no BibTeX, run for the stripped and unstripped variants both:
  **19 pp, 0 errors, 0 overfull boxes, 0 undefined citations or references**,
  the same four cosmetic underfull hboxes #41 documents, identical file length
  and identical content streams between variants. The count moved 18 -> 19
  because the four-line affiliation and the longer abstract push references
  [30] to [34] onto their own page, which is a third full rather than a stub.
  Comments field updated to 19 pages. Zenodo concept DOI
  `10.5281/zenodo.22252076` re-confirmed in all four places it appears:
  `backmatter.tex`, `reproducibility.tex`, `ARXIV_SUBMISSION.md` and
  `README.md`. Firewall re-run clean: no `novel`+`framework` adjacency in
  manuscript prose, `red to green` appears only negated, no named condition,
  formative framing intact in both abstract and intro.
  **Policy checked against live arXiv pages, not memory.** The cs review /
  survey / position rule (blog, 2025-10-31) requires prior acceptance plus
  journal-ref and DOI in metadata, and workshop review does not qualify. It
  binds cs.HC. This manuscript is not a review or a position paper: it ships a
  released system, a quantified benchmark measurement and a structured
  evaluation instrument, and the repositioning is meant to make that legible
  at a skim. The full-English requirement (in force 2026-02-11) is satisfied.
  Springer Nature permits preprint posting, so arXiv does not forfeit SN
  Computer Science. Endorsement: the corresponding author is already endorsed
  for cs, confirmed by the author this session.
  **OPEN — the Introduction is NOT repositioned.** The session prompt referred
  to three intro diffs (a), (b), (c) and an optional triplet tweak that were
  lost when the prior session was cleared. `sections/intro.tex` is byte-for-
  byte unchanged in this commit. It must be revisited before submission.
  **This closes no P6 gate.** Gate A (the author read) and Gate B (the cold
  run) remain untouched and still block the v1.0.0 tag.

- **2026-09-09 #50 — Introduction: coin-flip line moved from the title.**
  Supersedes #49's "the Introduction is NOT repositioned" in part. The
  Introduction now opens on **"A coin flip is not a red light."** That sentence
  was the manuscript's title until #49 renamed it to name the artifact, and
  without this line the phrase appeared nowhere in the paper. The third
  paragraph already pays it off, so it reads as a claim stated and then earned.
  One added line. No claim, number, citation or disclaimer changed.
  **Considered and rejected:** renaming the two subsection headings ("What we
  claim, and what we do not", "What kind of evidence this is") to look less
  like a position paper. The section structure is already research-shaped —
  Related Work, Data, Method, Evaluation, Limitations, Reproducibility — and
  the honest headings are worth more than the cosmetic gain.
  **STILL OPEN:** the three intro diffs (a), (b), (c) from the cleared session
  remain unrecovered. `git show 6993541:paper/sections/intro.tex` returns the
  file whose own (a)(b)(c) comment describes the already-applied #47 pass, so
  it does not recover them. Only the coin-flip move was specified well enough
  to act on.
  **Verified:** repackaged and rebuilt from the extracted tarball — 15 files,
  0 leaked comment lines, 19 pp, 0 errors, 0 overfull boxes, 0 undefined
  citations or references, 0 LaTeX warnings. No dot-prefixed files in the
  archive (arXiv deletes those on announcement) and `\date{}` is empty, so no
  `\today` to drift on rebuild.

- **2026-09-09 #51 — Two moderation facts that raise the bar, recorded so a
  future session does not rediscover them.** Both from arXiv's own moderation
  and content-type pages, fetched 2026-09-09.
  **(a) A prior decline means closer scrutiny.** arXiv states: "Submitters who
  have had works previously delayed or declined by arXiv should anticipate
  closer scrutiny on future submissions. In some cases, authors may be required
  to establish a conventional publication record." The corresponding author has
  a recent decline, so this submission is read against a higher bar than a
  first-time one. That is the case for the #49/#50 repositioning, not an
  argument against submitting.
  **(b) "Undergraduate or high-school research" is a listed content type arXiv
  typically does not accept.** The new corresponding address
  `12202120601029@adit.ac.in` is an enrollment-number address. This needs an
  author decision before submission: the listed exclusion is aimed at course
  projects and coursework write-ups, and this manuscript is not one — it has a
  clinical co-author, a released and archived artifact, a quantified benchmark
  measurement and a structured evaluation — but the affiliation string should
  not invite the reading. Options are to state a department affiliation without
  the enrollment-number address, or to use an address that does not encode
  student status. NOT decided here.
  **(c) Appeals are final and carry no feedback,** and arXiv may require journal
  acceptance before considering one. There is no cheap second attempt, which is
  why the pre-submission audit is worth its cost.

- **2026-09-09 #52 — Corresponding address decoupled from enrollment number.**
  Supersedes #49(d) on the e-mail only. The ADIT / CVM University affiliation
  set in #49 is UNCHANGED and stays in `main.tex`, `ARXIV_SUBMISSION.md` and
  `README.md`. The corresponding address reverts to
  `maitreyasapariya@gmail.com`.
  **Why.** #51(b): arXiv lists "undergraduate or high-school research" among
  content types it typically does not accept, and #51(a): a submitter with a
  prior decline is told to anticipate closer scrutiny. `12202120601029@adit.ac.in`
  encodes an enrollment number. This manuscript is not coursework — clinical
  co-author, released and archived artifact, quantified benchmark measurement,
  structured evaluation instrument — and the fix is to stop inviting the
  reading rather than to argue with it after the fact. Author decision,
  2026-09-09.
  **Better option if it exists:** a name-based `adit.ac.in` alias beats a
  personal address, because it carries the institution as well as the name. One
  line in `main.tex` and one in `ARXIV_SUBMISSION.md`. Not available at time of
  writing.
  **Verified:** repackaged and rebuilt from the extracted tarball — 15 files, 0
  leaked comment lines, 0 dot-prefixed entries, 19 pp, 0 errors, 0 overfull
  boxes, 0 undefined citations or references, 0 LaTeX warnings. Enrollment
  number appears nowhere under `paper/` or in `README.md`.

- **2026-09-09 #53 — FACULTY-REVIEW SNAPSHOT: commit `7346ae4`.**
  (`7346ae47bd040bf0e43c5bf90241aa99a68d58bd`, branch `revision/sncs-framing`.)
  This is the version that goes to faculty. **Not merged to `main`, no PR
  open.** The merge is the last step, after faculty review and the final
  moderation pass — deliberately, so `main` keeps matching the last public
  state until the paper is actually cleared.
  **What landed in the snapshot.**
  (a) *Intro name injection.* "Our response is to make the abstention decision
  part of the rendering rather than part of the model" becomes "Our response,
  **which we call Three Voices**, makes the abstention decision part of the
  rendering rather than part of the model." Plain, no `\emph`, matching the
  abstract, which introduces the name; this is its first binding in the body.
  Both subsection headings left alone, per #50. Paragraph rewrapped to the
  file's ~76-column convention; no other wording moved.
  (b) *Affiliation provenance corrected.* The author-block comment claimed
  Aditi Patil's "city and state" were confirmed on 2026-09-08. She confirmed
  **city (Vadodara) and country (India)**. Gujarat is in the affiliation string
  because it is the state containing Vadodara, not because she confirmed it
  separately. The affiliation string itself is unchanged.
  (c) *Corresponding address stays* `maitreyasapariya@gmail.com` (#52). No
  faculty-style `adit.ac.in` alias was available; skipped rather than chased.
  **`/anti-ai` on the one changed sentence: clean, no rewrite.** No AI
  vocabulary, no triplet, no participial tail, no significance inflation.
  Paragraph burstiness 21/26/15/10 words, outside the flat 15-25 band. The
  "rendering rather than the model" contrast was kept: it carries the thesis
  and it predates this edit.
  **Build, verified cold rather than asserted.** Package rebuilt, extracted
  into an empty directory, `pdflatex` three passes, no BibTeX: 15 files, 0
  leaked comment lines, 0 dot-prefixed entries, 0 aux/output files, **19 pp, 0
  errors, 0 overfull boxes, 0 undefined citations or references, 0 LaTeX
  warnings**. In-repo `paper/main.pdf` rebuilt from the same source and is
  content-identical to the cold build (62 bytes differ, all in the trailing
  timestamp/ID region). That PDF is the faculty package. Citations 34 cited /
  34 in `refs.bib` / 34 `\bibitem`, no orphans in either direction.
  **Moderation gates re-run against this snapshot: LIKELY PASS.** Checks 1, 2,
  3, 5, 6, 7 pass. Two risks stand, both recorded and neither fixed here.
  (i) *Normative register in the Introduction.* Three phrases — "entitled to
  be told" (l.49), "vulnerability" (l.76), "least power" (l.79) — are the
  register a moderator reads as position-paper advocacy; the check skill names
  "what X is entitled to" explicitly. They are confined to the Introduction:
  the **abstract and title carry none of it**, and the shopfront is what triage
  reads. Left alone because Phase A was scoped to two specified diffs, and
  because the phrases are the paper's actual research question. Revisit only if
  faculty flag it.
  (ii) *Prior decline.* Per #51(a) this submitter is read against a higher bar.
  Not fixable, only compensated for.

- **2026-09-09 #54 — FACULTY-REVIEW SNAPSHOT SUPERSEDED: `a119504` replaces
  `7346ae4`.** (`a11950490c08df67f557cea14dfd4f3181a66e9f`.) Still on
  `revision/sncs-framing`, still **not merged to `main`, still no PR**.
  **The manuscript carried a false claim about its own headline mechanism.**
  Four sites said the highest-severity signal is withheld "from the mother's
  channel **and from no other**". It is withheld from the ASHA card as well.
  **The code is the proof, and it is the code we archive and cite.**
  `band_for()` returns one band; `render_asha()` takes that same band and sets
  its header from `BAND_LABEL`. Run this session against the shipped source:
  `band_for("high risk", 0.012)` -> `AMBER` -> header `ELEVATED — needs
  follow-up`; `band_for("high risk", 0.90)` -> `RED` -> header `HIGH — needs
  follow-up`. The gate withholds RED from **both** downstream tiers. Only the
  clinician tier is untouched, and it never calls `band_for` at all.
  **The paper already contradicted itself.** §4.1 defines the alarm as "the red
  lamp and the urgent spoken message for the mother, **the \textsc{high} header
  on the health worker's card**", and §4.2 says the band is computed once and
  shared across all three tiers. The figure caption managed the contradiction
  inside one sentence: "The other two panels carry the derated band instead...
  withheld from her channel and from no other."
  **Fixed in four prose sites** — `abstract.tex`, `intro.tex`, the
  Figure~1 caption, §4.4 — plus the regenerated `ARXIV_SUBMISSION.md`
  transcription (now 1760 chars / 277 words, against the 1920 ceiling).
  **§4.4's "The grading runs against power" also went.** It implied a monotone
  three-level gradient in the abstention. The gate is binary: clinician versus
  the two who cannot interrogate the model. What separates those two is how
  much of the model's state each is asked to hold, not severity — the card
  carries the drivers and a next step, the lamp carries neither.
  **Two sites deliberately NOT changed.** `intro.tex:78` and
  `related_work.tex:84` say the assertions are "graded so that the reader with
  the least power to interrogate the system receives the most conservative
  signal". That remains true: the three *assertions* are graded (raw split /
  header plus drivers plus next step / lamp plus one sentence), and the
  mother's is the least assertive. Only the *gate* is binary, and neither
  sentence claims otherwise.
  **`src/render.py` corrected too**, since it is archived and cited: the
  `RED_MARGIN` comment and the `band_for` docstring both described shared logic
  as mother-only. `band_for`'s docstring now says the band drives both cards
  and carries an explicit note against reintroducing the claim.
  **This was an OVERSELL FIREWALL breach** — the false version made the
  mechanism sound sharper and more novel than it is — and every prior pass
  missed it, including the moderation audits of #53, which checked whether
  claims were *supported* but not whether they were *self-consistent*. It was
  found in external review. Lesson recorded: the firewall needs a check that
  reads the claim against the renderer, not only against the tables.
  **Verified:** cold build from the extracted package — 15 files, 0 leaked
  comment lines, 0 dot-prefixed entries, **19 pp, 0 errors, 0 overfull boxes, 0
  undefined citations or references, 0 LaTeX warnings**; in-repo `main.pdf`
  content-identical to the cold build. `paper/main.pdf` at this commit is the
  faculty package.

- **2026-09-15 #57 — REPOSITIONING PASS: one "Limitations and Future Work"
  section, the contribution type named, and the invented self-label removed.**
  Branch `revision/sncs-framing`, not committed at time of writing. Structural
  and rhetorical only. **No limitation was removed from the paper, no number,
  no citation and no claim changed.** The governing rule for the whole pass:
  *state each limitation once, in the section that owns it, and point from
  everywhere else.* Net honesty constant, net repetition down.

  **Why now.** The census below is the finding. Every disclaimer in the
  manuscript was individually defensible and collectively disabling:

  | disclaimer | sites before | after |
  |---|---|---|
  | "design and feasibility artifact" | 4 | **0** |
  | "formative / single-evaluator" | 4 | 4 (one is the Section 5 title) |
  | "no mother / CHW / clinician has used it" | 3 | 3 |
  | "gated on ethics clearance" | 5 | 4 (one is Declarations, required) |
  | "not evidence that any tier helps" | 3 | 3 |
  | "future work" | 3, no owner | **2, both Section 7 headings** |

  A moderator reading the abstract and page one met self-negation as the
  dominant move. That is arXiv's "lacks originality, novelty, significance"
  decline reason, restated by us, in our own shopfront.

  **(a) Section 6 is now Section 7 "Limitations and Future Work"** and owns
  every forward-looking claim in the manuscript. New final subsection 7.5
  "Future work" collects the three scattered `is future work` tails — one in
  `three_tiers.tex`, two in `limitations.tex`. The factual half of each
  statement stayed exactly where it was; only the forward-looking half moved.
  "Evaluated on a workstation" folded into 7.1 (same limitation family, one
  fewer heading). **The section absorbed a whole new subsection and still came
  out one word SHORTER than before: 719 -> 718 body words**, paid for by
  line-level grammatical compression. Keep it that way.
  *Moderation rationale:* arXiv lists "proposals for future research" among
  content types it does not accept. Future work scattered as three apologies
  leans that way; one bounded subsection is ordinary research convention.

  **(b) "This is a design and feasibility artifact" is GONE from the
  manuscript** — all four sites. That phrase appears in no taxonomy and can
  only read as an apology. The Introduction now names the contribution types
  in HCI's own vocabulary instead: two artifact contributions and one
  empirical one. **New citation, resolved in-session against Crossref per the
  CLAUDE.md gate** (`api.crossref.org/works/10.1145/2907069`, record fetched,
  title / both authors / journal / volume / issue / pages / year / publisher
  read off it): Wobbrock & Kientz, *Research contributions in human-computer
  interaction*, Interactions 23(3):38-44, 2016. `refs.bib` 35 -> 36.
  This is the pass's highest-leverage change and it is also more ACCURATE than
  what it replaced.

  **(c) The abstract no longer ENDS on a disclaimer.** Paragraph 3 reordered:
  the novelty-boundary sentence moved to its head, and the paragraph closes on
  what the work delivers. #49 moved that same sentence out of the end of
  paragraph 1 on exactly this reasoning and did not follow it through to the
  end of the abstract. **All eight checklist items survive**; item (1) is
  restated to "the contribution type is named and no user-validated system is
  claimed", which items (2)(3)(4) already carry. 1827 -> **1824 characters**,
  289 -> 284 words, against the 1920 ceiling.

  **(d) The position-paper risk recorded in #53 turned out to be already
  closed.** #53 left three phrases in the Introduction — "entitled to be
  told", "vulnerability", "least power" — deferred to "revisit only if faculty
  flag it". They are **not in the file**: #56's compression removed them. What
  remains of that register is three uses of "entitled" in `three_tiers.tex`,
  and all three apply to the MODEL or the SENDER, not to a person — a claim
  about evidential warrant, not advocacy. **Kept deliberately.** One genuine
  fix in `related_work.tex`: the novelty claim said the rendering is a
  function of "stakeholder vulnerability"; per #54 the gate actually keys on
  what each reader can interrogate, so it now says that. More accurate, and it
  takes the advocacy word out of the highest-visibility sentence in Section 2.
  *This matters more than #53 knew.* Since 2025-10-31 a cs.* **position paper
  must already have completed peer review**, with documentation, or is
  "likely to be rejected" — so a moderator who files this as a position paper
  DECLINES it rather than holding it, and appeals are final and carry no
  feedback. Had the phrases survived #56, this pass would have removed them.

  **(e) `arxiv/` regenerated — it had silently drifted.** The packaged upload
  set was built 2026-09-11 and **did not contain `sections/conclusion.tex`**;
  `arxiv/main.tex` had no `\input` for it. #56 flagged this as BLOCKING and it
  is now closed. Packaging is now scripted rather than hand-copied: whole-line
  comments only (trailing `%` is load-bearing in `three_tiers.tex`'s subfigure
  block and must survive), and the file list is read off `main.tex`'s own
  `\input` lines so it cannot drift again. 532 comment lines stripped,
  **16 files**, 0 leaked comment lines, 0 dot-prefixed entries.

  **(f) `ARXIV_SUBMISSION.md` regenerated.** Abstract block re-derived from
  `sections/abstract.tex` mechanically, not retyped. Upload list now sixteen
  files. **The Comments field said "1 figure, 1 table" and the paper has
  THREE tables** (`tab:models`, `tab:leakage`, `tab:matrix`, counted from
  `main.aux`) — understated since #56 added two of them. Now "20 pages, 1
  figure, 3 tables".

  **`/anti-ai` run on every changed block** (use case 3.1, academic). Found
  and fixed: one ungrammatical sentence this pass introduced ("reports it
  defects first"), one precious antithesis ("re-asking rather than
  re-asserting"), one broken parallelism ("no field claim, no claim..., and
  none that..."), and one over-compressed ellipsis ("name their own"). Left
  alone deliberately: ~11 instances of "X, not Y" across the changed prose.
  Scope-drawing is this paper's rhetorical job and the construction is precise
  here, not evasive. Burstiness of the new 7.5 is 35/11/39/7 words, well
  outside the flat 15-25 band.

  **Verified, not asserted.** In-repo build: **20 pp, 0 errors, 0 overfull
  boxes, 0 undefined citations or references, 0 LaTeX warnings.** Citations
  reconcile **36 cited / 36 in `refs.bib` / 36 `\bibitem`**, no orphans in
  either direction. Cold build from the regenerated package, extracted into an
  empty directory, `pdflatex` x3 and **no bibtex** (the shipped `.bbl` is
  used, as arXiv would): 16 files, **20 pp, 0/0/0/0**. Oversell-firewall greps
  clean: no `novel`+`framework`, no clinical-validity claim, the Decision Log
  #21 condition name absent.

  **What this pass did NOT do.** No new experiment, no calibration run, no
  symmetric gate implementation — it stays future work, which is the point of
  (a). The Section 1.1 / 1.2 headings are untouched (#50 considered and
  rejected renaming them; that stands). No publisher template, no
  reference-style conversion, no bibliography reordering (#47 defers these).
  Gate A — the author's end-to-end read — is **still open and still blocks the
  tag**, and this pass moved prose, so it needs the read more than before.

- **2026-09-15 #58 — ADVERSARIAL MODERATION AUDIT RUN AGAINST #57, AND THE
  FOUR THINGS IT FOUND.** Full `arxiv-moderator` pass over the regenerated
  upload set, live policy fetched the same day (10 arXiv pages + 2 external).
  **Verdict: SUBMIT, no blocking finding.** No reclassify risk; `cs.HC`
  primary with `cs.LG` cross-list confirmed as earned rather than scattershot.
  Reference integrity independently re-measured: **36 checked / 36 resolved /
  0 failed**, including `wobbrock2016contributions` added hours earlier.
  Abstract 1824 / 1920 characters, pure ASCII. Zero leaked comment lines in
  the upload — the only `%` surviving are the five line-joining ones inside
  `three_tiers.tex`'s subcaption block and four escaped `\%`, which is
  correct. All eight abstract checklist disclaimers verified present after
  #57's reorder.

  **(a) THE FINDING, and it is the #54 defect class again.** `README.md`
  still carried **"withheld from the mother's channel and from no other"** —
  the exact false exclusivity claim that commit `a119504` corrected in the
  manuscript on 2026-09-09, and that `src/render.py:165-169` carries an
  explicit comment warning against. The paper stakes its artifact claim on
  that repo (`backmatter.tex`, `reproducibility.tex` both cite it), so the
  archive of record was asserting what the manuscript disclaims.
  **#54 recorded the lesson as "the firewall needs a check that reads the
  claim against the renderer." The check was added and then run only over
  `paper/`.** CLAUDE.md non-negotiable #8 says the prose gate covers
  "everything under `paper/` **and README prose**"; the README half was not
  swept, by me, in the pass whose entire subject was claim hygiene. Fixed at
  four sites: the exclusivity claim, "stakeholder vulnerability" (the phrase
  #57 removed from `related_work.tex` on the same grounds), the
  "design and feasibility artifact" self-label, and a stale "(17 pp)".
  A fifth, which the audit did not catch: the repo map said `refs.bib` holds
  31 entries; it holds 36.
  **Standing rule from here: any sweep for a claim defect runs over
  `README.md` in the same pass, not as a follow-up.**

  **(b) `\graphicspath` reached above the submission root.** The packaged
  `main.tex` carried `{{./}{../results/figures/}}`. Harmless in fact — the
  cold build resolved all three PNGs from `./` and never consulted the second
  root — but a path-traversal entry has no business in an upload tree. The
  packaging script now narrows it to `{{./}}` in the packaged copy only;
  `paper/main.tex` keeps both roots so the repo build still resolves figures
  from the renderer's committed output with no duplicated copy that can
  drift. Do not hand-edit it back.

  **(c) `ARXIV_SUBMISSION.md` disagreed with itself.** Its Comments field and
  upload list were regenerated in #57; the *verification prose* below them was
  not, and still claimed 34 references, fifteen files and a 19-page PDF.
  Whoever pasted the form would have been reading a document contradicting
  its own numbers. Regenerated to 36 / sixteen / 20 pp, with the
  `\graphicspath` divergence documented so it does not read as an error.
  Comments field also now says "1 figure (3 panels)" — one float, three
  subfigures.

  **(d) SUPERSEDES #56 ON ONE POLICY FACT.** #56 recorded "arXiv never runs
  BibTeX, so they are inert surface." That is **false as of 2026-09-15**:
  `submit_tex.html` states arXiv now processes `.bib` via bibtex/biblatex and
  **blocks a submission carrying neither a `.bbl` nor the needed `.bib`**.
  No effect on this submission — `arxiv/main.bbl` ships, its name matches
  `main.tex`, and the cold build runs `pdflatex` three times with no bibtex —
  but a future session reusing #56's sentence would be reasoning from a
  retired fact.

  **(e) NOT VERIFIED, and it needs the author before a submission window
  opens: the cs.HC endorsement.** #56 records it as confirmed, but that is an
  author claim and no session can check it. The endorsement page fetched this
  run says automatic endorsement now requires **both** a qualifying
  institutional email **and** having claimed ownership of a co-author's
  submission. The corresponding address is `maitreyasapariya@gmail.com`, set
  deliberately by #52 to avoid the enrollment-number reading, and a personal
  address does not satisfy the institutional half. If the standing
  endorsement is real it carries; if the form asks, the route is a personal
  endorsement from an established cs.HC author. **Identify a fallback
  endorser before opening the form, not after.** #52's trade is still the
  right one and should not be reversed — an enrollment-number address against
  the "undergraduate or high-school research" exclusion is the worse
  exposure.

  **Considered and declined:** the audit's suggestion that `intro.tex`'s
  "two artifact contributions — a rendering mechanism and the pipeline that
  implements it" counts one system twice under the Wobbrock & Kientz
  taxonomy. The reading is arguable and the audit rated it "very low"
  confidence, but collapsing it to one artifact contribution costs the
  three-item stack that `main.tex`'s CONTRIBUTION STACK pins. Left as is;
  recorded here so the next session does not rediscover it as novel.

  **Also confirmed by the audit, worth keeping:** the three surviving uses of
  "entitled" in `three_tiers.tex` hold up to a hostile read — each predicates
  evidential warrant on the model or the sender, never a person's claim on
  anyone, and `:116-117` is load-bearing justification for departing from the
  risk-communication literature. The 60-second cold triage reads as a
  research paper, not a position paper. The prior decline was a different
  paper, so no declined text is being recycled.

  **Verified after (a)-(c): cold build from the repackaged set, extracted into
  an empty directory, `pdflatex` x3 and no bibtex — 16 files, 20 pp, 0
  errors, 0 overfull boxes, 0 undefined citations or references, 0 LaTeX
  warnings, and all three PNGs confirmed loaded from `./`.**

  **Gate A — the author's end-to-end read of the 20 pp PDF — remains OPEN and
  still blocks the tag.** Nothing in this audit substitutes for it. Nothing in
  #57 or #58 has been committed, tagged or uploaded.

- **2026-10-09 #59 — PRE-REGISTRATION: out-of-fold probabilities for all 451
  records, and what the gate does with them. Written and committed BEFORE
  anything below is computed.** (#57 and #58 were committed first, as
  `c657617`, so this entry sits on a clean baseline.)

  **Why.** Every case probability the paper quotes is in-sample:
  `src/explain.py:126-127` fits the forest on all 451 rows and then predicts
  those same rows. Rows 66 and 382 each share their six-feature vector with a
  row carrying a different label (66/156 mid/high, 382/403 low/high), so their
  near-ties are what a forest does with a label conflict it was trained on.
  Nothing in the repository says how the vehicle scores records it was NOT
  fitted on. This entry fixes, in advance, what will be measured.

  **What will be computed**, inside the existing `python -m src.model`, after
  every existing output is written and without touching `evaluate()`:
  (a) **Out-of-fold class probabilities for all 451 deduplicated records** from
  `FINAL_MODEL` (random forest, no resampling, `n_estimators=300`,
  `random_state=42`), each pipeline built by `_build_pipeline` exactly as
  `evaluate()` builds it, over the identical splitter
  `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`. A plain fold
  loop, equivalent to `cross_val_predict(method="predict_proba")`, because (c)
  needs the fold models themselves. Row indexing is `prepare_modeling_frame`'s
  reset index, the one `explain.py` and the paper's row numbers use. `pred` is
  the argmax; `margin` is top-one minus top-two, as at `explain.py:100`.
  **Consistency check, also fixed in advance:** the pooled out-of-fold
  confusion matrix must equal the summed confusion matrix `evaluate()` reports
  for RF/none (high row `[14, 17, 81]`, per "Model" above). If it does not,
  stop and report rather than proceed.
  (b) **Bands from the existing `render.band_for` and `RED_MARGIN = 0.15`,
  imported, not reimplemented.** The import is local to the new function,
  because `src/render.py:46` imports `src.model`.
  (c) **`explain.select_cases` itself, imported and called on the out-of-fold
  probabilities**, to see which rows its four criteria pick. For
  `boundary_mid`'s driver condition (#1 |SHAP| for the predicted class is BS or
  SystolicBP) the SHAP values come from the **fold model that produced each
  row's out-of-fold probability**: `shap.TreeExplainer` on that fold's forest,
  over its held-out rows. Author decision, 2026-10-09.
  (d) **Sensitivity of band counts at margins 0.10 / 0.15 / 0.20, reported
  only.** `band_for` is reused with `render.RED_MARGIN` patched for the call
  (`unittest.mock.patch.object`) and restored afterwards.

  **Outputs, two new files only.** `results/tables/p1_oof_predictions.csv`:
  one row per record with `row_index, true_label, p_low, p_mid, p_high, pred,
  margin, band, conflict_vector, twin_rows` (`twin_rows` = the other indices
  sharing the six-feature vector, `;`-separated, empty if none).
  `results/tables/p1_gate_summary.csv`: band x true label; predicted-high
  total, RED, and derated-to-AMBER by true label; true-high records reaching
  RED / AMBER / GREEN; predicted-low with margin < 0.15 by true label; band x
  true label split by `conflict_vector`; band counts at 0.10 / 0.15 / 0.20; and
  a `case_selection` section holding (c)'s four picks (author decision,
  2026-10-09).

  **What does NOT change as a result, whatever the numbers show.** No
  threshold, no model, no band rule, no selection criterion. `RED_MARGIN` stays
  0.15, `FINAL_MODEL` stays RF/none, and the four case rows that `explain.py`,
  `render.py` and the paper use stay as they are. Nothing under `paper/` or
  `results/figures/` is touched, and `src.explain`, `src.render` and
  `src.evaluate` are not run. The seven existing CSVs in `results/tables/` must
  come back byte-identical (SHA-256 taken before this entry was written), and
  the two new CSVs must be byte-identical across two runs of `src.model`.
  Read-only side checks in the same pass: the cached raw CSV's row count
  against UCI's listed 1,013 instances, and rows 66 / 156 / 382 / 403 in-sample
  next to out-of-fold. **Results go in a separate entry, #60**, so that this
  text stays as committed (author decision, 2026-10-09).

- **2026-10-09 #60 — RESULTS of the #59 pre-registration: out-of-fold
  probabilities and what the gate does with them.** Reporting only. No
  threshold, model, band rule or selection criterion changed, nothing under
  `paper/` or `results/figures/` was touched, and `src.explain`, `src.render`
  and `src.evaluate` were not run. Implemented as `oof_gate_analysis()` in
  `src/model.py`, called at the end of `run()`, so `python -m src.model` now
  writes five CSVs instead of three.

  **Consistency check passed.** The pooled out-of-fold confusion matrix equals
  the summed matrix `evaluate()` reports for RF/none, `[[184, 38, 11], [60, 24,
  22], [14, 17, 81]]`. This is asserted in code before anything is written.

  **One deviation from #59's wording, found and fixed in the run.** The first
  two runs gave different bytes for `p1_oof_predictions.csv`: 38 of 451 rows
  differed in the last bit (max 2.2e-16), while `p1_gate_summary.csv` was
  identical. The root cause is in scikit-learn (`_forest.py:731-737, 956-958`):
  with `n_jobs=-1`, `predict_proba` adds per-tree probabilities into one array
  under a lock, in the order threads finish. A scratch test confirmed it: 15
  calls with `n_jobs=-1` gave 15 distinct byte outputs, `n_jobs=1` gave 1, and
  a refit was bitwise identical, so fitting is deterministic. **Fix:** each
  fold forest predicts with `n_jobs=1`, set after fitting. The trees are the
  same and only the summation order is fixed. Against the parallel output the
  probabilities moved by at most 2.2e-16, and no prediction, band or count
  changed. **The same latent issue exists at `src/explain.py:127`** (in-sample
  `predict_proba`, `n_jobs=-1`). It was not touched. `shap_case_summary.csv`
  came back byte-identical in #55's cold run, but nothing in the code
  guarantees that it always will.

  **Hash proof.** SHA-256 was taken before #59 was written and re-checked after
  two final runs (A, B). All seven existing CSVs are byte-identical:
  heuristic_matrix `e3b2acb9…748c`, p1_cohort_summary `7ad4214b…776f`,
  p1_duplicate_leakage `1ab11cac…2286`, p1_model_metrics `68086a33…6851`,
  shap_case_contributions `d1b4c12d…e2e1`, shap_case_summary `16f5ca6b…dc65`,
  shap_global_mean_abs `bda07763…594a`. The new files are byte-identical
  across runs A and B: `p1_oof_predictions.csv` `a6f2422b…9d96`,
  `p1_gate_summary.csv` `aa87b621…712b`.

  **Gate counts, out-of-fold, `RED_MARGIN = 0.15`** (columns: true low / mid /
  high = total):
  - GREEN 184 / 60 / 14 = 258.
  - AMBER 41 / 29 / 20 = 90.
  - RED 8 / 17 / 78 = 103.
  - Predicted high: 11 / 22 / 81 = 114. Of these, RED 8 / 17 / 78 = 103 and
    derated to AMBER 3 / 5 / 3 = 11.
  - The 112 true-high records reach RED 78, AMBER 20 (17 predicted mid plus 3
    derated) and GREEN 14.
  - Ungated GREEN near-ties (predicted low, margin < 0.15): 14 / 5 / 3 = 22.
  - Split by `conflict_vector`. True (71 rows on the 35 vectors): GREEN
    5 / 23 / 4, AMBER 21 / 1 / 7, RED 4 / 6 / 0. False (380 rows): GREEN
    179 / 37 / 10, AMBER 20 / 28 / 13, RED 4 / 11 / 78.
  - Sensitivity, reported only: at margin 0.10, GREEN 258, AMBER 88, RED 105.
    At 0.15: 258 / 90 / 103. At 0.20: 258 / 91 / 102.

  **`explain.select_cases` re-applied to out-of-fold probabilities, with fold
  SHAP for the driver condition.** The in-sample picks were 196 / 16 / 66 /
  382. Out of fold:
  - `confident_low` = row 48 (P(low) 1.0; two rows tie and the argmax takes
    the first).
  - `confident_high` = row 99 (0.997; two rows tie).
  - `boundary_mid` = **row 426**, true mid, predicted high at 0.233 / 0.382 /
    0.384, margin 0.0018, AMBER.
  - `failure_mode` = **row 325**, true low, predicted high at 0.411 / 0.148 /
    0.441, margin 0.029, AMBER.
  - None of the four sits on a conflicting vector.

  **The twin rows, in-sample next to out-of-fold** (low / mid / high):
  - **Row 66** (true mid, fold 3). In-sample 0.013 / 0.487 / 0.499, predicted
    high, margin 0.012, AMBER. **Out of fold 0.050 / 0.193 / 0.757, predicted
    high, margin 0.563, RED.**
  - **Row 156** (true high, its twin, fold 0). In-sample: not in any committed
    file. Out of fold 0.073 / 0.843 / 0.083, predicted mid, margin 0.760,
    AMBER.
  - **Row 382** (true low, fold 3). In-sample 0.451 / 0.097 / 0.453, predicted
    high, margin 0.002, AMBER. **Out of fold 0.264 / 0.719 / 0.017, predicted
    mid, margin 0.455, AMBER.**
  - **Row 403** (true high, its twin, fold 3). In-sample: not in any committed
    file. Out of fold identical to 382: both were held out by the same fold
    model and have identical features. Predicted mid, AMBER.
  - Because a forest's output depends only on the six features, the in-sample
    values for 156 and 403 would equal those of 66 and 382, up to the last bit.

  **Raw-file side check.** `data/raw/maternal_health_risk.csv` has 1015
  physical lines: one header and 1014 records. There are no blank lines, no
  repeated header and no malformed rows (every line has 7 fields), lines are
  CRLF and the file ends in a newline. pandas reads 1014 rows, with 562 exact
  duplicates and 2 rows at HR < 20. UCI's own API (`/api/dataset?id=863`)
  reports `num_instances: 1013`. Nothing in the file accounts for the
  difference.

  **Facts for the next session, recorded without proposing any change.**
  - `reproducibility.tex` names three CSVs for `src.model`; it now writes five.
  - #55's cold-run count of 33 non-audio artifacts is now 35.
  - Every case probability the paper quotes is still the in-sample one from
    `shap_case_summary.csv`. Whether and how the manuscript responds is an
    author decision, and Gate A is still open.
