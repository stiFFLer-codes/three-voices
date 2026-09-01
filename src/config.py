"""Central configuration: paths, seeds, dataset constants.

Call ``set_seeds()`` at the top of every script to keep the whole pipeline
deterministic.
"""
from __future__ import annotations

import os
import random
from pathlib import Path

# ---------------------------------------------------------------------------
# Reproducibility
# ---------------------------------------------------------------------------
RANDOM_SEED = 42


def set_seeds(seed: int = RANDOM_SEED) -> None:
    """Seed every source of randomness we touch. Call first, always."""
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    try:
        import numpy as np

        np.random.seed(seed)
    except ImportError:
        pass


# ---------------------------------------------------------------------------
# Paths (resolved relative to the repo root, so scripts work from anywhere)
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
RESULTS_DIR = ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"
TABLES_DIR = RESULTS_DIR / "tables"
MODELS_DIR = ROOT / "models"

RAW_CACHE = RAW_DIR / "maternal_health_risk.csv"

# ---------------------------------------------------------------------------
# Dataset: UCI Maternal Health Risk (id=863, CC BY 4.0)
# https://doi.org/10.24432/C5DP5D
# ---------------------------------------------------------------------------
DATASET_ID = 863

FEATURE_COLUMNS = ["Age", "SystolicBP", "DiastolicBP", "BS", "BodyTemp", "HeartRate"]
TARGET_COLUMN = "RiskLevel"

# Ordered so index == severity. This drives the mother-to-be traffic-light
# visual later:  low -> green,  mid -> amber,  high -> red.
RISK_ORDER = ["low risk", "mid risk", "high risk"]
RISK_TO_INT = {label: i for i, label in enumerate(RISK_ORDER)}
INT_TO_RISK = {i: label for label, i in RISK_TO_INT.items()}
