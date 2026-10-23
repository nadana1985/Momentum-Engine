"""
Core Test 4: File Format & Downstream Schema Integrity
As specified in Issues-identified.pdf:
Checks that the output tables and exports produced by the engine and build_csv
contain all columns required by the hourly operations scripts, NiceGUI dashboard,
and SNS alerts.
Prevents breaks like the missing 'trade_type' column before they reach production.
"""

import sys
from pathlib import Path
import pytest
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v15.ops_paths import resolve_tape_dir


REQUIRED_RAW_COLUMNS = [
    "asset", "tier", "book", "entry", "exit", "entry_price",
    "exit_price", "stop_price", "log_ret", "pnl", "reason", "is_open"
]

REQUIRED_CSV_COLUMNS = [
    "asset", "tier", "book", "status", "trade_type", "entry",
    "entry_price", "stop_price", "pnl", "log_ret", "duration_hours"
]


def test_canonical_tape_schema_integrity():
    """Verify canonical production tape has all mandatory quantitative fields."""
    canon_tape = ROOT / "data" / "canonical" / "canonical_v15_0_tape.parquet"
    if not canon_tape.exists():
        canon_tape = ROOT / "v15_standalone" / "data" / "canonical" / "canonical_v15_0_tape.parquet"

    assert canon_tape.exists(), f"Canonical tape not found at {canon_tape}"
    df = pd.read_parquet(canon_tape)

    missing = [c for c in REQUIRED_RAW_COLUMNS if c not in df.columns]
    assert not missing, f"Canonical tape missing required columns: {missing}"


def test_build_csv_schema_and_trade_type(tmp_path, monkeypatch):
    """Verify that build_csv creates closed_trades.csv and open_trades.csv with trade_type."""
    tape_dir = tmp_path / "data" / "all_tapes" / "v15_test"
    tape_dir.mkdir(parents=True)

    # Synthetic raw trades
    raw_df = pd.DataFrame({
        "asset": ["BTC", "SOL"],
        "tier": ["Tier 1", "Tier 1"],
        "book": ["Book 1", "Book 2 (Coiled Squeeze)"],
        "entry": ["2026-03-01 10:00:00", "2026-03-02 12:00:00"],
        "exit": ["2026-03-01 18:00:00", None],
        "duration_hours": [8.0, None],
        "entry_price": [60000.0, 150.0],
        "exit_price": [62000.0, None],
        "stop_price": [58000.0, 140.0],
        "initial_stop": [58000.0, 140.0],
        "raw_pnl": [0.0333, 0.0],
        "pnl": [0.0333, 0.0],
        "sizing_weight": [1.0, 1.0],
        "log_ret": [0.0328, 0.0],
        "mfe": [0.04, 0.02],
        "mae": [-0.01, -0.01],
        "reason": ["target_reached", "open_at_end"],
        "status": ["CLOSED", "OPEN"],
        "is_open": [False, True],
        "is_reclaim": [False, False],
        "is_continuation": [False, False],
        "is_book3": [False, False],
        "pct_lam": [0.5, 0.5],
        "turnover_at_entry": [10.0, 5.0],
    })
    raw_df.to_parquet(tape_dir / "trades.parquet", index=False)

    monkeypatch.setenv("KRONOS_TAPE_DIR", str(tape_dir))
    from momentum_v15.build_csv import main as run_build_csv

    run_build_csv()

    closed_csv = tape_dir / "closed_trades.csv"
    open_csv = tape_dir / "open_trades.csv"

    assert closed_csv.exists(), "closed_trades.csv was not generated"
    assert open_csv.exists(), "open_trades.csv was not generated"

    df_closed = pd.read_csv(closed_csv)
    df_open = pd.read_csv(open_csv)

    for name, df_sub in [("closed_trades.csv", df_closed), ("open_trades.csv", df_open)]:
        missing_csv = [c for c in REQUIRED_CSV_COLUMNS if c not in df_sub.columns]
        assert not missing_csv, f"{name} is missing mandatory columns: {missing_csv}"
        assert "trade_type" in df_sub.columns, f"{name} must contain 'trade_type'"

    assert df_closed.iloc[0]["trade_type"] == "Standard Breakout"
    assert df_open.iloc[0]["trade_type"] == "Squeeze Hunter"
