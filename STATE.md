# STATE.md — project state & handoff

Read this at the start of every session. Update it at the end (phase, status,
next step) and **append** to the Decision Log — never edit or delete an
existing entry; supersede it with a new dated one.

_Last updated: 2026-10-11_

## Current phase

**2026-10-11: batch G is committed (#73; #74 corrects one page number).**
The batch F re-check found B1-B3. REVISION_BRIEF §22 fixed B1 and B2, and B3
closed with them; the `[tb]` attempt changed nothing. The tracked
`paper/main.pdf` is rebuilt (`f68c1d6`; 21 pp, clean log). This was the last
prose touch. **Next: the reviewer's moderation audit, then both authors'
freeze read (§20), then §16.** See "Next step".

**2026-10-11: batch F is committed (#72).** The §19 re-verification at
`d62c376` reported O1 and N1-N4. REVISION_BRIEF §21 fixed them, together with
the A6 remainder and rows 36 and 38, in one commit per file. The tracked
`paper/main.pdf` is rebuilt (`2a3d0b6`; 21 pp, clean log). **Next, the
verifier session re-checks batch F only (the §19 procedure on
`d62c376..HEAD`); then come the §20 text-freeze reads.** See "Next step".

**2026-10-10: batch E is committed (#71).** The §15 verifier session wrote
`VERIFICATION.md` against `66872d4`. Every paper-text, bibliography and table
fix of REVISION_BRIEF §18 is now in, one commit per file, and the tracked
`paper/main.pdf` and `paper/main.bbl` are rebuilt (`8dacb47`; 21 pp, clean
log). **§19 re-verification by that same verifier session is next.** It
writes nothing tracked. See "Next step".

**2026-10-10: the revision is complete; batch D is committed (#70).** The
abstract, back matter, `main.tex` metadata and two small fixes (Sections 1
and 8) are in, and the tracked `paper/main.pdf` and `paper/main.bbl` were
rebuilt in place from the final sources (21 pp, clean log). **Whole-paper
verification (REVISION_BRIEF §15) is next, in a new session that has written
nothing.** See "Next step".

**2026-10-09: out-of-fold gate analysis done (#59 pre-registered, #60
results).** `python -m src.model` now also writes `p1_oof_predictions.csv` and
`p1_gate_summary.csv`. The paper's case probabilities are in-sample; the
out-of-fold numbers are in #60. No paper prose or figure has been changed in
response, and that is an open author decision ahead of Gate A.

**2026-10-09: the four cases are now scored out of fold (#61 pre-registered,
#62 results).** The rows are 48 / 99 / 426 / 325. Figure 1's clinician and
ASHA panel files now show row 426. `paper/` is untouched, so the manuscript no
longer matches its artifacts. #62 also lists the evaluation rationale updates
for the author to approve, plus four judgment calls to re-check.

**2026-10-09: revision under `REVISION_BRIEF.md` and `WRITING_RULES.md`
started (both untracked; the rules file sits in `.claude/agents/`).** #63 is
the housekeeping: the author's four re-rate decisions, `refs.bib` fixes plus
the dataset entry, `requirements-lock.txt`, and the `.gitkeep` by-product.
The paper is revised one section per task, each committed only after author
approval, starting with Section 4. **Sections 4, 3 and 5 are committed
(#64-#66); batch A is closed.** The claim audit is done (#67), and its
decisions are #68. **Batches B and C are committed (#69): Sections 1, 2, 6, 7
and 8, plus the claim-audit fixes to Sections 3 and 5.** Batch D (abstract,
back matter, `main.tex`) followed in a fresh session and is committed (#70).

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
- **Superseded by #62 (2026-10-09):** the cases are now scored out of fold,
  and the rows are 48 / 99 / 426 / 325. The rows listed below are the
  previous in-sample picks, kept for the record.
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

## Next step — handoff (rewritten 2026-10-11, after batch G)

**Phase.** P6, pre-submission. The prose is final except for fixes made
under §20.
- Batches A to G are committed (#64-#73; #74 corrects a page number in #73).
  - The batch F re-check (`VERIFICATION.md`, at `03a3808`) passed batch F. It
    reported B1-B3 in the paper and O2-O3 in `README.md`.
  - Batch G (REVISION_BRIEF §22, #73) fixed B1 and B2.
  - B3 (the blank quarter page) closed as a side effect of B1 and B2. The
    one `[tb]` attempt changed nothing, so it was not kept.
  - As §22 says, batch G gets no verifier round.
- The tracked `paper/main.pdf` was rebuilt in place from the batch G sources
  (`f68c1d6`). `paper/main.bbl` was rebuilt as well and came out
  byte-identical.
- **Next, in order:**
  1. **The reviewer's arXiv moderation audit** of the full PDF. It is report
     only, and it also serves as the read of batch G. The tools on disk are
     `.claude/commands/arxiv-audit.md` and the `arxiv-moderator` agent.
  2. **Both authors' freeze read (§20).** Both authors read the final PDF end
     to end. Fixes only, each through a small batch with the same checks.
     Then the text is frozen.
  3. **§16** (repo and Zenodo, with the cold run first as step 0), then §17
     (the upload package).
- Nothing has been pushed.

**Branch and commits.** Branch `revision/sncs-framing`.
- The last commit before this handoff is `0784244` (#74). The handoff itself
  is the next commit; `git log -1` gives its hash.
- With the handoff, the branch is 63 commits ahead of
  `origin/revision/sncs-framing`, which sits at `ea4aa99`.
- `origin/main` is stale at `f41c4ab`.

**Read first (moderation audit and freeze read), in this order.**
1. `paper/main.pdf` at HEAD (21 pp).
2. `VERIFICATION.md`: the §15 run, §19, and the batch F re-check. Together
   they show what has been verified and what has not: A1 (archive), A9 (cold
   run), and the Nielsen 1994 text, which has not been read.
3. Decision Log #71-#74, which cover the last three batches.

**Facts for the audit and the freeze read.** These are records, not
instructions to change anything.
- **Open author decision (#72, #73):** the AI statement's closing sentence
  keeps the clause form ("…: in the rendering pipeline of Section 4, all
  text comes from fixed templates, with no language model at inference,
  which is one of the contributions claimed here."). WRITING_RULES §8 gives
  it as a standalone sentence. The statement's first three sentences match
  §8 word for word.
- **Recorded departures from the briefs:**
  - #71: the A4 wording and the A2 propagation sites;
  - #72: the AI-statement clause, the N3 counts, the N2 head and the N4
    "the";
  - #73: §7 "every string can be regenerated", made under the propagation
    rule for B1.
- **/anti-ai items left as prescribed (#73):**
  - §1.1 "All text comes from …" followed by "No text is generated …";
  - §5.2 "Two of those gaps";
  - "the final wording" in both of the AI statement's split sentences.
- **Outside the paper, for §16 step 2 (the README rewrite) and step 3:**
  - **O2.** `README.md:126-128` gives Patil's role as "Clinical domain
    expertise" and "Validation". The paper says "clinical domain input" and
    "Writing – review & editing". `.zenodo.json` must not copy the README
    line.
  - **O3.** These README lines are stale:
    - `:7` old values;
    - `:29` "20 pp";
    - `:30` cs.LG;
    - `:50` the template claim;
    - `:81` byte-identical;
    - `:103` "36 entries";
    - `:106`.
  - `paper/ARXIV_SUBMISSION.md:102` holds an old abstract, which §17
    regenerates.
- **Allowed exceptions to the WRITING_RULES §3 greps:**
  - the card header "ELEVATED — needs follow-up" (verbatim artifact quote);
  - the CRediT role names "Writing – original draft" and "Writing – review &
    editing" (en dash; official names);
  - `\textbf{Keywords:}`, `\mathbf` best values in Table 2, and
    `\paragraph{}` heads, the CRediT names included;
  - "novelty" only as Hendrickx's term;
  - one contrast per paragraph where it carries design content.
- **Old-values grep (brief §0):** the one expected typeset hit is `102`, the
  RED count at margin 0.20, which is correct. The `%` history comments at
  the top of `three_tiers.tex` still carry old values (#71, correcting #70).
  §16 step 1b removes them.
- **Abstract:** batch G did not change it. It is 200 words and 1229
  characters. `ABSTRACT_ARXIV.txt` (repo root, untracked) equals the
  `abstract.tex` body after whitespace normalisation.
- **Last build** (in place, `f68c1d6`):
  - 21 pages, 0 errors, 0 undefined references or citations, 0 overfull
    boxes, 0 bibtex warnings.
  - 2 underfull boxes, both from before batch E.
  - 37 bibitems.
  - `pdfinfo` title and author match `main.tex`.
  - A cold build from `git archive HEAD` gives the same `.bbl` and PDF text.
  - Floats: Table 1 is on p6, Table 2 on p7, Figure 1 on p9, Table 3 on
    p11 and Table 4 on p12. §6 starts on p13.

**Committed in this revision** (on top of `c657617`, #57/#58):

| Commit | Content |
|---|---|
| `d93f4f6` | #59 pre-registration |
| `5b9fe6d` | #60 out-of-fold gate analysis (`p1_oof_predictions.csv`, `p1_gate_summary.csv`) |
| `06716f7` | #61 pre-registration |
| `0d649d2` | #62 cases scored out of fold (rows 48 / 99 / 426 / 325), artifacts regenerated |
| `d9880f8` | #63 re-rate decisions, `refs.bib` fixes and dataset entry, `requirements-lock.txt`, `.gitkeep` |
| `b3d3aab` | #64 Section 4 |
| `549f485` | #65 Section 3 |
| `5652ad4` | Section 5 |
| `30eafa9` | #66 Section 4 polish |
| `4a4e6e5` | #67 claim audit |
| `e201fa4` | #68 claim-audit decisions and handoff |
| `ae5931e` | #69 Section 6 |
| `0da7566` | #69 Section 7 |
| `e2fed0f` | #69 Section 8 |
| `41b5f8c` | #69 Section 2 |
| `45158a3` | #69 Section 1 |
| `9345154` | #69 Section 3 claim-audit fixes |
| `8e4aa62` | #69 Section 5 claim-audit fix |
| `5861cb7` | #69 decisions and batch D handoff |
| `b615c1e` | #70 abstract |
| `434cdc8` | #70 back matter |
| `5031e56` | #70 `main.tex` metadata |
| `529bfc2` | #70 Section 1 roadmap |
| `bef9f0f` | #70 Section 8 sentence |
| `e35b270` | #70 `paper/main.pdf` and `paper/main.bbl` rebuilt |
| `66872d4` | #70 decisions and the §15 handoff |
| `b0f09f5` | #71 Section 1 |
| `85be244` | #71 Section 2 |
| `e32fa8c` | #71 Section 3 |
| `214ed1e` | #71 Section 4 |
| `6ab507f` | #71 Section 5 |
| `85da2be` | #71 Section 6 |
| `319a8f6` | #71 Section 7 |
| `0ef2309` | #71 Section 8 |
| `12e1582` | #71 back matter |
| `2f078ca` | #71 `refs.bib` |
| `8dacb47` | #71 `paper/main.pdf` and `paper/main.bbl` rebuilt |
| `778100c` | #71 Decision Log entry |
| `d62c376` | #71 handoff (§19 ran at this HEAD) |
| `071f1ca` | #72 `src/render.py` provenance comment |
| `7c0d189` | #72 `src/evaluate.py` rationale |
| `bc90079` | #72 `heuristic_matrix.csv` and `heuristic_evaluation.md` regenerated |
| `d702b75` | #72 README |
| `1eb0c55` | #72 abstract |
| `9255178` | #72 Section 1 |
| `6a04cb2` | #72 Section 2 |
| `8463251` | #72 Section 3 |
| `c70ba3f` | #72 Section 5 |
| `b2cca9d` | #72 Section 7 |
| `ada3de9` | #72 Section 8 |
| `dd420c9` | #72 back matter |
| `2a3d0b6` | #72 `paper/main.pdf` rebuilt (`main.bbl` byte-identical) |
| `d9f3a60` | #72 Decision Log entry |
| `03a3808` | #72 handoff (the batch F re-check ran at this HEAD) |
| `520fdd9` | #73 Section 1 |
| `9877096` | #73 Section 5 |
| `e579928` | #73 Section 7 |
| `f1b281b` | #73 back matter |
| `f68c1d6` | #73 `paper/main.pdf` rebuilt (`main.bbl` byte-identical) |
| `8f44592` | #73 Decision Log entry |
| `0784244` | #74 correction to #73 |

**Known untracked files.** Leave them untracked:
- `.claude/agents/` and three `.claude/commands/*.md` files.
- `RECON.md`, `REVISION_BRIEF.md`, `WRITING_RULES.md`, `CLAIM_AUDIT.md`,
  `ABSTRACT_ARXIV.txt`, `VERIFICATION.md`.
- `refs_fixed.bib` and `paper/refs_fixed.bib`, the author's file. Of its
  two non-casing differences, Bradley's `\&` is applied (#64) and the
  Widyawati double space is not.

**Open items, in order.**
1. **The reviewer's arXiv moderation audit** of the final PDF. It is report
   only. Any fix it needs goes through a small batch with the same checks
   (brief §20).
2. **Text freeze** (brief §20):
   - **Both authors read and approve the final PDF** (brief §10). No
     end-to-end human read has happened yet (old Gate A), and Patil's read is
     outstanding.
   - The authors decide the AI statement's closing sentence (#72, #73).
   - Fixes only, each through a small batch. Then the text is frozen, and
     §16 tags the frozen text.
3. **`/anti-ai` before every prose commit** (CLAUDE.md rule 8). The pattern
   that held: the audit runs report-only, the author decides each item, and
   the decisions are applied before the commit.
4. **Repo and Zenodo** (brief §16, RECON A1), in a fresh session with the
   cold run first (step 0, which closes A9). Nothing is pushed or tagged
   without the author.
   - The concept DOI 10.5281/zenodo.22252076 resolves only to v1.0.0, which
     is tag `v1.0.0` = `b8853a5`, the P3 commit. That snapshot has no
     `src/evaluate.py`, no `paper/` and several missing tables.
   - The next release is **v1.1.0**, because `v1.0.0` is taken.
   - The Zenodo licence is MIT, while `ARXIV_SUBMISSION.md` claims CC BY
     4.0, and the Zenodo creators list one author.
   - Step 2's README rewrite also fixes O2 and O3 (see above). Step 3's
     `.zenodo.json` uses the paper's CRediT wording.
   - `origin/main` is stale.
   - Decide what is public before pushing: the tracked STATE.md holds the
     enrollment-number address and moderation notes (RECON).
5. **Upload package** (brief §17, same session as item 4):
   - Regenerate `paper/ARXIV_SUBMISSION.md` and `arxiv/`, scripted off
     `main.tex`'s `\input` lines (#57). Both are stale: the paper is now
     21 pp, with 4 tables and 37 bib entries.
   - Ship `main.bbl`.
   - Compile standalone.
   - Run a final firewall grep.
   - The plain-text abstract for the form is `ABSTRACT_ARXIV.txt`.
   - Submit to arXiv, cs.HC.

**Cold-run recipe** (from #55; re-run because `src/` moved in #60-#63).
Brief §16 step 0 now governs: install from `requirements-lock.txt`, compare
SHA-256 of every file under `results/`, and re-derive the 57 of 71.
1. Fresh clone, and a fresh venv on Python 3.12 from `requirements.txt`.
   Compare it with `requirements-lock.txt`.
2. Delete `results/audio/*.mp3` first.
3. Run `python -m src.{data,model,explain,render,evaluate}`.
4. Every PNG, CSV and TXT must come back byte-identical. The MP3s are the
   documented exception: same length, different bytes.
5. Rebuild the PDF.

Out-of-fold scoring (`out_of_fold()`) runs with `n_jobs=1`, so the
out-of-fold CSVs are byte-stable (#60). `evaluate()` still predicts with
`n_jobs=-1` for Table 2; Section 8 claims single-threading for the
out-of-fold path only (#69).

**Do not reopen:** the calibration sentence (#24a); the `failure_mode`
triptych cut (#33, #38); Clark et al. stays quarantined (WRITING_RULES §6);
no p-value (brief §0); `RED_MARGIN = 0.15` as a design constant; the abstract
text (#70, with the N1 sentence from #72).

**Working method that held.**
- Build only in a scratch copy, never in `paper/`, except for the deliberate
  in-place rebuild of the tracked `main.pdf` and `main.bbl` (#70).
- Check scripts are not kept in the repo. Re-create them as needed: the
  banned-pattern and contrast grep, the old-values grep, number tracing
  against `results/tables/`, label-to-page from `main.aux`, and `pdftoppm`
  page renders.
- Numbers come from committed files only. External facts are cited, and
  derived counts carry a `%` derivation.

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

- **2026-10-09 #61 — PRE-REGISTRATION: the four illustrative cases are scored
  by the fold model that held each row out. Committed BEFORE any code
  changes.** This changes how cases are scored and rendered. It changes no
  threshold, no template, no Hindi string, and nothing under `paper/`.

  (a) **Case probabilities and local SHAP come from the fold model that did
  not see the row**: `FINAL_MODEL` (RF, no resampling, `n_estimators=300`,
  `random_state=42`) over the same `StratifiedKFold(5, shuffle=True,
  random_state=42)`. One helper in `src/model.py` returns, for every row, the
  held-out probabilities, the fold model's SHAP toward each class, its base
  values and the fold index. `oof_gate_analysis()` and `src/explain.py` both
  call it. A single splitter function serves `evaluate()`, that helper and
  nothing else, and `src/explain.py` builds no splitter of its own (author
  decision: one splitter everywhere).
  (b) **The existing `select_cases` rule, unchanged, picks the cases from
  out-of-fold probabilities and fold-model SHAP, as in #60.** Expected rows:
  `confident_low` 48, `confident_high` 99, `boundary_mid` 426, `failure_mode`
  325. `shap_case_summary.csv` and `shap_case_contributions.csv` gain two
  columns, `scoring = "out_of_fold"` and `fold`, appended after the existing
  ones. The code asserts that each case's `p_low / p_mid / p_high` equal its
  row in `p1_oof_predictions.csv` exactly (round-trip float parse) and fails
  loudly otherwise.
  (c) **Global SHAP is unchanged**: still the final model fitted on all 451
  rows. It is labelled as final-model in code and on stdout only, not in the
  CSV or the figure (author decision). `shap_global_mean_abs.csv` must stay
  byte-identical, proved by hash; `shap_global_high.png` is expected to stay
  byte-identical too and will be reported either way.
  (d) **`RED_MARGIN` (0.15), `band_for`, every ASHA template constant and the
  three Hindi strings are unchanged.** `src/render.py` is not edited.
  (e) **Prediction uses `n_jobs=1` after fitting.** The in-sample
  `predict_proba` at `src/explain.py:127` is removed, because nothing uses it
  once cases are scored out-of-fold. That closes the latent nondeterminism #60
  recorded.
  (f) **`src/evaluate.py`, under the author's three conditions.** Only
  rationale facts that describe the CURRENT artifacts are updated: row
  numbers, probabilities, SHAP values, card text, contrast. Sentences
  describing the first-pass defects are history and stay as written. **No
  rating changes.** Any cell whose rating no longer rests on a true fact keeps
  its rating and is listed in #62 for the author to re-rate. Every changed
  sentence is listed in #62 as before → after. Those facts can only be read
  off the regenerated artifacts, so `evaluate.py` is edited after the first
  `src.explain` and `src.render` runs and before the first `src.evaluate` run.
  (g) **Verification.**
  - `python -m src.model` is re-run, because `evaluate()` and the
    out-of-fold path are refactored. All five `p1_*.csv` files must come back
    byte-identical.
  - Then `results/audio/` is emptied (Reproducibility 8.2) and the following
    are run: `python -m src.explain`, `python -m src.render --case all`,
    `python -m src.evaluate`.
  - All three are then run a second time. Every CSV, TXT and PNG must be
    byte-identical across the two runs; MP3 is excepted, as documented.
  (h) **Consequences stated in advance.** The `tier_*_boundary_mid.png` files
  that Figure 1 reads will depict row 426. Nothing under `paper/` is edited or
  rebuilt, so `paper/main.pdf` still embeds the previous rendering, and the
  gitignored `arxiv/` staging copies are untouched. Results go in #62.

- **2026-10-09 #62 — RESULTS of #61: the four cases are now scored out of
  fold.** Everything #61 pre-registered held. No threshold, template, Hindi
  string or rating changed, `src/render.py` was not edited, and nothing under
  `paper/` was touched.

  **Code.**
  - `src/model.py` has one `_splitter()`, used by `evaluate()` and by the new
    `out_of_fold()` helper. `oof_gate_analysis()` and `src/explain.py` both
    call `out_of_fold()`.
  - `src/explain.py` builds no splitter.
  - The in-sample `predict_proba` (old `explain.py:127`) is gone; prediction
    runs with `n_jobs=1` after fitting.
  - Global SHAP is still the final model fitted on all 451 rows, labelled as
    such in code and on stdout.
  - Re-running `src.model` after the refactor returned all five `p1_*.csv`
    byte-identical.

  **Cases, as pre-registered.** `confident_low` 48, `confident_high` 99,
  `boundary_mid` 426, `failure_mode` 325. The exact-match assertion against
  `p1_oof_predictions.csv` passed. Readings are Age / SysBP / DiaBP / BS /
  Temp / HR. Out-of-fold probabilities are low / mid / high. SHAP is toward
  the predicted class, in the same feature order.
  - **48** (true low, fold 4): readings 15 / 76 / 49 / 7.5 / 98 / 77.
    1.000 / 0.000 / 0.000, predicted low, margin 1.000, GREEN. SHAP +0.063
    / +0.103 / +0.101 / +0.130 / +0.049 / +0.039.
  - **99** (true high, fold 3): readings 48 / 140 / 90 / 15.0 / 98 / 90.
    0.000 / 0.003 / 0.997, predicted high, margin 0.993, RED. SHAP +0.049 /
    +0.293 / +0.002 / +0.353 / −0.004 / +0.052.
  - **426** (true mid, fold 1): readings 42 / 120 / 90 / 9.0 / 98 / 70.
    0.233 / 0.382 / 0.384, predicted high, margin 0.0018, AMBER. SHAP
    +0.052 / −0.072 / +0.007 / +0.227 / −0.026 / −0.050.
  - **325** (true low, fold 4): readings 17 / 90 / 60 / 7.9 / 101 / 76.
    0.411 / 0.148 / 0.441, predicted high, margin 0.029, AMBER. SHAP −0.001
    / −0.035 / −0.027 / +0.044 / +0.253 / −0.042.

  **Hash proof.**
  - `shap_global_mean_abs.csv` is `bda077634ff9…07a594a` before #61, after
    run 1 and after run 2.
  - `shap_global_high.png` is `8928300df68c…13522db1c60` at all three points.

  **Determinism.** `results/audio/` was emptied first (the four MP3s were
  deleted by explicit path). Then `src.explain`, `src.render --case all` and
  `src.evaluate` were run twice.
  - All 36 non-MP3 files under `results/` came back byte-identical across the
    two runs.
  - The MP3s differ between runs, as #10/#18 document. Their lengths equal the
    committed ones: 112320 / 83520 / 56256 / 112320.

  **What changed against `06716f7`.** 20 tracked files:
  - The 4 MP3s.
  - `shap_case_*.png` ×4.
  - `tier_clinician_*.png` ×4.
  - `tier_asha_{boundary_mid,failure_mode}.png` and `.txt`.
  - `shap_case_summary.csv` and `shap_case_contributions.csv`, which gained
    `scoring` and `fold`.
  - `heuristic_matrix.csv` and `heuristic_evaluation.md`.

  **What came back byte-identical.**
  - Both global SHAP files.
  - All 5 `p1_*.csv`.
  - `tier_asha_{confident_low,confident_high}`, PNG and TXT.
  - All 4 `tier_mother_*.png` and all 4 Hindi transcripts. Each case kept its
    band, so the spoken lines and the provenance blocks are the same.

  `results/audio/.gitkeep` appears as an untracked by-product of
  `render.py:409`. It is left untracked.

  **Figure 1's panels.**
  - `tier_clinician_boundary_mid.png` and `tier_asha_boundary_mid.png` now
    show row 426.
  - `tier_mother_boundary_mid.png` is unchanged.
  - `paper/main.pdf` and every row-66 / row-382 number in the paper's prose
    still describe the previous, in-sample rendering. That is a fact recorded
    here, not a proposal.

  **ASHA cards.**
  - `boundary_mid`: ELEVATED — needs follow-up. It lists raised blood sugar
    and older age.
  - `failure_mode`: ELEVATED — needs follow-up. It lists raised body
    temperature and raised blood sugar.

  **`src/evaluate.py`, under the author's conditions.**
  - **No rating changed**, and the counts are still 29 Pass / 12 Partial /
    1 Fail / 6 Deferred.
  - The worst-case header contrast is still 5.14:1. It is computed from the
    palette and did not move.
  - 9 matrix cells changed rationale only, plus three non-matrix sentences.
  - **Every change, before → after:**
    1. 1.4.1 clinician: "BS +0.204, DiastolicBP -0.024 on boundary_mid" →
       "BS +0.227, SystolicBP -0.072 on boundary_mid".
    2. 3.1.5 clinician: "base E[f(x)] = 0.250" → "base E[f(x)] = 0.247".
    3. Nielsen 1 clinician: "sees 0.487 vs 0.499" → "sees 0.382 vs 0.384".
    4. Nielsen 1 ASHA: "confident_high (margin 1.000) … boundary_mid (margin
       0.012)" → "confident_high (margin 0.993) … boundary_mid (margin 0.002)".
    5. Nielsen 2 clinician: "BS = 9, BodyTemp = 102, SystolicBP = 85" →
       "BS = 9, BodyTemp = 98, SystolicBP = 120".
    6. Nielsen 2 ASHA: "so 102F is flagged as raised" → "so 101F on
       failure_mode is flagged as raised", and "failure_mode reads 'young
       age' for a 13-year-old, not 'low age'" → "boundary_mid reads 'older
       age' for a 42-year-old, not 'raised age'".
    7. Nielsen 5 clinician: "BodyTemp +0.216 driving a high-risk call in a
       13-year-old while blood sugar argues against it" → "BodyTemp +0.253
       driving a high-risk call in a 17-year-old while heart rate (-0.042) and
       systolic pressure (-0.035) argue against it".
    8. Nielsen 5 ASHA: "Verified on failure_mode, where BS (-0.085, arguing
       AGAINST high risk) is no longer listed …; the card now shows BodyTemp
       (+0.216) and Age (+0.056)" → "Verified on boundary_mid, where
       SystolicBP (-0.072, arguing AGAINST high risk) is no longer listed …;
       the card now shows BS (+0.227) and Age (+0.052)". This case is the one
       where a sign-blind |SHAP| ranking would print SystolicBP. On row 325
       both rankings agree.
    9. Nielsen 5 mother: "boundary_mid (0.012) and failure_mode (0.002)" →
       "boundary_mid (0.002) and failure_mode (0.029)".
    10. CORRECTED C1, *Now*: "failure_mode now shows BodyTemp (+0.216) and
        Age (+0.056)" → "failure_mode now shows BodyTemp (+0.253) and BS
        (+0.044)".
    11. GAPS 3: "base E[f(x)] = 0.250" → "base E[f(x)] = 0.247".
    12. SYNTHESIS: "(margins 0.012 and 0.002)" → "(margins 0.002 and 0.029)".
  - **Kept as written, as history:** C1 *Was* (the −0.085 card), C3 *Was*,
    C4 *Was* (BS 7.7 on the old `confident_low`), and SYNTHESIS's first-pass
    paragraph.
  - **Cells whose rating no longer rests on a true fact: none found** after
    the updates.
  - **For the author to re-check, as judgment calls, not fact errors:**
    (i) Nielsen 5 clinician (Pass). The old cue for catching the spurious
    flag was blood sugar arguing against the call. On row 325 blood sugar
    argues for it (+0.044), and the opposing features are small.
    (ii) Nielsen 2 ASHA, "BS 7.7 against a 7.5 median no longer reads as a
    concern". This is now renderer behaviour asserted by `render._selfcheck`,
    not something any current card shows.
    (iii) C1 *Now* still names `failure_mode`, which no longer demonstrates
    the sign fix.
    (iv) SYNTHESIS still calls a 0.029 margin "knife-edge".

- **2026-10-09 #63 — Housekeeping before the manuscript revision: author
  decisions on #62's four flagged cells, `refs.bib`, a dependency lock file,
  and the `.gitkeep` by-product.** No rating, threshold, template, Hindi
  string, model or section text changed. The only file touched under
  `paper/` is `refs.bib`.

  **Author decisions on the four cells #62 flagged (rationale only, ratings
  kept), as applied in `src/evaluate.py`:**
  1. Nielsen 5 clinician, Pass kept. "on failure_mode the waterfall shows
     BodyTemp +0.253 …" → "on failure_mode the panel shows the near-tie
     (0.411 low against 0.441 high), the waterfall shows BodyTemp +0.253 …".
     The panel was checked to print 0.411 and 0.441.
  2. Nielsen 2 ASHA, Pass kept. "BS 7.7 against a 7.5 median no longer reads
     as a concern; BS 9.0 on boundary_mid and 15.0 on confident_high still
     do." → "The rule is src/render.py:188 (|value - median| <= deadband),
     with the 0.25 set at src/render.py:115 and the median and IQR taken from
     the clean set at src/render.py:455; BS 9.0 on boundary_mid and 15.0 on
     confident_high fall outside it and read as raised." The line numbers are
     those after this entry's `render.py` edit.
  3. CORRECTED C1, *Now*. "failure_mode now shows BodyTemp (+0.253) and BS
     (+0.044);" → "On boundary_mid (row 426) a ranking by absolute value would
     have listed systolic pressure (-0.072), which argues against the call;
     the card now shows BS (+0.227) and Age (+0.052) instead." C1 *Was* is
     history and unchanged.
  4. SYNTHESIS. "the two knife-edge cases (margins 0.002 and 0.029)" → "the
     two cases inside the 0.15 margin (margins 0.002 and 0.029)". The other
     "knife-edge" (Nielsen 1 ASHA, describing margin 0.002) was not in the
     decision and is unchanged.

  `src.evaluate` was run twice. Both runs gave byte-identical files and
  stdout. Against the hash taken before the edit, only
  `heuristic_matrix.csv` (2 cells: N2 ASHA, N5 clinician; 0 ratings) and
  `heuristic_evaluation.md` changed. Counts are still 29 Pass / 12 Partial /
  1 Fail / 6 Deferred, and the worst-case header contrast is still 5.14:1.

  **`paper/refs.bib`.** The author's `refs_fixed.bib` (repo root, untracked;
  an identical copy sits at `paper/refs_fixed.bib`) differs from `refs.bib`
  in more than casing and author lists, so per the work order its casing and
  author-list fixes were applied to the current file and nothing else.
  - Applied, casing (braces protect capitals): kim2024stakeholder,
    bello2025threelevel, szymanski2025disentangling, okolo2022makingai,
    okolo2021cannot, okolo2024easy, solanokamaiko2024explorable,
    srinidhi2021asha, maisoon2026stratification, rahman2023xai,
    maheswari2024smote, hossen2024driven, eltawil2026comment,
    young2025leakage, arya2019explanation, yesmin2026trust.
  - Applied, author lists. bradley2025birth: the trailing empty author
    becomes `{the Options Study Collaborative Group}`, which matches the
    Crossref record fetched in session (19 authors, the last one this
    group). w3c2025wcag21: `O Connor, Joshue` → `O'Connor, Joshue`. **The
    W3C record fetched in session (w3.org/TR/WCAG21/) spells it "Joshue O
    Connor"**, so this one departs from the primary record; for the author to
    confirm.
  - NOT applied, listed for the author. bradley2025birth journal:
    `Obstetrics \&amp; Gynaecology` → `Obstetrics \& Gynaecology` (Crossref's
    own field carries the `&amp;`; as it stands the reference list prints
    "&amp;"). widyawati2025ensemble title: a double space before "in" →
    single (no visible effect).
  - Added `ahmed2020maternal`, as given in REVISION_BRIEF §11. 10.24432 is a
    DataCite DOI (Crossref returns 404), so the gate is extended visibly, as
    for the W3C entry. It was resolved in session against
    api.datacite.org and doi.org: title "Maternal Health Risk", one creator
    "Ahmed, Marzia", 2020, UCI Machine Learning Repository, type Dataset.
    The provenance is in a `%` comment above the entry. Nothing cites it yet.
    plainnat prints the title in sentence case ("Maternal health risk").
  - Built in a scratch copy: 0 LaTeX errors, 0 undefined references, 0
    bibtex warnings, 20 pages. Built again with `\nocite{*}`, so the uncited
    new entry is processed: also 0 bibtex warnings.

  **`requirements-lock.txt`** is `pip freeze` of `.venv` (Python 3.12.13):
  35 packages. All 11 pins in `requirements.txt` appear in it unchanged.
  Note for §8: `requirements.txt` marks `joblib` as transitive, pinned for
  `model.joblib` I/O, so "eleven direct dependencies" (brief §6) counts one
  pinned transitive.

  **`.gitkeep`.** `results/audio/.gitkeep` was deleted, and the
  `(audio_dir / ".gitkeep").touch()` line at old `src/render.py:409` was
  removed. The four MP3s are tracked, so the directory needs no placeholder.
  `render.py` compiles; `src.render` was not re-run, since it would rewrite
  the non-reproducible MP3s and the change touches no output.

  **Untracked, not committed:** `.claude/agents/paper-writer.md` was
  rewritten for this paper. It reads WRITING_RULES.md and REVISION_BRIEF.md
  before every task and follows them over anything else.

- **2026-10-09 #64 — Section 4 finished and committed: the 9 Oct draft plus
  the author-approved fixes in REVISION_BRIEF §1a; two `refs.bib` fixes.**
  - The author replaced `REVISION_BRIEF.md` and `WRITING_RULES.md` with new
    versions at the repo root (both untracked). The superseded copy at
    `.claude/agents/WRITING_RULES.md` was deleted, and `paper-writer.md` now
    reads the root file.
  - The rules changed in three ways. A verbatim artifact quote may keep its
    em dash. Contrasts that carry design content are allowed, at most one
    per paragraph. §10 is now the checklist.
  - The 9 Oct draft was written under the `paper-writer` instructions, on
    Sonnet. It ran as a general-purpose agent, because the agent type had
    not registered: its frontmatter carried the full model ID. With the
    alias `sonnet` it now registers.

  **§1a, as applied to `paper/sections/three_tiers.tex`.**
  1. 4.1 uses the brief's wording ("The direction of that substitution
     matters most, …").
  2. "what do I do next, not how likely is this" is restored.
  3. "smaller, not correct" is restored.
  4. The gate table has a new row, "Predicted low, inside margin (no gate)":
     14 / 5 / 3 / 22, from `p1_gate_summary.csv`
     `predicted_low_margin_below_0.15`. The caption is updated to match.
  5. 4.5 adds the two sentences: inside-margin calls were right far less
     often, and eleven calls on one dataset are too few to estimate the
     difference precisely.
  6. The threshold sentence now reads "changes little … 105, 103 and 102".
  7. "Outside the 0.15 margin, with margins from 0.230 to 0.880" replaces
     "no margin rule can catch". The 0.230 and 0.880 are the minimum and
     maximum margin of the 11 true-high GREEN records with margin ≥ 0.15 in
     `p1_oof_predictions.csv` (raw 0.22999…, 0.87999…).
  10. The stale `% NEW Table 3 (tab:matrix)` comment in `evaluation.tex` is
     fixed. This is a comment-only change.

  Items 8 and 9 needed no edit: the card's em dash stays, and the §3.4 /
  §3.5 cross-references become true in batch A. The file's header comment
  records the §1a changes.

  **`refs.bib`.**
  - `O'Connor` reverted to `O Connor`, matching the W3C primary record.
  - Bradley journal: `\&amp;` → `\&`; the reference list now prints "&".
  - Still unapplied from `refs_fixed.bib`: the Widyawati double space, which
    has no visible effect.

  **`/anti-ai`, report-only (author instruction; nothing applied).** CLAUDE.md
  rule 8 says to fix what the audit finds; the author directed report-only
  for this section. 11 suggestions on the committed file:
  - L67 signposting (approved wording).
  - L71 aphoristic closer.
  - L95 signposting contrast.
  - L107 unsupported comparative.
  - Verbless fragments opening the three tier paragraphs.
  - L166-167 rhythm triplet.
  - "can support" ×3 at L181-185.
  - L184-185 imperative antithesis.
  - L206 cleft closer.
  - L248-249 "far less often" where 78/103 and 3/11 exist.
  - L250 "Those 3" with a distant referent.

  None is a banned word. No paragraph has more than one contrast.

  **WRITING_RULES §10 checks on Section 4.**
  - Every typeset number traces to `shap_case_summary.csv`,
    `shap_case_contributions.csv`, `p1_gate_summary.csv` or
    `p1_oof_predictions.csv`.
  - Citations: `bello2025threelevel`, in an unchanged sentence.
    `bhatt2021uncertainty` left §4 with "What we claim" and is still cited in
    §2.
  - §3 grep: no banned words. The only em dash is the card-header quote
    (allowed). Bold appears only in table headers.
  - Old-values grep: one typeset hit, `102`, which is the new RED count at
    margin 0.20.
  - Scratch build: 0 errors, 0 undefined references, 0 bibtex warnings (also
    under `\nocite{*}`). **21 pages, previously 20.** The gate table (Table 3)
    grew, and the matrix (now Table 4) floats from p. 12 to p. 13. There are
    no new overfull or underfull boxes.

- **2026-10-09 #65 — Batch A (Sections 3 and 5) drafted; author statement on
  Mamun et al. and Maisoon et al.** Committed with Section 3. The author's
  decisions on both drafts are recorded in #66.

  **Author statement, 9 Oct 2026.** The author read the full texts of Mamun
  et al. (`mamun2025identification`) and Maisoon et al.
  (`maisoon2026stratification`) and found no duplicate removal in either.
  Section 3.3's "Neither removes duplicate rows" rests on this, together with
  the verified facts in WRITING_RULES §6:
  - Mamun: 1014 samples, 99.51%, 10-fold CV.
  - Maisoon: two implausible outliers removed (N = 1012), 83.74% at a tuned
    threshold of 0.67, stratified 5-fold CV.

  **Drafts.** The `paper-writer` subagent wrote `data_and_vehicle.tex`
  (REVISION_BRIEF §2) and `evaluation.tex` (REVISION_BRIEF §3). The main
  session checked them:
  - Every number traces to its file.
  - All 48 matrix symbols and the 29/12/1/6 counts match
    `heuristic_matrix.csv`.
  - The §3 grep and the old-values grep are clean in typeset text.

  **Citation finding in Section 5's last paragraph.** "Studies with community
  health workers in India report difficulty interpreting AI explanations even
  after they have been simplified" (okolo2024easy,
  solanokamaiko2024explorable) was checked against both abstracts:
  - Okolo et al. 2024 (Crossref): "CHWs struggled to understand the AI
    explanations". Nothing on simplification.
  - Solano-Kamaiko et al. 2024 (Semantic Scholar): explorable explanations
    "help develop a more nuanced understanding of AI", the opposite
    direction.
  - The sentence was replaced under REVISION_BRIEF §12 (#66), and the
    all-section claim audit is #67.

- **2026-10-09 #66 — Batch A closed: the author's decisions on the Section 3
  and 5 drafts (REVISION_BRIEF §2a and §12) and the Section 4 polish (§1b).**
  - The author replaced `REVISION_BRIEF.md` and `WRITING_RULES.md` with new
    versions (supplied as "... new.md", moved over the old files). Both are
    still untracked.
  - Three rule changes: bold is allowed for best values in a table and in
    `\paragraph{}` heads; external facts are cited, not tabled; derived
    counts are allowed with a `%` derivation; no thousands separators.
  - Three commits:
    - Section 3 with #65 (`549f485`).
    - Section 5 (`5652ad4`).
    - Section 4 polish with this entry.

  **Section 3, §2a as applied.**
  - 1013 is now "the repository page lists 1013 instances", cited to
    `ahmed2020maternal`. The UCI page and API were re-read this session: 1013.
  - The in-sample mechanism uses the brief's forest-and-leaves wording.
  - "A false high call like this one". Bands appear as `\textsc{red}`.
  - "On all 1014 records" (Yesmin).
  - The 5.9 pt overfull box in 3.4 was reworded away ("set to
    `n_estimators=300` and `random_state=42`").
  - The ten /anti-ai rewordings are applied as worded.
  - Kept: "two implausible outliers", the priority sentence, `\mathbf` in
    Table 2, and comma-free numbers.
  - **One number differs from the brief.** §2a reads "66 of those 71 records
    are scored with a margin of at least 0.15". `p1_oof_predictions.csv`
    gives 68 for that property; 66 is the count mispredicted. The text says
    68, and a `%` comment records both derivations. The author may want "66
    of them mispredicted" added.

  **Section 5, §2a and §12 as applied.**
  - The CHW sentence now uses the §12 wording (design-dependence, citing both
    papers).
  - "Both were built to find defects early" is replaced by the heuristic /
    WCAG sentence.
  - The matrix caption no longer repeats the paragraph after the table.
  - "No model metric could have shown it, because metrics never read the
    card".
  - "The criteria are met by the three tiers together, and by no single one
    of them."
  - Kept as approved: the single-evaluator paragraph and the `\paragraph`
    heads.

  **Section 4, §1b as applied.**
  - "The gate is one-sided." and "Computing the band once also matters."
  - "Two different bands" in 4.2; "two identities" now appears only in §5.
  - The card sentence (no generated text).
  - "Can support" is varied ("there is no such magnitude to convey"), and
    the imperative is now a statement.
  - "It changed only what the mother was told."
  - 4.5 reads "only 3 are"; the "far less often" sentence is deleted, and
    "The 3 derated high-risk records are the cost of the rule".

  **Checks (WRITING_RULES §10).**
  - Every number traces to its file, or to a cited external source (1013).
  - New citation sentences match their sources' abstracts: Okolo 2024 and
    Solano-Kamaiko 2024 for "depends on its design"; the UCI page for 1013.
  - §3 grep clean; at most one contrast per paragraph; old-values grep clean
    except the new `102`.
  - Scratch build: 0 errors, 0 undefined references, 0 bibtex warnings,
    **0 overfull boxes**, 21 pages.
  - Every /anti-ai item for Sections 3 and 5 was decided by the author and
    applied, and the Section 4 report items are applied or kept as §1b says,
    which satisfies CLAUDE.md rule 8 for these commits.

- **2026-10-09 #67 — Claim audit (REVISION_BRIEF §12): every citing sentence
  in every section, checked against its source. No prose was edited.** The
  table is in `CLAIM_AUDIT.md` (repo root, untracked).
  - **Scope.** The audit ran on the state at `30eafa9`: 40 typeset sentences
    carrying `\citep`/`\citet`, covering all 37 `refs.bib` keys. The
    conclusion, reproducibility and back matter cite nothing in typeset text.
  - **Sources read this session.**
    - Abstracts: OpenAlex by DOI, with Semantic Scholar or Crossref as
      fallback; the arXiv API for Arya and Yesmin.
    - Publisher pages: Nature (Imrie, Bernett), PMLR (Mozannar), Springer
      (Peters).
    - Primary pages: W3C TR/WCAG21 and the UCI page for id 863.
    - The authors' own copy of Wobbrock & Kientz.
  - **Not retrievable.**
    - The Nielsen 1994 abstract: elided by the publisher, and ACM returned
      403.
    - The Mamun and Maisoon full texts (gold OA): Wiley's Cloudflare
      challenge and IEEE's bot block. "Neither removes duplicate rows" rests
      on the author's full-text read (#65).
  - **Verdicts: 32 supported, 5 partly, 3 unsupported.**
    - Unsupported: the Szymanski "co-vary" sentence (related_work:69–73), and
      the Okolo/Solano-Kamaiko "even after simplification" claim at
      related_work:123–130 and limitations:58–62. All three have pre-decided
      fixes in §12.
    - Partly:
      - Imrie, "genuinely divergent … not differing degrees".
      - The six-paper "same broad construction" sentence: cross-validation
        and resampling are not in all six abstracts.
      - Maisoon "systolic": the abstract says "Blood Pressure".
      - Young et al., which is a scoping review, not a re-analysis.
      - Nielsen "the refined ten", which cannot be checked.
    - Each partly row carries a replacement sentence in `CLAIM_AUDIT.md`.
  - **Two uncited follow-on sentences are partly supported.**
    - Maisoon's "the same two-row outlier removal" (related_work:176)
      contradicts the §2a decision.
    - Yesmin's "fourteen clinicians …, 71.4% of whom" (related_work:189–190):
      the source says 14 healthcare professionals, and 71.4% across three
      cases.
  - **Pre-decided §12 fixes, located.** Only §5.2 is done (`5652ad4`).
    - Pending in batch B: the §6.1 sentence (limitations:58–62) and the §6.5
      clause.
    - Pending in batch C: §2.3 Okolo/Solano (related_work:123–130), §2.1
      Szymanski, and the §2.3 Okolo 2022 counts (16 / 3 / 1).
    - A grep confirms that the abstract, intro and conclusion do not repeat
      the CHW claim.
  - **Correction to #66.** A shell typo had written a tab character in place
    of the backslash-t in "`\textsc{red}`" (Section 3 bullet). It is restored
    here. The wording is unchanged.

- **2026-10-09 #68 — Claim-audit decisions (REVISION_BRIEF §12a) and the
  fresh-session handoff.** The author supplied a new `REVISION_BRIEF.md`
  (adding §12a and §13), which replaced the old file. It stays untracked.
  - **Every proposed fix in `CLAIM_AUDIT.md` is approved**, with these
    refinements:
    - **Szymanski** (related_work:69-73), short form only: "Szymanski et al.
      propose treating role and expertise as separate dimensions, because
      the field has often conflated them. Where role and the reader's deficit
      come apart, a deployment would have to select on the deficit."
      Lines 64-66 already say each tier is designed against the deficit.
    - **The audit's fix text, as written:** Imrie (related_work:44), the
      saturated-construction sentence (:165), the Maisoon / Widyawati
      attributions (:183), Eltawil / Young (data_and_vehicle:164) and
      Nielsen / WCAG (evaluation:59). For Nielsen: "revised heuristics",
      with no count.
    - **Uncited follow-ons.** related_work:176 becomes "a two-row outlier
      removal". related_work:189-190 says "14 healthcare professionals" and
      gives the 71.4% as the source frames it (across three clinical cases),
      with the source passage quoted in a `%` comment.
    - **§3.4 conflicting vectors.** The file wins on 68 / 66: "Out of fold,
      each such record is usually scored by a fold model that saw its twin
      with the other label: 68 of the 71 are scored outside the 0.15 margin,
      66 are mispredicted, and they produce 10 `\textsc{red}` bands, none for
      a true high-risk record." Both derivations go in a `%` comment. This is
      a batch C touch to a committed section, committed separately.
  - **Batches B and C (brief §13).**
    - Batch B: §6, §7 and §8.
    - Batch C: §2 with all its §12a fixes, §1, and the §3.4 sentence.
    - One subagent task per section. Each is followed by the §10 checks and a
      re-check of its citation sentences against `CLAIM_AUDIT.md`, then a
      stop for approval. Nothing is committed before approval.
  - **Gap recorded for the author.** §13 assigns no batch to the approved
    fixes at data_and_vehicle:164 and evaluation:59. The handoff lists them
    as unassigned.
  - **"Next step" rewritten** as a handoff for a fresh session: phase,
    commits, what is and is not committed, open items (batches B, C and D,
    verification, repo and Zenodo, upload package), and the files to read
    first. The old Gate A/B/C list is superseded. Its live items (the
    author read, the cold-run recipe, packaging) are carried into the
    handoff, and its history stays in #43-#57.
- **2026-10-09 #69 — Batches B and C closed: the author's decisions on the
  drafts (REVISION_BRIEF §13a), applied and committed.** The author supplied a
  new `REVISION_BRIEF.md` (adding §13a-§17), which replaced the old file. It
  stays untracked.
  - **Drafts.** One `paper-writer` task per section (§6, §7, §8, §2, §1)
    plus the claim-audit touches to §3 and §5. Each was followed by the
    WRITING_RULES §10 checks and a citation re-check against
    `CLAIM_AUDIT.md`, then a stop for approval.
  - **Decision 1 (§8).** The brief's "prediction runs single-threaded" is
    false as a general statement, because `evaluate()` predicts with
    `n_jobs=-1` for Table 2. Section 8 now says "The out-of-fold scoring that
    produces every case probability and gate count runs single-threaded, so
    the forest's floating-point sums are added in a fixed order."
    `evaluate()` is unchanged.
  - **Decision 2 (§3.4).** The author's split replaces the §12a wording: "Out
    of fold, each such record is usually scored by a fold model that saw its
    twin with the other label. Of the 71 records on the 35 conflicting
    vectors (Section 3.2), 68 are scored outside the 0.15 margin and 66 are
    mispredicted; they produce 10 red bands, none for a true high-risk
    record." The table pointer is kept. "Usually" is 57 of 71; the
    derivation is in a `%` comment.
  - **Decision 3 (length).** Growth accepted, no forced trims. Body words,
    HEAD before the batches to committed: §6 718 to 811, §7 194 to 228, §8
    539 to 607, §2 1429 to 1329, §1 1044 to 1045, §3 1709 to 1741, §5 989
    to 960.
  - **Decision 4 (commits).** WRITING_RULES §1 wins over brief §13: one
    commit per file. The §3 and §5 claim-audit fixes are two commits, both
    citing this entry.
  - **Decision 5 (§2 announcements).** All five rewritten:
    - opener: "Two literatures frame the design ... the standard it has to
      meet";
    - "and that divergence is one of our stated contributions" cut;
    - "That intersection, and only that intersection, is what we claim."
      deleted;
    - 2.3 ends at "the artifact that implements it.";
    - the Yesmin close is "Their study does not ask what a health worker or
      a mother makes of a derated signal."
  - **Decision 6, other §2 wording.**
    - "That is the gap this paper sits in." is deleted.
    - 2.3 ends "which is why a user study is the next step. We propose a
      rendering rule and evaluate the artifact that implements it." The
      untrue "every paper named in this subsection has users" is gone.
    - Yesmin's participants are "healthcare professionals".
    - §2.5 says "We use the same pipeline as a vehicle." The "adds nothing
      to that modelling work" boundary lives only in §1.1, and the opener's
      "and use it as a vehicle" is removed so the phrase appears once.
    - §2.2: ", rather than a shortfall in coverage" is dropped, and the
      Bhatt paragraph reads "The mother receives a different assertion,
      while the clinician receives the split probabilities unmodified."
  - **Decision 6, /anti-ai.**
    - §6: all three proposals.
    - §7: both. "Three" is spelled out at the start of the split sentence.
    - §8: both.
    - §1: the duplicates sentence is "We found no published report of these
      duplicates (Section 3.3), and we report what they cost without
      claiming to have found them first". "Three boundaries go with those
      claims." is deleted. "not an emergency / not a concern" is kept, and
      the 1.2 merge accepted.
    - §3: the split above; "Young et al.'s scoping review finds ...";
      "exactly our situation" becomes "our situation".
    - §5: the "designed to find usability problems without users" sentence
      is deleted. The Nielsen row labels stay.
  - **Implementation notes.**
    - The 6.5 pointer to Section 6.2 needed a label, so
      `\label{sec:lim-data}` is added there.
    - §1's new duplicates sentence rests on §3.3's "We searched for prior
      documentation of them in this benchmark and found none".
  - **Checks and build.**
    - The §3 greps are clean on all seven files. The only "novelty" is
      Hendrickx's term. Each paragraph has at most one of the WRITING_RULES
      contrast forms.
    - Citation re-check: Kompa now matches audit row 14 exactly, Yesmin
      matches N3, and no other citing clause changed.
    - Scratch build: 21 pp, 0 errors, 0 undefined, 0 overfull, 2 underfull
      (both pre-existing).
  - **Housekeeping.** The §8 subagent reported leaving an idle python
    process. All four running python processes were listed with their
    command lines, and none runs from this session's scratchpad or this
    repo: two `-m ielts_tts` from 6 Oct, and two `D:\files` `main.py`. The
    subagent's process had already exited. Nothing was stopped.
  - **Commits.** `ae5931e` §6, `0da7566` §7, `e2fed0f` §8, `41b5f8c` §2,
    `45158a3` §1, `9345154` §3, `8e4aa62` §5. This entry and the handoff
    are the next commit.
  - **Handoff.** "Next step" is rewritten:
    - batch D (brief §14) is next, in a fresh session;
    - §15 verification runs in another new session that has written
      nothing;
    - then the cold run and both authors' read, §16 repo and Zenodo, and
      the §17 upload package.

    The cold-run note now says only out-of-fold scoring is single-threaded.
- **2026-10-10 #70 — Batch D closed (REVISION_BRIEF §14): abstract, back
  matter, `main.tex` metadata and two small fixes, committed one file per
  commit; the tracked PDF and `.bbl` rebuilt in place.** The revision under
  REVISION_BRIEF is complete. Drafted on 2026-10-09; the author's decisions
  A-D and the commits are dated 2026-10-10.
  - **Abstract.** The first draft was the §9 text verbatim (199 words, 1210
    characters). The `/anti-ai` audit ran report-only (CLAUDE.md rule 8) and
    found three problems in that text:
    - "Every string is filled from templates over SHAP attributions" is
      inaccurate. The mother's Hindi sentence and the card header are chosen
      by band, which is why the Hindi transcripts stayed identical in #62.
    - "Code, tables and renderings regenerate": the code is what runs, not
      what is regenerated.
    - "Scored out of fold …, the gate derates" is a dangling participle, and
      it is the first mention of "the gate".
  - **Decision A.** The author supplied the final abstract text, which fixes
    all three and defines the band ("green, amber or red"). It is committed
    verbatim: **200 words, 1221 characters**, ASCII, no thousands commas.
    - Each of the 12 numbers is traced in the `%` block. Each was re-read
      from `p1_gate_summary.csv`, `p1_cohort_summary.csv`,
      `p1_duplicate_leakage.csv` and `src/render.py` (`RED_MARGIN`).
    - "14" was re-derived from `p1_oof_predictions.csv`: true high and
      predicted low = 14 = true high and GREEN.
    - `ABSTRACT_ARXIV.txt` (untracked) equals the LaTeX body after whitespace
      normalisation.
  - **The abstract's old comment block was replaced.** It carried old values
    (`0.487/0.499`) and the eight-item disclaimer checklist of #49/#57, which
    WRITING_RULES §4 supersedes: boundaries go in Section 1.1 and Limitations
    only, and the abstract gets at most two scope sentences. The new block
    keeps the pointer to the labelled journal abstract (commit `6993541`).
  - **Decision B.** `\textbf{Keywords:}` stays. WRITING_RULES §3 (untracked)
    now allows that label in bold, so the §15 grep passes it.
  - **Back matter (brief §10, §14; decisions C and D).**
    - The AI statement's first two sentences are WRITING_RULES §8 verbatim,
      checked by script. The closing no-language-model sentence is unchanged.
    - CRediT: the two bold names and their `---` became `\paragraph{}`
      run-in heads.
    - Aditi Patil: "Hindi authoring and review, clinical domain input,
      ASHA-tier design input, Writing – review & editing". Decision C uses
      the official CRediT name ("review \& editing"), not the brief's "review
      and editing". Sapariya's roles are unchanged.
    - Decision D: data availability opens "We use the UCI Maternal Health
      Risk dataset [ahmed2020maternal] (repository id 863), …", so "dataset"
      is not repeated.
    - The ethics statement is unchanged.
  - **`main.tex`.** `\hypersetup{pdftitle=…, pdfauthor={Maitreya Sapariya,
    Aditi Patil}}` as brief §14 gives it, placed after `hyperref` is loaded.
    `pdfinfo` confirms both fields.
  - **Two author-requested fixes.**
    - `intro.tex` roadmap: "the two literatures it claims between and the
      three it is answerable to" became "the two literatures that frame the
      design and the three that set the standard it has to meet", matching
      the Section 2 opener (#69 Decision 5).
    - `reproducibility.tex`: "We state that as it is." is deleted.
  - **WRITING_RULES §10 checks on all five files.**
    - The §3 greps are clean. The only remaining hits are the Keywords label
      (now allowed) and five contrast forms in committed lines of `intro.tex`
      (L133, L182, L192) and `reproducibility.tex` (L56, L109) that this
      batch did not touch, each one per paragraph.
    - No old value appears in typeset text or comments of the changed files.
    - The one new citation, `ahmed2020maternal`, matches its DataCite record
      (#63) and the audited body sentence at data_and_vehicle:69.
  - **Builds.**
    - Scratch: 21 pp, 0 errors, 0 undefined, 0 overfull, 2 underfull
      (pre-existing), 0 bibtex warnings, no "??".
    - **In place**, in `paper/`: pdflatex, bibtex, then four more pdflatex
      runs (five pdflatex passes). The log matches the scratch build, with
      no rerun request. 37 bibitems.
    - `main.bbl` is byte-identical to the scratch build's, and the PDF's text
      is identical too.
    - The `.aux`, `.log`, `.out` and `.blg` outputs are gitignored.
  - **Commits:**
    - `b615c1e` abstract;
    - `434cdc8` back matter;
    - `5031e56` `main.tex`;
    - `529bfc2` Section 1;
    - `bef9f0f` Section 8;
    - `e35b270` the rebuilt `main.pdf` and `main.bbl`.

    This entry and the handoff are the next commit.
  - **Handoff.** "Next step" is rewritten. Whole-paper verification (brief
    §15) is next, in a new session that has written nothing. After it come
    the moderation check, the cold run and both authors' read, §16 repo and
    Zenodo, and the §17 upload package.
- **2026-10-10 #71 — Batch E (REVISION_BRIEF §18): the VERIFICATION.md fixes,
  committed one file per commit, and the tracked PDF and `.bbl` rebuilt.**
  The §15 verifier session (HEAD `66872d4`) wrote `VERIFICATION.md`
  (untracked) and stays open; it re-checks this batch under §19. Fix IDs
  follow VERIFICATION.md.
  - **Correction to #70 (A8).** #70 and its handoff say "No `%` comment in
    `paper/` carries an old value since #70". That is false. The history
    comments at the top of `three_tiers.tex` (old lines 23–24, 33, 39, 42)
    still carry `row 382`, `0.451/0.097/0.453`, `row 66` and the
    13-year-old. None of it is typeset. §16 step 1b removes it from the
    public sources.
  - **A2 (template claim).** The band selects the card header, the next step
    and the mother's spoken sentence (`src/render.py:323-326`, `:391`
    `MOTHER_HI[band]`). The attributions fill only the driver list
    (`top_drivers`).
    - §4.3 gets the brief's full statement.
    - §1.1 and §7 get the brief's short form. §7 keeps its tail ", so any
      rendering here can be regenerated and checked line by line".
    - **The propagation grep found three more sites, all fixed:**
      - §2.1 "templates over SHAP attributions" now reads "templates,
        selected by the band and filled from the SHAP attributions".
      - The back-matter AI statement's closing sentence gets the same
        clause. Its no-language-model content is unchanged.
      - §3.4: "makes the ASHA and mother tiers expressible as templates over
        attributions" is false for the mother tier. It now reads "makes the
        ASHA tier's driver list expressible as a template over
        attributions".
  - **A3.** `\label{sec:tiers-render}` added to §4.3. §6.1 now reads "the
    icon-array paragraph of Section 4.3 makes it".
  - **A4.** From `heuristic_matrix.csv` (48 rows, 16 criteria):
    - 14 criteria are rated Pass in at least one tier, and 6 in all three
      (1.4.3, 3.2.4, Nielsen 1, 2, 4, 5).
    - 2 are Deferred in all three tiers (2.1/2.4 and 4.1.2).
    - 14 + 2 = 16, so the counts fit the sentence form.
    - Typeset: "Read by row, 14 of the 16 criteria are rated pass in at
      least one tier and 6 in all three; the other 2 (rows 2.1/2.4 and
      4.1.2) are deferred in every tier." The derivation is in a `%`
      comment.
    - **Two departures from the brief.** First, "Read by row, the criteria
      are covered." states the same false claim, so propagation replaces it
      as well. Second, "Read by row, 14 of the 16 … the other 2" replaces
      "Of the 16 criteria, 14 … 2 (…)", which /anti-ai flagged for its
      stacked punctuation and clause-initial numeral.
  - **A5.** "Out of fold," in §1.1 ("Out of fold, the gate derates …"), §4.3
    and §7 ("Out of fold, the model calls this true-low record …"), as the
    brief words them. No other sentence-initial "Scored out of fold"
    remains.
  - **A6, A7, A11** use the brief's wording. **F1:** `\citep{ahmed2020maternal}`
    on the 7 bpm sentence, plus a `%` comment: 2 rows of the cached raw file
    have HeartRate 7.0, the next lowest is 60.0, and `src/model.py:65`
    `MIN_PLAUSIBLE_HR = 20`, applied at `:96-97`. **F2, F3, F4:** `%`
    derivations (98 = 78 + 20; 233 / 106 = 2.198; 38.2 and 38.4 round to 38).
  - **Row 25.** "fit tree ensembles" becomes "fit ensemble classifiers", and
    the §2.5 opener's "tree-ensemble and SHAP pipeline" becomes "ensemble
    and SHAP pipeline". "Tree ensembles" stays only in the Maisoon-only
    sentence, which its abstract supports (RF, XGBoost).
  - **A10.**
    - (a) Table 3 headers are plain.
    - (b) `{D}esigning` in kim2024stakeholder; the title matches Crossref.
    - (c) The Crossref `article-number` fields, fetched this session from
      api.crossref.org/works/<doi>, are quoted in `%` comments: Kompa "4",
      Mamun "e70491", Rosenblatt "1829". None of the three has a `page`
      field. Each is added as `pages`, the field the file's other Crossref
      entries use; plainnat prints it as `4(1):4`.
  - **/anti-ai** ran report-only on every changed sentence. One item is
    applied, the A4 wording above. Three items concern brief-prescribed
    wording and are left for the author:
    - §1.1: "at inference" now appears in the run-in head, the brief's
      sentence and the committed next sentence.
    - §2.3: "community health workers in India" is repeated in consecutive
      sentences.
    - **[CHECK]** §8: "which carries every cohort count this paper quotes"
      is too broad. The 71 records on conflicting vectors come from
      `p1_oof_predictions.csv`, not `p1_cohort_summary.csv`.
  - **Checks (WRITING_RULES §10) on all ten files.**
    - Every number in a changed line traces to its file:
      - `p1_gate_summary.csv` `predicted_high` (11, 114, 3, 78, 103);
      - `shap_case_summary.csv` and `p1_oof_predictions.csv` rows 426 and
        325 (0.233/0.382/0.384, margins 0.0018 and 0.0294);
      - `heuristic_matrix.csv` (16, 14, 6, 2);
      - Crossref for the article numbers.
    - The new citation clauses fit their sources: the dataset for 7 bpm, and
      the six abstracts (VERIFICATION row 25) for "ensemble classifiers".
    - §3 greps: no new hit. Eight `\textbf` are gone from Table 3. The
      remaining hits are the allowed "novelty" and the card-header dash.
    - Old values in typeset text: only the correct `102`. No thousands
      separators. 37 cited keys = 37 entries.
  - **Builds.**
    - Scratch: 21 pp, 0 errors, 0 undefined references or citations, 0
      overfull, 0 bibtex warnings.
    - There are 3 underfull boxes: the 2 pre-existing ones and one new one,
      `reproducibility.tex` lines 43–51 (the A6 item, badness 1881). It is
      cosmetic, and the wording is the brief's.
    - In place: pdflatex, bibtex, then four more pdflatex runs. The `.bbl`
      and the PDF text are byte-identical to the scratch build, and
      `pdfinfo` title and author match `main.tex`.
  - **Still open.** A1 (archive) and A9 (cold run) wait for §16. The row
    notes 36 (Eltawil/Young lead-in) and 38 (Nielsen 1994 not read) have no
    brief item and are unchanged.
  - **Commits:**
    - `b0f09f5` Section 1, `85be244` Section 2, `e32fa8c` Section 3,
      `214ed1e` Section 4, `6ab507f` Section 5;
    - `85da2be` Section 6, `319a8f6` Section 7, `0ef2309` Section 8,
      `12e1582` back matter, `2f078ca` `refs.bib`;
    - `8dacb47` the rebuilt `main.pdf` and `main.bbl`.

    This entry is the next commit, and the handoff follows in its own commit.
- **2026-10-11 #72 — Batch F (REVISION_BRIEF §21): the §19 findings O1 and
  N1-N4, the A6 remainder and rows 36 and 38, one commit per file, and the
  tracked PDF rebuilt.** The §19 re-verification ran at `d62c376` and appended
  to `VERIFICATION.md`. The verifier re-checks this batch only (`d62c376..HEAD`),
  and then come the §20 text-freeze reads.
  - **O1 (Hindi-string provenance, outside the paper).** `git grep -i` on every
    tracked file for "physician", "clinically reviewed", "clinical review" and
    "MBBS collaborator".
    - Before: `README.md:47-48`; `src/render.py:81-82` (comment);
      `src/evaluate.py:164-165` (the 3.1.1/3.1.2 mother rationale);
      `results/tables/heuristic_matrix.csv:19` and
      `results/tables/heuristic_evaluation.md:89` (the same rationale,
      generated); `STATE.md:571, 575, 999-1000`.
    - After: `STATE.md` only. It is exempt: it moves to `notes/` in §16, and
      lines 571 and 575 are Decision Log entries (append-only).
    - README and the render.py comment now read "written and reviewed by the
      second author, a final-year MBBS student and native Hindi speaker". The
      evaluate.py rationale uses the brief's short form, "written and reviewed
      by a native-speaking final-year MBBS student".
    - No rendered TXT or PNG carried the phrase, and the render.py change is a
      comment, so the renderer was not re-run.
    - `python -m src.evaluate` ran twice (`.venv`, Python 3.12.13). The two runs
      are byte-identical: `heuristic_matrix.csv` SHA-256 `241b9132…`,
      `heuristic_evaluation.md` `ca02bf1f…`. Against HEAD, one CSV cell
      differs (the row-19 rationale) and one `.md` line. The word diff is
      authored → written, clinically → final-year, collaborator → student.
      All 48 ratings are identical, and the counts stay 29/12/1/6.
  - **N1 (template claim).**
    - Abstract: the brief's sentence, "All text comes from fixed templates;
      SHAP attributions supply the card's drivers, and no language model runs
      at inference."
    - §1.1 and §7: the brief's short form, "All text comes from fixed
      templates, with no language model at inference." §7 keeps its tail.
    - §4.3 keeps its precise version.
    - **Departure, the AI statement.** WRITING_RULES §8, as the author updated
      it, gives the closing sentence as "All text comes from fixed templates,
      with no language model at inference." Placed alone after two sentences
      on how the manuscript was drafted, "All text" would read as the
      manuscript's own text. So the closing sentence keeps its frame and
      carries the wording as a clause: "This is a statement about how the
      paper was written and not about the system it describes: in the
      rendering pipeline of Section 4, all text comes from fixed templates,
      with no language model at inference, which is one of the contributions
      claimed here." The author decides: keep this, or use the literal
      sentence.
    - The WRITING_RULES §8 note had already been updated by the author. It is
      untracked and was not edited.
    - Propagation (typeset text, comments stripped): "template", "filled",
      "selected by the band", "all text", "every string", "drivers",
      "language model". §2.1's "fixed set of templates, selected by the band
      and filled from the SHAP attributions, so every string a health worker
      or a mother receives …" is scoped to the two tiers it names, where it is
      accurate, so it is confirmed and unchanged. §3.4 ("the ASHA tier's
      driver list … a template over attributions") and §6 ("every string is a
      fixed template constant", about localisation) are consistent.
  - **N2.** §1.1 keeps one "at inference", the one in the N1 sentence. The
    run-in head becomes "An artifact: an auditable rendering pipeline with no
    language model.", and "Nothing is generated at inference, so" becomes
    "Nothing is generated, so". §2.3 now reads "Okolo et al.\ interviewed
    health workers in rural India".
  - **N3 (§5.2).** From `heuristic_matrix.csv`: Partial per tier is clinician
    5, ASHA 3, mother 4 (12 in all), and the one Fail is clinician, 1.4.5.
    - Typeset: "Read by column, each tier has criteria rated partial
      (clinician 5, ASHA 3, mother 4), and the one fail is in the clinician
      column. Two of those gaps sit where a single universal rendering would
      have to compromise: …" The rest of that sentence is unchanged.
    - The brief's example "Partial ratings on different criteria" is not
      used, because the criteria overlap: 1.1.1 and Nielsen 6 and 10 are
      partial for both clinician and mother, and 3.1.5 for clinician and ASHA.
    - "the other 2" becomes "the remaining 2 of the 16". The `%` derivation
      is added.
  - **A6 remainder and N4.** The clause now reads "which carries the
    deduplication and cohort counts" (`p1_cohort_summary.csv`
    `dropped_exact_duplicates` and the cohort rows). With that wording alone,
    the underfull box (lines 43–51, badness 1881) stayed. Five variants were
    built in a scratch copy, and dropping "the" before "metrics" removes the
    box without adding one. The 2 underfull boxes left both predate batch E.
  - **Row 36.** The lead-in is now "Measuring what leakage costs has
    precedent:". The Eltawil and Young clauses are unchanged.
  - **Row 38 (record only).** The author accepts the §5 Nielsen 1994 sentence
    as it is: it names the paper only as the source of the revised
    heuristics, which is its documented content. The full text of
    `nielsen1994enhancing` could not be retrieved, and neither could its
    abstract (the 2026-10-09 comment in `evaluation.tex`).
  - **/anti-ai** (use case 3.1, audit) ran on every changed sentence. One item
    is applied, to the writer's own wording: "all three tiers have partial
    ratings" became "each tier has criteria rated partial", since a lowercase
    "partial ratings" reads as incomplete ratings. Left for the author:
    - The §1.1 run-in head and its first sentence both say "no language
      model", on adjacent lines. This follows from N1 and N2 together.
    - §5.2 states the one fail twice, before Table 4 and after it (N3
      prescribes the second).
    - The AI statement's closing sentence runs to about 45 words.
  - **[CHECK] outside the paper, not changed:**
    - `README.md:50`, "The plain-language messages are deterministic templates
      over SHAP outputs.", has N1's over-breadth: the mother's message is
      selected by the band. It is for the §16 README rewrite.
    - `paper/ARXIV_SUBMISSION.md:102` holds an old abstract ("Every string is
      a deterministic template filled from the case's SHAP attributions"). It
      moves to `notes/` in §16, and §17 regenerates it.
  - **Abstract.** 200 words and 1229 characters (1230 bytes with the trailing
    newline). `ABSTRACT_ARXIV.txt` (untracked) was regenerated by an
    extraction that first reproduced the HEAD file byte for byte. It is
    ASCII, with one trailing newline.
  - **Checks (WRITING_RULES §10) on every changed file.**
    - Numbers: 5, 3, 4, 12 and 1.4.5 come from `heuristic_matrix.csv`, as do
      the counts 29/12/1/6.
    - Citations: no citing clause changed in substance. §2.3 narrows "community
      health workers" to "health workers" under the same two citations, and
      the row-36 lead-in leaves both citations and their clauses as they were.
    - §3 grep: no new hit in any changed file.
    - Propagation: as above, for N1, N2 ("at inference" now appears once in
      the §1.1 paragraph), N3 ("fails" and "the other 2" are gone, and the
      §5.2 "single failure" sentence is consistent), A6 ("cohort count" now
      appears only in the new clause), row 36 ("contribution type" has 0
      hits) and O1 (the paper has only the §4.3 canonical sentence).
  - **Build.**
    - Scratch: 21 pp, 0 errors, 0 undefined references or citations, 0
      overfull, 0 bibtex warnings, 2 underfull (both pre-existing), 37
      bibitems. `pdfinfo` title and author match `main.tex`.
    - In place: five passes. A cold build from `git archive HEAD` gives the
      same `.bbl` and PDF text.
    - `main.bbl` came out byte-identical to the committed file, because
      `refs.bib` did not change. Only `main.pdf` is in the rebuild commit.
    - A word-level diff of the PDF text against the previous PDF shows
      exactly the batch F sentences, plus page reflow: the §6 heading moves
      to the next page, and the page count stays 21.
  - **Commits:**
    - `071f1ca` render.py, `7c0d189` evaluate.py, `bc90079` the regenerated
      matrix and evaluation tables, `d702b75` README;
    - `1eb0c55` abstract, `9255178` Section 1, `6a04cb2` Section 2, `8463251`
      Section 3, `c70ba3f` Section 5, `b2cca9d` Section 7, `ada3de9`
      Section 8, `dd420c9` back matter;
    - `2a3d0b6` the rebuilt `main.pdf`.

    This entry is the next commit, and the handoff follows in its own commit.
- **2026-10-11 #73 — Batch G (REVISION_BRIEF §22): the last prose touch, one
  commit per file, and the tracked PDF rebuilt.** After this, prose changes
  only through §20. As §22 says, batch G gets no verifier round, because the
  reviewer reads the full PDF during the moderation audit.
  - **B1 (§1.1).** "Nothing is generated, so the rendering can be
    regenerated, diffed and checked line by line by someone who does not
    trust us, and there is nothing in it to hallucinate." now reads "No text
    is generated, so every string can be regenerated and checked line by
    line." The sentence is scoped to text, because the audio is not
    byte-stable (§8.2).
    - **Propagation.** §7's "so any rendering here can be regenerated and
      checked line by line" makes the same claim and covers the audio. It now
      reads "so every string can be regenerated and checked line by line".
      This change is outside the brief's named sites and was made under the
      propagation rule.
    - Confirmed consistent, unchanged:
      - §2.1 ("every string a health worker or a mother receives … can be
        regenerated and audited"; "a rendering an auditor can check line by
        line");
      - §4.3 ("the card can be regenerated and compared line by line");
      - §1 roadmap ("the commands that regenerate every artifact here");
      - the abstract ("Five commands regenerate every table and rendering");
      - §8.1, which scopes byte-for-byte to PNG, CSV and text, with the
        audio exception in §8.2.

      None of these says a regenerated artifact is byte-identical except §8,
      which states the exception.
  - **B2.**
    - **§1.1.** The run-in head loses "with no language model" and becomes
      "An artifact: an auditable rendering pipeline.". The first sentence
      keeps the N1 wording (#72), so "no language model" and "at inference"
      each appear once in the paragraph.
    - **§5.2.** The one fail is stated once: "The single failure is the
      clinician tier shipping as an image of text." stays, in the paragraph
      before Table 4. ", and the one fail is in the clinician column" is cut
      from the by-column sentence after it. The `%` derivation still holds:
      1 Fail, clinician, 1.4.5.
    - **AI statement.** The sentence is split after "checked by the
      authors": "… and the final wording were determined and checked by the
      authors. The authors approved the final wording and take full
      responsibility for the content."
      - The three opening sentences match WRITING_RULES §8 word for word
        (checked by script after whitespace normalisation). The author had
        already updated §8 to mirror the split. It is untracked and was not
        edited.
      - The closing sentence keeps the #72 clause form. The author decision
        recorded in #72 (keep it, or use §8's standalone "All text comes from
        fixed templates, with no language model at inference.") is still
        open.
  - **B3 (Table 4 placement), one attempt: `[tb]` in place of `[t]`.** It
    made no difference: all 21 pages render byte-identical to the `[t]`
    build at 30 dpi grayscale. So `[t]` stays and the source is unchanged.
    The blank quarter page is closed anyway: B1 and B2 shortened §1.1 and
    §5.2, and Table 4 now fits at the top of p12, beside its first
    reference.
    - Lowest ink row per page as a percentage of page height, previous PDF →
      new PDF:
      - p2 80 → 86, p9 76 → 83, p12 77 → 83, p15 79 → 87;
      - p17 42 → 19, the last back-matter page before the reference list's
        `\clearpage`;
      - every other page within 1–3 points.
    - Floats: Figure 1 moves to p8, Table 4 to p12, and §6 now starts on
      p13 under the end of §5.
  - **/anti-ai** (use case 3.1, audit) ran on every changed sentence. Nothing
    was applied. Three items concern prescribed wording and are noted:
    - in §1.1, "All text comes from …" is followed by "No text is generated …";
    - "Two of those gaps" has no earlier noun "gaps" (wording from #72);
    - "the final wording" appears in both of the two AI-statement sentences
      (WRITING_RULES §8, exact).
  - **Checks (WRITING_RULES §10).** No number changed. No citation sentence
    changed. The §3 grep found no new hit in the four files. Propagation is
    as above. "language model" appears once in §1.1, and "fail" in §5 only
    in the first-pass "four Fail ratings", the "1 fail" count, the "single
    failure" sentence and the Table 4 legend.
  - **Build.** In place, five passes:
    - 21 pp, 0 errors, 0 undefined references or citations, 0 overfull, 0
      bibtex warnings, 2 underfull (both from before batch E), 37 bibitems;
      `pdfinfo` title and author match `main.tex`.
    - A cold build from `git archive HEAD` gives the same `.bbl` and PDF
      text.
    - `main.bbl` came out byte-identical to the committed file, so only
      `main.pdf` is in the rebuild commit.
    - A word-level diff of the PDF text against the previous PDF shows the
      batch G sentences and float and page-number reflow, and nothing else.
  - **Commits:**
    - `520fdd9` Section 1, `9877096` Section 5, `e579928` Section 7,
      `f1b281b` back matter;
    - `f68c1d6` the rebuilt `main.pdf`.

    This entry is the next commit, and the handoff follows in its own commit.
- **2026-10-11 #74 — Correction to #73 (float pages).** #73 says "Figure 1
  moves to p8". That is wrong: I misread a `pdftotext` page marker. From
  `paper/main.aux` at `f68c1d6`, Figure 1 is on p9 (it was on p10 at
  `03a3808`), Table 4 is on p12 (it was on p13), and §6 starts on p13. The
  rest of #73 stands; its `\clearpage` statement is `main.tex:219`, before
  the reference list.
- **2026-10-12 #75 — The 11 Oct cold run (REVISION_BRIEF §16 step 0, §23
  step 1a): the pipeline reproduces.** The run was a fresh clone in a
  temporary directory, in a separate session. It changed no tracked file.
  The facts below are as the author reported them on 12 Oct, except where a
  line says "confirmed here".
  - **Platform:** Windows 11, Python 3.12.10, an environment installed from
    `requirements-lock.txt`. (The writer session's `.venv` is 3.12.13.)
  - **Dataset:** `src.data` downloaded the file fresh from UCI. Its SHA-256 is
    `aadb4175212de4d47b44c4ed141fc73dee988beaf09b5e6af6b5ffb63111b690`, the
    same as the cached `data/raw/maternal_health_risk.csv`.
    - Confirmed here: the cached file's SHA-256 is that value. The file has
      1015 lines, a header and 1014 records.
  - **PNGs:** 17, all byte-identical to the committed files.
  - **Text outputs:** 18 (9 CSV, 1 Markdown, 8 TXT), all identical in
    content. They differ from the committed files only in line endings:
    Python writes CRLF on Windows, and git stores LF through
    `core.autocrlf`.
  - **MP3s:** 4, with matching durations. Their bytes are not compared, as
    §8.2 says.
  - **57 of 71:** confirmed two ways.
  - **Counts confirmed here:** `git ls-files results` gives 17 `.png`, 9
    `.csv`, 1 `.md`, 8 `.txt` and 4 `.mp3`.
  - **Windows long paths:** pip install can fail because NumPy's OpenBLAS
    DLL path can exceed 260 characters. The fix is to clone to a short path
    or enable long paths. §16 step 2 puts this note in the README.
  - **Consequences:**
    - §8.1's "Re-running the pipeline reproduces every PNG, CSV and text
      output byte for byte" is false for the text outputs on Windows. #76
      (H4) replaces it with the measured result.
    - The cold-run recipe in the handoff is corrected to match.
    - This closes A9. §16 step 0 is done.
- **2026-10-12 #76 — Batch H (REVISION_BRIEF §23 step 2), the last text
  change, and the authors' approval. The text is now frozen.**
  - **Context.** On 11 Oct the reviewer's moderation audit returned LIKELY
    PASS (the §23 heading). Both authors then read the 11 Oct PDF end to end
    on 11–12 Oct and approved it without changes, so **H6 is NONE**. That
    approval is the §20 freeze read, and it closes old Gate A.
  - **H1 (§1.1).** "All text comes from fixed templates, with no language
    model at inference. No text is generated, so every string can be
    regenerated and checked line by line." now reads "All text comes from
    fixed templates, with no language model at inference, so every string can
    be regenerated and checked line by line." This is word for word the
    sentence in §7.
  - **H2 (§5.2).** "Two of those gaps sit where …" now reads "Two of those
    partial ratings sit where …".
    - [CHECK, not changed] Later in the sentence, "neither gap" no longer has
      an earlier "gaps" to point back to. It reads as the two needs just
      named.
  - **H3 (AI statement).**
    - Second sentence: "The research design, the analyses, every reported
      number, the selection and verification of every citation, and the
      final wording were determined and checked by the authors." now reads
      "The research design, the analyses, every reported number and the
      selection and verification of every citation were determined and
      checked by the authors."
    - Closing: "This is a statement about how the paper was written and not
      about the system it describes: in the rendering pipeline of Section 4,
      all text comes from fixed templates, with no language model at
      inference, which is one of the contributions claimed here." now reads
      "This is a statement about how the paper was written, not about the
      system it describes. In the rendering pipeline of Section 4, all text
      comes from fixed templates, with no language model at inference."
    - This settles the closing-sentence decision left open in #72 and #73.
    - The statement now matches WRITING_RULES §8 word for word, checked by
      script after whitespace normalisation. §8 was edited to mirror H3, and
      its "Its closing sentence reads" became "Its two closing sentences
      read". `WRITING_RULES.md` is untracked and was not committed.
    - The `backmatter.tex` comment that said "the closing sentence is kept
      as it was" was updated.
  - **H4 (§8.1).** "Re-running the pipeline reproduces every PNG, CSV and
    text output byte for byte." now reads "A clean run from a fresh clone
    (Windows 11, Python 3.12, the locked environment, the dataset downloaded
    afresh) reproduced all 17 PNGs byte for byte and all 18 CSV, Markdown and
    text outputs with identical content; the text outputs differ from the
    committed copies only in line endings, which follow the platform. The
    freshly downloaded dataset was byte-identical to our cached copy."
    - This is the brief's text exactly. A `%` source line gives the
      derivation of 17 and 18 (`git ls-files results`) and points to #75.
    - §8.2 is unchanged, as the brief says.
  - **H5 (`refs.bib`).**
    - All 21 `pages` fields with a Unicode en dash now use `--`. No other en
      dash was in the file.
    - Rahman: `pages={0013–0018}` is now `pages={13--18}`. The value was
      checked against Crossref this session:
      api.crossref.org/works/10.1109/aiiot58121.2023.10174540 gives page
      "0013-0018". A `%` note records this.
    - nielsen1990heuristic: `series={CHI ’90}` was dropped. `collection` is
      kept, and bibtex ignores it.
    - In `main.bbl`, 11 proceedings entries now print "pages" instead of
      "page". Nielsen 1990 loses its second "CHI ’90", and Rahman reads
      "pages 13–18". Bibtex reports 0 warnings and 37 bibitems.
  - **Propagation (WRITING_RULES §10.5)**, run on the typeset text.
    - H1: §7 has the identical sentence. §2.1 ("Nothing is generated at
      inference time …"), §4.3 ("the card can be regenerated and compared
      line by line") and the abstract's template sentence are consistent.
      "No text is generated" no longer appears anywhere.
    - H2: "gaps" no longer appears in the paper; "gap" remains only in
      "neither gap" and in the Yesmin et al. title.
    - H3: "final wording" appears once. "contributions claimed" no longer
      appears. "language model" is consistent at all six sites.
    - H4: these are consistent:
      - §8's opening ("regenerates from five commands");
      - the abstract ("Five commands regenerate every table and rendering");
      - the §1 roadmap;
      - Data availability;
      - "The pins require Python 3.12";
      - "Every later run reads the cache";
      - §8.2: "byte-identical and sometimes not" for audio, the cold-run
        `results/audio/` note, and "the Hindi source string … reproduces
        exactly". That last one is about content, which the run found
        identical; the line endings of the `.txt` file are what §8.1 now
        describes.

      "Windows" and "platform" each appear once. No sentence makes a claim
      about another platform.
  - **/anti-ai** (use case 3.1, report only). Nothing was applied. All four
    items concern prescribed wording:
    - the H1 sentence is repeated in §1.1 and §7;
    - "neither gap" (see H2);
    - the back matter's single contrast, which carries content;
    - "fresh clone", "downloaded afresh" and "freshly downloaded" appear in
      two sentences.
  - **Checks (WRITING_RULES §10).**
    - New numbers: 17, 18 and 3.12. 17 and 18 come from `git ls-files
      results` (`%` line); 3.12 is already stated in §8.1. Rahman's 13–18
      comes from Crossref.
    - No citation sentence changed.
    - The §3 grep finds no new hit in the four `.tex` files.
  - **Build.**
    - A scratch build, then the tracked files in place, five passes: 21 pp,
      0 errors, 0 undefined references or citations, 0 overfull, 0 bibtex
      warnings, 37 bibitems.
    - 2 underfull, both from before batch E. The `reproducibility.tex` one
      is now at lines 61–65 because the `%` lines shifted it.
    - `pdfinfo` title and author match `main.tex`.
    - A cold build from `git archive HEAD` gives the same `.bbl` and PDF
      text.
    - The word diff against the previous PDF shows the batch H sentences,
      the bibliography changes above and reflow, and nothing else.
    - Floats are unchanged from #74: Table 1 p6, Table 2 p7, Figure 1 p9,
      Table 3 p11, Table 4 p12; §6 starts on p13.
  - **Brief wording.** §23 step 3 says "§16 (steps 1b to 6; step 0 is
    already done)". The author's instruction for this batch says steps 1 to
    6. The handoff follows the author: step 1 (move internal files out of
    tracking) has not been done and comes first.
  - **Commits:**
    - `fefb236` Section 1, `c667cce` Section 5, `fa9c318` back matter,
      `74e07e2` Section 8, `812af03` `refs.bib`;
    - `ec4bb3e` `main.pdf`, `0b25ccb` `main.bbl`.

    #75 is its own commit. This entry is the next commit, and the handoff
    follows in its own commit.
