"""Paper vs live resting-limit fills. Not an exchange order placer."""

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v15.config import (
    Book3FlushReclaimConfig,
    CalendarConfig,
    ExecutionConfig,
    V12Config,
)
from momentum_v15.oms_fills import (
    execution_from_env,
    limit_fill_price,
    working_orders_from_states,
    write_working_orders,
)


def test_execution_defaults_to_paper_limit():
    assert V12Config().execution.mode == "paper_limit"
    assert ExecutionConfig().mode == "paper_limit"


def test_execution_from_env(monkeypatch):
    monkeypatch.delenv("KRONOS_EXECUTION", raising=False)
    assert execution_from_env().mode == "paper_limit"
    monkeypatch.setenv("KRONOS_EXECUTION", "live")
    assert execution_from_env().mode == "live_limit"
    monkeypatch.setenv("KRONOS_EXECUTION", "LIVE_LIMIT")
    assert execution_from_env().mode == "live_limit"
    monkeypatch.setenv("KRONOS_EXECUTION", "paper")
    assert execution_from_env().mode == "paper_limit"


def test_limit_fill_price_paper_vs_live_gap():
    bid = 92.0
    # Gap through the bid: open 90, low 89
    assert limit_fill_price(bid, 90.0, 89.0, "paper_limit") == 92.0
    assert limit_fill_price(bid, 90.0, 89.0, "live_limit") == 90.0
    # Traded down to the bid, no gap
    assert limit_fill_price(bid, 95.0, 91.5, "paper_limit") == 92.0
    assert limit_fill_price(bid, 95.0, 91.5, "live_limit") == 92.0
    # Never traded to the bid
    assert limit_fill_price(bid, 95.0, 93.0, "paper_limit") is None
    assert limit_fill_price(bid, 95.0, 93.0, "live_limit") is None


def _gap_bar_frame() -> pd.DataFrame:
    idx = pd.DatetimeIndex([pd.Timestamp("2025-06-10 12:00:00")])
    return pd.DataFrame(
        {
            "open": [90.0],
            "high": [91.0],
            "low": [89.0],
            "close": [90.5],
            "volume": [1000.0],
            "quote_volume": [90000.0],
            "tier": ["Tier 1"],
            "btc_macro_bull": [True],
        },
        index=idx,
    )


def test_book3_paper_limit_fills_at_bid_on_gap():
    bid_px = 92.0
    bar_open = 90.0
    bar_low = 89.0
    fill = limit_fill_price(bid_px, bar_open, bar_low, mode="paper_limit")
    assert fill == 92.0


def test_book3_live_limit_fills_at_open_on_gap():
    bid_px = 92.0
    bar_open = 90.0
    bar_low = 89.0
    fill = limit_fill_price(bid_px, bar_open, bar_low, mode="live_limit")
    assert fill == 90.0
    rebased_stop = fill * (1.0 - 0.08)
    np.testing.assert_allclose(rebased_stop, 82.8)


def test_working_orders_snapshot(tmp_path):
    states = {
        "AAA": {
            "last_ts": "2025-06-10T12:00:00",
            "engine": {
                "active_flush_bid": {
                    "bid_px": 1.25,
                    "stop_px": 1.15,
                    "target_px": 1.40,
                    "armed_ts": "2025-06-10T10:00:00",
                    "ttl_bars": 72,
                    "veto_gate": "Core 4: Whale Firewall",
                }
            },
        }
    }
    orders = working_orders_from_states(states)
    assert len(orders) == 1
    assert orders[0]["asset"] == "AAA"
    assert orders[0]["book"] == "Book 3"
    assert orders[0]["price"] == 1.25
    path = tmp_path / "working_orders.json"
    write_working_orders(path, orders)
    blob = json.loads(path.read_text(encoding="utf-8"))
    assert blob["count"] == 1
    assert blob["orders"][0]["type"] == "LIMIT"
