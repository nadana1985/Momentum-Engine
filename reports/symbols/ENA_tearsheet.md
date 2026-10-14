# Kronos V12: Institutional Symbol Tear Sheet — `ENA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+146.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`4.32x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+24.39%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`25.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+27.3% / -3.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-04-03 13:00` | `2024-04-07 13:00` | Live | `$0.8574` | `$0.9303` | **+8.50%** | **+8.16%** | +63.5% | -12.6% | `shelf_target_reclaim` |
| 2 | Book 4 | `2024-11-06 22:00` | `2024-11-10 02:00` | 76.0h | `$0.4798` | `$0.5758` | **+50.48%** | **+38.44%** | +21.7% | -2.8% | `target_reclaim` |
| 3 | Book 3 | `2024-12-05 01:00` | `2024-12-05 02:00` | 1.0h | `$0.8547` | `$0.9290` | **+8.70%** | **+8.34%** | +9.5% | -0.2% | `target_reclaim` |
| 4 | Book 1 | `2025-07-10 16:00` | `2025-07-11 04:00` | 12.0h | `$0.3030` | `$0.3635` | **+34.65%** | **+30.31%** | +25.4% | -4.0% | `target_reclaim` |
| 5 | Book 4 | `2025-07-19 15:00` | `2025-07-20 09:00` | 18.0h | `$0.4078` | `$0.4894` | **+52.23%** | **+43.36%** | +21.0% | -0.7% | `target_reclaim` |
| 6 | Book 4 | `2026-08-21 05:00` | `2026-08-22 03:00` | 22.0h | `$0.1308` | `$0.1570` | **+19.12%** | **+17.74%** | +22.9% | -2.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+138.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ENA`

* **Total Candidate Breakouts Filtered (Vetoed):** `42`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `31` (73.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+390.4%`
* **Missed Upside Forgone:** `-225.1%`
* **Net Veto Alpha:** `+165.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `38` | `90.5%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `4.8%` |
| `Core 4: Funding Rate Cap` | `2` | `4.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*