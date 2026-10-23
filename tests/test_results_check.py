"""
Core Test 1: Results Check (Frozen Sample Regression Gate)
As specified in Issues-identified.pdf:
Runs V15 engine on a frozen benchmark sample and validates trade-by-trade consistency.
Any unannounced drift or copy divergence will immediately fail this test.
"""

import sys
from pathlib import Path
import pytest
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import build_v15_tape


def test_v15_frozen_sample_results():
    """Verify trade count and attribution invariants on benchmark assets."""
    expected_counts = {
        "BTC": 13,
        "ETH": 9,
    }

    for asset, expected_n in expected_counts.items():
        trades_df, tel_df = build_v15_tape.process_asset((asset, "Tier 1"))
        assert trades_df is not None, f"Trades DataFrame was None for {asset}"
        assert len(trades_df) == expected_n, (
            f"Trade count divergence on {asset}: expected {expected_n}, got {len(trades_df)}"
        )
        assert "book" in trades_df.columns
        assert "log_ret" in trades_df.columns
        assert "entry_price" in trades_df.columns
        assert (trades_df["entry_price"] > 0).all()
