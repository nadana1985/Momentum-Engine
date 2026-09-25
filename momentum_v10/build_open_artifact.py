import pandas as pd

open_df = pd.read_csv("data/all_tapes/v10_production/open_trades.csv")
if "pnl_pct" not in open_df.columns and "pnl" in open_df.columns:
    open_df["pnl_pct"] = pd.to_numeric(open_df["pnl"], errors="coerce") * 100.0
if "mfe_pct" not in open_df.columns and "mfe" in open_df.columns:
    open_df["mfe_pct"] = pd.to_numeric(open_df["mfe"], errors="coerce") * 100.0
if "exit_price" not in open_df.columns and {"entry_price", "pnl"}.issubset(open_df.columns):
    open_df["exit_price"] = pd.to_numeric(open_df["entry_price"], errors="coerce") * (
        1.0 + pd.to_numeric(open_df["pnl"], errors="coerce")
    )
if "duration_hours" not in open_df.columns:
    open_df["duration_hours"] = float("nan")

total_open = len(open_df)
avg_pnl = open_df["pnl_pct"].mean()
median_pnl = open_df["pnl_pct"].median()
cum_pnl = open_df["pnl_pct"].sum()

md = f"# V10 Production Open Trades Report\n\n"
md += f"## Portfolio Summary\n"
md += f"- **Total Open Trades**: {total_open:,}\n"
md += f"- **Mean Open PnL**: {avg_pnl:+.2f}%\n"
md += f"- **Median Open PnL**: {median_pnl:+.2f}%\n"
md += f"- **Cumulative Unrealized PnL**: {cum_pnl:+,.1f}%\n\n"

md += f"## Engine Distribution\n\n"
eng_counts = open_df['engine'].value_counts()
for eng, count in eng_counts.items():
    eng_pnl = open_df[open_df['engine'] == eng]['pnl_pct'].sum()
    md += f"- `{eng}`: {count} open trades (Cum PnL: {eng_pnl:+,.1f}%)\n"

md += f"\n---\n\n## Top Active Open Positions\n\n"
top_50 = open_df.sort_values(by='pnl_pct', ascending=False).head(50)

md += "| Asset | Engine | Entry Time | Entry Px | Current Px | Duration (h) | MFE % | Current PnL % |\n"
md += "|---|---|---|---|---|---|---|---|\n"

for _, r in top_50.iterrows():
    duration = r["duration_hours"]
    duration_txt = f"{duration:.0f}h" if pd.notna(duration) else "—"
    exit_px = r["exit_price"]
    exit_txt = f"{exit_px:.6g}" if pd.notna(exit_px) else "—"
    md += (
        f"| **{r['asset']}** | {r['engine']} | {r['entry']} | {r['entry_price']:.6g} | "
        f"{exit_txt} | {duration_txt} | +{r['mfe_pct']:.1f}% | **{r['pnl_pct']:+.2f}%** |\n"
    )

with open("v10_open_trades.md", "w") as f:
    f.write(md)

print("v10_open_trades.md generated successfully!")
