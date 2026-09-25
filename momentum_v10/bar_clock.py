"""1h bars are tradable only after the hour has closed.

A Binance kline requested mid-hour includes the forming candle. Its close is
the last trade so far, not the hourly close. Stepping it, then refusing to
revisit that timestamp, locks in the partial bar.
"""
from __future__ import annotations

import pandas as pd

HOUR = pd.Timedelta(hours=1)


def _naive(value) -> pd.Timestamp:
    ts = pd.Timestamp(value)
    if ts.tzinfo is not None:
        ts = ts.tz_convert("UTC").tz_localize(None)
    return ts


def bar_is_closed(open_time, now) -> bool:
    """A bar that opens at T is closed once now >= T + 1 hour."""
    return _naive(open_time) + HOUR <= _naive(now)


def drop_forming_klines(frame: pd.DataFrame, now_ms: int) -> pd.DataFrame:
    """Remove klines whose close_time is still in the future."""
    if frame.empty or "close_time" not in frame.columns:
        return frame
    closed = pd.to_numeric(frame["close_time"], errors="coerce") < int(now_ms)
    return frame.loc[closed].copy()


def drop_forming_hours(frame: pd.DataFrame, now_ms: int, column: str = "timestamp") -> pd.DataFrame:
    """Remove rows whose 1h bucket has not closed. timestamp is the bar open."""
    if frame.empty or column not in frame.columns:
        return frame
    opened = pd.to_numeric(frame[column], errors="coerce")
    return frame.loc[opened + 3_600_000 <= int(now_ms)].copy()
