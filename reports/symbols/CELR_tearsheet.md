# Kronos V12: Institutional Symbol Tear Sheet — `CELR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `28` (`28` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `28` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`67.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.384`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+126.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`3.55x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.52%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-16.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`42.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.6% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 17:00` | `2022-10-27 17:00` | 48.0h | `$0.0153` | `$0.0152` | **-0.37%** | **-0.37%** | +4.1% | -3.4% | `fast_decay_cut` |
| 2 | Book 3 | `2023-01-18 16:00` | `2023-01-20 22:00` | 54.0h | `$0.0125` | `$0.0146` | **+17.14%** | **+15.82%** | +18.3% | -1.0% | `target_reclaim` |
| 3 | Book 3 | `2023-01-25 17:00` | `2023-01-25 21:00` | 4.0h | `$0.0153` | `$0.0161` | **+5.33%** | **+5.20%** | +7.8% | -0.3% | `target_reclaim` |
| 4 | Book 3 | `2023-02-03 02:00` | `2023-02-03 23:00` | 21.0h | `$0.0188` | `$0.0203` | **+8.06%** | **+7.75%** | +9.3% | -0.9% | `target_reclaim` |
| 5 | Book 3 | `2023-02-05 12:00` | `2023-02-08 12:00` | 72.0h | `$0.0190` | `$0.0188` | **-1.01%** | **-1.01%** | +4.8% | -5.4% | `time_expiry` |
| 6 | Book 3 | `2023-02-13 09:00` | `2023-02-15 19:00` | 58.0h | `$0.0198` | `$0.0227` | **+14.66%** | **+13.68%** | +20.7% | -5.0% | `target_reclaim` |
| 7 | Book 5 (Shelf Absorption Squeeze) | `2023-03-19 19:00` | `2023-03-23 19:00` | Live | `$0.0209` | `$0.0227` | **+8.50%** | **+8.16%** | +32.6% | -10.8% | `shelf_target_reclaim` |
| 8 | Book 3 | `2023-04-17 05:00` | `2023-04-19 00:00` | 43.0h | `$0.0271` | `$0.0291` | **+7.34%** | **+7.09%** | +8.2% | -6.0% | `target_reclaim` |
| 9 | Book 3 | `2023-07-05 15:00` | `2023-07-08 15:00` | 72.0h | `$0.0165` | `$0.0158` | **-4.45%** | **-4.55%** | +5.9% | -6.2% | `time_expiry` |
| 10 | Book 4 | `2023-11-02 03:00` | `2023-11-09 16:00` | 181.0h | `$0.0153` | `$0.0130` | **-7.55%** | **-8.18%** | +5.7% | -15.0% | `structural_stop` |
| 11 | Book 3 | `2023-11-12 00:00` | `2023-11-12 06:00` | 6.0h | `$0.0155` | `$0.0162` | **+4.94%** | **+4.82%** | +5.3% | -1.4% | `target_reclaim` |
| 12 | Book 3 | `2023-11-14 11:00` | `2023-11-16 04:00` | 41.0h | `$0.0150` | `$0.0163` | **+8.70%** | **+8.34%** | +10.2% | -6.3% | `target_reclaim` |
| 13 | Book 3 | `2023-12-11 02:00` | `2023-12-11 10:00` | 8.0h | `$0.0182` | `$0.0198` | **+8.70%** | **+8.34%** | +11.0% | -6.3% | `target_reclaim` |
| 14 | Book 3 | `2023-12-12 17:00` | `2023-12-13 06:00` | 13.0h | `$0.0192` | `$0.0176` | **-8.23%** | **-8.59%** | +3.5% | -8.6% | `stop_loss` |
| 15 | Book 3 | `2023-12-18 01:00` | `2023-12-21 01:00` | 72.0h | `$0.0188` | `$0.0195` | **+3.41%** | **+3.35%** | +4.5% | -7.9% | `time_expiry` |
| 16 | Book 3 | `2024-02-13 13:00` | `2024-02-14 04:00` | 15.0h | `$0.0187` | `$0.0194` | **+4.17%** | **+4.08%** | +4.2% | -1.3% | `target_reclaim` |
| 17 | Book 3 | `2024-03-05 16:00` | `2024-03-05 19:00` | 3.0h | `$0.0296` | `$0.0271` | **-8.23%** | **-8.59%** | +6.9% | -8.3% | `stop_loss` |
| 18 | Book 3 | `2024-03-06 12:00` | `2024-03-09 12:00` | 72.0h | `$0.0321` | `$0.0328` | **+2.17%** | **+2.15%** | +8.5% | -3.0% | `time_expiry` |
| 19 | Book 3 | `2024-11-12 10:00` | `2024-11-13 18:00` | 32.0h | `$0.0134` | `$0.0143` | **+7.15%** | **+6.91%** | +7.2% | -5.0% | `target_reclaim` |
| 20 | Book 4 | `2024-11-21 13:00` | `2024-11-23 17:00` | 52.0h | `$0.0151` | `$0.0181` | **+60.55%** | **+49.02%** | +24.8% | -4.3% | `target_reclaim` |
| 21 | Book 3 | `2025-04-26 13:00` | `2025-04-29 07:00` | 66.0h | `$0.0103` | `$0.0107` | **+4.17%** | **+4.08%** | +4.2% | -4.7% | `target_reclaim` |
| 22 | Book 3 | `2025-05-12 18:00` | `2025-05-12 20:00` | 2.0h | `$0.0106` | `$0.0115` | **+8.32%** | **+7.99%** | +10.7% | -0.3% | `target_reclaim` |
| 23 | Book 3 | `2025-05-15 14:00` | `2025-05-17 12:00` | 46.0h | `$0.0106` | `$0.0098` | **-8.23%** | **-8.59%** | +5.9% | -8.4% | `stop_loss` |
| 24 | Book 3 | `2025-08-06 03:00` | `2025-08-06 15:00` | 12.0h | `$0.0070` | `$0.0073` | **+4.17%** | **+4.08%** | +5.0% | -0.8% | `target_reclaim` |
| 25 | Book 3 | `2025-10-09 23:00` | `2025-10-10 19:00` | 20.0h | `$0.0081` | `$0.0074` | **-8.23%** | **-8.59%** | +4.0% | -10.3% | `stop_loss` |
| 26 | Book 3 | `2026-09-01 13:00` | `2026-09-04 13:00` | 72.0h | `$0.0022` | `$0.0022` | **+1.19%** | **+1.19%** | +5.2% | -3.2% | `time_expiry` |
| 27 | Book 2 | `2026-09-13 01:00` | `2026-09-15 01:00` | 48.0h | `$0.0022` | `$0.0021` | **-4.55%** | **-4.65%** | +4.4% | -6.0% | `fast_decay_cut` |
| 28 | Book 4 | `2026-09-19 18:00` | `2026-09-19 19:00` | 1.0h | `$0.0026` | `$0.0031` | **+19.16%** | **+17.75%** | +25.7% | -0.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `15` | `100.0%` | **`+164.9%`** |
| `time_expiry` | `5` | `60.0%` | **`+1.1%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-5.0%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `CELR`

* **Total Candidate Breakouts Filtered (Vetoed):** `1194`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `638` (53.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `143`
* **Saved Capital Losses Avoided:** `+9,638.5%`
* **Missed Upside Forgone:** `-4,762.2%`
* **Net Veto Alpha:** `+4,876.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `469` | `39.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `333` | `27.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `187` | `15.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `133` | `11.1%` |
| `Core 1: Macro Bear Veto` | `72` | `6.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*