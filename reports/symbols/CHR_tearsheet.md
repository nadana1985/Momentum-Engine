# Kronos V12: Institutional Symbol Tear Sheet — `CHR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `20` (`20` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `20` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.773`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+53.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.70x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+2.65%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-25.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`24.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.1% / -7.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-01-24 22:00` | `2023-01-25 21:00` | 23.0h | `$0.1442` | `$0.1525` | **+5.74%** | **+5.58%** | +6.8% | -1.5% | `target_reclaim` |
| 2 | Book 3 | `2023-02-05 12:00` | `2023-02-07 16:00` | 52.0h | `$0.1691` | `$0.1810` | **+7.02%** | **+6.78%** | +14.8% | -5.4% | `target_reclaim` |
| 3 | Book 3 | `2023-04-19 08:00` | `2023-04-20 16:00` | 32.0h | `$0.1745` | `$0.1602` | **-8.23%** | **-8.59%** | +5.3% | -8.8% | `stop_loss` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2023-09-09 03:00` | `2023-09-13 03:00` | Live | `$0.1023` | `$0.1062` | **+3.80%** | **+3.73%** | +-1.7% | -15.8% | `shelf_trail` |
| 5 | Book 3 | `2023-10-24 15:00` | `2023-10-24 22:00` | 7.0h | `$0.1005` | `$0.1047` | **+4.17%** | **+4.08%** | +5.2% | -1.3% | `target_reclaim` |
| 6 | Book 3 | `2023-11-21 15:00` | `2023-11-21 22:00` | 7.0h | `$0.1278` | `$0.1173` | **-8.23%** | **-8.59%** | +2.5% | -9.5% | `stop_loss` |
| 7 | Book 3 | `2023-12-04 11:00` | `2023-12-04 13:00` | 2.0h | `$0.1358` | `$0.1516` | **+11.66%** | **+11.03%** | +13.7% | -1.9% | `target_reclaim` |
| 8 | Book 3 | `2024-01-03 13:00` | `2024-01-03 17:00` | 4.0h | `$0.2423` | `$0.2634` | **+8.70%** | **+8.34%** | +13.4% | -6.9% | `target_reclaim` |
| 9 | Book 3 | `2024-01-11 15:00` | `2024-01-12 22:00` | 31.0h | `$0.2676` | `$0.2455` | **-8.23%** | **-8.59%** | +5.7% | -8.2% | `stop_loss` |
| 10 | Book 3 | `2024-02-19 12:00` | `2024-02-20 04:00` | 16.0h | `$0.4609` | `$0.4230` | **-8.23%** | **-8.59%** | +1.4% | -8.8% | `stop_loss` |
| 11 | Book 3 | `2024-05-23 13:00` | `2024-05-25 01:00` | 36.0h | `$0.3353` | `$0.3663` | **+9.24%** | **+8.83%** | +9.9% | -6.3% | `target_reclaim` |
| 12 | Book 3 | `2024-08-26 23:00` | `2024-08-27 08:00` | 9.0h | `$0.2308` | `$0.2118` | **-8.23%** | **-8.59%** | +1.8% | -9.0% | `stop_loss` |
| 13 | Book 3 | `2024-09-30 15:00` | `2024-10-01 15:00` | 24.0h | `$0.2023` | `$0.1857` | **-8.23%** | **-8.59%** | +1.4% | -11.6% | `stop_loss` |
| 14 | Book 3 | `2024-11-12 10:00` | `2024-11-12 22:00` | 12.0h | `$0.1888` | `$0.1993` | **+5.58%** | **+5.43%** | +6.5% | -3.9% | `target_reclaim` |
| 15 | Book 4 | `2024-11-18 15:00` | `2024-11-24 06:00` | 135.0h | `$0.2165` | `$0.2598` | **+40.28%** | **+34.73%** | +20.6% | -9.3% | `target_reclaim` |
| 16 | Book 3 | `2025-05-15 08:00` | `2025-05-17 00:00` | 40.0h | `$0.1148` | `$0.1053` | **-8.23%** | **-8.59%** | +4.3% | -8.2% | `stop_loss` |
| 17 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0151` | `$0.0158` | **+4.17%** | **+4.08%** | +8.3% | -4.9% | `target_reclaim` |
| 18 | Book 3 | `2026-09-09 22:00` | `2026-09-10 06:00` | 8.0h | `$0.0160` | `$0.0167` | **+4.17%** | **+4.08%** | +4.2% | -4.3% | `target_reclaim` |
| 19 | Book 3 | `2026-09-10 11:00` | `2026-09-11 12:00` | 25.0h | `$0.0160` | `$0.0147` | **-8.23%** | **-8.59%** | +1.8% | -8.0% | `stop_loss` |
| 20 | Book 2 | `2026-09-22 14:00` | `2026-09-22 17:00` | 3.0h | `$0.0194` | `$0.0245` | **+28.30%** | **+25.09%** | +36.8% | -6.7% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `10` | `100.0%` | **`+93.0%`** |
| `stop_loss` | `8` | `0.0%` | **`-68.7%`** |
| `shelf_trail` | `1` | `100.0%` | **`+3.7%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+25.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `CHR`

* **Total Candidate Breakouts Filtered (Vetoed):** `677`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `341` (50.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `166`
* **Saved Capital Losses Avoided:** `+4,518.6%`
* **Missed Upside Forgone:** `-5,316.5%`
* **Net Veto Alpha:** `+-797.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `375` | `55.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `101` | `14.9%` |
| `Core 1: Macro Bear Veto` | `93` | `13.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `68` | `10.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `40` | `5.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*