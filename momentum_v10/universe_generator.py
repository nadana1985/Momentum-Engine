# Version 10
"""universe_generator.py — parallel dual-engine batch tear-sheet generator.

Combines the two perfected pieces:

  * Engine:  momentum_v10/cta_dual.py  (compute_features + run_cta,
             True Dynamic Fix: armed P99-shock ignition + P90-OI continuation)
  * Format:  scratch/format_dash_meaningful.py (Macro Scorecard, Behavioral
             Analytics, contextual exit reasons: Round Trip vs Failed Ignition)

Iterates every *_USDT_1h.parquet in data/raw_shards/, injects Open Interest
from data/exotic_shards/ (defaults OI change to 0.0 when missing), simulates
the full dual engine per asset, and writes an institutional markdown tear
sheet to data/all_tapes/v6_production/{ASSET}_tear_sheet.md.

Execution is parallelized with ProcessPoolExecutor; a per-asset failure is
logged to errors.log and never aborts the run.

Usage:
    python -m momentum_v10.universe_generator [--data-dir data/raw_shards]
                                                 [--out data/all_tapes/v6_production]
                                                 [--workers N]
"""

from __future__ import annotations

import argparse
import math
import os

# --- Thread-count firewall: must be set BEFORE numpy/pandas are imported ---
# ProcessPoolExecutor workers each import numpy, which spawns its own BLAS pool.
# 16 workers × 16 BLAS threads = 256 threads on 16 cores → thrashing / OS deadlock.
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("SCIPY_OPENBLAS64_NUM_THREADS", "1")   # bundled scipy-openblas64 (NumPy 2.1.1+)
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")


from concurrent.futures import ProcessPoolExecutor, as_completed
import re
from pathlib import Path

import pandas as pd


from momentum_v10.config import CtaConfig, EXOTIC_DIR, FeatureConfig
from momentum_v10.cta_dual import compute_features, run_cta
from momentum_v10.features import load_asset


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def discover_assets(data_dir: Path) -> list[str]:
    """Extract the asset symbol from every valid raw shard filename."""
    suffix = '_USDT_1h.parquet'
    assets = sorted(
        p.name[: -len(suffix)]
        for p in data_dir.glob(f'*{suffix}')
        if p.name.endswith(suffix)
    )
    # Symbols are [A-Z0-9]. Names mangled to '?' on a non-UTF-8 save cannot be
    # matched to Binance or the exotic shards; leave them out of the book.
    return [a for a in assets if re.fullmatch(r"[A-Z0-9]+", a)]


def load_with_oi(asset: str, data_dir: Path) -> pd.DataFrame:
    """Load the 1h shard and join Open Interest from the exotic shard.

    Missing / corrupt exotic shards silently default oi_change to 0.0 so the
    engine still runs (the exhaustion exit simply never fires for that asset).
    """
    file = data_dir / f'{asset}_USDT_1h.parquet'
    df = load_asset(file)
    try:
        metrics_file = EXOTIC_DIR / f'{asset}USDT_metrics.parquet'
        metrics = pd.read_parquet(metrics_file)
        metrics['timestamp'] = pd.to_datetime(metrics['timestamp'], unit='ms')
        metrics.set_index('timestamp', inplace=True)
        metrics = metrics.resample('1h').last().ffill()

        cols_to_join = ['sum_open_interest']
        # Signal 2: USD OI value — join if present
        if 'sum_open_interest_value' in metrics.columns:
            cols_to_join.append('sum_open_interest_value')
        if 'count_toptrader_long_short_ratio' in metrics.columns:
            cols_to_join.append('count_toptrader_long_short_ratio')

        df = df.join(metrics[cols_to_join], how='left')
        df['sum_open_interest'] = df['sum_open_interest'].ffill()
        df['oi_change'] = df['sum_open_interest'].pct_change()

        # Signal 2: USD OI change — forward-fill then compute pct change
        if 'sum_open_interest_value' in df.columns:
            df['sum_open_interest_value'] = df['sum_open_interest_value'].ffill()
        else:
            df['sum_open_interest_value'] = float('nan')

        if 'count_toptrader_long_short_ratio' in df.columns:
            df['count_toptrader_long_short_ratio'] = df['count_toptrader_long_short_ratio'].ffill()
            df['topLongShortAccountRatio'] = df['count_toptrader_long_short_ratio']
        else:
            df['count_toptrader_long_short_ratio'] = 1.0
            df['topLongShortAccountRatio'] = 1.0

    except Exception:
        df['oi_change'] = 0.0
        df['sum_open_interest_value'] = float('nan')
        df['count_toptrader_long_short_ratio'] = 1.0
        df['topLongShortAccountRatio'] = 1.0

    try:
        funding_file = EXOTIC_DIR / f'{asset}USDT_funding.parquet'
        funding = pd.read_parquet(funding_file)
        funding['timestamp'] = pd.to_datetime(funding['timestamp'], unit='ms')
        funding.set_index('timestamp', inplace=True)
        funding = funding.resample('1h').last().ffill()
        
        if 'funding_rate' in funding.columns:
            df = df.join(funding[['funding_rate']], how='left')
            df['funding_rate'] = df['funding_rate'].ffill()
        else:
            df['funding_rate'] = 0.0
    except Exception:
        df['funding_rate'] = 0.0
    return df


# ---------------------------------------------------------------------------
# Advanced institutional metrics — exact definitions from
# scratch/format_dash_meaningful.py (win/loss masks, PF, expectancy, MDD,
# winner/loser splits, exit efficiency).
# ---------------------------------------------------------------------------

def format_duration(seconds: float) -> str:
    if pd.isna(seconds):
        return '0h'
    d = int(seconds // 86400)
    h = int((seconds % 86400) // 3600)
    if d > 0:
        return f'{d}d {h}h'
    return f'{h}h'


def compute_scorecard(trades: pd.DataFrame) -> dict:
    """Mirror format_dash_meaningful.py's Macro Scorecard + Behavioral maths."""
    win_mask = trades['pnl'] > 0
    loss_mask = trades['pnl'] <= 0
    total_trades = len(trades)

    win_rate = (len(trades[win_mask]) / total_trades * 100) if total_trades > 0 else 0
    cumulative_pnl = trades['pnl'].sum() * 100
    cumulative_mfe = trades['mfe'].sum() * 100
    cumulative_mae = trades['mae'].sum() * 100

    gross_profit = trades[win_mask]['pnl'].sum()
    gross_loss = abs(trades[loss_mask]['pnl'].sum())
    profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else float('inf')

    expectancy = (trades['pnl'].mean() * 100) if total_trades > 0 else 0

    cumulative = trades['pnl'].cumsum()
    peak = cumulative.cummax()
    drawdown = cumulative - peak
    mdd = (drawdown.min() * 100) if not drawdown.empty else 0

    avg_win = trades[win_mask]['pnl'].mean() * 100 if len(trades[win_mask]) > 0 else 0
    avg_loss = trades[loss_mask]['pnl'].mean() * 100 if len(trades[loss_mask]) > 0 else 0

    trades = trades.copy()
    trades['duration'] = (trades['exit'] - trades['entry']).dt.total_seconds()
    avg_dur_win = trades[win_mask]['duration'].mean()
    avg_dur_loss = trades[loss_mask]['duration'].mean()

    avg_mfe_win = trades[win_mask]['mfe'].mean() * 100 if len(trades[win_mask]) > 0 else 0
    avg_mae_win = trades[win_mask]['mae'].mean() * 100 if len(trades[win_mask]) > 0 else 0

    trades['efficiency'] = trades['pnl'] / trades['mfe'].replace(0, 1e-8)
    avg_eff = trades[win_mask]['efficiency'].mean() * 100 if len(trades[win_mask]) > 0 else 0

    return dict(
        total_trades=total_trades,
        win_rate=win_rate,
        cumulative_pnl=cumulative_pnl,
        cumulative_mfe=cumulative_mfe,
        cumulative_mae=cumulative_mae,
        profit_factor=profit_factor,
        expectancy=expectancy,
        mdd=mdd,
        avg_win=avg_win,
        avg_loss=avg_loss,
        avg_dur_win=avg_dur_win,
        avg_dur_loss=avg_dur_loss,
        avg_mfe_win=avg_mfe_win,
        avg_mae_win=avg_mae_win,
        avg_eff=avg_eff,
    )


def contextual_reason(reason: str, mfe: float) -> str:
    """Map raw exit reason -> contextual label (exact format_dash_meaningful logic)."""
    if reason == 'exhaustion':
        return '**OI CAPITULATION (TOP CAUGHT)**'
    if reason == 'open_at_end':
        return '*(Still Open)*'
    # Structural stop: categorize by how far the trade ran first.
    mfe_val = mfe * 100
    if mfe_val < 3.0:
        return '*Failed Ignition (Stop Loss)*'
    if mfe_val >= 10.0:
        return 'Round Trip (Massive Bleed Out)'
    return 'Round Trip (Minor Bleed Out)'


# ---------------------------------------------------------------------------
# Tear-sheet rendering
# ---------------------------------------------------------------------------

def render_tear_sheet(asset: str, df: pd.DataFrame, trades: pd.DataFrame) -> str:
    """Render the institutional markdown tear sheet (format_dash_meaningful.py)."""
    lines: list[str] = []
    first_ts, last_ts = df.index.min(), df.index.max()

    lines.append(f'# {asset} — Institutional Momentum Tear Sheet')
    lines.append('')
    lines.append('### The Engine Definition')
    lines.append(f'* **Timeframe Analyzed:** {first_ts} to {last_ts}')
    lines.append('* **Ignition Rule:** True Dynamic Fix (ATR & P90 OI Continuation)')
    lines.append('* **Exit Rules:** Structural Ignition Low OR OI Exhaustion Harvester')

    if trades.empty:
        lines.append('')
        lines.append('**NO TRADES**')
        return '\n'.join(lines)

    m = compute_scorecard(trades)

    lines.append('')
    lines.append('### The Macro Scorecard')
    lines.append(f"* **Total Ignitions:** {m['total_trades']}")
    lines.append(f"* **Win Rate:** {m['win_rate']:.1f}%")
    lines.append(f"* **Cumulative PnL:** {m['cumulative_pnl']:+.1f}%")
    lines.append(f"* **Cumulative MFE:** {m['cumulative_mfe']:+.1f}%")
    lines.append(f"* **Cumulative MAE:** {m['cumulative_mae']:+.1f}%")
    pf = m['profit_factor']
    lines.append(f"* **Profit Factor:** {'inf' if not math.isfinite(pf) else f'{pf:.2f}'}")
    lines.append(f"* **Expectancy per Trade:** {m['expectancy']:+.1f}%")
    lines.append(f"* **Max Drawdown (MDD):** {m['mdd']:+.1f}%")

    lines.append('')
    lines.append('### Behavioral Analytics')
    lines.append(f"* **Avg Winner / Avg Loser:** {m['avg_win']:+.1f}% / {m['avg_loss']:+.1f}%")
    lines.append(f"* **Avg Duration (Win / Loss):** {format_duration(m['avg_dur_win'])} / {format_duration(m['avg_dur_loss'])}")
    lines.append(f"* **Avg Peak MFE (Winners):** {m['avg_mfe_win']:+.1f}%")
    lines.append(f"* **Avg Peak MAE (Winners):** {m['avg_mae_win']:+.1f}%")
    lines.append(f"* **Avg Exit Efficiency:** {m['avg_eff']:.1f}%")

    lines.append('')
    lines.append('### The Granular Tape')
    lines.append('| Engine Type | Ignition Time | Exit Time | Duration | Entry Px | Exit Px | Net PnL | Peak MFE | Peak MAE | Exit Reason |')
    lines.append('|---|---|---|---|---|---|---|---|---|---|')

    trades = trades.sort_values('entry').copy()
    trades['duration'] = (trades['exit'] - trades['entry']).dt.total_seconds()
    for _, t in trades.iterrows():
        mfe_val = t['mfe'] * 100
        ep = t.get('entry_price', float('nan'))
        xp = t.get('exit_price', float('nan'))
        ep_fmt = f"{ep:g}" if pd.notna(ep) else "—"
        xp_fmt = f"{xp:g}" if pd.notna(xp) else "—"
        lines.append(
            f"| **{t['engine']}** | {t['entry']} | {t['exit']} | "
            f"{format_duration(t['duration'])} | {ep_fmt} | {xp_fmt} | {t['pnl'] * 100:+.1f}% | "
            f"{mfe_val:+.1f}% | {t['mae'] * 100:+.1f}% | "
            f"{contextual_reason(t['reason'], t['mfe'])} |"
        )

    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Worker (picklable module-level function for ProcessPoolExecutor)
# ---------------------------------------------------------------------------

def process_asset(args: tuple[str, str]) -> tuple[str, str | None, str | None]:
    """Run the full dual engine for one asset. Returns (asset, markdown, error)."""
    asset, data_dir = args
    try:
        df = load_with_oi(asset, Path(data_dir))
        fcfg = FeatureConfig(
            shock_percentile=99.0,
            shock_mult=None,
            year_min_periods=720,
            dormant_mode='relative',
            max_notional_usd=150000.0,
            require_taker=True,
            taker_buffer=0.01,
            first_of_run=True,
        )
        cfg = CtaConfig()
        feat = compute_features(df, fcfg, asset=asset)
        trades = run_cta(feat, cfg, asset=asset)
        return asset, render_tear_sheet(asset, df, trades), None
    except Exception as e:  # noqa: BLE001 — one bad shard must never kill the universe
        return asset, None, f'{type(e).__name__}: {e}'


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description='Batch-generate institutional tear sheets for the whole universe.')
    parser.add_argument('--data-dir', type=str, default='data/raw_shards')
    parser.add_argument('--out', type=str, default='data/all_tapes/v10_production')
    parser.add_argument('--workers', type=int, default=None,
                        help='ProcessPoolExecutor workers (default: min(16, cpu_count))')
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    errors_log = out_dir / 'errors.log'

    assets = discover_assets(data_dir)
    total = len(assets)
    print(f'[universe_generator] discovered {total} assets in {data_dir}')
    print(f'[universe_generator] output -> {out_dir}')

    workers = args.workers or min(16, os.cpu_count() or 1)
    ok, failed = 0, 0
    failures: list[str] = []

    with ProcessPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(process_asset, (a, str(data_dir))): a for a in assets}
        for i, fut in enumerate(as_completed(futures), 1):
            asset, markdown, error = fut.result()
            if error is not None:
                failed += 1
                failures.append(f'{asset}: {error}')
                with errors_log.open('a', encoding='utf-8') as f:
                    f.write(f'{asset}: {error}\n')
                print(f'[{i}/{total}] FAIL {asset}: {error}')
                continue
            (out_dir / f'{asset}_tear_sheet.md').write_text(markdown, encoding='utf-8')
            ok += 1
            if i % 50 == 0 or i == total:
                print(f'[{i}/{total}] ok={ok} failed={failed}')

    print()
    print(f'[universe_generator] DONE: {ok}/{total} tear sheets written to {out_dir}')
    if failures:
        print(f'[universe_generator] {failed} asset(s) FAILED — see {errors_log}')
        for line in failures:
            print(f'  - {line}')
    else:
        print('[universe_generator] zero failures')


if __name__ == '__main__':
    main()



