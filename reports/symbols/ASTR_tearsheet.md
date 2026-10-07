# Kronos V12: Institutional Symbol Tear Sheet — `ASTR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+15.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.17x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+7.72%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.0% / -2.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-04-10 10:00` | `2023-04-17 10:00` | 168.0h | `$0.0650` | `$0.0715` | **+9.90%** | **+9.44%** | +15.4% | -1.9% | `time_cap` |
| 2 | Book 2 | `2026-05-05 01:00` | `2026-05-12 01:00` | 168.0h | `$0.0087` | `$0.0093` | **+6.19%** | **+6.00%** | +12.5% | -2.1% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `100.0%` | **`+15.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `ASTR`

* **Total Candidate Breakouts Filtered (Vetoed):** `174`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `118` (67.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+1,217.3%`
* **Missed Upside Forgone:** `-115.4%`
* **Net Veto Alpha:** `+1,101.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `65` | `37.4%` |
| `Core 1: Macro Bear Veto` | `45` | `25.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `37` | `21.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `27` | `15.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*