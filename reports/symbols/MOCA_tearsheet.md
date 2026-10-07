# Kronos V12: Institutional Symbol Tear Sheet — `MOCA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+25.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.29x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+25.62%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`153.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+38.3% / -2.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-04-22 14:00` | `2025-04-28 23:00` | 153.0h | `$0.0806` | `$0.1041` | **+29.20%** | **+25.62%** | +38.3% | -2.5% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+25.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `MOCA`

* **Total Candidate Breakouts Filtered (Vetoed):** `43`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (79.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+383.7%`
* **Missed Upside Forgone:** `-67.6%`
* **Net Veto Alpha:** `+316.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `22` | `51.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `16` | `37.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `5` | `11.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*