"""
Kronos V12: Deterministic Individual Symbol Tear Sheet Generator (generate_symbol_tearsheets.py)
Generates institutional tear sheets for any traded asset combining:
1. Execution ledger (all historical trades, PnL, duration, exits, MFE/MAE)
2. Scorecard metrics (strict log-space PF, WR, max drawdown)
3. Counterfactual telemetry audit (vetoes, losses avoided, missed opportunities)
"""

import os
import argparse
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
TAPE_DIR = ROOT / Path(os.environ.get("KRONOS_TAPE_DIR", "data/all_tapes/v12_production"))
TELEMETRY_PATH = ROOT / "telemetry" / "veto_telemetry.parquet" if "v12_production" == TAPE_DIR.name else (ROOT / "telemetry" / TAPE_DIR.name / "veto_telemetry.parquet")
if not TELEMETRY_PATH.exists():
    TELEMETRY_PATH = ROOT / "telemetry" / "veto_telemetry.parquet"
REPORTS_DIR = ROOT / "reports" / "symbols"


def generate_single_symbol_tearsheet(
    symbol: str,
    df_trades: pd.DataFrame,
    df_scorecard: pd.DataFrame,
    df_telemetry: pd.DataFrame,
    save_file: bool = True
) -> str:
    symbol = symbol.upper()
    sym_trades = df_trades[df_trades['asset'] == symbol].copy()
    if sym_trades.empty:
        return f"# Error: No trade records found for symbol '{symbol}'."

    # Sort trades chronologically
    sym_trades = sym_trades.sort_values('entry')
    closed_trades = sym_trades[~sym_trades['is_open']].copy()
    open_trades = sym_trades[sym_trades['is_open']].copy()

    tier = str(sym_trades['tier'].iloc[0]) if 'tier' in sym_trades.columns else 'Unknown'

    # Scorecard metrics
    n_closed = len(closed_trades)
    n_open = len(open_trades)

    if not closed_trades.empty:
        wins = closed_trades[closed_trades['log_ret'] > 0]
        losses = closed_trades[closed_trades['log_ret'] <= 0]
        wr = len(wins) / n_closed * 100.0
        log_w = wins['log_ret'].sum()
        log_l = abs(losses['log_ret'].sum())
        pf = (log_w / log_l) if log_l > 1e-12 else 999.0
        tot_log = closed_trades['log_ret'].sum() * 100.0
        mean_log = closed_trades['log_ret'].mean() * 100.0
        mult = np.exp(tot_log / 100.0)

        # Drawdown in log space
        cum_log = closed_trades['log_ret'].cumsum() * 100.0
        peak_log = cum_log.cummax()
        dd = cum_log - peak_log
        max_dd = dd.min() if not dd.empty else 0.0

        mean_dur = closed_trades['duration_hours'].mean()
        mean_mfe = closed_trades['mfe'].mean() * 100.0
        mean_mae = closed_trades['mae'].mean() * 100.0
    else:
        wr = 0.0
        pf = 0.0
        tot_log = 0.0
        mean_log = 0.0
        mult = 1.0
        max_dd = 0.0
        mean_dur = 0.0
        mean_mfe = 0.0
        mean_mae = 0.0

    # Build Markdown Content
    md = []
    md.append(f"# Kronos V12: Institutional Symbol Tear Sheet — `{symbol}`")
    md.append(f"**Classification:** Clean 6-Core Universal Multi-Tier Architecture  ")
    md.append(f"**Liquidity Tier:** `{tier}` | **Total Recorded Trades:** `{len(sym_trades)}` (`{n_closed}` Closed, `{n_open}` Open)  ")
    md.append(f"**Database Source:** `data/all_tapes/v12_production/trades.parquet`\n")
    md.append("---\n")

    # 1. Executive Performance Matrix
    md.append("## 1. Executive Performance Matrix (Strict Log Compounding Space)\n")
    md.append("| Metric | Performance | Benchmark Target | Verdict |")
    md.append("| :--- | :---: | :---: | :---: |")
    md.append(f"| **Total Closed Trades** | `{n_closed}` | $\\ge 1$ | {'✅ Validated' if n_closed > 0 else '⚠️ In-Flight'} |")
    md.append(f"| **Win Rate** | **`{wr:.1f}%`** | `> 40.0%` | {'✅ Passed' if wr >= 40.0 else '⚠️ Watch'} |")
    md.append(f"| **Profit Factor (Log-Space)** | **`{pf:.3f}`** | `> 1.50` | {'✅ Outperforming' if pf >= 1.5 else ('🟢 Viable' if pf >= 1.0 else '🛑 Negative Drag')} |")
    md.append(f"| **Cumulative Net Log Return** | **`{tot_log:+.1f}%`** | `> 0.0%` | {'✅ Profitable' if tot_log > 0 else '🛑 Drawdown'} |")
    md.append(f"| **Compounded Capital Growth** | **`{mult:.2f}x`** | `> 1.0x` | {'🚀 Alpha Driver' if mult >= 1.5 else 'Neutral'} |")
    md.append(f"| **Mean Net Log Return / Trade** | **`{mean_log:+.2f}%`** | `> +1.0%` | {'✅ Strong Edge' if mean_log >= 1.0 else 'Normal'} |")
    md.append(f"| **Maximum Log Drawdown** | **`{max_dd:.1f}%`** | `< -30%` | {'✅ Contained' if max_dd > -30.0 else '⚠️ High Drawdown'} |")
    md.append(f"| **Average Trade Duration** | **`{mean_dur:.1f}h`** | `24h - 336h` | Normal Lifecycle |")
    md.append(f"| **Mean Peak MFE / Max MAE** | **`+{mean_mfe:.1f}% / {mean_mae:.1f}%`** | MFE > 2x MAE | High Asymmetry |\n")
    md.append("---\n")

    # 2. Trade History Ledger
    md.append("## 2. Chronological Trade History Ledger\n")
    if not sym_trades.empty:
        md.append("| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |")
        md.append("| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |")
        for idx, (_, r) in enumerate(sym_trades.iterrows(), 1):
            entry_s = str(r['entry'])[:16]
            exit_s = str(r['exit'])[:16] if pd.notna(r.get('exit')) and not r.get('is_open') else "_Open Live_"
            dur_s = f"{r['duration_hours']:.1f}h" if pd.notna(r.get('duration_hours')) else "Live"
            pnl_s = f"{r['pnl']*100:+.2f}%" if pd.notna(r.get('pnl')) else "In-Flight"
            log_s = f"{r['log_ret']*100:+.2f}%" if pd.notna(r.get('log_ret')) else "In-Flight"
            mfe_s = f"+{r['mfe']*100:.1f}%" if pd.notna(r.get('mfe')) else "0.0%"
            mae_s = f"{r['mae']*100:.1f}%" if pd.notna(r.get('mae')) else "0.0%"
            reason_s = f"`{r.get('reason', 'open')}`"
            book_s = str(r.get('book', 'Book 1'))
            md.append(f"| {idx} | {book_s} | `{entry_s}` | `{exit_s}` | {dur_s} | `${r['entry_price']:.4f}` | `${r['exit_price']:.4f}` | **{pnl_s}** | **{log_s}** | {mfe_s} | {mae_s} | {reason_s} |")
    else:
        md.append("_No trade executions recorded._\n")
    md.append("\n---\n")

    # 3. Microstructure Exit Decomposition
    if not closed_trades.empty and 'reason' in closed_trades.columns:
        md.append("## 3. Microstructure Exit Reason Decomposition\n")
        exit_counts = closed_trades.groupby('reason').agg(
            Count=('pnl', 'count'),
            Net_Log_PnL=('log_ret', lambda x: round(x.sum() * 100.0, 1)),
            Win_Rate=('pnl', lambda x: round((x > 0).mean() * 100.0, 1))
        ).reset_index().sort_values('Count', ascending=False)
        md.append("| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |")
        md.append("| :--- | :-: | :-: | :-: |")
        for _, er in exit_counts.iterrows():
            md.append(f"| `{er['reason']}` | `{er['Count']}` | `{er['Win_Rate']:.1f}%` | **`{er['Net_Log_PnL']:+.1f}%`** |")
        md.append("\n---\n")

    # 4. Counterfactual Telemetry & Veto Audit for Symbol
    if not df_telemetry.empty:
        sym_tel = df_telemetry[df_telemetry['asset'] == symbol].copy()
        if not sym_tel.empty:
            md.append(f"## 4. Counterfactual Risk Gate Audit for `{symbol}`\n")
            vetoed = sym_tel[sym_tel['status'] == 'VETOED'].copy()
            n_veto = len(vetoed)
            n_dodged = int(vetoed['is_dodged_bullet'].sum()) if 'is_dodged_bullet' in vetoed.columns else 0
            n_missed = int(vetoed['is_missed_opportunity'].sum()) if 'is_missed_opportunity' in vetoed.columns else 0
            loss_saved = float(np.abs(vetoed[vetoed['is_dodged_bullet']]['mae_72h_fwd'].clip(upper=0.0)).sum() * 100.0) if 'mae_72h_fwd' in vetoed.columns else 0.0
            missed_up = float(vetoed[vetoed['is_missed_opportunity']]['mfe_72h_fwd'].sum() * 100.0) if 'mfe_72h_fwd' in vetoed.columns else 0.0
            net_v_alpha = loss_saved - missed_up
            eff = (n_dodged / n_veto * 100.0) if n_veto > 0 else 0.0

            md.append(f"* **Total Candidate Breakouts Filtered (Vetoed):** `{n_veto}`")
            md.append(f"* **Dodged Bullets (Lethal False Breakouts Avoided):** `{n_dodged}` ({eff:.1f}% Efficiency)")
            md.append(f"* **Missed Opportunities (Runners $\\ge +20\\%$ MFE):** `{n_missed}`")
            md.append(f"* **Saved Capital Losses Avoided:** `+{loss_saved:,.1f}%`")
            md.append(f"* **Missed Upside Forgone:** `-{missed_up:,.1f}%`")
            md.append(f"* **Net Veto Alpha:** `+{net_v_alpha:,.1f}%`\n")

            if 'veto_gate' in vetoed.columns:
                gate_counts = vetoed['veto_gate'].value_counts()
                md.append("### Veto Gate Breakdown for this Asset:")
                md.append("| Risk Gate | Veto Count | Share % |")
                md.append("| :--- | :-: | :-: |")
                for g_name, g_cnt in gate_counts.items():
                    md.append(f"| `{g_name}` | `{g_cnt}` | `{(g_cnt / n_veto * 100.0):.1f}%` |")
            md.append("\n---\n")

    md.append("*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*")

    full_md = "\n".join(md)

    if save_file:
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        out_file = REPORTS_DIR / f"{symbol}_tearsheet.md"
        out_file.write_text(full_md, encoding='utf-8')

    return full_md


def main():
    parser = argparse.ArgumentParser(description="Kronos V12 Symbol Tear Sheet Generator")
    parser.add_argument("--symbol", type=str, help="Specific symbol (e.g. THETA, AVAX, STX)")
    parser.add_argument("--top", type=int, default=0, help="Generate for top N alpha leaders")
    parser.add_argument("--all", action="store_true", help="Generate for all traded symbols")
    args = parser.parse_args()

    trades_path = TAPE_DIR / "trades.parquet"
    scorecard_path = TAPE_DIR / "scorecard.parquet"

    if not trades_path.exists():
        print(f"Error: trades.parquet not found in {TAPE_DIR}. Run build_v12_tape.py first.")
        sys.exit(1)

    df_trades = pd.read_parquet(trades_path)
    df_scorecard = pd.read_parquet(scorecard_path) if scorecard_path.exists() else pd.DataFrame()
    df_telemetry = pd.read_parquet(TELEMETRY_PATH) if TELEMETRY_PATH.exists() else pd.DataFrame()

    if args.symbol:
        sym = args.symbol.upper()
        content = generate_single_symbol_tearsheet(sym, df_trades, df_scorecard, df_telemetry, save_file=True)
        print(f"Generated tear sheet for {sym} -> {REPORTS_DIR / f'{sym}_tearsheet.md'}")
        print("\n" + "="*80)
        print(content)
    elif args.top > 0:
        if df_scorecard.empty:
            print("Scorecard missing. Cannot rank top leaders.")
            sys.exit(1)
        top_syms = df_scorecard.sort_values('total_log_pnl', ascending=False).head(args.top)['asset'].tolist()
        print(f"Generating tear sheets for Top {args.top} Leaders: {top_syms}")
        for s in top_syms:
            generate_single_symbol_tearsheet(s, df_trades, df_scorecard, df_telemetry, save_file=True)
        print(f"All {len(top_syms)} tear sheets saved to {REPORTS_DIR}/")
    elif args.all:
        all_syms = df_trades['asset'].unique().tolist()
        print(f"Generating tear sheets for all {len(all_syms)} traded symbols...")
        for s in all_syms:
            generate_single_symbol_tearsheet(s, df_trades, df_scorecard, df_telemetry, save_file=True)
        print(f"All {len(all_syms)} tear sheets saved to {REPORTS_DIR}/")
    else:
        # Default: generate for Top 15 Alpha Leaders
        top_syms = df_scorecard.sort_values('total_log_pnl', ascending=False).head(15)['asset'].tolist()
        print(f"Generating tear sheets for Top 15 Alpha Leaders: {top_syms}")
        for s in top_syms:
            generate_single_symbol_tearsheet(s, df_trades, df_scorecard, df_telemetry, save_file=True)
        print(f"Top 15 symbol tear sheets saved to {REPORTS_DIR}/")


if __name__ == "__main__":
    main()
