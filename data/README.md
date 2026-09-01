# Data provenance

This project uses the **UCI Maternal Health Risk** dataset only.

- Source: UCI Machine Learning Repository, dataset id **863**
- DOI: https://doi.org/10.24432/C5DP5D
- License: **CC BY 4.0** (share/adapt with attribution)
- Creator: Marzia Ahmed (2020)

Attribution (required by CC BY 4.0):

> Ahmed, M. (2020). *Maternal Health Risk* [Dataset]. UCI Machine Learning
> Repository. https://doi.org/10.24432/C5DP5D

## Regenerating the cache

The raw CSV is not committed by default. Recreate it with:

```bash
python -m src.data          # writes data/raw/maternal_health_risk.csv
```

The file is ~50 KB. If you prefer a fully self-contained repo that does not
depend on UCI uptime, you may commit the cached CSV — the CC BY 4.0 license
permits redistribution with the attribution above.

**No real, private, or clinical patient data belongs in this folder.**
