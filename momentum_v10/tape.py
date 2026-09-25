# Version 10
"""
DEPRECATED: This is an old/archived file.
Use the V3 Dynamic Architecture (cta_dual.py, universe_generator.py).
"""
"""Per-asset full-history post-shock tape -> markdown.

Replaces scratch/generate_post_shock_tape.py (full-history mode) over the
shared feature core, so its numbers can never drift from scan.py again: same
gate, same dormant logic, same forward-outcome semantics, one-candle isolation
judged against the SAME flag universe that produced the event list.

Usage:
  python -m momentum_v10.tape --asset ZEC --out scratch/zec_tape.md
  python -m momentum_v10.tape --asset ZEC --shock-mult 15        # old fixed-15x tape
  python -m momentum_v10.tape --asset ZEC --lax-year --no-taker  # reproduces the 107-event p99 tape
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from .config import BARS_1YR, FeatureConfig, OutcomeConfig, SHARD_DIR
from .features import enrich, load_asset
from .outcomes import event_stats


def _fmt(x, nd=4):
    if x is None or (isinstance(x, float) and pd.isna(x)):
        return '—'
    return f'{x:.{nd}f}'


def _fmt_pct(x):
    if x is None or (isinstance(x, float) and pd.isna(x)):
        return '—'
    return f'{x:+.2f}%'


def build_tape(asset: str, out: Path, cfg: FeatureConfig, ocfg: OutcomeConfig,
               tape_hours: int = 72, data_dir: Path = SHARD_DIR):
    file = data_dir / f'{asset}_USDT_1h.parquet'
    if not file.exists():
        print(f'ERROR: no shard for {asset}')
        return
    df = load_asset(file)
    feat = enrich(df, cfg)
    flag_col = '_ignition'
    flags = feat.index[feat[flag_col]]

    with open(out, 'w', encoding='utf-8') as f:
        f.write(f'# {asset} — Full-History Post-Shock Tape\n\n')
        f.write(f'- **Shard:** `{file.name}`\n')
        f.write(f'- **History:** {df.index.min()} → {df.index.max()} UTC ({len(df):,} hourly bars)\n')
        defn = (f'shock > {cfg.gate_label()} & close > causal 24h high & '
                f'dormant book (30d median notional < 1yr median notional)'
                if cfg.dormant_mode == 'relative' else
                f'shock > {cfg.gate_label()} & close > causal 24h high & dormant mode: {cfg.dormant_mode}')
        if cfg.require_taker:
            defn += ' & aggressive taker flow (taker > own 30d median + 0.01)'
        f.write(f'- **Definition:** {defn}\n')
        f.write(f'- **Year baseline:** {cfg.year_label()}\n')
        f.write(f'- **Ignitions:** {len(flags)} (flag universe: '
                f"{'strict w/ taker' if cfg.require_taker else 'tape w/o taker'})\n\n")

        if len(flags) == 0:
            f.write('No ignition events in full history.\n')
            print(f'{asset}: no ignitions in full history')
            return

        f.write('## Summary\n\n')
        f.write('| # | Ignition (UTC) | Entry Close | Shock | Gate | Taker | Aggr | 3h MFE/MAE | '
                '6h MFE/MAE | 24h MFE/MAE | 1w MFE/MAE | Peak (low held) | Low break | 1-candle |\n')
        f.write('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n')
        for i, t in enumerate(flags, 1):
            pos = feat.index.get_loc(t)
            r = feat.iloc[pos]
            s = event_stats(feat, pos, ocfg, flag_col)
            aggr = '✓' if bool(r['is_aggressive_flow']) else '✗'
            lb = str(int(s['low_break_hour'])) if not pd.isna(s['low_break_hour']) else 'held'
            f.write(
                f"| {i} | {t} | {r['close']:.6f} | {r['shock_mult']:.1f}x | "
                f"{r['shock_thresh']:.2f}x | {_fmt(r['taker_ratio'])} | {aggr} | "
                f"{_fmt_pct(s['mfe_3h'])}/{_fmt_pct(s['mae_3h'])} | "
                f"{_fmt_pct(s['mfe_6h'])}/{_fmt_pct(s['mae_6h'])} | "
                f"{_fmt_pct(s['mfe_24h'])}/{_fmt_pct(s['mae_24h'])} | "
                f"{_fmt_pct(s['mfe_168h'])}/{_fmt_pct(s['mae_168h'])} | "
                f"{_fmt_pct(s['peak_gain_low_held'])} | {lb} | {s['one_candle_ignition']} |\n")
        f.write('\n\n---\n\n')

        for i, t in enumerate(flags, 1):
            pos = feat.index.get_loc(t)
            r = feat.iloc[pos]
            s = event_stats(feat, pos, ocfg, flag_col)
            entry = float(r['close'])
            trig_low = float(r['low'])
            n = len(feat)

            f.write(f'## Event {i}: {t} UTC\n\n### Trigger bar\n\n')
            f.write('| Field | Value |\n|---|---|\n')
            f.write(f'| Close (entry) | {entry:.6f} |\n')
            f.write(f'| Trigger-bar low | {trig_low:.6f} |\n')
            f.write(f'| Volume | {r["volume"]:,.0f} |\n')
            f.write(f'| Shock multiplier | {r["shock_mult"]:.1f}x vs {r["vol_24h_avg"]:,.0f} causal 24h avg |\n')
            f.write(f'| Shock gate | {cfg.gate_label()} (threshold {r["shock_thresh"]:.2f}x) |\n')
            f.write(f'| 24h-high breakout | {r["close"]:.6f} > {r["price_24h_high"]:.6f} ✓ |\n')
            f.write(f'| Dormant book | 30d med {r["p50_30d"]:,.0f} < 1yr med {r["p50_1yr"]:,.0f} ✓ |\n')
            f.write(f'| Taker ratio | {_fmt(r["taker_ratio"])} vs 30d median {_fmt(r["p50_taker_30d"])} '
                    f'+ 0.01 → {"aggressive ✓" if bool(r["is_aggressive_flow"]) else "NOT aggressive ✗"} |\n')

            f.write('\n### Forward outcome\n\n| Metric | +3h | +6h | +24h | +1w |\n|---|---|---|---|---|\n')
            f.write(f"| MFE | {_fmt_pct(s['mfe_3h'])} | {_fmt_pct(s['mfe_6h'])} | "
                    f"{_fmt_pct(s['mfe_24h'])} | {_fmt_pct(s['mfe_168h'])} |\n")
            f.write(f"| MAE | {_fmt_pct(s['mae_3h'])} | {_fmt_pct(s['mae_6h'])} | "
                    f"{_fmt_pct(s['mae_24h'])} | {_fmt_pct(s['mae_168h'])} |\n")
            f.write(f"\n- **Peak gain while trigger low held:** {_fmt_pct(s['peak_gain_low_held'])}\n")
            if not pd.isna(s['low_break_hour']):
                f.write(f"- **Trigger low first broken:** hour {int(s['low_break_hour'])} after trigger\n")
            else:
                f.write('- **Trigger low held all 24h**\n')
            f.write(f"- **One-candle ignition:** {s['one_candle_ignition']} (isolated={s['isolated']}, "
                    f"next bar high {'>' if pos + 1 < n and feat['high'].iloc[pos + 1] > feat['high'].iloc[pos] else '≤'} trigger high)\n\n")

            f.write('### Tape (next 72 hourly bars)\n\n')
            f.write('| +h | Timestamp | Close | High | Low | Volume | Shock | vs entry |\n')
            f.write('|---|---|---|---|---|---|---|---|\n')
            f.write(f'| 0 | {t} | {entry:.6f} | {r["high"]:.6f} | {trig_low:.6f} | '
                    f'{r["volume"]:,.0f} | {r["shock_mult"]:.1f}x | — |\n')
            for k in range(1, tape_hours + 1):
                if pos + k >= n:
                    break
                b = feat.iloc[pos + k]
                f.write(f'| {k} | {feat.index[pos + k]} | {b["close"]:.6f} | {b["high"]:.6f} | '
                        f'{b["low"]:.6f} | {b["volume"]:,.0f} | {b["shock_mult"]:.1f}x | '
                        f'{_fmt_pct((b["close"] / entry - 1) * 100)} |\n')
            f.write('\n\n---\n\n')
    print(f'Full-history tape written: {out} ({len(flags)} events)')


def main():
    ap = argparse.ArgumentParser(description='Per-asset full-history tape.')
    ap.add_argument('--asset', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--data-dir', type=Path, default=SHARD_DIR)
    ap.add_argument('--shock-percentile', type=float, default=99.0)
    ap.add_argument('--shock-mult', type=float, default=None)
    ap.add_argument('--lax-year', action='store_true')
    ap.add_argument('--no-taker', action='store_true')
    ap.add_argument('--tape-hours', type=int, default=72)
    args = ap.parse_args()

    cfg = FeatureConfig(shock_percentile=args.shock_percentile, shock_mult=args.shock_mult,
                        year_min_periods=720 if args.lax_year else BARS_1YR,
                        require_taker=not args.no_taker)
    build_tape(args.asset, Path(args.out), cfg, OutcomeConfig(),
               tape_hours=args.tape_hours, data_dir=args.data_dir)


if __name__ == '__main__':
    main()




