# arXiv submission sheet

The answer key for whoever fills in the arXiv web form: every field it asks
for, in the form it wants. Written 2026-09-03 during the P6 pre-submission
pass, and refreshed 2026-09-08 after the framing pass (Decision Log #47) moved
the abstract, the page count and the citation count. Nothing here has been
submitted.

---

## Categories

**Primary: `cs.HC` (Human-Computer Interaction).**
The contribution is an explanation design: how one prediction is rendered for
three readers of differing modality, literacy and decision authority. The
evaluation is a heuristic WCAG/Nielsen critique of the rendered artifacts. The
machine learning is a vehicle, not a result.

**Cross-list: `cs.LG` (Machine Learning).**
The leakage audit (duplicate rows moving macro-recall 0.580 to 0.859) and the
top-two-margin abstention gate are claims about model behaviour and evaluation
hygiene on a public benchmark, which is where an ML reader will look for them.

## License

**CC BY 4.0** (`http://creativecommons.org/licenses/by/4.0/`). Matches the
repository and the Zenodo deposit, and is compatible with the UCI dataset's own
CC BY 4.0 terms.

## DOI field

**Leave the arXiv DOI field empty.** The paper gets its own arXiv identifier on
submission. The Zenodo concept DOI `10.5281/zenodo.22252076` points at a
different object, the software and artifact deposit, and it is already cited in
the back matter and the Reproducibility section, where it belongs. That field
is reserved for a journal DOI of this same article, so leave it blank.

---

## Title (plain text)

```
Three Voices: Uncertainty-Gated Rendering of a Maternal-Health Risk Alarm for Mothers, Community Health Workers, and Clinicians
```

## Authors (plain text, arXiv order)

```
Maitreya Sapariya, Aditi Patil
```

- **Maitreya Sapariya** — Department of Information Technology, A. D. Patel
  Institute of Technology (ADIT), Charutar Vidya Mandal (CVM) University, New
  Vallabh Vidyanagar, Anand, Gujarat, India. ORCID 0009-0003-9346-3775.
  Corresponding author, maitreyasapariya@gmail.com.

  On the corresponding address: the affiliation is institutional and stays
  that way, but the address deliberately does **not** encode an enrollment
  number. arXiv lists "undergraduate or high-school research" among the
  content types it typically does not accept, and a submitter with a prior
  decline is told to "anticipate closer scrutiny", so there is no reason to
  hand a moderator a student-number address to read that way. Swap in a
  name-based `adit.ac.in` alias if one is available; that is strictly better
  than a personal address and is a one-line change in `main.tex` and here.
- **Aditi Patil** — Smt. B. K. Shah Medical Institute & Research Centre,
  Sumandeep Vidyapeeth (Deemed to be University).

## Abstract (plain text, paste verbatim)

De-LaTeX'd from `sections/abstract.tex`: math delimiters removed, `\emph`
rendered as straight double quotes, straight quotes throughout, no macros. The
wording is unchanged; this is a transcription.

Three unlabelled paragraphs (Decision Log #49), reordered 2026-09-11:
mechanism, then the leakage measurement, then the caveats. The reorder itself
was a whole-block swap of paragraphs 2 and 3 that changed no word of either;
the transcription measured 1760 characters both before and after it, which is
the mechanical proof. The count then moved to 1827 for a separate correction
made the same day: the duplicate count is now attributed to the 1012 rows that
survive the plausibility filter rather than to the dataset as distributed,
because the raw file holds 562 duplicates and 561 is the post-filter figure
the body has always reported. The Purpose / Methods /
Results / Conclusion labelling of Decision Log #47/#48 was dropped for the
arXiv submission: the journal requires it and arXiv does not, and the labels
put a structural signal on a shopfront that a moderator reads for what the
paper contributes. The labelled version is recoverable from commit 6993541 and
is restored before the journal submission.

Reordered again 2026-09-15, inside paragraph 3 only, and the count moved to
1824. The abstract no longer ENDS on a disclaimer: the novelty-boundary
sentence moved to the head of paragraph 3 and the paragraph now closes on what
the work delivers. Decision Log #49 moved that same sentence out of the end of
paragraph 1 because the last line of a paragraph is where a skimming moderator
lands; the identical reasoning applies to the last line of the abstract, which
#49 did not follow through on. Nothing is softened — the sentence is intact,
one position earlier — and all eight checklist items in
`sections/abstract.tex` survive. The self-label "This is a design and
feasibility artifact" is gone from the manuscript entirely; the Introduction
now names the contribution types in HCI's own vocabulary instead.

```
Three Voices renders a single maternal-health risk prediction as three stakeholder-specific action-signals, one each for a clinician, a community health worker, and a mother, and gates each signal on the model's own uncertainty. Below a fixed top-two margin the highest-severity signal is withheld from the mother's channel and the health worker's, while the clinician's view of the split is untouched: the derate is red to amber, never red to green, and amber still says "needs follow-up". Every string is a deterministic template filled from the case's SHAP attributions, with no language model at inference, so a rendering can be regenerated and audited line by line. Code, the rendered artifacts, the tables and the evaluation matrix are archived, and all of it regenerates from five commands.

We also report a leakage audit of the UCI Maternal Health Risk benchmark. Of the 1012 rows surviving a two-row plausibility filter, 561 are exact duplicates of an earlier row, and retaining them moves macro-recall from 0.580 to 0.859 under the same cross-validation. We quantify that cost; we do not claim to have found it first.

The abstention rule sits between stakeholder-tailored explanation and selective prediction; we claim their pairing, not either mechanism. Our evaluation is a formative single-evaluator heuristic critique of our own renderings; it found five defects, all corrected. It improved the design; it is not evidence that any tier helps a reader. No mother, health worker or clinician has used the system, the data is public, the task is generic maternal-health risk, and we make no clinical-validity claim; user studies with the three groups are the next step, gated on ethics clearance. The paper delivers the rendering mechanism, an auditable implementation, and a reproducible benchmark measurement.
```

**1824 characters**, against the hard ceiling of 1920 that `prep.html` states
("abstracts longer than 1920 characters will not be accepted"); 284 words. Both
counts are machine-measured on the block above, not estimated. The block is
generated from `sections/abstract.tex` rather than retyped, so it cannot drift
from the manuscript the way the previous transcription did — that one still
carried the pre-trim 250-word text after Decision Log #48 shortened the source
to 237, and claimed to be word-for-word identical while it was not.

284 words is over the 150–250 band SN Computer Science sets. That is accepted
here because arXiv sets no word limit, and because the labelled 237-word
abstract is restored for the journal submission.

Verified mechanically against `sections/abstract.tex`: after stripping `$` math
delimiters, `\noindent` and `\emph{}`, the two texts are word-for-word
identical. The block above is pure ASCII with straight quotes and no curly
punctuation, so it survives paste into the arXiv form unchanged. No line starts
with whitespace, which `prep.html` warns will defeat the form's automatic line
wrapping.

**Keywords** (the manuscript carries these under the abstract; arXiv has no
keywords field, so they go nowhere on the form):
explainable AI; uncertainty; selective prediction; maternal health; community
health workers; risk communication.

## Comments field (optional, suggested)

```
20 pages, 1 figure (3 panels), 3 tables. Code, figures and audio artifacts at https://github.com/stiFFLer-codes/three-voices and archived at https://doi.org/10.5281/zenodo.22252076
```

---

## Upload file list

Sixteen files. Preserve the `sections/` subdirectory; everything else sits at
the archive root. The list below is the order `main.tex` inputs them, and it is
generated from `main.tex` rather than maintained by hand — the fifteen-file
version of this list silently omitted `sections/conclusion.tex` for four days
after the Conclusion was added.

```
main.tex
main.bbl
refs.bib
tier_clinician_boundary_mid.png
tier_asha_boundary_mid.png
tier_mother_boundary_mid.png
sections/abstract.tex
sections/intro.tex
sections/related_work.tex
sections/data_and_vehicle.tex
sections/three_tiers.tex
sections/evaluation.tex
sections/limitations.tex
sections/conclusion.tex
sections/reproducibility.tex
sections/backmatter.tex
```

Upload nothing else. Leave out `main.pdf`, `main.aux`, `main.log`, `main.out`
and `main.blg`: arXiv builds the PDF itself, and stray aux files make that
build fail.

### Building the upload

The three PNGs live under `results/figures/` and are copied in at packaging
time. Tracking a second copy inside `paper/` was rejected deliberately, because
that copy could drift from the renderer's output and would weaken the
determinism guarantee the Reproducibility section makes (Decision Log #44).

```sh
mkdir -p arxiv/sections
cp paper/main.tex paper/main.bbl paper/refs.bib arxiv/
cp paper/sections/*.tex arxiv/sections/
cp results/figures/tier_{clinician,asha,mother}_boundary_mid.png arxiv/
# Strip whole-line % comments from the UPLOADED copies only. See below.
sed -i '/^[[:space:]]*%/d' arxiv/main.tex arxiv/sections/*.tex
cd arxiv && tar czf ../three-voices-arxiv.tar.gz .
```

### Why the comments are stripped from the upload

arXiv publishes the raw `.tex` source, so every `%` comment in it is public.
The repository copies carry the working notes this project runs on — the
outline map, the page budget, the contribution stack, the oversell firewall,
the per-section source provenance — and 155 of `main.tex`'s 216 lines are
comment. Among them, in these words: `EXPLICITLY NOT CLAIMED AS NOVEL`, `There
is no ML novelty here`, `Do not claim the mechanism`, `OVERSELL FIREWALL`.

Those lines are correct, and they are why the manuscript is honest. They are
also an argument the authors have with themselves. arXiv's moderation page
names "originality, novelty, significance" as a ground for declining a
submission, so the source as it stands hands a moderator the manuscript's own
internal case that parts of it are not novel. The prose already states every
one of those boundaries where a reader should meet them: Section 1.1 disclaims
all three occupied territories by name, and Section 2 does it again, one
literature at a time.

The `sed` is line-oriented and deletes only lines whose first non-space
character is `%`. No trailing in-line comment and no escaped `\%` is touched,
and the repository files are not modified. This matters for the one place it
could bite: `sections/three_tiers.tex` ends `\subcaptionbox{...}` lines with a
line-joining `%`, and those survive because the `%` is not the first character.

Both variants were compiled from an empty directory on 2026-09-09 and compared.
Identical page count (19), identical file length (609826 bytes), and identical
content streams: the two PDFs differ only in the trailing metadata region,
which is the creation timestamp and document ID that `pdflatex` stamps on every
run.

No source edit is needed. `main.tex` sets
`\graphicspath{{./}{../results/figures/}}`, so in the archive the root matches
first and the `../` entry is never consulted; nothing has to escape the
submission root. The same file compiles in the repository, where `./` holds no
PNGs and the second root resolves them from the renderer's committed output.

### Bibliography

We ship a pre-generated `main.bbl` and let arXiv use it. **Correcting what this
sheet said before 2026-09-09:** arXiv *does* now run bibliography processors —
`submit_tex.html` states it "provides support for bib file processing using
various processors like `biblatex` (with auto-selection of the correct backend)
and `bibtex`", and it blocks a submission that has neither a `.bbl` nor the
`.bib` it needs. Shipping the `.bbl` is still the right call, because it fixes
the output rather than leaving it to arXiv's TeX Live version, but the old
reason given here was wrong.

The same page requires that "the name of the `.bbl` file _must_ match the name
of the main `.tex` file". `main.bbl` against `main.tex` satisfies that.

The `.bbl` is current: **36 `\bibitem` entries against 36 `\cite` keys against
36 `refs.bib` entries**, no orphans in either direction (re-measured
2026-09-15). Some keys are cited in a `\citep` that spans a line break in
`sections/evaluation.tex`, so a line-oriented grep undercounts — count with a
multiline match. All 36 identifiers have been resolved against a Crossref DOI,
an arXiv ID, a PMLR record or the W3C Recommendation, per the CLAUDE.md
citation gate; the two added since 2026-09-09 are `yesmin2026trust` (arXiv
2601.07866) and `wobbrock2016contributions` (Crossref 10.1145/2907069).
`refs.bib` is included for provenance. `pdflatex` never opens it while the
`.bbl` is present, so dropping it would change nothing in the output.

### Standalone compile, verified

The sixteen files above were copied into an empty directory containing nothing
else (no `.aux`, `.log`, `.out` or `.pdf`) and compiled with `pdflatex` alone,
three passes, no BibTeX run. That is what arXiv does with a shipped `.bbl`.

**Result: 20-page PDF, 0 errors, 0 overfull boxes, 0 undefined citations or
references, 0 LaTeX warnings.** All 36 citations and every internal
cross-reference resolve from the shipped `.bbl`, numbered [1] through [36].
Re-verified 2026-09-15 after the repositioning pass (#57).

The page count has moved twice. 18 to 19 at the #49 moderation repositioning:
the four-line ADIT affiliation and the longer abstract pushed the last
references onto a page of their own. 19 to 20 across #56 and #57, which added
a Conclusion, a Section 4.4, two tables and one reference. Every figure is a
real page rather than a dangling stub.

**`\graphicspath` differs between the two copies, deliberately.**
`paper/main.tex` carries `{{./}{../results/figures/}}` so the repo build
resolves figures from the renderer's committed output with no duplicated copy
that can drift. The packaged `arxiv/main.tex` carries `{{./}}` alone: the
three PNGs sit beside the sources in the upload, and a submission tree should
not contain a path that reaches above its own root. The packaging script makes
that substitution; do not hand-edit it back.

### Packages

Eleven, all of them long-standing standard TeX Live packages. None is a local
or personal `.sty`, and the standalone compile below pulled every one from the
distribution, so nothing needs bundling with the upload. Eyeball the list
anyway before you submit.

| Package | Options |
|---|---|
| `inputenc` | `utf8` |
| `fontenc` | `T1` |
| `lmodern` | — |
| `geometry` | `margin=1in` |
| `graphicx` | — |
| `subcaption` | — |
| `booktabs` | — |
| `amsmath` | — |
| `microtype` | — |
| `hyperref` | `hidelinks` |
| `natbib` | `numbers,sort&compress` |

Document class: `article`, options `11pt,a4paper`. `lmodern` is load-bearing:
`[T1]{fontenc}` alone falls back to bitmap EC fonts, which `microtype` cannot
expand and which arXiv rejects (Decision Log #41).

No `\input` or `\include` points outside the upload: all nine targets are
`sections/*.tex`. No absolute path appears anywhere in the sources.

---

## Known warnings

The build log carries **four underfull hbox warnings and nothing else**. They
are output of `\setlength{\emergencystretch}{3em}`, added to clear three
overfull boxes where unbreakable `\texttt{}` filenames spilled up to 61 pt into
the margin (Decision Log #41). The trade was taken knowingly: four loose lines
in `\texttt{}`-heavy list items bought the margin back. They are cosmetic and
need no action before submission.
