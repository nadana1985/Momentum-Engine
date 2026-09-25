"""Tests for momentum_v10 L5 relative strength ranking generator."""
import os
from pathlib import Path
import pandas as pd
import numpy as np
import pytest

from momentum_v10.config import FeatureConfig
from momentum_v10.cta_dual import compute_features
from momentum_v10.features import load_asset


def test_l5_ranking_artifact_schema_and_integrity():
    l5_path = Path("data/l5_ranking.parquet")
    if not l5_path.exists():
        pytest.skip("data/l5_ranking.parquet has not been generated yet.")

    df = pd.read_parquet(l5_path)
    assert not df.empty, "L5 ranking parquet is empty"

    # 1. Canonical Schema
    assert list(df.columns) == ["date", "symbol", "rank"], f"Unexpected columns: {df.columns}"
    assert df["rank"].dtype == "int64", f"Expected int64 rank, got {df['rank'].dtype}"
    assert (df["rank"] >= 1).all(), "Ranks must be strictly positive integers >= 1"

    # 2. No nulls in key fields
    assert df["date"].notna().all(), "Null dates found in L5 ranking"
    assert df["symbol"].notna().all(), "Null symbols found in L5 ranking"

    # 3. Date format and ordering
    dates = df["date"].unique()
    assert len(dates) > 10, f"Expected at least 10 weekly dates, got {len(dates)}"

    # 4. Monotonic ranking check per date
    for dt, grp in df.groupby("date"):
        ranks = grp["rank"].tolist()
        assert ranks == sorted(ranks), f"Ranks for {dt} are not sorted: {ranks[:5]}"
        assert len(ranks) == len(set(ranks)), f"Duplicate ranks found for date {dt}"


def test_cta_dual_l5_integration():
    l5_path = Path("data/l5_ranking.parquet")
    if not l5_path.exists():
        pytest.skip("data/l5_ranking.parquet has not been generated yet.")

    eth_shard = Path("data/raw_shards/ETH_USDT_1h.parquet")
    if not eth_shard.exists():
        pytest.skip("ETH shard not found.")

    from momentum_v10.universe_generator import load_with_oi
    df = load_with_oi("ETH", Path("data/raw_shards"))
    fcfg = FeatureConfig(l5_ranking_path=l5_path)
    feat = compute_features(df, fcfg, asset="ETH")

    assert "l5_rank_pctile" in feat.columns
    valid_pctiles = feat["l5_rank_pctile"].dropna()
    assert len(valid_pctiles) > 0, "Expected non-zero valid l5_rank_pctile rows for ETH"
    assert (valid_pctiles >= 0.0).all() and (valid_pctiles <= 1.0).all(), "Percentiles must be in [0, 1]"

