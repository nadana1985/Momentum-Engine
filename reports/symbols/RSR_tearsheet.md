# Kronos V12: Institutional Symbol Tear Sheet — `RSR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `26` (`26` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `26` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`88.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`7.407`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+165.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`5.21x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+6.35%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.3% / -5.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-11 13:00` | `2021-08-20 15:00` | 218.0h | `$0.0417` | `$0.0501` | **+21.73%** | **+19.97%** | +20.3% | -12.1% | `target_reclaim` |
| 2 | Book 3 | `2022-03-31 14:00` | `2022-03-31 23:00` | 9.0h | `$0.0185` | `$0.0197` | **+6.44%** | **+6.24%** | +13.9% | -5.7% | `target_reclaim` |
| 3 | Book 3 | `2023-01-14 09:00` | `2023-01-16 01:00` | 40.0h | `$0.0038` | `$0.0040` | **+4.17%** | **+4.08%** | +4.2% | -7.6% | `target_reclaim` |
| 4 | Book 3 | `2023-01-16 08:00` | `2023-01-16 11:00` | 3.0h | `$0.0039` | `$0.0041` | **+4.17%** | **+4.08%** | +4.9% | -2.6% | `target_reclaim` |
| 5 | Book 3 | `2023-04-03 01:00` | `2023-04-04 12:00` | 35.0h | `$0.0040` | `$0.0046` | **+13.46%** | **+12.63%** | +13.7% | -1.2% | `target_reclaim` |
| 6 | Book 3 | `2023-07-02 04:00` | `2023-07-02 22:00` | 18.0h | `$0.0024` | `$0.0025` | **+4.17%** | **+4.08%** | +4.5% | -0.1% | `target_reclaim` |
| 7 | Book 3 | `2023-11-03 01:00` | `2023-11-03 14:00` | 13.0h | `$0.0021` | `$0.0022` | **+7.03%** | **+6.79%** | +7.9% | -0.2% | `target_reclaim` |
| 8 | Book 3 | `2023-11-09 16:00` | `2023-11-09 17:00` | 1.0h | `$0.0024` | `$0.0026` | **+8.70%** | **+8.34%** | +17.9% | -0.1% | `target_reclaim` |
| 9 | Book 3 | `2023-11-12 00:00` | `2023-11-14 00:00` | 48.0h | `$0.0027` | `$0.0025` | **-8.23%** | **-8.59%** | +6.8% | -9.0% | `stop_loss` |
| 10 | Book 3 | `2023-12-11 02:00` | `2023-12-11 06:00` | 4.0h | `$0.0029` | `$0.0026` | **-8.23%** | **-8.59%** | +2.6% | -13.7% | `stop_loss` |
| 11 | Book 3 | `2024-02-10 09:00` | `2024-02-13 00:00` | 63.0h | `$0.0024` | `$0.0025` | **+4.17%** | **+4.08%** | +4.4% | -4.0% | `target_reclaim` |
| 12 | Book 3 | `2024-02-20 15:00` | `2024-02-22 05:00` | 38.0h | `$0.0027` | `$0.0029` | **+7.90%** | **+7.60%** | +8.8% | -3.1% | `target_reclaim` |
| 13 | Book 3 | `2024-03-04 17:00` | `2024-03-05 13:00` | 20.0h | `$0.0041` | `$0.0045` | **+8.70%** | **+8.34%** | +11.9% | -1.4% | `target_reclaim` |
| 14 | Book 3 | `2024-03-05 19:00` | `2024-03-05 23:00` | 4.0h | `$0.0040` | `$0.0045` | **+13.14%** | **+12.35%** | +14.5% | -10.3% | `target_reclaim` |
| 15 | Book 3 | `2024-03-15 03:00` | `2024-03-15 15:00` | 12.0h | `$0.0064` | `$0.0073` | **+13.90%** | **+13.02%** | +14.6% | -2.6% | `target_reclaim` |
| 16 | Book 5 (Shelf Absorption Squeeze) | `2024-03-21 16:00` | `2024-03-25 16:00` | Live | `$0.0077` | `$0.0084` | **+8.50%** | **+8.16%** | +59.6% | -9.2% | `shelf_target_reclaim` |
| 17 | Book 3 | `2024-03-22 12:00` | `2024-03-22 17:00` | 5.0h | `$0.0077` | `$0.0084` | **+8.70%** | **+8.34%** | +9.3% | -0.4% | `target_reclaim` |
| 18 | Book 3 | `2024-05-19 11:00` | `2024-05-20 07:00` | 20.0h | `$0.0085` | `$0.0088` | **+4.17%** | **+4.08%** | +5.6% | -5.4% | `target_reclaim` |
| 19 | Book 3 | `2024-05-22 04:00` | `2024-05-23 13:00` | 33.0h | `$0.0085` | `$0.0078` | **-8.23%** | **-8.59%** | +2.4% | -9.5% | `stop_loss` |
| 20 | Book 3 | `2024-11-24 15:00` | `2024-11-24 22:00` | 7.0h | `$0.0083` | `$0.0090` | **+8.70%** | **+8.34%** | +9.9% | -2.0% | `target_reclaim` |
| 21 | Book 5 (Shelf Absorption Squeeze) | `2024-12-03 09:00` | `2024-12-07 09:00` | Live | `$0.0149` | `$0.0162` | **+8.50%** | **+8.16%** | +66.7% | -33.3% | `shelf_target_reclaim` |
| 22 | Book 3 | `2025-04-26 12:00` | `2025-04-29 06:00` | 66.0h | `$0.0090` | `$0.0096` | **+6.73%** | **+6.51%** | +6.9% | -6.1% | `target_reclaim` |
| 23 | Book 3 | `2025-07-04 08:00` | `2025-07-06 21:00` | 61.0h | `$0.0069` | `$0.0072` | **+4.59%** | **+4.49%** | +5.8% | -3.6% | `target_reclaim` |
| 24 | Book 4 | `2025-07-13 11:00` | `2025-07-17 12:00` | 97.0h | `$0.0080` | `$0.0096` | **+22.04%** | **+20.23%** | +20.1% | -5.2% | `target_reclaim` |
| 25 | Book 3 | `2025-08-14 12:00` | `2025-08-17 12:00` | 72.0h | `$0.0088` | `$0.0093` | **+5.53%** | **+5.38%** | +8.1% | -1.4% | `time_expiry` |
| 26 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0013` | `$0.0013` | **+5.71%** | **+5.55%** | +25.8% | -2.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `20` | `100.0%` | **`+169.2%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+5.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `RSR`

* **Total Candidate Breakouts Filtered (Vetoed):** `1015`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `553` (54.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `112`
* **Saved Capital Losses Avoided:** `+6,919.7%`
* **Missed Upside Forgone:** `-3,747.9%`
* **Net Veto Alpha:** `+3,171.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `465` | `45.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `266` | `26.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `130` | `12.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `86` | `8.5%` |
| `Core 1: Macro Bear Veto` | `68` | `6.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*