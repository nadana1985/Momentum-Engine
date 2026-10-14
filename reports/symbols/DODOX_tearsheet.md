# Kronos V12: Institutional Symbol Tear Sheet — `DODOX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `20` (`20` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `20` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.446`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+118.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`3.27x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+5.92%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`39.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.5% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-10-02 18:00` | `2023-10-03 09:00` | 15.0h | `$0.0989` | `$0.1031` | **+4.17%** | **+4.08%** | +6.1% | -1.8% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2023-10-03 23:00` | `2023-10-07 23:00` | Live | `$0.1005` | `$0.1091` | **+8.50%** | **+8.16%** | +2.6% | -17.7% | `shelf_target_reclaim` |
| 3 | Book 3 | `2023-10-05 16:00` | `2023-10-06 21:00` | 29.0h | `$0.1024` | `$0.1090` | **+6.51%** | **+6.31%** | +7.1% | -1.7% | `target_reclaim` |
| 4 | Book 3 | `2023-10-31 15:00` | `2023-11-01 20:00` | 29.0h | `$0.1095` | `$0.1143` | **+4.40%** | **+4.31%** | +4.6% | -4.5% | `target_reclaim` |
| 5 | Book 3 | `2023-12-05 18:00` | `2023-12-06 01:00` | 7.0h | `$0.1562` | `$0.1697` | **+8.70%** | **+8.34%** | +10.8% | -1.4% | `target_reclaim` |
| 6 | Book 3 | `2023-12-26 17:00` | `2023-12-27 01:00` | 8.0h | `$0.2168` | `$0.2356` | **+8.70%** | **+8.34%** | +9.9% | -2.8% | `target_reclaim` |
| 7 | Book 3 | `2024-02-28 17:00` | `2024-02-29 01:00` | 8.0h | `$0.2011` | `$0.2308` | **+14.74%** | **+13.75%** | +17.4% | -2.0% | `target_reclaim` |
| 8 | Book 3 | `2024-03-03 07:00` | `2024-03-05 02:00` | 43.0h | `$0.2323` | `$0.2595` | **+11.70%** | **+11.07%** | +12.5% | -0.7% | `target_reclaim` |
| 9 | Book 3 | `2024-07-23 04:00` | `2024-07-26 04:00` | 72.0h | `$0.1205` | `$0.1246` | **+3.43%** | **+3.37%** | +4.6% | -7.1% | `time_expiry` |
| 10 | Book 3 | `2024-07-30 00:00` | `2024-07-30 05:00` | 5.0h | `$0.1276` | `$0.1370` | **+7.32%** | **+7.07%** | +8.0% | -1.0% | `target_reclaim` |
| 11 | Book 3 | `2024-07-30 15:00` | `2024-08-01 15:00` | 48.0h | `$0.1317` | `$0.1209` | **-8.23%** | **-8.59%** | +7.4% | -8.7% | `stop_loss` |
| 12 | Book 3 | `2024-11-12 10:00` | `2024-11-15 10:00` | 72.0h | `$0.1214` | `$0.1204` | **-0.86%** | **-0.86%** | +5.3% | -8.0% | `time_expiry` |
| 13 | Book 4 | `2024-11-18 23:00` | `2024-11-27 22:00` | 215.0h | `$0.1328` | `$0.1593` | **+43.05%** | **+36.79%** | +20.1% | -14.4% | `target_reclaim` |
| 14 | Book 3 | `2024-11-28 10:00` | `2024-11-30 05:00` | 43.0h | `$0.1527` | `$0.1591` | **+4.17%** | **+4.08%** | +4.5% | -2.3% | `target_reclaim` |
| 15 | Book 3 | `2024-12-03 14:00` | `2024-12-03 16:00` | 2.0h | `$0.1686` | `$0.1832` | **+8.70%** | **+8.34%** | +9.0% | -0.4% | `target_reclaim` |
| 16 | Book 3 | `2025-02-13 11:00` | `2025-02-14 11:00` | 24.0h | `$0.1054` | `$0.0967` | **-8.23%** | **-8.59%** | +2.9% | -8.1% | `stop_loss` |
| 17 | Book 3 | `2025-05-01 19:00` | `2025-05-03 16:00` | 45.0h | `$0.0505` | `$0.0464` | **-8.23%** | **-8.59%** | +2.8% | -9.1% | `stop_loss` |
| 18 | Book 3 | `2025-07-14 15:00` | `2025-07-15 16:00` | 25.0h | `$0.0446` | `$0.0466` | **+4.51%** | **+4.41%** | +8.4% | -4.4% | `target_reclaim` |
| 19 | Book 3 | `2025-07-17 16:00` | `2025-07-18 04:00` | 12.0h | `$0.0456` | `$0.0496` | **+8.81%** | **+8.45%** | +9.2% | -0.5% | `target_reclaim` |
| 20 | Book 5 (Shelf Absorption Squeeze) | `2026-07-12 20:00` | `2026-07-16 20:00` | Live | `$0.0198` | `$0.0215` | **+8.50%** | **+8.16%** | +17.2% | -27.5% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `13` | `100.0%` | **`+125.3%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `time_expiry` | `2` | `50.0%` | **`+2.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `DODOX`

* **Total Candidate Breakouts Filtered (Vetoed):** `559`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `219` (39.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `80`
* **Saved Capital Losses Avoided:** `+2,498.6%`
* **Missed Upside Forgone:** `-2,993.8%`
* **Net Veto Alpha:** `+-495.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `390` | `69.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `94` | `16.8%` |
| `Core 1: Macro Bear Veto` | `55` | `9.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `20` | `3.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*