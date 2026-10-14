# Kronos V12: Institutional Symbol Tear Sheet — `BAT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `30` (`30` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `30` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`63.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.328`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+29.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.34x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.97%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-27.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`94.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.3% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-06 15:00` | `2021-08-22 09:00` | 378.0h | `$0.6922` | `$0.8307` | **+20.71%** | **+19.10%** | +22.9% | -6.2% | `target_reclaim` |
| 2 | Book 3 | `2022-04-01 02:00` | `2022-04-02 17:00` | 39.0h | `$0.8395` | `$0.9343` | **+11.29%** | **+10.70%** | +14.2% | -2.2% | `target_reclaim` |
| 3 | Book 3 | `2022-04-05 23:00` | `2022-04-06 13:00` | 14.0h | `$0.8395` | `$0.7704` | **-8.23%** | **-8.59%** | +2.0% | -8.3% | `stop_loss` |
| 4 | Book 3 | `2023-01-14 09:00` | `2023-01-16 02:00` | 41.0h | `$0.2284` | `$0.2379` | **+4.17%** | **+4.08%** | +4.9% | -6.6% | `target_reclaim` |
| 5 | Book 4 | `2023-02-15 19:00` | `2023-03-03 01:00` | 366.0h | `$0.3050` | `$0.2592` | **-18.12%** | **-19.64%** | +10.0% | -20.1% | `structural_stop` |
| 6 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.2251` | `$0.2563` | **+15.87%** | **+14.86%** | +17.6% | -3.4% | `time_cap` |
| 7 | Book 3 | `2023-04-05 18:00` | `2023-04-08 18:00` | 72.0h | `$0.2834` | `$0.2825` | **-0.31%** | **-0.31%** | +5.3% | -2.5% | `time_expiry` |
| 8 | Book 2 | `2023-06-21 16:00` | `2023-06-28 16:00` | 168.0h | `$0.1860` | `$0.1884` | **+1.53%** | **+1.52%** | +10.1% | -2.3% | `time_cap` |
| 9 | Book 3 | `2023-07-05 12:00` | `2023-07-08 12:00` | 72.0h | `$0.1988` | `$0.1874` | **-5.72%** | **-5.90%** | +3.2% | -6.2% | `time_expiry` |
| 10 | Book 3 | `2023-07-18 06:00` | `2023-07-21 06:00` | 72.0h | `$0.1997` | `$0.2005` | **+0.42%** | **+0.42%** | +3.2% | -2.0% | `time_expiry` |
| 11 | Book 4 | `2023-10-23 22:00` | `2023-10-30 22:00` | 168.0h | `$0.2053` | `$0.2087` | **+1.24%** | **+1.23%** | +4.1% | -6.6% | `stagnation_cut` |
| 12 | Book 3 | `2023-11-02 15:00` | `2023-11-05 12:00` | 69.0h | `$0.2079` | `$0.2174` | **+4.58%** | **+4.48%** | +5.1% | -3.2% | `target_reclaim` |
| 13 | Book 3 | `2023-11-07 15:00` | `2023-11-08 06:00` | 15.0h | `$0.2110` | `$0.2198` | **+4.17%** | **+4.08%** | +5.4% | -0.1% | `target_reclaim` |
| 14 | Book 3 | `2023-11-09 16:00` | `2023-11-11 00:00` | 32.0h | `$0.2124` | `$0.2265` | **+6.63%** | **+6.42%** | +8.4% | -7.3% | `target_reclaim` |
| 15 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$0.2272` | `$0.2413` | **+6.20%** | **+6.02%** | +9.8% | -1.9% | `time_expiry` |
| 16 | Book 3 | `2024-01-03 12:00` | `2024-01-06 05:00` | 65.0h | `$0.2459` | `$0.2256` | **-8.23%** | **-8.59%** | +6.6% | -17.4% | `stop_loss` |
| 17 | Book 3 | `2024-03-11 00:00` | `2024-03-11 05:00` | 5.0h | `$0.3413` | `$0.3601` | **+5.52%** | **+5.37%** | +5.9% | -1.8% | `target_reclaim` |
| 18 | Book 3 | `2024-03-15 03:00` | `2024-03-16 18:00` | 39.0h | `$0.3303` | `$0.3031` | **-8.23%** | **-8.59%** | +4.8% | -8.6% | `stop_loss` |
| 19 | Book 3 | `2024-05-23 12:00` | `2024-05-26 12:00` | 72.0h | `$0.2454` | `$0.2454` | **+0.00%** | **+0.00%** | +4.0% | -5.2% | `time_expiry` |
| 20 | Book 4 | `2024-11-11 18:00` | `2024-11-18 17:00` | 167.0h | `$0.1919` | `$0.2303` | **+14.48%** | **+13.67%** | +20.1% | -8.7% | `target_reclaim` |
| 21 | Book 3 | `2024-12-03 13:00` | `2024-12-03 20:00` | 7.0h | `$0.3164` | `$0.3360` | **+6.19%** | **+6.01%** | +9.6% | -3.6% | `target_reclaim` |
| 22 | Book 3 | `2025-04-27 12:00` | `2025-04-28 11:00` | 23.0h | `$0.1468` | `$0.1529` | **+4.17%** | **+4.08%** | +5.1% | -3.9% | `target_reclaim` |
| 23 | Book 3 | `2025-04-29 23:00` | `2025-05-01 09:00` | 34.0h | `$0.1479` | `$0.1541` | **+4.17%** | **+4.08%** | +4.4% | -2.3% | `target_reclaim` |
| 24 | Book 3 | `2025-05-03 09:00` | `2025-05-04 21:00` | 36.0h | `$0.1498` | `$0.1397` | **-6.68%** | **-6.92%** | +0.4% | -7.4% | `stall_bailout` |
| 25 | Book 4 | `2025-07-16 17:00` | `2025-08-02 16:00` | 407.0h | `$0.1574` | `$0.1430` | **-11.13%** | **-11.69%** | +17.4% | -9.2% | `structural_stop` |
| 26 | Book 3 | `2025-10-10 20:00` | `2025-10-10 21:00` | 1.0h | `$0.1514` | `$0.1390` | **-8.23%** | **-8.59%** | +8.6% | -16.4% | `stop_loss` |
| 27 | Book 5 (Shelf Absorption Squeeze) | `2025-11-27 16:00` | `2025-12-01 16:00` | Live | `$0.2370` | `$0.2571` | **+8.50%** | **+8.16%** | +17.0% | -8.3% | `shelf_target_reclaim` |
| 28 | Book 3 | `2026-08-23 05:00` | `2026-08-23 11:00` | 6.0h | `$0.0673` | `$0.0701` | **+4.19%** | **+4.10%** | +4.7% | -1.1% | `target_reclaim` |
| 29 | Book 2 | `2026-09-13 02:00` | `2026-09-15 18:00` | 64.0h | `$0.0776` | `$0.0712` | **-9.13%** | **-9.53%** | +8.2% | -9.4% | `initial_stop` |
| 30 | Book 3 | `2026-09-28 08:00` | `2026-10-01 08:00` | 72.0h | `$0.0899` | `$0.0891` | **-0.83%** | **-0.84%** | +4.8% | -2.5% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `12` | `100.0%` | **`+86.2%`** |
| `time_expiry` | `6` | `50.0%` | **`-0.6%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `time_cap` | `2` | `100.0%` | **`+16.4%`** |
| `structural_stop` | `2` | `0.0%` | **`-31.3%`** |
| `initial_stop` | `1` | `0.0%` | **`-9.5%`** |
| `stall_bailout` | `1` | `0.0%` | **`-6.9%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stagnation_cut` | `1` | `100.0%` | **`+1.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `BAT`

* **Total Candidate Breakouts Filtered (Vetoed):** `1364`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `640` (46.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `156`
* **Saved Capital Losses Avoided:** `+7,806.2%`
* **Missed Upside Forgone:** `-5,387.5%`
* **Net Veto Alpha:** `+2,418.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `656` | `48.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `393` | `28.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `235` | `17.2%` |
| `Core 1: Macro Bear Veto` | `56` | `4.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `24` | `1.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*