# Three Voices

Code and artifacts for the paper **"Three Voices: Uncertainty-Gated Rendering
of a Maternal-Health Risk Alarm for Mothers, Community Health Workers, and
Clinicians"** by Maitreya Sapariya and Aditi Patil.

Three Voices renders one maternal-health risk prediction as three action
signals: a decomposition for a clinician, a referral card for a community
health worker, and a three-lamp visual with one spoken Hindi sentence for the
mother. When a high-risk call falls within a fixed top-two margin of 0.15, red
is withheld from the health worker and the mother and replaced by amber, which
still asks for follow-up; the clinician sees the probabilities unchanged. The
work uses only the public UCI Maternal Health Risk dataset and makes no claim
to predict real patients' outcomes; no user study has been run.

The compiled paper is [`paper/main.pdf`](paper/main.pdf); its LaTeX sources
and `main.bbl` are in [`paper/`](paper/). Every release is archived on Zenodo
under the concept DOI
[10.5281/zenodo.22252076](https://doi.org/10.5281/zenodo.22252076), which
resolves to the latest version.

## Reproducing the results

Requires **Python 3.12**. The NumPy and scikit-learn releases pinned in
`requirements.txt` predate the 3.13 and 3.14 wheels and will not build on a
newer interpreter.

```bash
python3.12 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements-lock.txt
```

**Windows:** clone to a short path (for example `C:\tv`) or enable Windows
long paths before installing. During `pip install`, the path of NumPy's
OpenBLAS DLL can exceed 260 characters, and the install then fails.

Then run the five commands in order:

```bash
python -m src.data               # downloads the UCI dataset once and caches it in data/raw/
python -m src.model              # model comparison, leakage and gate tables; saves the model
python -m src.explain            # global and per-case SHAP tables and figures
python -m src.render --case all  # the three tiers for all four cases
python -m src.evaluate           # the WCAG 2.1 and Nielsen rating matrix
```

Outputs go to `results/figures/` (PNG), `results/tables/` (CSV, Markdown and
text) and `results/audio/` (MP3).

A clean run from a fresh clone (Windows 11, Python 3.12, the locked
environment, the dataset downloaded afresh) reproduced all 17 PNGs byte for
byte and all 18 CSV, Markdown and text outputs with identical content; the
text outputs differ from the committed copies only in line endings, which
follow the platform. The freshly downloaded dataset was byte-identical to our
cached copy.

The MP3s are the exception. The Hindi audio comes from a remote speech
service outside our seed control, so a re-run can return different bytes for
the same input. The record of each spoken message is its Hindi source string,
committed in `results/tables/tier_mother_<case>_hi.txt`. Empty
`results/audio/` before re-rendering: the renderer can leave an existing MP3
in place and still report success.

## Repository layout

| Path | Contents |
|---|---|
| `src/` | The pipeline: `config.py` (seed, paths), `data.py`, `model.py`, `explain.py`, `render.py`, `evaluate.py` |
| `results/` | Every figure, table and audio file the paper reports, written by the five commands |
| `paper/` | LaTeX sources, `refs.bib`, `main.bbl` and the compiled `main.pdf` |
| `data/` | Dataset provenance and licence; the cached CSV is not committed |

## Authors

**Maitreya Sapariya** (corresponding author), Department of Information
Technology, A. D. Patel Institute of Technology (ADIT), Charutar Vidya Mandal
(CVM) University, New Vallabh Vidyanagar, Anand, Gujarat, India.
ORCID [0009-0003-9346-3775](https://orcid.org/0009-0003-9346-3775).
Contributions: Conceptualization, Methodology, Software, Formal analysis,
Writing – original draft.

**Aditi Patil**, Smt. B. K. Shah Medical Institute & Research Centre,
Sumandeep Vidyapeeth (Deemed to be University), Vadodara, Gujarat, India.
Contributions: Hindi authoring and review, clinical domain input, ASHA-tier
design input, Writing – review & editing.

## How to cite

GitHub's "Cite this repository" button reads [`CITATION.cff`](CITATION.cff).
In text form:

> Sapariya, M., & Patil, A. (2026). *Three Voices: code and artifacts for
> Uncertainty-Gated Rendering of a Maternal-Health Risk Alarm* (Version 1.1.0)
> [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.22252076

Please also cite the dataset (its CC BY 4.0 licence requires attribution):

> Ahmed, M. (2020). *Maternal Health Risk* [Dataset]. UCI Machine Learning
> Repository. https://doi.org/10.24432/C5DP5D

## Licences

- Code: MIT, see [`LICENSE`](LICENSE).
- Paper: the text and figures of paper/main.pdf and its LaTeX sources are licensed CC BY 4.0, the same licence as the arXiv version.
- Dataset: UCI Maternal Health Risk (id 863) by Marzia Ahmed (2020), CC BY
  4.0. It is not redistributed here; `python -m src.data` downloads it. See
  [`data/README.md`](data/README.md).
