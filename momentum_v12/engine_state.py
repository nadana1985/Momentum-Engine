"""
JSON-safe persistence for run_v12_engine sleeve state.

Bar-index fields (tau_bar, touch_bar, bot_bar, retest_bar) are stored as
timestamps so a sliding 9,000-bar live window can remap them on the next hour.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any, Dict, Optional

import numpy as np
import pandas as pd

ENGINE_SLEEVE_KEYS = (
    "active",
    "last_exit_ts",
    "last_exit_reason",
    "last_exit_pnl",
    "last_entry_price",
    "flush_low_since_exit",
    "active_shadow_anchor",
    "active_flush_bid",
    "active_b4_setup",
    "active_b1_anchor",
    "active_b5_bid",
    "last_b5_arm_ts",
    "active_b6_setup",
    "active_b2_delayed",
)

_BAR_TS_PAIRS = (
    ("tau_bar", "tau_ts"),
    ("bot_bar", "bot_ts"),
    ("touch_bar", "touch_ts"),
    ("retest_bar", "retest_ts"),
)

_TS_FIELD_NAMES = {
    "last_exit_ts",
    "last_b5_arm_ts",
    "entry_time",
    "armed_ts",
    "trigger_ts",
    "tau_ts",
    "touch_ts",
    "bot_ts",
    "retest_ts",
}


def utc_now_naive() -> pd.Timestamp:
    """Timezone-naive UTC now. Safe on pandas 2.x (utcnow().tz_localize is not)."""
    return pd.Timestamp(datetime.now(timezone.utc).replace(tzinfo=None))


def closed_bar_mask(index: pd.Index, now: Optional[pd.Timestamp] = None) -> np.ndarray:
    """True where the 1h bar open + 1h is already in the past."""
    now = utc_now_naive() if now is None else pd.Timestamp(now)
    if getattr(now, "tzinfo", None) is not None:
        now = now.tz_localize(None)
    return (pd.DatetimeIndex(index) + pd.Timedelta(hours=1)) <= now


def empty_engine_state() -> Dict[str, Any]:
    return {
        "active": None,
        "last_exit_ts": None,
        "last_exit_reason": None,
        "last_exit_pnl": 0.0,
        "last_entry_price": 0.0,
        "flush_low_since_exit": float("inf"),
        "active_shadow_anchor": None,
        "active_flush_bid": None,
        "active_b4_setup": None,
        "active_b1_anchor": None,
        "active_b5_bid": None,
        "last_b5_arm_ts": None,
        "active_b6_setup": None,
        "active_b2_delayed": None,
    }


def _to_naive_ts(v: Any) -> Optional[pd.Timestamp]:
    if v is None or v == "":
        return None
    ts = pd.Timestamp(v)
    if pd.isna(ts):
        return None
    if ts.tz is not None:
        ts = pd.Timestamp(ts.tz_convert("UTC").to_pydatetime().replace(tzinfo=None))
    return ts


def _stamp_bar_fields(obj: Optional[dict], index: Optional[pd.Index]) -> Optional[dict]:
    if not obj or index is None or len(index) == 0:
        return obj
    out = dict(obj)
    idx = pd.DatetimeIndex(index)
    for bar_key, ts_key in _BAR_TS_PAIRS:
        if bar_key not in out:
            continue
        try:
            bar_i = int(out[bar_key])
        except (TypeError, ValueError):
            continue
        if 0 <= bar_i < len(idx):
            out[ts_key] = pd.Timestamp(idx[bar_i])
        else:
            out[ts_key] = pd.Timestamp(idx[0]) + pd.Timedelta(hours=bar_i)
    return out


def _remap_bar_fields(obj: Optional[dict], index: Optional[pd.Index]) -> Optional[dict]:
    if not obj or index is None or len(index) == 0:
        return obj
    out = dict(obj)
    idx = pd.DatetimeIndex(index)
    for bar_key, ts_key in _BAR_TS_PAIRS:
        ts = out.get(ts_key)
        if ts is None:
            continue
        ts = _to_naive_ts(ts)
        if ts is None:
            continue
        loc = idx.get_indexer([ts])[0]
        if loc >= 0:
            out[bar_key] = int(loc)
        else:
            hours = (pd.Timestamp(idx[0]) - ts).total_seconds() / 3600.0
            out[bar_key] = int(round(-hours))
        out[ts_key] = ts
    return out


def _hydrate_nested(obj: Any) -> Any:
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k in _TS_FIELD_NAMES:
                out[k] = _to_naive_ts(v)
            else:
                out[k] = _hydrate_nested(v)
        return out
    return obj


def hydrate_engine_state(
    state: Optional[Dict[str, Any]],
    index: Optional[pd.Index] = None,
) -> Dict[str, Any]:
    """Deep-copy persisted state and remap bar indices onto `index`."""
    out = empty_engine_state()
    if not state:
        return out
    src = state.get("engine") if isinstance(state.get("engine"), dict) else state
    for k in ENGINE_SLEEVE_KEYS:
        if k in src:
            out[k] = deepcopy(src[k])
    out = _hydrate_nested(out)
    if out["flush_low_since_exit"] is None:
        out["flush_low_since_exit"] = float("inf")
    for sleeve in ("active_b1_anchor", "active_b4_setup", "active_b6_setup"):
        out[sleeve] = _remap_bar_fields(out[sleeve], index)
    return out


def snapshot_engine_state(sleeves: Dict[str, Any], index: Optional[pd.Index]) -> Dict[str, Any]:
    """Capture live locals into a remappable state dict."""
    out = empty_engine_state()
    for k in ENGINE_SLEEVE_KEYS:
        if k in sleeves:
            out[k] = deepcopy(sleeves[k])
    for sleeve in ("active_b1_anchor", "active_b4_setup", "active_b6_setup"):
        out[sleeve] = _stamp_bar_fields(out[sleeve], index)
    return out


def _jsonable(v: Any) -> Any:
    if isinstance(v, dict):
        return {k: _jsonable(x) for k, x in v.items()}
    if isinstance(v, (pd.Timestamp, datetime)):
        ts = _to_naive_ts(v)
        return None if ts is None else ts.isoformat()
    if isinstance(v, (np.bool_,)):
        return bool(v)
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, (np.floating, float)):
        fv = float(v)
        if np.isnan(fv):
            return None
        if np.isinf(fv):
            return None
        return fv
    return v


def engine_state_to_jsonable(state: Dict[str, Any]) -> Dict[str, Any]:
    return _jsonable(state)


def engine_state_from_jsonable(raw: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    return hydrate_engine_state(raw, index=None)
