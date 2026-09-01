# One Prediction, Three Voices

*Designing AI that explains itself differently to different people.*

A single maternal-health risk prediction, rendered through three
stakeholder-specific explanation layers — a clinician SHAP dashboard, an ASHA
worker plain-language card, and a mother-to-be voice + non-numeric visual — in
low-resource, non-English deployment contexts.

**The contribution is the explanation architecture, not the model.** The model
is a vehicle for demonstrating the tiered rendering. This is a design framework
and feasibility demonstration; it makes **no clinical-validity claim** about
predicting real patients' outcomes.

## Data

Public, openly licensed data only:
[UCI Maternal Health Risk](https://doi.org/10.24432/C5DP5D) (id=863, CC BY 4.0).
No real patient records are used. The native target is 3-class
(low / mid / high risk), which maps cleanly onto the mother-to-be traffic-light
visual (green / amber / red).

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m src.data          # Phase 0 gate: pulls, caches, and reports the dataset
```

The first run downloads the dataset and caches it to `data/raw/`. Every later
run reads the cache, so the pipeline is deterministic and network-independent.

## Roadmap

| Phase | Deliverable |
|------|-------------|
| P0 | Reproducibility spine (`python -m src.data`) |
| P1 | Model vehicle — LR / RF / XGBoost, stratified k-fold, SMOTE-in-fold, metrics |
| P2 | SHAP engine — global + local SHAP for 3 representative cases |
| P3 | Three-tier renderer — dashboard + ASHA card + Hindi voice + visual |
| P4 | Heuristic evaluation — WCAG 2.1 + Nielsen (no human subjects) |
| P5 | Manuscript — arXiv-ready |
| P6 | Cold-run + submit (arXiv cs.HC) |

See `CLAUDE.md` for the operating rules this repo is built on.

## Citation

If you use this work, please also cite the dataset:

> Ahmed, M. (2020). *Maternal Health Risk* [Dataset]. UCI Machine Learning
> Repository. https://doi.org/10.24432/C5DP5D

## License

Code: MIT (see `LICENSE`). Dataset: CC BY 4.0 (see `data/README.md`).
