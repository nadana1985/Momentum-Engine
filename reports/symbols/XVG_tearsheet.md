# Kronos V12: Institutional Symbol Tear Sheet — `XVG`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `16` (`16` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `16` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`62.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.144`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+46.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.59x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+2.91%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-23.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`53.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.4% / -13.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-07-06 23:00` | `2023-07-10 23:00` | Live | `$0.0075` | `$0.0081` | **+8.50%** | **+8.16%** | +4.2% | -35.8% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2023-07-31 06:00` | `2023-08-04 06:00` | Live | `$0.0047` | `$0.0051` | **+8.50%** | **+8.16%** | +1.1% | -22.6% | `shelf_target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2023-09-09 11:00` | `2023-09-13 11:00` | Live | `$0.0035` | `$0.0032` | **-8.20%** | **-8.56%** | +-2.9% | -16.3% | `shelf_stop_loss` |
| 4 | Book 3 | `2023-10-02 18:00` | `2023-10-05 18:00` | 72.0h | `$0.0035` | `$0.0033` | **-5.65%** | **-5.81%** | +4.0% | -7.3% | `time_expiry` |
| 5 | Book 3 | `2023-12-31 22:00` | `2024-01-03 12:00` | 62.0h | `$0.0039` | `$0.0036` | **-8.23%** | **-8.59%** | +6.5% | -21.5% | `stop_loss` |
| 6 | Book 5 (Shelf Absorption Squeeze) | `2024-02-25 21:00` | `2024-02-29 21:00` | Live | `$0.0054` | `$0.0058` | **+8.50%** | **+8.16%** | +36.6% | -24.2% | `shelf_target_reclaim` |
| 7 | Book 5 (Shelf Absorption Squeeze) | `2024-04-01 09:00` | `2024-04-05 09:00` | Live | `$0.0074` | `$0.0080` | **+8.50%** | **+8.16%** | +76.3% | -35.5% | `shelf_target_reclaim` |
| 8 | Book 3 | `2024-08-25 01:00` | `2024-08-27 21:00` | 68.0h | `$0.0042` | `$0.0039` | **-8.23%** | **-8.59%** | +3.1% | -10.7% | `stop_loss` |
| 9 | Book 4 | `2024-11-10 21:00` | `2024-11-13 16:00` | 67.0h | `$0.0042` | `$0.0051` | **+36.97%** | **+32.23%** | +34.0% | -2.0% | `target_reclaim` |
| 10 | Book 3 | `2025-04-27 01:00` | `2025-04-28 12:00` | 35.0h | `$0.0052` | `$0.0054` | **+4.17%** | **+4.08%** | +4.3% | -6.0% | `target_reclaim` |
| 11 | Book 3 | `2025-04-30 03:00` | `2025-05-03 03:00` | 72.0h | `$0.0054` | `$0.0053` | **-0.62%** | **-0.62%** | +4.0% | -5.2% | `time_expiry` |
| 12 | Book 3 | `2025-05-11 02:00` | `2025-05-12 04:00` | 26.0h | `$0.0062` | `$0.0065` | **+5.31%** | **+5.18%** | +7.0% | -3.0% | `target_reclaim` |
| 13 | Book 3 | `2025-07-18 10:00` | `2025-07-20 06:00` | 44.0h | `$0.0074` | `$0.0081` | **+8.66%** | **+8.30%** | +10.6% | -7.5% | `target_reclaim` |
| 14 | Book 3 | `2026-09-05 13:00` | `2026-09-08 13:00` | 72.0h | `$0.0029` | `$0.0029` | **+1.98%** | **+1.96%** | +8.3% | -4.8% | `time_expiry` |
| 15 | Book 3 | `2026-09-09 22:00` | `2026-09-09 23:00` | 1.0h | `$0.0029` | `$0.0027` | **-8.23%** | **-8.59%** | +9.1% | -11.5% | `stop_loss` |
| 16 | Book 3 | `2026-09-28 14:00` | `2026-10-01 14:00` | 72.0h | `$0.0031` | `$0.0032` | **+3.05%** | **+3.00%** | +8.8% | -2.7% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `4` | `100.0%` | **`+32.6%`** |
| `time_expiry` | `4` | `50.0%` | **`-1.5%`** |
| `target_reclaim` | `4` | `100.0%` | **`+49.8%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `XVG`

* **Total Candidate Breakouts Filtered (Vetoed):** `712`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `354` (49.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `266`
* **Saved Capital Losses Avoided:** `+4,558.8%`
* **Missed Upside Forgone:** `-11,027.6%`
* **Net Veto Alpha:** `+-6,468.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `641` | `90.0%` |
| `Core 1: Macro Bear Veto` | `31` | `4.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `31` | `4.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `9` | `1.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*