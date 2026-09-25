"""Live open/closed book helpers.

open_at_end rows are end-of-replay marks. They are not live positions and
they are not closed trades. The live runner owns open_trades.csv and only
appends exits that are not already in closed_trades.csv.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd


def _norm_time(series: pd.Series) -> pd.Series:
    ts = pd.to_datetime(series, errors="coerce", utc=True)
    return ts.dt.strftime("%Y-%m-%d %H:%M:%S").fillna("")


def trade_key(df: pd.DataFrame) -> pd.Series:
    asset = df["asset"].astype(str) if "asset" in df.columns else ""
    engine = df["engine"].astype(str) if "engine" in df.columns else ""
    entry = _norm_time(df["entry"]) if "entry" in df.columns else ""
    if "exit" in df.columns:
        exit_ = _norm_time(df["exit"])
    else:
        exit_ = pd.Series("", index=df.index)
    return asset + "|" + engine + "|" + entry + "|" + exit_


def dedupe_new_trades(existing: pd.DataFrame | None, new: pd.DataFrame | None) -> pd.DataFrame:
    """Drop rows whose (asset, engine, entry, exit) is already in existing."""
    if new is None or new.empty:
        return new.iloc[0:0].copy() if new is not None else pd.DataFrame()
    keyed = new.copy()
    keys = trade_key(keyed)
    keyed = keyed.loc[~keys.duplicated(keep="last")].copy()
    if existing is None or existing.empty:
        return keyed
    seen = set(trade_key(existing))
    keep = ~trade_key(keyed).isin(seen)
    return keyed.loc[keep].copy()


def _reason(df: pd.DataFrame) -> pd.Series:
    if "reason" not in df.columns:
        return pd.Series("", index=df.index)
    return df["reason"].fillna("").astype(str).str.strip()


def count_open(df: pd.DataFrame | None) -> int:
    """Live opens only. A file of open_at_end marks counts as zero."""
    if df is None or df.empty:
        return 0
    if "reason" not in df.columns:
        return int(len(df))
    reason = _reason(df)
    live = reason.eq("") | reason.eq("nan")
    return int(live.sum())


def count_closed(df: pd.DataFrame | None) -> int:
    """Closed exits. open_at_end marks are excluded."""
    if df is None or df.empty:
        return 0
    if "reason" not in df.columns:
        return int(len(df))
    return int((~_reason(df).eq("open_at_end")).sum())


def preserve_research_open(path: Path) -> Path | None:
    """Copy a research open_at_end file aside before the live runner replaces it."""
    dest = path.with_name("research_open_at_end.csv")
    if dest.exists() or not path.exists() or path.stat().st_size == 0:
        return None
    df = pd.read_csv(path)
    if "reason" not in df.columns or not _reason(df).eq("open_at_end").any():
        return None
    df.to_csv(dest, index=False)
    return dest
