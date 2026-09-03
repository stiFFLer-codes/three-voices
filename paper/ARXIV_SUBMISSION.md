# arXiv submission sheet

The answer key for whoever fills in the arXiv web form: every field it asks
for, in the form it wants. Written 2026-09-03 during the P6 pre-submission
pass. Nothing here has been submitted.

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
A Coin Flip Is Not a Red Light: Grading a Maternal-Health Risk Alarm for Mothers, Community Health Workers, and Clinicians
```

## Authors (plain text, arXiv order)

```
Maitreya Sapariya, Aditi Patil
```

- **Maitreya Sapariya** — Independent Researcher. ORCID 0009-0003-9346-3775.
  Corresponding author.
- **Aditi Patil** — Smt. B. K. Shah Medical Institute & Research Centre,
  Sumandeep Vidyapeeth (Deemed to be University).

## Abstract (plain text, paste verbatim)

De-LaTeX'd from `sections/abstract.tex`: math delimiters removed, `\emph`
rendered as straight double quotes, straight quotes throughout, no macros. The
wording is unchanged; this is a transcription.

```
A maternal-health risk model splits a case 0.487 against 0.499 between two adjacent risk levels. A clinician can read that margin and discount it; a mother handed a red alarm for the same prediction cannot. Rendering a coin flip as an emergency to the reader least able to interrogate it is the failure we address.

We render one prediction for three readers and gate the rendering on the model's own uncertainty: below a fixed top-two margin the highest-severity signal is withheld from the mother's channel and from no other. The derate is red to amber, never red to green, and amber still says "needs follow-up".

Three claims, each bounded. Abstention rendered by stakeholder vulnerability rather than uniformly, which is an intersection of two established literatures and not the gating mechanism. Deterministic templating over SHAP attributions, with no language model at inference. And a leakage audit: retaining this benchmark's 561 duplicate rows moves macro-recall from 0.580 to 0.859, a measurement we report rather than a problem we claim to have found.

This is a design and feasibility artifact. Our evaluation is a formative single-evaluator critique of our own renderings: it found five defects and is not evidence that the tiers help anyone. Nobody in the three groups has used the system, and user studies are the next step, gated on ethics. The data is public, the task is generic maternal-health risk, and we make no clinical-validity claim.
```

235 words, counted as the manuscript counts them. arXiv sets no abstract limit,
and the overrun against the 150–200 house target is the deliberate call
recorded in Decision Log #38.

Verified mechanically against `sections/abstract.tex`: after stripping `$` math
delimiters and `\emph{}`, the two texts are word-for-word identical. The block
above is pure ASCII with straight quotes and no curly punctuation, so it
survives paste into the arXiv form unchanged.

**Keywords** (the manuscript carries these under the abstract; arXiv has no
keywords field, so they go nowhere on the form):
explainable AI; uncertainty; selective prediction; maternal health; community
health workers; risk communication.

## Comments field (optional, suggested)

```
17 pages, 1 figure, 1 table. Code, figures and audio artifacts at https://github.com/stiFFLer-codes/three-voices and archived at https://doi.org/10.5281/zenodo.22252076
```

---

## Upload file list

Fifteen files. Preserve the `sections/` subdirectory; everything else sits at
the archive root.

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
cd arxiv && tar czf ../three-voices-arxiv.tar.gz .
```

No source edit is needed. `main.tex` sets
`\graphicspath{{./}{../results/figures/}}`, so in the archive the root matches
first and the `../` entry is never consulted; nothing has to escape the
submission root. The same file compiles in the repository, where `./` holds no
PNGs and the second root resolves them from the renderer's committed output.

### Bibliography

arXiv runs LaTeX but **not** BibTeX, so `main.bbl` is the bibliography. It is
tracked for exactly this reason and is current: 31 `\bibitem` entries against
31 `\cite` keys against 31 `refs.bib` entries, no orphans in either direction.
`refs.bib` is included for provenance. `pdflatex` never opens it while the
`.bbl` is present, so dropping it would change nothing in the output.

### Standalone compile, verified

The fifteen files above were copied into an empty directory containing nothing
else (no `.aux`, `.log`, `.out` or `.pdf`) and compiled with `pdflatex` alone,
three passes, no BibTeX run. That is what arXiv does.

**Result: 17-page PDF, 0 errors, 0 overfull boxes, no undefined citations or
references.** All 31 citations and every internal cross-reference resolve from
the shipped `.bbl`.

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
