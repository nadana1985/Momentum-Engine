"""
Kronos V12: Parquet/CSV Ledger Splitter in Strict Compounding Log Space (build_csv.py)
Eliminates arithmetic percentage addition illusions permanently.
Calculates net log returns, compounding capital multiples, and precomputes scorecard.parquet.

AUDIT FIXES:
  CRITICAL-3: Profit Factor now computed in log-return space (not arithmetic pnl sums).
  HIGH-6:     UTC timezone handled robustly — tz-naive timestamps throughout.
  MEDIUM-3:   Preserves entry_oi_usd column if present.
  MEDIUM-8:   Adds trade_type column for Reclaim / Continuation / Standard filter.
"""

import os
import sys
from pathlib import Path
import numpy as np
import pandas as pd
ROOT = Path(__file__).resolve().parent.parent
tape_dir_env = os.environ.get("KRONOS_TAPE_DIR", "data/all_tapes/v12_production")
raw_tape_dir = Path(tape_dir_env)
if raw_tape_dir.is_absolute():
    TAPE_DIR = raw_tape_dir
elif (ROOT / raw_tape_dir).exists():
    TAPE_DIR = ROOT / raw_tape_dir
elif raw_tape_dir.exists():
    TAPE_DIR = raw_tape_dir
else:
    TAPE_DIR = ROOT / raw_tape_dir
RAW_CSV = TAPE_DIR / "master_raw_tape.csv"
TRADES_PARQUET = TAPE_DIR / "trades.parquet"
CLOSED_CSV = TAPE_DIR / "closed_trades.csv"
CLOSED_PARQUET = TAPE_DIR / "closed_trades.parquet"
OPEN_CSV = TAPE_DIR / "open_trades.csv"
OPEN_PARQUET = TAPE_DIR / "open_trades.parquet"
ALL_CSV = TAPE_DIR / "all_trades.csv"
SCORECARD_PARQUET = TAPE_DIR / "scorecard.parquet"
SCORECARD_CSV = TAPE_DIR / "scorecard.csv"
SYMBOLS_DIR = TAPE_DIR / "symbols"


def _log_pf(wins: pd.Series, losses: pd.Series) -> float:
    """
    CRITICAL-3 FIX: Profit Factor in strict log-return space.
    PF = sum(positive log_ret) / abs(sum(negative log_ret))
    This is the only mathematically consistent PF in a compounding system.
    Arithmetic PF sums (pnl %) were deprecated in AGENTS.md (V6-V8 audit).
    """
    log_wins  = wins['log_ret'].clip(lower=0.0).sum()
    log_losses = abs(losses['log_ret'].clip(upper=0.0).sum())
    return (log_wins / log_losses) if log_losses > 1e-12 else 999.0


def main():
    if not TRADES_PARQUET.exists() and not RAW_CSV.exists():
        print(f"No trades found in {TAPE_DIR}. Run build_v12_tape.py first.")
        return

    if TRADES_PARQUET.exists():
        df = pd.read_parquet(TRADES_PARQUET)
    else:
        df = pd.read_csv(RAW_CSV)

    if df.empty:
        print("Trades dataset is empty.")
        return

    # Normalize numeric columns
    for num_col in ['pnl', 'log_ret', 'mfe', 'mae', 'entry_price', 'exit_price',
                    'stop_price', 'duration_hours', 'entry_oi_usd']:
        if num_col in df.columns:
            df[num_col] = pd.to_numeric(df[num_col], errors='coerce')

    # Status column
    df['status'] = np.where(df['reason'] == 'open_at_end', 'OPEN', 'CLOSED')
    df['is_open'] = df['status'] == 'OPEN'

    # MEDIUM-8: Trade type label for dashboard filtering
    def _trade_type(row):
        if row.get('is_book3', False) or str(row.get('book', '')).startswith('Book 3'):
            return 'Flush Reclaim'
        if row.get('is_reclaim', False):
            return 'Bear-Trap Reclaim'
        if row.get('is_continuation', False):
            return 'Continuation'
        if str(row.get('book', '')).startswith('Book 2'):
            return 'Squeeze Hunter'
        return 'Standard Breakout'
    df['trade_type'] = df.apply(_trade_type, axis=1)

    # Strict Log Compounding Metrics
    if 'log_ret' not in df.columns or df['log_ret'].isna().all():
        df['log_ret'] = np.log(np.maximum(1e-6, 1.0 + df['pnl']))

    df['log_ret_pct'] = df['log_ret'] * 100.0
    df['pnl_pct'] = df['pnl'] * 100.0
    df['mfe_pct'] = df['mfe'] * 100.0
    df['mae_pct'] = df['mae'] * 100.0

    # HIGH-6 FIX: Robust tz-naive datetime handling throughout
    # Always strip timezone info to keep arithmetic consistent
    def _parse_dt_naive(series: pd.Series) -> pd.Series:
        parsed = pd.to_datetime(series.astype(str).str.replace('T', ' '), errors='coerce')
        if parsed.dt.tz is not None:
            parsed = parsed.dt.tz_localize(None)
        return parsed

    df['entry'] = df['entry'].astype(str).str.replace('T', ' ')
    df['entry_dt'] = _parse_dt_naive(df['entry'])

    if 'exit' in df.columns:
        df['exit'] = df['exit'].astype(str).str.replace('T', ' ')
        df['exit_dt'] = _parse_dt_naive(df['exit'])
    else:
        df['exit_dt'] = pd.NaT

    # HIGH-6 FIX: Use tz-naive UTC now for open trade duration
    now_naive = pd.Timestamp.utcnow().replace(tzinfo=None)
    open_mask = df['status'] == 'OPEN'
    if open_mask.any():
        entry_naive = _parse_dt_naive(df.loc[open_mask, 'entry'])
        df.loc[open_mask, 'duration_hours'] = (now_naive - entry_naive).dt.total_seconds() / 3600.0

    df['duration'] = df['duration_hours'].apply(lambda h: f"{int(h)}h" if pd.notna(h) else "")

    # Save Cleaned Trades Parquet & All Trades CSV
    df = df.sort_values(['asset', 'entry_dt']).reset_index(drop=True)
    df.to_parquet(TRADES_PARQUET, index=False)
    df.to_csv(ALL_CSV, index=False)

    # Split Open & Closed
    open_df = df[df['status'] == 'OPEN'].copy()
    open_df.to_csv(OPEN_CSV, index=False)
    open_df.to_parquet(OPEN_PARQUET, index=False)

    closed_df = df[df['status'] == 'CLOSED'].copy()
    closed_df.to_csv(CLOSED_CSV, index=False)
    closed_df.to_parquet(CLOSED_PARQUET, index=False)

    # -----------------------------------------------------------------------
    # ALL BOOKS EXPORT & MULTI-BOOK ATTRIBUTION LEDGERS (For Dashboard & Analysis)
    # -----------------------------------------------------------------------
    ALL_BOOKS_CSV = TAPE_DIR / "all_books.csv"
    df.to_csv(ALL_BOOKS_CSV, index=False)

    # Individual book exports (Book 1, Book 2, Book 3)
    for b in ['Book 1', 'Book 2', 'Book 3']:
        b_slug = b.lower().replace(' ', '')
        b_df = df[df['book'] == b].copy()
        b_df.to_csv(TAPE_DIR / f"{b_slug}_trades.csv", index=False)
        b_df[b_df['status'] == 'CLOSED'].to_csv(TAPE_DIR / f"{b_slug}_closed.csv", index=False)
        b_df[b_df['status'] == 'OPEN'].to_csv(TAPE_DIR / f"{b_slug}_open.csv", index=False)

    # Summary table across books
    books_summary_rows = []
    for b in ['Book 1', 'Book 2', 'Book 3']:
        b_closed = closed_df[closed_df['book'] == b]
        b_open = open_df[open_df['book'] == b]
        n_closed = len(b_closed)
        if n_closed > 0:
            b_wins = b_closed[b_closed['log_ret'] > 0]
            b_losses = b_closed[b_closed['log_ret'] <= 0]
            b_wr = len(b_wins) / n_closed * 100.0
            b_log_pf = _log_pf(b_wins, b_losses)
            pos_pnl = b_wins['pnl'].sum()
            neg_pnl = abs(b_losses['pnl'].sum())
            b_pnl_pf = (pos_pnl / neg_pnl) if neg_pnl > 1e-12 else 999.0
            tot_log = b_closed['log_ret'].sum() * 100.0
            mean_log = b_closed['log_ret'].mean() * 100.0
            mult = float(np.exp(tot_log / 100.0))
        else:
            b_wr, b_log_pf, b_pnl_pf, tot_log, mean_log, mult = 0.0, 0.0, 0.0, 0.0, 0.0, 1.0

        books_summary_rows.append({
            'book': b,
            'name': 'Continuation Breakout' if b == 'Book 1' else ('Coiled Squeeze' if b == 'Book 2' else 'Bull Flush Reclaim'),
            'closed_trades': n_closed,
            'open_trades': len(b_open),
            'total_trades': n_closed + len(b_open),
            'win_rate_pct': round(b_wr, 2),
            'log_profit_factor': round(b_log_pf, 3),
            'pnl_profit_factor': round(b_pnl_pf, 3),
            'net_log_pnl_pct': round(tot_log, 1),
            'capital_multiple': round(mult, 2),
            'mean_log_ret_pct': round(mean_log, 2),
        })

    # Portfolio Total Row
    tot_wins = closed_df[closed_df['log_ret'] > 0]
    tot_losses = closed_df[closed_df['log_ret'] <= 0]
    tot_wr = len(tot_wins) / len(closed_df) * 100.0 if len(closed_df) > 0 else 0.0
    tot_log_pf = _log_pf(tot_wins, tot_losses)
    pos_pnl = tot_wins['pnl'].sum()
    neg_pnl = abs(tot_losses['pnl'].sum())
    tot_pnl_pf = (pos_pnl / neg_pnl) if neg_pnl > 1e-12 else 999.0
    tot_log_sum = closed_df['log_ret'].sum() * 100.0
    tot_mean_log = closed_df['log_ret'].mean() * 100.0
    tot_mult = float(np.exp(tot_log_sum / 100.0))

    books_summary_rows.append({
        'book': 'All Books',
        'name': 'Unified V12.2 Portfolio',
        'closed_trades': len(closed_df),
        'open_trades': len(open_df),
        'total_trades': len(df),
        'win_rate_pct': round(tot_wr, 2),
        'log_profit_factor': round(tot_log_pf, 3),
        'pnl_profit_factor': round(tot_pnl_pf, 3),
        'net_log_pnl_pct': round(tot_log_sum, 1),
        'capital_multiple': round(tot_mult, 2),
        'mean_log_ret_pct': round(tot_mean_log, 2),
    })

    books_summary_df = pd.DataFrame(books_summary_rows)
    books_summary_df.to_csv(TAPE_DIR / "books_summary.csv", index=False)

    # Precompute Strict Log Scorecard & Export Per-Symbol CSVs
    SYMBOLS_DIR.mkdir(parents=True, exist_ok=True)
    scorecards = []
    for asset, grp in df.groupby('asset'):
        # Export individual symbol trades
        asset_file = SYMBOLS_DIR / f"{asset}_trades.csv"
        grp.to_csv(asset_file, index=False)

        closed_grp = grp[grp['status'] == 'CLOSED']
        tot_closed = len(closed_grp)
        tot_all = len(grp)
        tier = grp['tier'].iloc[0] if 'tier' in grp.columns else "Tier 1"

        if tot_closed > 0:
            win_mask  = closed_grp['log_ret'] > 0
            loss_mask = closed_grp['log_ret'] <= 0
            wins   = closed_grp[win_mask]
            losses = closed_grp[loss_mask]

            win_rate = (len(wins) / tot_closed * 100.0)

            # CRITICAL-3 FIX: Profit Factor in log-return space
            pf = _log_pf(wins, losses)

            tot_log  = closed_grp['log_ret'].sum() * 100.0
            mean_log = closed_grp['log_ret'].mean() * 100.0
            multiple = np.exp(tot_log / 100.0)

            # Peak-to-trough drawdown in log compounding space
            cum_log = closed_grp['log_ret'].cumsum()
            max_log_dd = ((cum_log - cum_log.cummax()).min() * 100.0) if not cum_log.empty else 0.0

            # MFE / MAE cumulative
            mfe_mean = closed_grp['mfe'].mean() * 100.0
            mae_mean = closed_grp['mae'].mean() * 100.0
            mfe_p90  = float(np.percentile(closed_grp['mfe'].fillna(0) * 100.0, 90))
            mae_p90  = float(np.percentile(closed_grp['mae'].fillna(0) * 100.0, 10))  # worst 10%

            dur_mean = closed_grp['duration_hours'].mean() if 'duration_hours' in closed_grp else 0.0
        else:
            win_rate = pf = tot_log = mean_log = 0.0
            multiple = 1.0
            max_log_dd = mfe_mean = mae_mean = mfe_p90 = mae_p90 = dur_mean = 0.0

        scorecards.append({
            'asset':          asset,
            'tier':           tier,
            'total_trades':   tot_all,
            'closed_trades':  tot_closed,
            'win_rate':       round(win_rate, 2),
            'profit_factor':  round(pf, 3),          # CRITICAL-3: log-space PF
            'total_log_pnl':  round(tot_log, 2),
            'mean_log_pnl':   round(mean_log, 3),    # MEDIUM-4: edge per trade
            'capital_multiple': round(multiple, 3),
            'max_log_drawdown': round(max_log_dd, 2),
            'mfe_mean_pct':   round(mfe_mean, 2),
            'mae_mean_pct':   round(mae_mean, 2),
            'mfe_p90_pct':    round(mfe_p90, 2),     # 90th percentile MFE
            'mae_p10_pct':    round(mae_p90, 2),     # worst 10% MAE
            'dur_mean_hours': round(float(dur_mean), 1),
        })

    df_sc = pd.DataFrame(scorecards).sort_values('total_log_pnl', ascending=False).reset_index(drop=True)
    df_sc.to_parquet(SCORECARD_PARQUET, index=False)
    df_sc.to_csv(SCORECARD_CSV, index=False)

    print(f"  [build_csv] Successfully exported {len(closed_df)} closed, {len(open_df)} open trades.")
    print(f"  [build_csv] Precomputed {len(df_sc)} ticker scorecards in strict log-compounding space (PF = log-space).")
    print(f"  [build_csv] Exported individual symbol CSV files to: {SYMBOLS_DIR}/")

    if not df_sc.empty:
        print("\n  === TOP 5 ALPHA LEADERS (Log-Space PF) ===")
        for _, row in df_sc.head(5).iterrows():
            print(f"    - {row['asset']:<10} ({row['tier']}): {int(row['closed_trades'])} trades | "
                  f"WR: {row['win_rate']:5.1f}% | Log PF: {row['profit_factor']:.3f} | "
                  f"Mean Edge: {row['mean_log_pnl']:+.2f}%/trade | Log PnL: {row['total_log_pnl']:+6.1f}% | "
                  f"Mult: {row['capital_multiple']:.2f}x")

        print("\n  === BOTTOM 5 DRAG LAGGARDS ===")
        for _, row in df_sc.tail(5).iterrows():
            print(f"    - {row['asset']:<10} ({row['tier']}): {int(row['closed_trades'])} trades | "
                  f"WR: {row['win_rate']:5.1f}% | Log PF: {row['profit_factor']:.3f} | "
                  f"Mean Edge: {row['mean_log_pnl']:+.2f}%/trade | Log PnL: {row['total_log_pnl']:+6.1f}% | "
                  f"Max DD: {row['max_log_drawdown']:.1f}%")


if __name__ == "__main__":
    main()
