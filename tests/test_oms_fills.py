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

from momentum_v12.config import (
    Book3FlushReclaimConfig,
    CalendarConfig,
    ExecutionConfig,
    V12Config,
)
from momentum_v12.engine_state import empty_engine_state
from momentum_v12.engine_v12 import run_v12_engine
from momentum_v12.oms_fills import (
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


def _flush_state() -> dict:
    st = empty_engine_state()
    st["active_flush_bid"] = {
        "trigger_px": 100.0,
        "bid_px": 92.0,
        "stop_px": 92.0 * 0.92,
        "target_px": 100.0,
        "armed_ts": pd.Timestamp("2025-06-10 10:00:00"),
        "ttl_bars": 72,
        "veto_gate": "test",
        "candidate_setup": "test",
    }
    return st


def _book3_cfg(mode: str) -> V12Config:
    return V12Config(
        book3_flush=Book3FlushReclaimConfig(enable_book3_flush_reclaim=True),
        calendar=CalendarConfig(enable_calendar_firewall=False),
        execution=ExecutionConfig(mode=mode),
    )


def test_book3_paper_limit_fills_at_bid_on_gap():
    cfg = _book3_cfg("paper_limit")
    trades, state = run_v12_engine(
        _gap_bar_frame(), "GAP", cfg=cfg, state=_flush_state()
    )
    assert state["active"] is not None
    assert state["active"]["book"] == "Book 3"
    np.testing.assert_allclose(float(state["active"]["entry_price"]), 92.0)
    assert state["active_flush_bid"] is None
    assert not trades.empty


def test_book3_live_limit_fills_at_open_on_gap():
    cfg = _book3_cfg("live_limit")
    trades, state = run_v12_engine(
        _gap_bar_frame(), "GAP", cfg=cfg, state=_flush_state()
    )
    assert state["active"] is not None
    assert state["active"]["book"] == "Book 3"
    np.testing.assert_allclose(float(state["active"]["entry_price"]), 90.0)
    np.testing.assert_allclose(
        float(state["active"]["stop"]), 90.0 * 0.92, rtol=1e-12
    )
    assert state["active_flush_bid"] is None
    assert not trades.empty


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
