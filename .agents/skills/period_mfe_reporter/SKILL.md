---
name: period_mfe_reporter
description: Instructions and standard procedure for analyzing any historical duration window across raw OHLCV shards, extracting period Lows, Highs, exact UTC timestamps, and generating institutional MFE (Maximum Favorable Excursion) reports and CSV datasets.
---

# Period High/Low & MFE Analysis Skill

This skill teaches the AI agent how to extract period High/Low extremes and generate institutional MFE reports across any requested historical duration window using the deterministic tool [`scripts/calc_period_high_low_mfe.py`](file:///f:/kronos_v1_alt/scripts/calc_period_high_low_mfe.py).

---

## 1. When to Use This Skill
Activate this skill whenever the user asks to:
- Find the high and low of assets across a specific date range or duration window (e.g., "mar 2023 to august 2023", "Q1 2024", "Jan to Dec 2023", etc.).
- Check whether high dates occurred ahead of (after) low dates and calculate MFE.
- Screen the raw shards (`data/raw_shards/`) for multi-bagger runners, upward momentum breadth, or severe drawdown tokens during a specific historical window.
- Generate an institutional Markdown report or CSV dataset for a time window.

---

## 2. Core Quantitative Concepts & Rules

1. **Deterministic OHLCV Shard Extraction:**
   - Raw data source: `data/raw_shards/*.parquet` (1h candles with `timestamp` in epoch ms, `low`, and `high`).
   - All timestamps must be handled in UTC (`YYYY-MM-DD HH:MM:SS UTC`).

2. **Period Extremes:**
   - **Period Low:** Absolute lowest price across all candles in the window: $\min(\text{low}_t)$, along with its exact UTC timestamp $t_{\text{low}}$.
   - **Period High:** Absolute highest price across all candles in the window: $\max(\text{high}_t)$, along with its exact UTC timestamp $t_{\text{high}}$.

3. **Directional Precedence & MFE Formulation:**
   - **Upward Regime ($t_{\text{high}} > t_{\text{low}}$):**
     The asset established its cyclical low first and subsequently rallied to its period high.
     $$\text{MFE (\%)} = \frac{\text{High} - \text{Low}}{\text{Low}} \times 100$$
     $$\text{MFE Multiplier} = \frac{\text{High}}{\text{Low}}$$
     $$\text{Log Return} = \ln\left(\frac{\text{High}}{\text{Low}}\right)$$
   - **Downward / Drawdown Regime ($t_{\text{high}} < t_{\text{low}}$):**
     The asset peaked early and decayed into the period low.
     $$\text{Max Drawdown (\%)} = \frac{\text{Low} - \text{High}}{\text{High}} \times 100$$
     In this case, upward MFE from low to high is `N/A`.

---

## 3. Standard Execution Procedures

### A. Full Universe Scan & Report Generation
Whenever asked to analyze or produce a report for a duration window:
```bash
python scripts/calc_period_high_low_mfe.py --window "<START> to <END>" --report reports/mfe/mfe_report_<SLUG>.md
```
*Examples:*
```bash
# Month names
python scripts/calc_period_high_low_mfe.py --window "mar 2023 to august 2023" --report reports/mfe/mfe_report_mar_aug_2023.md

# ISO format
python scripts/calc_period_high_low_mfe.py --start "2024-01-01" --end "2024-06-30" --report reports/mfe/mfe_report_h1_2024.md
```

### B. Single Symbol Tear Sheet
To evaluate an individual token (e.g. BTC, ETH, SOL, ARPA):
```bash
python scripts/calc_period_high_low_mfe.py --symbol BTC --window "mar 2023 to august 2023"
```

---

## 4. Expected Deliverables to User
When completing a request:
1. **Report Location:** Provide a clickable markdown link to the generated report: `[mfe_report.md](file:///f:/kronos_v1_alt/reports/mfe/mfe_report_....md)`.
2. **Dataset Location:** Point to the exported CSV in `data/research/`.
3. **Executive Summary Table:**
   - Active Universe & Upward Regime % ($t_{\text{high}} > t_{\text{low}}$)
   - Median and Max MFE
   - Benchmark comparison (BTC, ETH, SOL)
   - Top 5 to 10 MFE gainers table
