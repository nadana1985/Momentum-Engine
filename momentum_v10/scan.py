# Version 10
"""
DEPRECATED: This is an old/archived file.
Use the V3 Dynamic Architecture (cta_dual.py, universe_generator.py).
"""
"""Universe ignition scan -> CSV with forward-outcome columns.

Replaces scratch/dual_tier_momentum_scan.py, scratch/scan_hyper_shocks.py,
scratch/unified_ignition_scanner.py and scratch/check_assets.py with one
consumer over the shared feature core.

Defaults reproduce the validated p99 strict scan exactly:
  python -m momentum_v10.scan --out scratch/ignitions_p99.csv

Examples:
  python -m momentum_v10.scan --shock-mult 15        # fixed-15x behavior
  python -m momentum_v10.scan --lax-year --no-taker  # old tape-generator universe
  python -m momentum_v10.scan --first-of-run         # one flag per episode
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from .config import BARS_1YR, FeatureConfig, OutcomeConfig, SHARD_DIR
from .features import enrich, load_asset
from .outcomes import event_stats


def scan_asset(path: Path, cfg: FeatureConfig, ocfg: OutcomeConfig,
               window_start=None, window_end=None, lookback_hours: int | None = None):
    """Return (event_frame, stats_dict, n_bars) for one shard, or (None, stats).

    Window: explicit [window_start, window_end] if given (per-asset end capped
    by the shard's own last bar), otherwise the last lookback_hours up to the
    shard's last bar.
    """
    stats = dict(shock_bars=0, breakout_bars=0, dormant_bars=0, aggr_bars=0,
                 ignitions=0, excluded='', bars=0)
    df = load_asset(path)
    if len(df) < BARS_1YR:
        stats['excluded'] = 'len<8760'
        return None, stats

    asset_end = df.index.max()
    if window_start is not None or window_end is not None:
        start = pd.Timestamp(window_start) if window_start is not None else df.index.min()
        end = pd.Timestamp(window_end) if window_end is not None else asset_end
    else:
        end = asset_end
        start = end - pd.Timedelta(hours=lookback_hours)
    feat = enrich(df, cfg)
    window = feat.loc[start:end]

    # cumulative funnel over window bars
    w_shock = (window['shock_mult'] > window['shock_thresh']) & (window['volume'] > 0)
    w_break = w_shock & window['breakout']
    w_dorm = w_break & window['is_dormant_book']
    w_aggr = w_dorm & window['is_aggressive_flow']
    stats.update(bars=len(df), shock_bars=int(w_shock.sum()),
                 breakout_bars=int(w_break.sum()), dormant_bars=int(w_dorm.sum()),
                 aggr_bars=int(w_aggr.sum()))

    flags = window[window['ignition_signal']]
    if flags.empty:
        return None, stats

    highs = feat['high'].to_numpy()
    lows = feat['low'].to_numpy()
    closes = feat['close'].to_numpy()
    n = len(feat)
    pos = feat.index.get_indexer(flags.index)

    rows = []
    for p, (idx, flag) in zip(pos, flags.iterrows()):
        s = event_stats(feat, p, ocfg)
        rec = {
            'timestamp': idx,
            'shock_mult': float(flag['shock_mult']),
            'shock_thresh': float(flag['shock_thresh']),
            'taker_ratio': float(flag['taker_ratio']),
            'mfe_3h': s['mfe_3h'], 'mae_3h': s['mae_3h'],
            'mfe_6h': s['mfe_6h'], 'mae_6h': s['mae_6h'],
            'mfe_24h': s['mfe_24h'], 'mae_24h': s['mae_24h'],
            'mfe_168h': s['mfe_168h'], 'mae_168h': s['mae_168h'],
            'ret_168h': s['ret_168h'],
            'peak_gain_low_held': s['peak_gain_low_held'],
            'low_break_hour': s['low_break_hour'],
            'one_candle_ignition': s['one_candle_ignition'],
        }
        rows.append(rec)
    events = pd.DataFrame(rows)
    stats['ignitions'] = int(flags['ignition_signal'].sum())
    return events, stats


def main():
    ap = argparse.ArgumentParser(description='Unified ignition universe scan.')
    ap.add_argument('--days', type=int, default=30)
    ap.add_argument('--start', default=None, help='YYYY-MM-DD inclusive window start (overrides --days)')
    ap.add_argument('--end', default=None, help='YYYY-MM-DD inclusive window end (overrides --days)')
    ap.add_argument('--out', default='scratch/ignitions.csv')
    ap.add_argument('--data-dir', type=Path, default=SHARD_DIR)
    ap.add_argument('--shock-percentile', type=float, default=99.0,
                    help="gate = trailing-1yr p{SHOCK_PERCENTILE} of own shock_mult (default 99)")
    ap.add_argument('--shock-mult', type=float, default=None,
                    help='use a fixed volume-shock multiplier (e.g. 15) instead of the percentile')
    ap.add_argument('--lax-year', action='store_true',
                    help='allow partial 1yr baselines (min_periods 720) instead of strict 8760')
    ap.add_argument('--no-taker', action='store_true',
                    help='drop the aggressive-taker-flow filter (old tape-generator definition)')
    ap.add_argument('--first-of-run', action='store_true',
                    help='flag only the first bar of each consecutive-hour episode')
    args = ap.parse_args()

    cfg = FeatureConfig(
        shock_percentile=args.shock_percentile,
        shock_mult=args.shock_mult,
        year_min_periods=720 if args.lax_year else BARS_1YR,
        require_taker=not args.no_taker,
        first_of_run=args.first_of_run,
    )
    ocfg = OutcomeConfig()
    scan_hours = args.days * 24
    if args.start or args.end:
        win_desc = f'{args.start or "earliest"} -> {args.end or "latest"}'
    else:
        win_desc = f'last {args.days} days'

    cols = (['asset', 'timestamp', 'shock_mult', 'shock_thresh', 'taker_ratio']
            + [f'{m}_{h}h' for h in ocfg.horizons for m in ('mfe', 'mae')]
            + ['ret_168h', 'peak_gain_low_held', 'low_break_hour', 'one_candle_ignition'])
    results = []
    totals = dict(shock_bars=0, breakout_bars=0, dormant_bars=0, aggr_bars=0, ignitions=0)
    n_scanned = n_excluded = n_error = 0

    print(f'Unified ignition scan | window: {win_desc} | shock gate: {cfg.gate_label()} | '
          f'year: {cfg.year_label()} | taker: {"on" if cfg.require_taker else "off"}')

    for i, file in enumerate(sorted(args.data_dir.glob('*.parquet')), 1):
        asset = file.stem.replace('_USDT_1h', '')
        try:
            if args.start or args.end:
                events, stats = scan_asset(file, cfg, ocfg,
                                           window_start=args.start, window_end=args.end)
            else:
                events, stats = scan_asset(file, cfg, ocfg, lookback_hours=scan_hours)
        except Exception as e:
            n_error += 1
            print(f'  [{asset}] ERROR: {e}', flush=True)
            continue
        if stats['excluded']:
            n_excluded += 1
            continue
        n_scanned += 1
        for k in totals:
            totals[k] += stats[k]
        if events is not None:
            events['asset'] = asset
            results.append(events)
        if i % 100 == 0:
            print(f'  scanned {i} files...', flush=True)

    print(f'\nFiles: {n_scanned} scanned | {n_excluded} excluded (<8760 bars) | {n_error} errors')
    print(f'Funnel (cumulative, window bars): shock gate: {totals["shock_bars"]} '
          f'| +24h-high break: {totals["breakout_bars"]} '
          f'| +dormant book: {totals["dormant_bars"]} '
          f'| +aggressive taker flow: {totals["aggr_bars"]}')

    if not results:
        print('\nNo ignition rows flagged in the window.')
        pd.DataFrame(columns=cols).to_csv(args.out, index=False)
        return

    all_events = pd.concat(results, ignore_index=True)
    all_events['timestamp'] = all_events['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
    all_events = all_events.sort_values(['timestamp', 'asset'])
    csv = all_events[cols].round({
        'shock_mult': 1, 'shock_thresh': 2, 'taker_ratio': 4, 'ret_168h': 2,
        'peak_gain_low_held': 2,
        **{f'mfe_{h}h': 2 for h in ocfg.horizons},
        **{f'mae_{h}h': 2 for h in ocfg.horizons},
    })
    print(f'\nFlagged {len(csv)} ignition rows across {csv["asset"].nunique()} assets -> {args.out}')

    complete = csv.dropna(subset=['mfe_24h'])
    print(f'\nForward outcome (complete +24h: {len(complete)} of {len(csv)} rows):')
    for h in ocfg.horizons:
        print(f'  +{h:>3d}h  median MFE {complete[f"mfe_{h}h"].median():+.2f}% | '
              f'median MAE {complete[f"mae_{h}h"].median():+.2f}%')
    c1w = complete.dropna(subset=['mfe_168h'])
    if len(c1w):
        print(f'  +1w close-to-close median {c1w["ret_168h"].median():+.2f}% | '
              f'MFE >= +10%: {(c1w["mfe_168h"] >= 10).mean() * 100:.0f}%')

    # stringify low_break_hour for the file (blank = trigger low held all 24h)
    csv['low_break_hour'] = csv['low_break_hour'].apply(
        lambda v: '' if pd.isna(v) else str(int(v)))
    csv.to_csv(args.out, index=False)


if __name__ == '__main__':
    main()




