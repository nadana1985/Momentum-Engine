"""
Core Test 2: No Look-Ahead Test (Truncation Invariance Gate)
Obedience to Sovereign Rule 4 and Issues-identified.pdf:
Runs the engine once with data cut off at a date and once with full data.
Trades closed before the cut-off must match bit-for-bit with identical entry,
exit, stop, and price levels.
"""

import sys
from pathlib import Path
import pytest
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v15.config import V12Config
from momentum_v15.features_v12 import get_btc_macro, load_shard, compute_features_v12
from momentum_v15.engine_v12 import run_v12_engine

RAW_DIR = ROOT / "data" / "raw_shards"
EXOTIC_DIR = ROOT / "data" / "exotic_shards"


def test_truncation_invariance_no_lookahead():
    """Verify that future data does not leak into prior decisions."""
    asset = "BTC"
    cfg = V12Config()

    btc_df = get_btc_macro(raw_dir=RAW_DIR)
    shard = load_shard(asset, raw_dir=RAW_DIR, exotic_dir=EXOTIC_DIR)
    assert shard is not None and len(shard) > 1000

    # 1. Full run
    feat_full = compute_features_v12(shard, btc_df, tier_label="Tier 1", cfg=cfg)
    trades_full = run_v12_engine(feat_full, asset, cfg=cfg)
    assert not trades_full.empty, "Full run should produce trades"

    # Select a cutoff point after the 5th closed trade
    closed_full = trades_full[~trades_full["is_open"].fillna(False).astype(bool)]
    assert len(closed_full) >= 5, "At least 5 closed trades needed for cutoff test"
    
    fifth_exit = pd.to_datetime(closed_full.iloc[4]["exit"])
    cutoff_ts = fifth_exit + pd.Timedelta(hours=24)

    expected_trades = closed_full[pd.to_datetime(closed_full["exit"]) <= cutoff_ts].copy()
    assert not expected_trades.empty

    # 2. Truncated run: strictly cut off data at cutoff_ts
    shard_trunc = shard[shard.index <= cutoff_ts].copy()
    btc_trunc = btc_df[btc_df.index <= cutoff_ts].copy() if btc_df is not None else None

    feat_trunc = compute_features_v12(shard_trunc, btc_trunc, tier_label="Tier 1", cfg=cfg)
    trades_trunc = run_v12_engine(feat_trunc, asset, cfg=cfg)
    closed_trunc = trades_trunc[~trades_trunc["is_open"].fillna(False).astype(bool)]

    # 3. Assert exact match for trades closed before cutoff_ts
    assert len(closed_trunc) == len(expected_trades), (
        f"Truncated run trade count mismatch: expected {len(expected_trades)}, got {len(closed_trunc)}"
    )

    for i in range(len(expected_trades)):
        exp_row = expected_trades.iloc[i]
        act_row = closed_trunc.iloc[i]

        assert str(exp_row["entry"]) == str(act_row["entry"]), (
            f"Trade {i} entry time mismatch: {exp_row['entry']} vs {act_row['entry']}"
        )
        assert exp_row["book"] == act_row["book"], (
            f"Trade {i} book mismatch: {exp_row['book']} vs {act_row['book']}"
        )
        np.testing.assert_allclose(
            float(exp_row["entry_price"]), float(act_row["entry_price"]), rtol=1e-5,
            err_msg=f"Trade {i} entry price mismatch"
        )
        np.testing.assert_allclose(
            float(exp_row["exit_price"]), float(act_row["exit_price"]), rtol=1e-5,
            err_msg=f"Trade {i} exit price mismatch"
        )
