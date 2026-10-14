# Kronos V12: Institutional Symbol Tear Sheet — `LISTA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `20` (`20` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `20` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.324`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+22.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.26x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.14%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-24.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`25.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.2% / -7.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-06-23 00:00` | `2024-06-27 00:00` | Live | `$0.5651` | `$0.6131` | **+8.50%** | **+8.16%** | +29.0% | -29.3% | `shelf_target_reclaim` |
| 2 | Book 3 | `2024-07-30 11:00` | `2024-07-31 00:00` | 13.0h | `$0.5789` | `$0.5313` | **-8.23%** | **-8.59%** | +3.1% | -9.0% | `stop_loss` |
| 3 | Book 2 | `2024-08-13 17:00` | `2024-08-14 13:00` | 20.0h | `$0.3928` | `$0.3605` | **-9.92%** | **-10.36%** | +2.0% | -10.1% | `initial_stop` |
| 4 | Book 3 | `2024-09-20 17:00` | `2024-09-21 01:00` | 8.0h | `$0.3540` | `$0.3698` | **+4.47%** | **+4.37%** | +5.3% | -1.3% | `target_reclaim` |
| 5 | Book 3 | `2024-10-15 05:00` | `2024-10-17 18:00` | 61.0h | `$0.4002` | `$0.3673` | **-8.23%** | **-8.59%** | +3.4% | -8.4% | `stop_loss` |
| 6 | Book 3 | `2024-11-11 05:00` | `2024-11-11 17:00` | 12.0h | `$0.3968` | `$0.4263` | **+7.42%** | **+7.16%** | +10.0% | -2.1% | `target_reclaim` |
| 7 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$0.3968` | `$0.3642` | **-8.23%** | **-8.59%** | +8.1% | -10.7% | `stop_loss` |
| 8 | Book 4 | `2024-11-26 22:00` | `2024-11-27 15:00` | 17.0h | `$0.4566` | `$0.5479` | **+21.04%** | **+19.39%** | +22.3% | -2.7% | `target_reclaim` |
| 9 | Book 5 (Shelf Absorption Squeeze) | `2025-02-10 15:00` | `2025-02-14 15:00` | Live | `$0.2312` | `$0.2508` | **+8.50%** | **+8.16%** | +34.9% | -17.2% | `shelf_target_reclaim` |
| 10 | Book 3 | `2025-02-13 16:00` | `2025-02-15 10:00` | 42.0h | `$0.2883` | `$0.2646` | **-8.23%** | **-8.59%** | +14.8% | -12.0% | `stop_loss` |
| 11 | Book 3 | `2025-04-16 08:00` | `2025-04-17 02:00` | 18.0h | `$0.1922` | `$0.1764` | **-8.23%** | **-8.59%** | +5.4% | -9.5% | `stop_loss` |
| 12 | Book 3 | `2025-05-22 10:00` | `2025-05-24 10:00` | 48.0h | `$0.2740` | `$0.2978` | **+8.70%** | **+8.34%** | +19.1% | -6.6% | `target_reclaim` |
| 13 | Book 3 | `2025-07-17 16:00` | `2025-07-18 05:00` | 13.0h | `$0.2577` | `$0.2809` | **+9.01%** | **+8.63%** | +9.3% | -0.7% | `target_reclaim` |
| 14 | Book 3 | `2025-07-23 09:00` | `2025-07-23 17:00` | 8.0h | `$0.2835` | `$0.2602` | **-8.23%** | **-8.59%** | +3.2% | -9.2% | `stop_loss` |
| 15 | Book 3 | `2025-07-24 07:00` | `2025-07-25 03:00` | 20.0h | `$0.2887` | `$0.2649` | **-8.23%** | **-8.59%** | +8.2% | -8.9% | `stop_loss` |
| 16 | Book 3 | `2025-09-19 02:00` | `2025-09-19 04:00` | 2.0h | `$0.2744` | `$0.2858` | **+4.17%** | **+4.08%** | +6.2% | -1.9% | `target_reclaim` |
| 17 | Book 3 | `2025-09-22 06:00` | `2025-09-22 18:00` | 12.0h | `$0.2843` | `$0.3073` | **+8.10%** | **+7.79%** | +9.3% | -2.8% | `target_reclaim` |
| 18 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0696` | `$0.0740` | **+6.22%** | **+6.03%** | +15.0% | -5.1% | `target_reclaim` |
| 19 | Book 3 | `2026-09-06 14:00` | `2026-09-09 14:00` | 72.0h | `$0.0778` | `$0.0795` | **+2.18%** | **+2.15%** | +4.7% | -5.7% | `time_expiry` |
| 20 | Book 3 | `2026-09-23 14:00` | `2026-09-26 14:00` | 72.0h | `$0.0795` | `$0.0870` | **+9.47%** | **+9.04%** | +11.0% | -2.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+65.8%`** |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `time_expiry` | `2` | `100.0%` | **`+11.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-10.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `LISTA`

* **Total Candidate Breakouts Filtered (Vetoed):** `644`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `368` (57.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `172`
* **Saved Capital Losses Avoided:** `+4,393.3%`
* **Missed Upside Forgone:** `-4,962.1%`
* **Net Veto Alpha:** `+-568.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `553` | `85.9%` |
| `Core 1: Macro Bear Veto` | `79` | `12.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `1.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `0.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*