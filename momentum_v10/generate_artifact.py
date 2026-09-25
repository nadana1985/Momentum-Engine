import pandas as pd

df = pd.read_csv("data/all_tapes/v10_production/closed_trades.csv")

# EXCLUDE OPEN TRADES
df = df[df['reason'] != 'open_at_end']

# Ensure numeric
for col in ['pnl', 'mfe', 'mae']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

total_trades = len(df)
success_df = df[df['pnl'] > 0]
fail_df = df[df['pnl'] <= 0]
win_rate = len(success_df) / total_trades * 100 if total_trades > 0 else 0
cum_pnl = df['pnl'].sum() * 100
cum_mfe = df['mfe'].sum() * 100

md = f"# V10.2 Production Tear Tape (True Verdict - Closed Book Only)\n\n"
md += f"## Global Statistics (Excluding Open Trades)\n"
md += f"- **Total Trades**: {total_trades:,}\n"
md += f"- **Win Rate**: {win_rate:.2f}%\n"
md += f"- **Cumulative PnL**: {cum_pnl:+,.1f}%\n"
md += f"- **Cumulative MFE**: {cum_mfe:+,.1f}%\n\n"

md += f"## Engine Breakdown\n\n"

engines = df['engine'].unique()
for eng in sorted([str(e) for e in engines if pd.notna(e)]):
    sub = df[df['engine'] == eng]
    t = len(sub)
    if t == 0: continue
    s = len(sub[sub['pnl'] > 0])
    f = len(sub[sub['pnl'] <= 0])
    wr = s / t * 100
    p = sub['pnl'].sum() * 100
    m = sub['mfe'].sum() * 100
    
    md += f"### {eng}\n"
    md += f"- **Total Trades**: {t:,} ({s:,} Success | {f:,} Failure)\n"
    md += f"- **Win Rate**: {wr:.2f}%\n"
    md += f"- **Cumulative PnL**: {p:+,.1f}%\n"
    md += f"- **Cumulative MFE**: {m:+,.1f}%\n\n"
    
with open("v10_2_tear_tape.md", "w") as f:
    f.write(md)
