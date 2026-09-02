# CLAUDE.md — operating rules for this repo

This repo produces the paper **"One Prediction, Three Voices"**: one ML
prediction on a public maternal-health dataset, rendered three ways
(clinician dashboard, ASHA plain-language card, mother-to-be voice + visual),
plus an honest heuristic evaluation and the manuscript.

## Non-negotiables (do not re-litigate these each session)

1. **The model is a vehicle, not the contribution.** The novelty is the
   three-tier explanation architecture. Do NOT chase accuracy. UCI Maternal
   Health Risk is saturated (~83–88% in published work). Get a clean, honest,
   leak-free baseline and move on.
2. **No data leakage.** SMOTE — and any resampling/scaling that learns from
   data — goes INSIDE each cross-validation training fold only, never before
   the split. Reviewers check this first.
3. **Only public data, ever.** This preprint uses the UCI Maternal Health
   Risk dataset (id=863, CC BY 4.0) and nothing else. No real patient
   records, not even de-identified. Real-data validation is a Phase-2 /
   journal question, gated on ethics clearance.
4. **No clinical-validity claims.** No output — code comment, figure caption,
   or manuscript sentence — may state or imply this predicts real patients'
   outcomes. It demonstrates an explanation design. Say exactly that.
5. **ASHA layer is deterministic / template-based.** No LLM generates the
   plain-language health message at inference time. Templates over SHAP
   outputs: defensible, reproducible, no hallucination.
6. **Determinism.** Call `config.set_seeds()` at the top of every script.
   Fixed seeds, pinned deps, cached data.
7. Never add Co-Authored-By, 'Generated with Claude Code', or Claude-Session
   trailers to any commit or PR.

## Repo map
- `src/config.py` — paths, seeds, dataset constants.
- `src/data.py`   — deterministic loader + `python -m src.data` gate.
- `results/`      — figures and tables (generated, reproducible).
- `models/`       — saved model artifact(s).
- `paper/`        — LaTeX manuscript.

## Phase gates (each ends in something showable)
- **P0** Reproducibility spine — `python -m src.data` pulls, caches, reports. Done when identical every run.
- **P1** Model vehicle — LR/RF/XGBoost, stratified k-fold, SMOTE-in-fold, metrics table, one saved model.
- **P2** SHAP engine — global + local SHAP for 3 chosen cases, values saved as data.
- **P3** Three-tier renderer — one case -> dashboard PNG + ASHA card + Hindi MP3 + visual.
- **P4** Heuristic evaluation — WCAG 2.1 + Nielsen rubric matrix. No human subjects.
- **P5** Manuscript — arXiv-ready PDF, repo linked.
- **P6** Cold-run + submit — fresh env, tagged release, arXiv (cs.HC).

## Current phase: P0
