# Kronos V12: Institutional Symbol Tear Sheet — `CTSI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `28` (`28` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `28` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.179`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+143.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`4.19x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+5.12%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-15.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`55.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.7% / -8.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-01-21 10:00` | `2023-01-22 05:00` | 19.0h | `$0.1304` | `$0.1358` | **+4.17%** | **+4.08%** | +6.5% | -1.3% | `target_reclaim` |
| 2 | Book 4 | `2023-01-28 05:00` | `2023-02-04 05:00` | 168.0h | `$0.1591` | `$0.1581` | **-0.33%** | **-0.33%** | +3.2% | -12.3% | `stagnation_cut` |
| 3 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.1311` | `$0.1526` | **+18.08%** | **+16.74%** | +21.4% | -4.0% | `time_cap` |
| 4 | Book 3 | `2023-04-17 10:00` | `2023-04-18 14:00` | 28.0h | `$0.2356` | `$0.2701` | **+14.63%** | **+13.66%** | +15.3% | -3.2% | `target_reclaim` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2023-05-01 01:00` | `2023-05-05 01:00` | Live | `$0.2156` | `$0.2339` | **+8.50%** | **+8.16%** | +0.3% | -33.1% | `shelf_target_reclaim` |
| 6 | Book 5 (Shelf Absorption Squeeze) | `2023-05-17 12:00` | `2023-05-21 12:00` | Live | `$0.1734` | `$0.1882` | **+8.50%** | **+8.16%** | +7.6% | -11.7% | `shelf_target_reclaim` |
| 7 | Book 3 | `2023-07-05 10:00` | `2023-07-08 10:00` | 72.0h | `$0.1530` | `$0.1516` | **-0.90%** | **-0.90%** | +4.9% | -5.0% | `time_expiry` |
| 8 | Book 5 (Shelf Absorption Squeeze) | `2023-07-10 15:00` | `2023-07-14 15:00` | Live | `$0.1474` | `$0.1599` | **+8.50%** | **+8.16%** | +7.6% | -12.0% | `shelf_target_reclaim` |
| 9 | Book 3 | `2023-07-13 04:00` | `2023-07-13 18:00` | 14.0h | `$0.1541` | `$0.1675` | **+8.70%** | **+8.34%** | +9.4% | -0.0% | `target_reclaim` |
| 10 | Book 4 | `2023-10-24 22:00` | `2023-11-05 06:00` | 272.0h | `$0.1442` | `$0.1731` | **+11.58%** | **+11.05%** | +23.8% | -2.9% | `target_reclaim` |
| 11 | Book 3 | `2023-12-11 02:00` | `2023-12-12 03:00` | 25.0h | `$0.1604` | `$0.1696` | **+5.72%** | **+5.56%** | +7.8% | -8.7% | `target_reclaim` |
| 12 | Book 3 | `2023-12-13 06:00` | `2023-12-16 06:00` | 72.0h | `$0.1601` | `$0.1722` | **+7.57%** | **+7.29%** | +12.8% | -0.9% | `time_expiry` |
| 13 | Book 3 | `2023-12-29 22:00` | `2024-01-01 22:00` | 72.0h | `$0.2143` | `$0.2196` | **+2.51%** | **+2.48%** | +3.7% | -3.6% | `time_expiry` |
| 14 | Book 3 | `2024-01-06 00:00` | `2024-01-06 06:00` | 6.0h | `$0.2232` | `$0.2048` | **-8.23%** | **-8.59%** | +3.7% | -9.8% | `stop_loss` |
| 15 | Book 5 (Shelf Absorption Squeeze) | `2024-01-21 14:00` | `2024-01-25 14:00` | Live | `$0.2260` | `$0.2452` | **+8.50%** | **+8.16%** | +8.3% | -20.8% | `shelf_target_reclaim` |
| 16 | Book 3 | `2024-02-11 20:00` | `2024-02-13 15:00` | 43.0h | `$0.2758` | `$0.3173` | **+15.03%** | **+14.00%** | +16.3% | -0.5% | `target_reclaim` |
| 17 | Book 3 | `2024-02-27 03:00` | `2024-02-28 09:00` | 30.0h | `$0.3466` | `$0.3767` | **+8.70%** | **+8.34%** | +11.3% | -1.2% | `target_reclaim` |
| 18 | Book 3 | `2024-02-28 17:00` | `2024-02-28 18:00` | 1.0h | `$0.3775` | `$0.4103` | **+8.70%** | **+8.34%** | +22.7% | -1.9% | `target_reclaim` |
| 19 | Book 3 | `2024-05-23 20:00` | `2024-05-24 03:00` | 7.0h | `$0.1968` | `$0.2126` | **+8.04%** | **+7.74%** | +8.1% | -2.7% | `target_reclaim` |
| 20 | Book 2 | `2024-08-09 08:00` | `2024-08-11 08:00` | 48.0h | `$0.1339` | `$0.1333` | **-0.59%** | **-0.59%** | +2.3% | -4.8% | `fast_decay_cut` |
| 21 | Book 3 | `2024-11-20 18:00` | `2024-11-22 23:00` | 53.0h | `$0.1450` | `$0.1629` | **+12.35%** | **+11.64%** | +13.9% | -2.8% | `target_reclaim` |
| 22 | Book 3 | `2025-07-18 20:00` | `2025-07-20 08:00` | 36.0h | `$0.0743` | `$0.0780` | **+4.94%** | **+4.82%** | +5.6% | -1.1% | `target_reclaim` |
| 23 | Book 3 | `2025-08-14 09:00` | `2025-08-14 16:00` | 7.0h | `$0.0743` | `$0.0682` | **-8.23%** | **-8.59%** | +1.4% | -9.3% | `stop_loss` |
| 24 | Book 4 | `2025-08-16 10:00` | `2025-08-16 14:00` | 4.0h | `$0.0884` | `$0.1061` | **+4.82%** | **+4.61%** | +31.7% | -2.4% | `target_reclaim` |
| 25 | Book 5 (Shelf Absorption Squeeze) | `2025-08-16 11:00` | `2025-08-20 11:00` | Live | `$0.0900` | `$0.0976` | **+8.50%** | **+8.16%** | +5.6% | -27.0% | `shelf_target_reclaim` |
| 26 | Book 5 (Shelf Absorption Squeeze) | `2026-04-02 15:00` | `2026-04-06 15:00` | Live | `$0.0412` | `$0.0447` | **+8.50%** | **+8.16%** | +7.1% | -36.2% | `shelf_target_reclaim` |
| 27 | Book 3 | `2026-09-13 14:00` | `2026-09-16 14:00` | 72.0h | `$0.0252` | `$0.0236` | **-6.49%** | **-6.71%** | +7.7% | -7.1% | `time_expiry` |
| 28 | Book 3 | `2026-10-08 15:00` | `2026-10-08 16:00` | 1.0h | `$0.0340` | `$0.0312` | **-8.23%** | **-8.59%** | +3.0% | -8.6% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `12` | `100.0%` | **`+102.2%`** |
| `shelf_target_reclaim` | `6` | `100.0%` | **`+48.9%`** |
| `time_expiry` | `4` | `50.0%` | **`+2.2%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.6%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-0.3%`** |
| `time_cap` | `1` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `CTSI`

* **Total Candidate Breakouts Filtered (Vetoed):** `467`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `379` (81.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `33`
* **Saved Capital Losses Avoided:** `+4,424.3%`
* **Missed Upside Forgone:** `-1,576.4%`
* **Net Veto Alpha:** `+2,847.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `194` | `41.5%` |
| `Core 1: Macro Bear Veto` | `192` | `41.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `49` | `10.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `22` | `4.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `7` | `1.5%` |
| `Core 4: Defensible Whale Dump` | `3` | `0.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*