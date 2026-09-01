"""Deterministic loader for the UCI Maternal Health Risk dataset (id=863).

Design goals:
  * One command, identical result every run.
  * Network is hit at most once; after that we read the local cache.
  * The loader NEVER cleans or drops rows silently. It reports issues via
    ``validate_raw()`` and leaves preprocessing decisions to Phase 1, where
    they can be documented and defended.

Run as a script to execute the Phase 0 gate:

    python -m src.data
"""
from __future__ import annotations

import argparse
import sys

import pandas as pd

from src import config


def load_raw(force_download: bool = False) -> pd.DataFrame:
    """Return the raw dataset as-is, using a local CSV cache.

    First call fetches from the UCI repository and writes the cache. Every
    later call reads the cache, so results are network-independent and
    byte-identical.
    """
    if config.RAW_CACHE.exists() and not force_download:
        return pd.read_csv(config.RAW_CACHE)

    try:
        from ucimlrepo import fetch_ucirepo
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "ucimlrepo is required for the first download. "
            "Install requirements: pip install -r requirements.txt"
        ) from exc

    dataset = fetch_ucirepo(id=config.DATASET_ID)
    df = pd.concat([dataset.data.features, dataset.data.targets], axis=1)

    config.RAW_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(config.RAW_CACHE, index=False)
    return df


def validate_raw(df: pd.DataFrame) -> dict:
    """Report data-quality flags WITHOUT mutating anything.

    These are known quirks of this dataset (duplicate rows, a few implausible
    HeartRate values). Surfacing them here means Phase 1 handles them
    explicitly and on the record, rather than a hidden ``dropna`` somewhere.
    """
    flags: dict = {
        "n_rows": len(df),
        "n_duplicate_rows": int(df.duplicated().sum()),
        "n_missing_values": int(df.isna().sum().sum()),
    }
    if "HeartRate" in df.columns:
        flags["implausible_heartrate_lt20bpm"] = int((df["HeartRate"] < 20).sum())
    if config.TARGET_COLUMN in df.columns:
        flags["class_distribution"] = (
            df[config.TARGET_COLUMN].astype(str).str.strip().str.lower()
            .value_counts()
            .to_dict()
        )
    return flags


def load_dataset(force_download: bool = False):
    """Return ``(X, y)`` ready for modelling.

    X: features DataFrame in canonical column order.
    y: integer-encoded target (0=low, 1=mid, 2=high) as an ordered Series.
    No rows are dropped or altered here.
    """
    df = load_raw(force_download=force_download)

    missing = set(config.FEATURE_COLUMNS + [config.TARGET_COLUMN]) - set(df.columns)
    if missing:
        raise ValueError(f"Dataset is missing expected columns: {sorted(missing)}")

    X = df[config.FEATURE_COLUMNS].copy()
    y_raw = df[config.TARGET_COLUMN].astype(str).str.strip().str.lower()

    unknown = set(y_raw.unique()) - set(config.RISK_TO_INT)
    if unknown:
        raise ValueError(f"Unexpected target labels: {sorted(unknown)}")

    y = y_raw.map(config.RISK_TO_INT).astype(int)
    y.name = config.TARGET_COLUMN
    return X, y


def _main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Phase 0 gate: pull + cache + report."
    )
    parser.add_argument(
        "--force-download",
        action="store_true",
        help="Ignore the cache and re-fetch from UCI.",
    )
    args = parser.parse_args(argv)

    df = load_raw(force_download=args.force_download)
    flags = validate_raw(df)

    print("UCI Maternal Health Risk — load report")
    print("-" * 42)
    print(f"cache: {config.RAW_CACHE}")
    for key, value in flags.items():
        print(f"{key}: {value}")

    X, y = load_dataset()
    print("-" * 42)
    print(f"X shape: {X.shape}  |  y shape: {y.shape}")
    print(f"target encoding: {config.RISK_TO_INT}")
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(_main())
