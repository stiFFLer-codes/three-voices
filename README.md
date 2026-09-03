# One Prediction, Three Voices

Code and artifacts for **"A Coin Flip Is Not a Red Light: Grading a
Maternal-Health Risk Alarm for Mothers, Community Health Workers, and
Clinicians."**

A maternal-health risk model splits one case 0.487 against 0.499 between two
adjacent risk levels. A clinician can read that margin and discount it; a
mother handed a red alarm for the same prediction cannot. This repository
renders that single prediction three ways and gates the rendering on the
model's own uncertainty: below a fixed top-two margin the highest-severity
signal is withheld from the mother's channel and from no other. The derate is
red to amber, never red to green, and amber still says *needs follow-up*. That
is the thesis: abstention graded by stakeholder vulnerability rather than
applied uniformly.

This is a design and feasibility artifact. **Nobody in the three groups has
used the system.** The evaluation is a formative, single-evaluator, heuristic
critique of our own renderings; it found five defects and is not evidence that
the tiers help anyone. The data is public, the task is generic maternal-health
risk with no condition named anywhere, and we make **no clinical-validity
claim** about predicting real patients' outcomes.

## Links

| | |
|---|---|
| Paper | [`paper/main.pdf`](paper/main.pdf) (17 pp) |
| Preprint | `[arXiv:XXXX.XXXXX]` — **placeholder, fill in after submission** (cs.HC, cross-list cs.LG) |
| Archive | [10.5281/zenodo.22252076](https://doi.org/10.5281/zenodo.22252076) — concept DOI, resolves to the latest release |
| Dataset | [UCI Maternal Health Risk](https://doi.org/10.24432/C5DP5D), id 863, CC BY 4.0 |
| Submission sheet | [`paper/ARXIV_SUBMISSION.md`](paper/ARXIV_SUBMISSION.md) |

## The three tiers

Each tier substitutes what its reader actually lacks.

- **Clinician** — signed SHAP contributions, all three class probabilities, and
  the raw feature table. Full decomposition for a trained reader.
- **Community health worker (ASHA)** — the two local drivers for this case
  through a fixed phrase map, under a header that states the risk level in
  words. Its contribution is cognitive-load reduction; the card ships in
  English, and localisation is string substitution deferred to deployment.
- **Mother-to-be** — one spoken Hindi sentence and a three-lamp visual, which
  deliver an action and stop there. No probability, no percentage, nothing that
  must be read. The Hindi strings were written and clinically reviewed by a
  native-speaking MBBS collaborator.

The plain-language messages are deterministic templates over SHAP outputs. No
language model generates health text at inference.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Five gates, in order. Each is runnable on its own and each writes files you can
diff against what is committed here.

```bash
python -m src.data       # downloads and caches the UCI dataset, reports the cohort
python -m src.model      # 5-fold CV over LR / RF / XGBoost, SMOTE in-fold; saves the model
python -m src.explain    # global + local SHAP, four criterion-selected cases, saved as CSV
python -m src.render     # the three tiers: dashboard PNG, ASHA card, Hindi text + MP3, lamp
python -m src.evaluate   # WCAG 2.1 + Nielsen matrix, 16 criteria x 3 tiers
```

Outputs land in `results/figures/` (PNG), `results/tables/` (CSV, card text,
Hindi source strings) and `results/audio/` (MP3).

### Determinism, and its one exception

Seeds are fixed through `config.set_seeds()`, dependencies are pinned in
`requirements.txt`, and the dataset is cached after the first run. Re-running
the pipeline returns every PNG, CSV and TXT byte-identical.

The exception is the synthesised audio. gTTS is a remote service outside our
seed control, so `results/audio/*.mp3` is **not reliably byte-reproducible**:
across our own re-runs one case came back identical and two did not, on
identical input. The deterministic record of each spoken message is the Hindi
source text in `results/tables/tier_mother_<case>_hi.txt`; the MP3 renders it.

gTTS serves here as an illustrative stand-in. It is general-purpose, untuned
for Indian-language health speech, and it voices Latin-script acronyms
unpredictably, which is why `ANM` is respelled phonetically in Devanagari in
the source string. AI4Bharat / Bhashini is the stated deployment path.

Two steps need network: the initial dataset download and the speech synthesis.
Without the second, the renderer still writes the message text and skips only
the MP3.

## Repo map

| Path | What it holds |
|---|---|
| `src/` | The five pipeline gates. `config.py` (seeds, paths), `data.py`, `model.py`, `explain.py`, `render.py`, `evaluate.py` |
| `paper/` | LaTeX sources, `refs.bib` (31 entries), `main.bbl`, the compiled `main.pdf`, and the arXiv submission sheet |
| `results/` | Every figure, table and audio file the paper cites, all regenerable from the five gates |
| `data/` | Provenance and licence for the dataset. The cached CSV is gitignored; `python -m src.data` recreates it |
| `related_work.md` | The literature sweep the Related Work section was drafted from. `main.tex` cites it by section number as the source for each claim |
| `STATE.md` | **The design-decision log.** Forty-five dated, append-only entries recording what was decided, what was rejected and why |

`STATE.md` is provenance, and it is where several of the paper's more awkward
admissions come from. It records that keeping the dataset's 561 duplicate rows
moves macro-recall from 0.580 to 0.859, that the 0.15 margin threshold is a
design constant rather than an empirical one, that the evaluation's own
grade-inflation guard was moved once and on what grounds, and that five defects
found by reading our own artifacts in role were fixed while the record of them
survived the repair. Read it to see how a number arrived.

## Authors

**Maitreya Sapariya**, Independent Researcher
([ORCID 0009-0003-9346-3775](https://orcid.org/0009-0003-9346-3775)),
corresponding author — Conceptualization, Methodology, Software, Formal
analysis, Writing (original draft).

**Aditi Patil**, Smt. B. K. Shah Medical Institute & Research Centre, Sumandeep
Vidyapeeth (Deemed to be University) — Clinical domain expertise, Hindi
authoring and review, ASHA-tier design input, Validation.

## Citation

Cite the preprint once it has an arXiv identifier. Please also cite the
dataset, which CC BY 4.0 requires:

> Ahmed, M. (2020). *Maternal Health Risk* [Dataset]. UCI Machine Learning
> Repository. https://doi.org/10.24432/C5DP5D

## License

Code: MIT, see [`LICENSE`](LICENSE). Paper and figures: CC BY 4.0. Dataset: CC
BY 4.0, held by its creator, see [`data/README.md`](data/README.md) for the
required attribution.
