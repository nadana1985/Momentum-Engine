# Kronos V12: Institutional Symbol Tear Sheet — `AERO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`85.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.871`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+95.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.60x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+13.67%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-19.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`129.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+23.4% / -5.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-04-22 15:00` | `2025-04-29 15:00` | 168.0h | `$0.4278` | `$0.6181` | **+54.76%** | **+45.30%** | +55.5% | -1.6% | `time_cap` |
| 2 | Book 3 | `2025-06-17 11:00` | `2025-06-17 19:00` | 8.0h | `$0.7443` | `$0.7806` | **+4.88%** | **+4.76%** | +6.0% | -6.6% | `target_reclaim` |
| 3 | Book 4 | `2025-06-18 21:00` | `2025-06-21 23:00` | 74.0h | `$0.8717` | `$0.7409` | **-18.12%** | **-19.64%** | +10.5% | -15.6% | `structural_stop` |
| 4 | Book 2 | `2025-07-09 19:00` | `2025-07-16 19:00` | 168.0h | `$0.7480` | `$0.9868` | **+34.16%** | **+29.65%** | +33.4% | -3.9% | `time_cap` |
| 5 | Book 3 | `2025-08-10 03:00` | `2025-08-10 14:00` | 11.0h | `$1.1178` | `$1.2150` | **+8.70%** | **+8.34%** | +13.7% | -0.7% | `target_reclaim` |
| 6 | Book 4 | `2026-06-19 15:00` | `2026-06-23 03:00` | 84.0h | `$0.4802` | `$0.5763` | **+5.22%** | **+5.09%** | +20.4% | -1.9% | `target_reclaim` |
| 7 | Book 4 | `2026-08-22 05:00` | `2026-09-07 15:00` | 394.0h | `$0.4768` | `$0.5722` | **+25.35%** | **+22.18%** | +24.5% | -7.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+40.4%`** |
| `time_cap` | `2` | `100.0%` | **`+74.9%`** |
| `structural_stop` | `1` | `0.0%` | **`-19.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `AERO`

* **Total Candidate Breakouts Filtered (Vetoed):** `293`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `235` (80.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `14`
* **Saved Capital Losses Avoided:** `+3,050.3%`
* **Missed Upside Forgone:** `-318.0%`
* **Net Veto Alpha:** `+2,732.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `287` | `98.0%` |
| `Core 4: Defensible Whale Dump` | `3` | `1.0%` |
| `Core 4: Funding Rate Cap` | `2` | `0.7%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*