# Kronos V12: Institutional Symbol Tear Sheet — `ANKR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `25` (`25` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `25` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`64.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.348`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+80.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.24x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.23%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`40.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.6% / -7.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-07-27 13:00` | `2021-08-01 23:00` | 130.0h | `$0.0846` | `$0.1015` | **+8.21%** | **+7.92%** | +26.5% | -8.9% | `target_reclaim` |
| 2 | Book 3 | `2022-04-04 17:00` | `2022-04-06 13:00` | 44.0h | `$0.0878` | `$0.0806` | **-8.23%** | **-8.59%** | +10.3% | -8.4% | `stop_loss` |
| 3 | Book 3 | `2023-02-09 22:00` | `2023-02-10 00:00` | 2.0h | `$0.0285` | `$0.0330` | **+15.68%** | **+14.56%** | +16.2% | -2.7% | `target_reclaim` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2023-02-21 14:00` | `2023-02-25 14:00` | Live | `$0.0453` | `$0.0491` | **+8.50%** | **+8.16%** | +5.9% | -40.5% | `shelf_target_reclaim` |
| 5 | Book 3 | `2023-02-21 21:00` | `2023-02-22 03:00` | 6.0h | `$0.0453` | `$0.0492` | **+8.70%** | **+8.34%** | +11.7% | -3.4% | `target_reclaim` |
| 6 | Book 3 | `2023-04-02 19:00` | `2023-04-05 19:00` | 72.0h | `$0.0347` | `$0.0354` | **+2.02%** | **+2.00%** | +8.2% | -6.2% | `time_expiry` |
| 7 | Book 3 | `2023-06-25 03:00` | `2023-06-26 16:00` | 37.0h | `$0.0262` | `$0.0240` | **-8.23%** | **-8.59%** | +3.6% | -8.2% | `stop_loss` |
| 8 | Book 3 | `2023-10-02 15:00` | `2023-10-05 15:00` | 72.0h | `$0.0199` | `$0.0189` | **-5.11%** | **-5.25%** | +2.7% | -7.5% | `time_expiry` |
| 9 | Book 3 | `2023-11-09 16:00` | `2023-11-10 02:00` | 10.0h | `$0.0244` | `$0.0258` | **+5.87%** | **+5.70%** | +7.8% | -10.5% | `target_reclaim` |
| 10 | Book 3 | `2024-02-13 14:00` | `2024-02-14 05:00` | 15.0h | `$0.0243` | `$0.0253` | **+4.17%** | **+4.08%** | +4.5% | -0.5% | `target_reclaim` |
| 11 | Book 3 | `2024-02-28 17:00` | `2024-02-29 08:00` | 15.0h | `$0.0308` | `$0.0359` | **+16.64%** | **+15.39%** | +18.0% | -1.4% | `target_reclaim` |
| 12 | Book 3 | `2024-03-03 07:00` | `2024-03-03 08:00` | 1.0h | `$0.0348` | `$0.0410` | **+18.00%** | **+16.55%** | +24.8% | -0.0% | `climax_whale_euphoria_harvest` |
| 13 | Book 3 | `2024-03-05 16:00` | `2024-03-05 19:00` | 3.0h | `$0.0380` | `$0.0349` | **-8.23%** | **-8.59%** | +6.5% | -20.3% | `stop_loss` |
| 14 | Book 3 | `2024-03-15 03:00` | `2024-03-16 18:00` | 39.0h | `$0.0511` | `$0.0469` | **-8.23%** | **-8.59%** | +8.1% | -10.9% | `stop_loss` |
| 15 | Book 3 | `2024-03-26 16:00` | `2024-03-27 02:00` | 10.0h | `$0.0544` | `$0.0621` | **+14.15%** | **+13.23%** | +15.7% | -0.7% | `target_reclaim` |
| 16 | Book 3 | `2024-04-02 08:00` | `2024-04-04 04:00` | 44.0h | `$0.0566` | `$0.0520` | **-8.23%** | **-8.59%** | +4.1% | -9.4% | `stop_loss` |
| 17 | Book 3 | `2024-09-28 06:00` | `2024-10-01 06:00` | 72.0h | `$0.0301` | `$0.0292` | **-2.92%** | **-2.96%** | +2.4% | -6.5% | `time_expiry` |
| 18 | Book 3 | `2024-11-10 20:00` | `2024-11-11 00:00` | 4.0h | `$0.0281` | `$0.0292` | **+4.17%** | **+4.08%** | +5.2% | -3.0% | `target_reclaim` |
| 19 | Book 4 | `2024-11-11 02:00` | `2024-11-19 12:00` | 202.0h | `$0.0298` | `$0.0358` | **+16.28%** | **+15.27%** | +21.0% | -7.6% | `target_reclaim` |
| 20 | Book 3 | `2024-11-28 15:00` | `2024-11-29 17:00` | 26.0h | `$0.0402` | `$0.0422` | **+4.99%** | **+4.87%** | +5.3% | -0.1% | `target_reclaim` |
| 21 | Book 3 | `2024-12-02 08:00` | `2024-12-02 21:00` | 13.0h | `$0.0403` | `$0.0437` | **+8.41%** | **+8.07%** | +9.6% | -1.2% | `target_reclaim` |
| 22 | Book 3 | `2025-07-14 15:00` | `2025-07-15 23:00` | 32.0h | `$0.0167` | `$0.0174` | **+4.17%** | **+4.08%** | +5.1% | -3.5% | `target_reclaim` |
| 23 | Book 5 (Shelf Absorption Squeeze) | `2026-03-18 00:00` | `2026-03-22 00:00` | Live | `$0.0052` | `$0.0056` | **+8.50%** | **+8.16%** | +10.3% | -17.9% | `shelf_target_reclaim` |
| 24 | Book 3 | `2026-09-03 03:00` | `2026-09-03 12:00` | 9.0h | `$0.0045` | `$0.0041` | **-8.23%** | **-8.59%** | +4.3% | -8.6% | `stop_loss` |
| 25 | Book 3 | `2026-09-28 05:00` | `2026-10-01 05:00` | 72.0h | `$0.0049` | `$0.0049` | **-0.08%** | **-0.08%** | +2.1% | -2.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `12` | `100.0%` | **`+105.6%`** |
| `stop_loss` | `6` | `0.0%` | **`-51.5%`** |
| `time_expiry` | `4` | `25.0%` | **`-6.3%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `ANKR`

* **Total Candidate Breakouts Filtered (Vetoed):** `559`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `224` (40.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `95`
* **Saved Capital Losses Avoided:** `+2,708.1%`
* **Missed Upside Forgone:** `-2,955.1%`
* **Net Veto Alpha:** `+-247.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `401` | `71.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `54` | `9.7%` |
| `Core 1: Macro Bear Veto` | `42` | `7.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `40` | `7.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `22` | `3.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*