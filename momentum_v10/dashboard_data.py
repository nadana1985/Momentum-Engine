"""Data files behind the dashboard (dashboard_v10.html).

The page loads these and computes every KPI, chart, filter, time range and sort
in the browser from the same rows, so all controls stay consistent:

    trades.json  {generated_utc, latest_bar_utc, open: [row], closed: [row]}
    meta.json    {generated_utc, latest_bar_utc, counts, status, history: [...]}
    config.json  engine thresholds (FeatureConfig / CtaConfig) + constants

A row: id, asset, engine, status (OPEN|CLOSED), entry, exit (UTC 'YYYY-MM-DD HH:MM'),
entry_px, px (current price if open, exit price if closed), pnl, mfe, mae (%),
hours, reason, stop, stop_pct (% from price to stop, open only).
dashboard_server.py serves the same files locally; site_export.py writes them.
"""
from __future__ import annotations

import dataclasses
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from momentum_v10 import config as cfgmod
from momentum_v10.config import TAPE_DIR

OPEN_CSV = TAPE_DIR / "open_trades.csv"
CLOSED_CSV = TAPE_DIR / "closed_trades.csv"
STATUS_JSON = TAPE_DIR / "hourly_status.json"
HISTORY_JSONL = TAPE_DIR / "status_history.jsonl"
HISTORY_KEEP = 500


def _num(v, nd=None):
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(f):
        return None
    return round(f, nd) if nd is not None else f


def _ts(v):
    t = pd.to_datetime(v, errors="coerce", utc=True)
    return None if pd.isna(t) else t.strftime("%Y-%m-%d %H:%M")


def _read(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()


def _age_hours(entry):
    t = pd.to_datetime(entry, errors="coerce", utc=True)
    if pd.isna(t):
        return None
    return round((pd.Timestamp.now(tz="UTC") - t).total_seconds() / 3600.0, 1)


def _reason(df):
    if "reason" not in df.columns:
        return pd.Series("", index=df.index)
    return df["reason"].fillna("").astype(str).str.strip()


def _rows(df: pd.DataFrame, status: str) -> list[dict]:
    out = []
    for r in df.to_dict("records"):
        entry_px = _num(r.get("entry_price", r.get("entry_px")))
        if status == "OPEN":
            px = _num(r.get("current_price"))
            pnl = _num(r.get("pnl"))
            if px is None and entry_px is not None and pnl is not None:
                px = entry_px * (1 + pnl)          # older ledgers without current_price
        else:
            px = _num(r.get("exit_price", r.get("exit_px")))
        stop_pct = _num(r.get("stop_pct"))
        out.append({
            "asset": str(r.get("asset", "")),
            "engine": str(r.get("engine", "")),
            "status": status,
            "entry": _ts(r.get("entry")),
            "exit": _ts(r.get("exit")) if status == "CLOSED" else None,
            "entry_px": entry_px,
            "px": px,
            "pnl": None if _num(r.get("pnl")) is None else round(_num(r.get("pnl")) * 100, 4),
            "mfe": None if _num(r.get("mfe")) is None else round(_num(r.get("mfe")) * 100, 4),
            "mae": None if _num(r.get("mae")) is None else round(_num(r.get("mae")) * 100, 4),
            "hours": _num(r.get("duration_hours"), 1) if _num(r.get("duration_hours")) is not None
                     else _age_hours(r.get("entry")) if status == "OPEN" else None,
            "reason": "" if status == "OPEN" else str(r.get("reason", "") or ""),
            "stop": _num(r.get("stop")) if status == "OPEN" else None,
            "stop_pct": None if stop_pct is None or status != "OPEN" else round(stop_pct * 100, 3),
        })
    return out


def latest_bar_utc() -> str | None:
    """Open time of the newest hourly bar the engine has processed."""
    try:
        st = json.loads((TAPE_DIR.parent.parent / "sync_state.json").read_text())
        raw = st.get("raw", {})
        if raw:
            ms = max(int(v) for v in raw.values() if v)
            return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M")
    except Exception:
        pass
    return None


def build_trades() -> dict:
    open_df = _read(OPEN_CSV)
    if not open_df.empty:
        r = _reason(open_df)
        open_df = open_df.loc[r.isin(["", "nan"])]
    closed_df = _read(CLOSED_CSV)
    if not closed_df.empty:
        closed_df = closed_df.loc[~_reason(closed_df).eq("open_at_end")]
        closed_df = closed_df.drop_duplicates(subset=[c for c in ("asset", "engine", "entry", "exit") if c in closed_df.columns])
    rows_open = _rows(open_df, "OPEN") if not open_df.empty else []
    rows_closed = _rows(closed_df, "CLOSED") if not closed_df.empty else []
    # Stable ids: order by entry time across both books.
    allrows = sorted(rows_open + rows_closed, key=lambda x: (x["entry"] or "", x["asset"], x["engine"]))
    for i, row in enumerate(allrows, 1):
        row["id"] = i
    return {
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        "latest_bar_utc": latest_bar_utc(),
        "open": rows_open,
        "closed": rows_closed,
    }


def append_status_history(status: dict) -> None:
    """Keep the last HISTORY_KEEP hourly statuses (one JSON per line)."""
    from momentum_v10.io_utils import atomic_write_text
    keep = {k: status.get(k) for k in ("started_utc", "finished_utc", "ok", "error", "open", "closed",
                                         "closed_this_hour", "ingest_updated", "ingest_failed",
                                         "ingest_delisted", "assets", "assets_failed", "fresh_pct",
                                         "ingest_seconds", "run_seconds")}
    keep["new_signals"] = len(status.get("new_signals") or [])
    lines = HISTORY_JSONL.read_text().splitlines() if HISTORY_JSONL.exists() else []
    lines.append(json.dumps(keep, default=str))
    atomic_write_text(HISTORY_JSONL, "\n".join(lines[-HISTORY_KEEP:]) + "\n")


def build_meta(trades: dict | None = None) -> dict:
    status = {}
    if STATUS_JSON.exists():
        try:
            status = json.loads(STATUS_JSON.read_text())
        except Exception:
            status = {}
    history = []
    if HISTORY_JSONL.exists():
        for line in HISTORY_JSONL.read_text().splitlines()[-48:]:
            try:
                history.append(json.loads(line))
            except Exception:
                continue
    status.pop("new_signals", None)
    t = trades or {}
    return {
        "generated_utc": t.get("generated_utc") or datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        "latest_bar_utc": t.get("latest_bar_utc") or latest_bar_utc(),
        "counts": {"open": len(t.get("open", [])), "closed": len(t.get("closed", []))},
        "status": status,
        "history": list(reversed(history)),
    }


def build_config() -> dict:
    def as_dict(obj):
        d = dataclasses.asdict(obj)
        return {k: (str(v) if isinstance(v, Path) else v) for k, v in d.items()}
    return {
        "feature_config_live": as_dict(cfgmod.FeatureConfig(
            shock_percentile=99.0, shock_mult=None, year_min_periods=720, dormant_mode="relative",
            max_notional_usd=150000.0, require_taker=True, taker_buffer=0.01, first_of_run=True)),
        "cta_config": as_dict(cfgmod.CtaConfig()),
        "constants": {k: getattr(cfgmod, k) for k in ("BARS_24H", "BARS_4H", "BARS_30D", "BARS_1YR",
                                                       "DONCHIAN_BARS", "DONCHIAN_ARM_MFE", "DONCHIAN_ENGINE")},
        "notes": {
            "slippage_per_side": 0.002,
            "fees_modelled": False,
            "funding_modelled": False,
            "fill": "close of the signal bar (+slippage)",
            "exit_check": "hourly close vs stop",
        },
    }


def data_file(name: str) -> dict | None:
    """Payload for data/<name> (used by the local server)."""
    if name == "trades.json":
        return build_trades()
    if name == "meta.json":
        return build_meta(build_trades())
    if name == "config.json":
        return build_config()
    return None
