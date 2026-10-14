# Kronos V12: Institutional Symbol Tear Sheet — `UNI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `21` (`21` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `21` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`52.4%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.143`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+174.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`5.72x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+8.30%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-13.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`124.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.4% / -6.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2020-12-30 17:00` | `2020-12-31 22:00` | 29.0h | `$4.3266` | `$5.1919` | **+121.83%** | **+77.71%** | +22.4% | -9.0% | `target_reclaim` |
| 2 | Book 4 | `2022-08-03 10:00` | `2022-08-10 10:00` | 168.0h | `$9.1006` | `$8.4703` | **-2.34%** | **-2.37%** | +3.2% | -11.4% | `stagnation_cut` |
| 3 | Book 1 | `2022-10-30 01:00` | `2022-11-01 01:00` | 48.0h | `$7.2581` | `$6.9715` | **-3.20%** | **-3.25%** | +1.5% | -7.8% | `fast_decay_cut` |
| 4 | Book 1 | `2023-01-12 07:00` | `2023-01-14 00:00` | 41.0h | `$6.0882` | `$6.3719` | **+8.34%** | **+8.06%** | +7.8% | -3.9% | `target_reclaim` |
| 5 | Book 4 | `2023-01-20 23:00` | `2023-02-19 22:00` | 719.0h | `$6.6800` | `$7.2591` | **+9.17%** | **+8.84%** | +14.0% | -9.0% | `time_expiry` |
| 6 | Book 2 | `2023-04-14 00:00` | `2023-04-17 00:00` | 72.0h | `$6.3779` | `$6.0897` | **-4.55%** | **-4.65%** | +2.0% | -4.4% | `stagnation_cut` |
| 7 | Book 1 | `2023-06-25 07:00` | `2023-06-28 01:00` | 66.0h | `$5.2631` | `$5.1581` | **-2.26%** | **-2.28%** | +5.5% | -2.3% | `fast_decay_cut` |
| 8 | Book 2 | `2023-07-13 16:00` | `2023-07-20 16:00` | 168.0h | `$5.6431` | `$5.9112` | **+4.76%** | **+4.65%** | +11.2% | -2.7% | `time_cap` |
| 9 | Book 2 | `2023-09-19 09:00` | `2023-09-20 21:00` | 36.0h | `$4.4701` | `$4.3631` | **-2.65%** | **-2.68%** | +0.2% | -3.8% | `stall_bailout` |
| 10 | Book 1 | `2023-11-09 06:00` | `2023-11-12 00:00` | 66.0h | `$5.3032` | `$5.2598` | **-0.65%** | **-0.65%** | +4.5% | -13.6% | `fast_decay_cut` |
| 11 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$6.2114` | `$6.2813` | **+1.12%** | **+1.12%** | +5.4% | -5.5% | `time_expiry` |
| 12 | Book 3 | `2024-02-25 03:00` | `2024-02-26 02:00` | 23.0h | `$10.4926` | `$11.4050` | **+8.70%** | **+8.34%** | +9.6% | -3.7% | `target_reclaim` |
| 13 | Book 3 | `2024-03-05 19:00` | `2024-03-06 04:00` | 9.0h | `$12.4586` | `$13.7250` | **+10.17%** | **+9.68%** | +17.8% | -10.7% | `target_reclaim` |
| 14 | Book 2 | `2024-05-15 15:00` | `2024-05-22 15:00` | 168.0h | `$7.2771` | `$9.2558` | **+28.87%** | **+25.54%** | +33.3% | -3.2% | `time_cap` |
| 15 | Book 3 | `2024-05-27 14:00` | `2024-05-28 22:00` | 32.0h | `$10.9210` | `$11.3760` | **+4.17%** | **+4.08%** | +5.6% | -2.9% | `target_reclaim` |
| 16 | Book 2 | `2024-09-13 15:00` | `2024-09-15 03:00` | 36.0h | `$7.0506` | `$6.7232` | **-4.90%** | **-5.02%** | +0.5% | -6.8% | `stall_bailout` |
| 17 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$9.2314` | `$8.4717` | **-8.23%** | **-8.59%** | +3.9% | -10.3% | `stop_loss` |
| 18 | Book 3 | `2024-12-05 22:00` | `2024-12-06 00:00` | 2.0h | `$14.5259` | `$15.7890` | **+8.70%** | **+8.34%** | +11.4% | -1.2% | `target_reclaim` |
| 19 | Book 2 | `2025-06-29 09:00` | `2025-07-01 23:00` | 62.0h | `$7.2370` | `$6.6745` | **-8.00%** | **-8.32%** | +3.7% | -9.1% | `initial_stop` |
| 20 | Book 1 | `2025-07-05 22:00` | `2025-07-21 14:00` | 376.0h | `$7.3824` | `$11.2787` | **+78.79%** | **+60.10%** | +59.2% | -5.1% | `climax_top_harvest` |
| 21 | Book 4 | `2026-07-26 15:00` | `2026-08-12 06:00` | 399.0h | `$3.9579` | `$3.5996` | **-4.17%** | **-4.27%** | +15.6% | -9.5% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+116.2%`** |
| `fast_decay_cut` | `3` | `0.0%` | **`-6.2%`** |
| `time_expiry` | `2` | `100.0%` | **`+10.0%`** |
| `stagnation_cut` | `2` | `0.0%` | **`-7.0%`** |
| `time_cap` | `2` | `100.0%` | **`+30.2%`** |
| `stall_bailout` | `2` | `0.0%` | **`-7.7%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+60.1%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.3%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `structural_stop` | `1` | `0.0%` | **`-4.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `UNI`

* **Total Candidate Breakouts Filtered (Vetoed):** `977`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `626` (64.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `230`
* **Saved Capital Losses Avoided:** `+7,987.9%`
* **Missed Upside Forgone:** `-7,856.3%`
* **Net Veto Alpha:** `+131.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `504` | `51.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `451` | `46.2%` |
| `Core 4: Funding Rate Cap` | `13` | `1.3%` |
| `Core 4: Whale Firewall` | `8` | `0.8%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*