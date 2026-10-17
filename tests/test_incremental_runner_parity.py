"""
Incremental live-runner parity.

The engine is a state machine: warmup through T-1 returns state_out, then
the remaining bars (including a position that is open across the cut) must
match a cold full-history run bit-for-bit.

Run:
    pytest tests/test_incremental_runner_parity.py -v
"""

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v12.config import V12Config, Book4Config
from momentum_v12.engine_state import (
    closed_bar_mask,
    engine_state_from_jsonable,
    engine_state_to_jsonable,
    utc_now_naive,
)
from momentum_v12.engine_v12 import run_v12_engine
from momentum_v12.features_v12 import compute_features_v12
from momentum_v12.live_runner_v12 import _closed_feature_frame


def _sbb_cfg() -> V12Config:
    """S-BB hourly reclaim path used to open a Book 4 across a cut."""
    return V12Config(
        book4=Book4Config(
            enable_p_nb_day_close_confirmation=False,
            enable_p_nb_microstructure_sizing=False,
        )
    )


def _synthetic_book4_frame(n: int = 2000) -> pd.DataFrame:
    dates = pd.date_range("2025-01-01", periods=n, freq="1h")
    c = np.full(n, 50.0)
    c[:200] = 150.0
    c[200:1000] = 50.0
    c[1000:1040] = np.linspace(50.0, 105.0, 40)
    c[1040:1070] = np.linspace(105.0, 92.0, 30)
    c[1070:1100] = np.linspace(92.0, 108.0, 30)
    c[1100:1150] = np.linspace(108.0, 135.0, 50)
    c[1150:] = 135.0
    h = c + 0.5
    l = c - 0.5
    return pd.DataFrame(
        {
            "timestamp": dates.astype(np.int64) // 10**6,
            "open": c,
            "high": h,
            "low": l,
            "close": c,
            "volume": np.full(n, 50000.0),
            "quote_volume": c * 50000.0,
            "sum_open_interest_value": np.full(n, 8000000.0),
            "count_toptrader_long_short_ratio": np.full(n, 1.80),
            "funding_rate": np.full(n, 0.0001),
            "taker_buy_quote_volume": c * 26000.0,
        },
        index=dates,
    )


def _trade_keyframe(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["entry"] = pd.to_datetime(out["entry"])
    out["exit"] = pd.to_datetime(out["exit"])
    return out.sort_values(["book", "entry", "exit"]).reset_index(drop=True)


def test_incremental_open_across_cut_matches_cold():
    """A Book 4 that is still open at the cut must resume stop/MFE from state."""
    cfg = _sbb_cfg()
    feat = compute_features_v12(
        _synthetic_book4_frame(), btc_df=None, tier_label="Tier 1", cfg=cfg
    )
    cold, cold_state = run_v12_engine(feat, "SYNTHETIC_B4_TOKEN", cfg=cfg)
    assert not cold.empty
    b4 = cold[cold["book"] == "Book 4"]
    assert not b4.empty

    first = b4.iloc[0]
    entry = pd.Timestamp(first["entry"])
    loc = feat.index.get_loc(entry)
    assert isinstance(loc, (int, np.integer))
    # Cut while the first Book 4 is live: 20 hours after entry, well before tape end.
    cut = int(loc) + 20
    assert 0 < cut < len(feat) - 5

    warm, warm_state = run_v12_engine(feat.iloc[: cut + 1], "SYNTHETIC_B4_TOKEN", cfg=cfg)
    warm_open = warm[warm["is_open"]] if not warm.empty else pd.DataFrame()
    assert not warm_open.empty, "cut must fall while a position is open"

    inc, inc_state = run_v12_engine(
        feat,
        "SYNTHETIC_B4_TOKEN",
        cfg=cfg,
        state=warm_state,
        start_after=feat.index[cut],
    )
    assert not inc.empty

    warm_closed = warm[~warm["is_open"]] if not warm.empty else warm
    parts = [p for p in (warm_closed, inc) if p is not None and not p.empty]
    combined = pd.concat(parts, ignore_index=True)
    combined = combined.sort_values(["book", "entry", "exit"]).reset_index(drop=True)

    cold_s = _trade_keyframe(cold)
    comb_s = _trade_keyframe(combined)
    assert len(comb_s) == len(cold_s)
    pd.testing.assert_series_equal(
        comb_s["entry"], cold_s["entry"], check_names=False
    )
    pd.testing.assert_series_equal(
        comb_s["exit"], cold_s["exit"], check_names=False
    )
    pd.testing.assert_series_equal(
        comb_s["reason"], cold_s["reason"], check_names=False
    )
    np.testing.assert_allclose(
        comb_s["log_ret"].astype(float).values,
        cold_s["log_ret"].astype(float).values,
        atol=1e-9,
    )
    np.testing.assert_allclose(
        comb_s["entry_price"].astype(float).values,
        cold_s["entry_price"].astype(float).values,
        atol=1e-9,
    )
    np.testing.assert_allclose(
        comb_s["stop_price"].astype(float).values,
        cold_s["stop_price"].astype(float).values,
        atol=1e-9,
    )

    # Final sleeve must still carry the live Book 4 (or the same flat state).
    assert (inc_state["active"] is None) == (cold_state["active"] is None)
    if cold_state["active"] is not None:
        assert inc_state["active"]["book"] == cold_state["active"]["book"]
        np.testing.assert_allclose(
            float(inc_state["active"]["entry_price"]),
            float(cold_state["active"]["entry_price"]),
            atol=1e-9,
        )
        np.testing.assert_allclose(
            float(inc_state["active"]["stop"]),
            float(cold_state["active"]["stop"]),
            atol=1e-9,
        )


def test_json_roundtrip_preserves_open_sleeve():
    cfg = _sbb_cfg()
    feat = compute_features_v12(
        _synthetic_book4_frame(), btc_df=None, tier_label="Tier 1", cfg=cfg
    )
    cold, _ = run_v12_engine(feat, "SYNTHETIC_B4_TOKEN", cfg=cfg)
    entry = pd.Timestamp(cold[cold["book"] == "Book 4"].iloc[0]["entry"])
    cut = int(feat.index.get_loc(entry)) + 20
    _, state = run_v12_engine(feat.iloc[: cut + 1], "SYNTHETIC_B4_TOKEN", cfg=cfg)
    assert state["active"] is not None
    blob = json.dumps(engine_state_to_jsonable(state))
    restored = engine_state_from_jsonable(json.loads(blob))
    assert restored["active"]["book"] == state["active"]["book"]
    np.testing.assert_allclose(
        float(restored["active"]["entry_price"]),
        float(state["active"]["entry_price"]),
        atol=1e-12,
    )


def test_forming_bar_is_not_closed_and_not_last_ts():
    now = pd.Timestamp("2026-03-01 16:30:00")
    idx = pd.date_range("2026-03-01 14:00:00", periods=3, freq="1h")
    # 14:00 closed, 15:00 closed, 16:00 still forming at 16:30
    mask = closed_bar_mask(idx, now)
    assert list(mask) == [True, True, False]
    feat = pd.DataFrame({"close": [1.0, 2.0, 3.0]}, index=idx)
    closed = _closed_feature_frame(feat, now)
    assert closed.index[-1] == idx[1]
    last_ts = closed.index[-1]
    assert last_ts + pd.Timedelta(hours=1) <= now


def test_utc_now_naive_is_naive():
    ts = utc_now_naive()
    assert ts.tzinfo is None
