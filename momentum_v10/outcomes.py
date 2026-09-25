# Version 10
"""
DEPRECATED: This is an old/archived file.
Use the V3 Dynamic Architecture (cta_dual.py, universe_generator.py).
"""
"""Shared forward-outcome (post-hoc label) computations.

These read bars t+1..t+N and are NEVER used to trigger anything — they exist
only to evaluate flags after the fact. One implementation serves both the scan
CSV and the markdown tape, so the two can no longer disagree.

Canonical semantics (mirrors the validated scratch/dual_tier_momentum_scan.py):
  - MFE/MAE on highs/lows vs the flagged bar's close, window t+1..t+N
  - ret_Nh  = close at t+N vs entry close
  - peak_gain_low_held = best high strictly BEFORE the trigger low first breaks
    within +low_hold_hours (NaN if it breaks on the first lookahead bar)
  - low_break_hour     = 1..N when the trigger low first breaks (NaN = held)
  - one_candle_ignition = isolated single-candle trigger (no other flags within
    the previous/next hour, judged against the SAME flag universe the consumer
    used) AND the next 1h candle's high > the trigger candle's high
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .config import OutcomeConfig


def event_stats(df: pd.DataFrame, pos: int, cfg: OutcomeConfig,
                flag_col: str = '_ignition') -> dict:
    """Forward-outcome stats for the ignition at row pos (0-based position)."""
    entry = float(df['close'].iloc[pos])
    trig_low = float(df['low'].iloc[pos])
    n = len(df)
    highs = df['high'].to_numpy()
    lows = df['low'].to_numpy()
    closes = df['close'].to_numpy()

    stats: dict = {}
    for h in cfg.horizons:
        if pos + 1 + h <= n:
            fut = slice(pos + 1, pos + 1 + h)
            stats[f'mfe_{h}h'] = (float(highs[fut].max()) / entry - 1.0) * 100.0
            stats[f'mae_{h}h'] = (float(lows[fut].min()) / entry - 1.0) * 100.0
        else:
            stats[f'mfe_{h}h'] = np.nan
            stats[f'mae_{h}h'] = np.nan

    rh = cfg.ret_horizon
    stats[f'ret_{rh}h'] = ((float(closes[pos + rh]) / entry - 1.0) * 100.0
                           if pos + rh < n else np.nan)

    # trigger-low hold over the next low_hold_hours bars
    H = cfg.low_hold_hours
    stats['peak_gain_low_held'] = np.nan
    stats['low_break_hour'] = np.nan
    if pos + 1 + H <= n:
        end = pos + 1 + H
        break_at = None
        for b in range(pos + 1, end):
            if lows[b] < trig_low:
                break_at = b
                break
        if break_at is None:
            stats['peak_gain_low_held'] = (float(highs[pos + 1:end].max()) / entry - 1.0) * 100.0
        else:
            stats['low_break_hour'] = float(break_at - pos)
            if break_at > pos + 1:
                stats['peak_gain_low_held'] = (float(highs[pos + 1:break_at].max()) / entry - 1.0) * 100.0

    # one-candle: isolation judged against the SAME flag universe (flag_col).
    # Only meaningful when pos IS a flagged bar; for non-flag positions the
    # search lands at the insertion point which may equal len(flags).
    flags = df.index[df[flag_col]]
    j = flags.searchsorted(df.index[pos])
    if j < len(flags) and flags[j] == df.index[pos]:
        left_ok = (j == 0) or (flags[j] - flags[j - 1] > pd.Timedelta(hours=1))
        right_ok = (j == len(flags) - 1) or (flags[j + 1] - flags[j] > pd.Timedelta(hours=1))
        isolated = bool(left_ok and right_ok)
    else:
        isolated = False
    next_extended = bool(pos + 1 < n and highs[pos + 1] > highs[pos])
    stats['one_candle_ignition'] = 'yes' if (isolated and next_extended) else 'no'
    stats['isolated'] = isolated
    return stats




