# Version 10
"""
DEPRECATED: This is an old/archived file.
Use the V3 Dynamic Architecture (cta_dual.py, universe_generator.py).
"""
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from momentum_v10.features import load_asset, enrich
from momentum_v10.config import CtaConfig, FeatureConfig
import argparse

REASON_LABELS = {
    'structural_stop': 'Structural Stop',
    'exhaustion': 'OI Exhaustion',
    'open_at_end': 'Open at End',
}


def compute_features(df: pd.DataFrame, fcfg: FeatureConfig) -> pd.DataFrame:
    out = enrich(df, fcfg)
    out['raw_long'] = out['strict_ignition']
    out['raw_short'] = False
    return out


def run_cta(df: pd.DataFrame, cfg: CtaConfig) -> pd.DataFrame:
    completed_trades = []
    active_trades = []

    for ts, row in df.iterrows():
        curr_close = float(row['close'])
        curr_high = float(row['high'])
        curr_low = float(row['low'])
        curr_open = float(row['open'])
        curr_shock = float(row.get('shock_mult', 0.0))
        curr_taker = float(row.get('taker_ratio', 0.5))
        curr_oi_change = float(row.get('oi_change', 0.0))

        candle_range = curr_high - curr_low
        upper_wick = curr_high - max(curr_close, curr_open)
        upper_wick_pct = upper_wick / candle_range if candle_range > 0 else 0

        # 1. Update and Check Exits for all active trades
        still_active = []
        for t in active_trades:
            t['trade_max_high'] = max(t['trade_max_high'], curr_high)
            t['trade_min_low'] = min(t['trade_min_low'], curr_low)

            exit_triggered = False
            exit_reason = ''
            exit_price = 0.0

            if curr_close < t['hard_stop']:
                exit_price = curr_close
                exit_triggered = True
                exit_reason = 'structural_stop'

            if not exit_triggered and curr_shock > 3.0 and (upper_wick_pct > 0.40 or curr_taker < 0.45) and curr_oi_change < 0.0:
                exit_price = curr_close
                exit_triggered = True
                exit_reason = 'exhaustion'

            if exit_triggered:
                pnl = (exit_price - t['entry_price']) / t['entry_price']
                completed_trades.append(dict(
                    asset=str(df.iloc[-1].get('asset', '')),
                    side='LONG', entry=t['entry_time'], exit=ts,
                    entry_price=t['entry_price'], exit_price=exit_price,
                    pnl=pnl, shock=t['entry_shock'],
                    mae=(t['trade_min_low'] - t['entry_price']) / t['entry_price'],
                    mfe=(t['trade_max_high'] - t['entry_price']) / t['entry_price'],
                    reason=exit_reason
                ))
            else:
                still_active.append(t)

        active_trades = still_active

        # 2. Check for new entries
        if bool(row.get('raw_long', False)):
            active_trades.append({
                'entry_time': ts,
                'entry_price': curr_close,
                'hard_stop': curr_low,
                'entry_shock': curr_shock,
                'trade_max_high': curr_high,
                'trade_min_low': curr_low
            })

    # Close out any remaining active trades
    for t in active_trades:
        pnl = (curr_close - t['entry_price']) / t['entry_price']
        completed_trades.append(dict(
            asset=str(df.iloc[-1].get('asset', '')),
            side='LONG', entry=t['entry_time'], exit=ts,
            entry_price=t['entry_price'], exit_price=curr_close,
            pnl=pnl, shock=t['entry_shock'],
            mae=(t['trade_min_low'] - t['entry_price']) / t['entry_price'],
            mfe=(t['trade_max_high'] - t['entry_price']) / t['entry_price'],
            reason='open_at_end'
        ))

    return pd.DataFrame(completed_trades)


# ---------------------------------------------------------------------------
# Advanced institutional metrics (independent, overlapping trades)
# ---------------------------------------------------------------------------

def compute_metrics(trades: pd.DataFrame) -> dict:
    """Compute the tear-sheet metrics over the independent overlapping trades.

    Each trade deploys 1 unit of notional (independent capital), so PnLs are
    summed directly. Returns a dict of pre-formatted-ready values.
    """
    n = len(trades)
    wins = trades[trades['pnl'] > 0]
    losses = trades[trades['pnl'] <= 0]

    # 1. Profit Factor: gross positive PnL / ABS(gross negative PnL)
    gross_pos = float(trades.loc[trades['pnl'] > 0, 'pnl'].sum())
    gross_neg = float(trades.loc[trades['pnl'] < 0, 'pnl'].sum())
    profit_factor = gross_pos / abs(gross_neg) if gross_neg != 0 else np.inf

    # 2. Expectancy: average net PnL across all trades
    expectancy = float(trades['pnl'].mean()) * 100

    # 3. Maximum Drawdown: cumulative equity curve, 1 unit of capital per
    #    overlapping trade. Realized PnL of each trade is marked at its exit
    #    hour; equity = 100 + running sum (each trade is an independent 1-unit
    #    book, so percentage PnLs sum directly). MDD = max % peak-to-trough.
    start, end = trades['entry'].min(), trades['exit'].max()
    idx = pd.date_range(start, end, freq='1h')
    realized = trades.groupby('exit')['pnl'].sum().reindex(idx, fill_value=0.0)
    equity = 100.0 + realized.cumsum()
    peak = equity.cummax()
    mdd = float(((equity - peak) / peak).min()) * 100

    # 4. Trade duration (hours between entry and exit)
    duration_h = (trades['exit'] - trades['entry']).dt.total_seconds() / 3600.0

    # 5. Winner / loser splits (avg duration, avg peak MFE, avg peak MAE)
    avg_dur_win_h = float(duration_h[wins.index].mean()) if len(wins) else 0.0
    avg_dur_loss_h = float(duration_h[losses.index].mean()) if len(losses) else 0.0
    avg_mfe_win = float(wins['mfe'].mean()) * 100 if len(wins) else 0.0
    avg_mae_win = float(wins['mae'].mean()) * 100 if len(wins) else 0.0
    avg_mfe_loss = float(losses['mfe'].mean()) * 100 if len(losses) else 0.0
    avg_mae_loss = float(losses['mae'].mean()) * 100 if len(losses) else 0.0

    # 6. Exit efficiency: for winning trades only, share of peak MFE captured
    eff = (wins['pnl'] / wins['mfe'].replace(0, np.nan)).dropna()
    exit_efficiency = float(eff.mean()) * 100 if len(eff) else 0.0

    return dict(
        n=n,
        win_rate=len(wins) / n * 100,
        total_pnl=float(trades['pnl'].sum()) * 100,
        profit_factor=profit_factor,
        expectancy=expectancy,
        mdd=mdd,
        avg_win=float(wins['pnl'].mean()) * 100 if len(wins) else 0.0,
        avg_loss=float(losses['pnl'].mean()) * 100 if len(losses) else 0.0,
        avg_dur_win_days=avg_dur_win_h / 24.0,
        avg_dur_loss_h=avg_dur_loss_h,
        avg_mfe_win=avg_mfe_win,
        avg_mae_win=avg_mae_win,
        avg_mfe_loss=avg_mfe_loss,
        avg_mae_loss=avg_mae_loss,
        exit_efficiency=exit_efficiency,
    )


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

def fmt_price(p: float) -> str:
    return f'{p:.8f}'.rstrip('0').rstrip('.')


def fmt_pct(x: float, nd: int = 1) -> str:
    sign = '+' if x >= 0 else ''
    return f'{sign}{x:.{nd}f}%'


def fmt_duration(hours: float) -> str:
    h = int(round(hours))
    days, hours_left = divmod(h, 24)
    if days:
        return f'{days}d {hours_left}h'
    return f'{hours_left}h'


# ---------------------------------------------------------------------------
# Output printers
# ---------------------------------------------------------------------------

def print_tear_sheet(asset: str, df: pd.DataFrame, trades: pd.DataFrame) -> None:
    """Print the institutional tear sheet (markdown) to stdout."""
    first_ts, last_ts = df.index.min(), df.index.max()

    print(f'# {asset} — Institutional Momentum Tear Sheet')
    print()
    print('### The Engine Definition')
    print(f'* **Timeframe Analyzed:** {first_ts} to {last_ts}')
    print('* **Ignition Rule:** P99 Volume Shock + Breakout + Dormant Book (Relative) + Taker Flow')
    print('* **Exit Rules:** Structural Ignition Low OR OI Exhaustion Harvester')

    if trades.empty:
        print()
        print('**NO TRADES**')
        return

    trades = trades.sort_values('entry')
    m = compute_metrics(trades)

    print()
    print('### The Macro Scorecard')
    print(f"* **Total Ignitions:** {m['n']}")
    print(f"* **Win Rate:** {m['win_rate']:.1f}%")
    print(f"* **Cumulative PnL:** {fmt_pct(m['total_pnl'])}")
    pf = m['profit_factor']
    print(f"* **Profit Factor:** {'inf' if not np.isfinite(pf) else f'{pf:.2f}'}")
    print(f"* **Expectancy per Trade:** {fmt_pct(m['expectancy'])}")
    print(f"* **Max Drawdown (MDD):** {fmt_pct(m['mdd'])}")

    print()
    print('### Behavioral Analytics')
    print(f"* **Avg Winner / Avg Loser:** {fmt_pct(m['avg_win'])} / {fmt_pct(m['avg_loss'])}")
    print(f"* **Avg Duration (Win / Loss):** {m['avg_dur_win_days']:.1f} Days / {m['avg_dur_loss_h']:.1f} Hours")
    print(f"* **Avg Peak MFE (Winners):** {fmt_pct(m['avg_mfe_win'])}")
    print(f"* **Avg Peak MAE (Winners):** {fmt_pct(m['avg_mae_win'])}")
    print(f"* **Avg Exit Efficiency:** {m['exit_efficiency']:.1f}%")

    print()
    print('### The Granular Tape')
    print('| Ignition Time | Entry Price | Exit Time | Exit Price | Duration | Net PnL | Peak MFE | Peak MAE | Exit Reason |')
    print('|---|---|---|---|---|---|---|---|---|')
    for _, t in trades.iterrows():
        # Open-at-end trades have no real exit: blank the exit columns, keep
        # the held-so-far Duration (entry -> last bar) and the MTM Net PnL.
        dur_h = (t['exit'] - t['entry']).total_seconds() / 3600.0
        reason = REASON_LABELS.get(t['reason'], str(t['reason']))
        if t['reason'] == 'open_at_end':
            exit_time = '—'
            exit_price = '—'
        else:
            exit_time = str(t['exit'])
            exit_price = fmt_price(t['exit_price'])
        print(
            f"| {t['entry']} | {fmt_price(t['entry_price'])} | {exit_time} | "
            f"{exit_price} | {fmt_duration(dur_h)} | "
            f"{fmt_pct(t['pnl'] * 100)} | {fmt_pct(t['mfe'] * 100)} | "
            f"{fmt_pct(t['mae'] * 100)} | {reason} |"
        )


def print_legacy(asset: str, trades: pd.DataFrame) -> None:
    """Print the original one-line-header + LONG-row stdout (old tape format)."""
    if trades.empty:
        print('=== NO TRADES ===')
        return

    trades = trades.sort_values('entry')
    wins = trades[trades['pnl'] > 0]
    win_rate = len(wins) / len(trades) * 100
    avg_pnl = trades['pnl'].mean() * 100
    total_pnl = trades['pnl'].sum() * 100

    print(f"=== {asset} INDEPENDENT IGNITION TAPE | {len(trades)} trades | win rate {win_rate:.0f}% | avg PnL {avg_pnl:+.2f}% | total {total_pnl:+.2f}% ===")
    for _, t in trades.iterrows():
        ts_e = t['entry'].strftime('%Y-%m-%d %H:%M:%S')
        ts_x = t['exit'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"LONG {ts_e} {ts_x} {t['pnl']:.6f} {t['mfe']:.6f} {t['mae']:.6f} {t['shock']:.6f} {t['reason']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--asset', type=str, required=True)
    parser.add_argument('--data-dir', type=str, default='data/raw_shards')
    parser.add_argument('--output-format', choices=['tear', 'legacy'], default='tear',
                        help='tear = institutional markdown tear sheet, legacy = old tape stdout')
    args = parser.parse_args()

    file = Path(args.data_dir) / f"{args.asset}_USDT_1h.parquet"
    df = load_asset(file)

    try:
        metrics_file = Path('data/exotic_shards') / f"{args.asset}USDT_metrics.parquet"
        metrics = pd.read_parquet(metrics_file)
        metrics['timestamp'] = pd.to_datetime(metrics['timestamp'], unit='ms')
        metrics.set_index('timestamp', inplace=True)
        metrics = metrics.resample('1h').last().ffill()
        df = df.join(metrics[['sum_open_interest']], how='left')
        df['sum_open_interest'] = df['sum_open_interest'].ffill()
        df['oi_change'] = df['sum_open_interest'].pct_change()
    except Exception as e:
        df['oi_change'] = 0.0

    fcfg = FeatureConfig(
        shock_percentile=99.0,
        shock_mult=None,
        year_min_periods=720,
        dormant_mode='relative',
        max_notional_usd=150000.0,
        require_taker=True,
        taker_buffer=0.01,
        first_of_run=True
    )

    cfg = CtaConfig()
    feat = compute_features(df, fcfg)
    trades = run_cta(feat, cfg)

    if args.output_format == 'legacy':
        print_legacy(args.asset, trades)
    else:
        print_tear_sheet(args.asset, df, trades)


if __name__ == '__main__':
    main()




