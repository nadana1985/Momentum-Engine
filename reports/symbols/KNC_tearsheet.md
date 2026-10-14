# Kronos V12: Institutional Symbol Tear Sheet — `KNC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `24` (`24` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `24` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`83.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.163`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+143.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`4.18x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+5.96%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`77.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.2% / -6.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-01-12 04:00` | `2021-01-16 23:00` | 115.0h | `$1.0612` | `$1.2734` | **+18.34%** | **+17.07%** | +21.1% | -9.1% | `target_reclaim` |
| 2 | Book 4 | `2021-08-13 20:00` | `2021-08-24 01:00` | 245.0h | `$1.8808` | `$2.2570` | **+15.17%** | **+14.29%** | +21.2% | -9.6% | `target_reclaim` |
| 3 | Book 3 | `2023-02-05 21:00` | `2023-02-06 01:00` | 4.0h | `$0.8152` | `$0.9173` | **+12.52%** | **+11.80%** | +17.5% | -0.3% | `target_reclaim` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2023-02-25 06:00` | `2023-03-01 06:00` | Live | `$0.8554` | `$0.9281` | **+8.50%** | **+8.16%** | +2.0% | -39.2% | `shelf_target_reclaim` |
| 5 | Book 3 | `2023-06-24 23:00` | `2023-06-26 01:00` | 26.0h | `$0.6190` | `$0.5680` | **-8.23%** | **-8.59%** | +8.1% | -8.8% | `stop_loss` |
| 6 | Book 4 | `2023-09-23 10:00` | `2023-10-23 09:00` | 719.0h | `$0.6565` | `$0.6555` | **+0.37%** | **+0.37%** | +13.4% | -7.4% | `time_expiry` |
| 7 | Book 3 | `2023-11-09 16:00` | `2023-11-10 21:00` | 29.0h | `$0.7318` | `$0.8528` | **+16.53%** | **+15.30%** | +16.8% | -4.4% | `target_reclaim` |
| 8 | Book 3 | `2023-11-14 00:00` | `2023-11-14 18:00` | 18.0h | `$0.8233` | `$0.7555` | **-8.23%** | **-8.59%** | +4.1% | -10.3% | `stop_loss` |
| 9 | Book 3 | `2024-02-13 14:00` | `2024-02-14 06:00` | 16.0h | `$0.6079` | `$0.6332` | **+4.17%** | **+4.08%** | +4.3% | -0.3% | `target_reclaim` |
| 10 | Book 3 | `2024-02-20 15:00` | `2024-02-23 15:00` | 72.0h | `$0.6458` | `$0.6727` | **+4.17%** | **+4.08%** | +4.3% | -4.2% | `target_reclaim` |
| 11 | Book 3 | `2024-02-28 17:00` | `2024-02-29 07:00` | 14.0h | `$0.6602` | `$0.7097` | **+7.50%** | **+7.23%** | +8.8% | -6.5% | `target_reclaim` |
| 12 | Book 3 | `2024-03-05 19:00` | `2024-03-06 21:00` | 26.0h | `$0.7145` | `$0.8263` | **+15.65%** | **+14.54%** | +15.8% | -10.1% | `target_reclaim` |
| 13 | Book 3 | `2024-03-15 09:00` | `2024-03-16 18:00` | 33.0h | `$0.9685` | `$0.8888` | **-8.23%** | **-8.59%** | +7.4% | -10.9% | `stop_loss` |
| 14 | Book 3 | `2024-05-23 13:00` | `2024-05-24 04:00` | 15.0h | `$0.5903` | `$0.6248` | **+5.85%** | **+5.68%** | +6.0% | -2.0% | `target_reclaim` |
| 15 | Book 3 | `2024-06-11 01:00` | `2024-06-11 10:00` | 9.0h | `$0.7331` | `$0.7696` | **+4.98%** | **+4.86%** | +5.9% | -0.9% | `target_reclaim` |
| 16 | Book 3 | `2024-06-12 12:00` | `2024-06-12 14:00` | 2.0h | `$0.7535` | `$0.7892` | **+4.74%** | **+4.64%** | +4.8% | -0.0% | `target_reclaim` |
| 17 | Book 3 | `2024-06-13 15:00` | `2024-06-14 10:00` | 19.0h | `$0.7535` | `$0.8013` | **+6.35%** | **+6.16%** | +6.7% | -5.7% | `target_reclaim` |
| 18 | Book 3 | `2024-09-30 02:00` | `2024-10-01 14:00` | 36.0h | `$0.5002` | `$0.4590` | **-8.23%** | **-8.59%** | +0.7% | -9.2% | `stop_loss` |
| 19 | Book 4 | `2024-11-16 05:00` | `2024-11-24 03:00` | 190.0h | `$0.5150` | `$0.6180` | **+29.12%** | **+26.07%** | +21.6% | -2.5% | `target_reclaim` |
| 20 | Book 3 | `2025-04-21 23:00` | `2025-04-22 15:00` | 16.0h | `$0.3413` | `$0.3568` | **+4.54%** | **+4.44%** | +4.9% | -2.3% | `target_reclaim` |
| 21 | Book 3 | `2025-04-28 01:00` | `2025-05-01 01:00` | 72.0h | `$0.3674` | `$0.3716` | **+1.13%** | **+1.12%** | +3.7% | -2.6% | `time_expiry` |
| 22 | Book 3 | `2025-07-11 22:00` | `2025-07-12 04:00` | 6.0h | `$0.3147` | `$0.3714` | **+18.00%** | **+16.55%** | +33.5% | -0.1% | `climax_whale_euphoria_harvest` |
| 23 | Book 3 | `2025-08-07 05:00` | `2025-08-08 18:00` | 37.0h | `$0.4090` | `$0.4446` | **+8.70%** | **+8.34%** | +9.5% | -0.1% | `target_reclaim` |
| 24 | Book 3 | `2026-09-23 14:00` | `2026-09-26 14:00` | 72.0h | `$0.1440` | `$0.1477` | **+2.61%** | **+2.58%** | +4.0% | -4.1% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `15` | `100.0%` | **`+148.6%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `time_expiry` | `3` | `100.0%` | **`+4.1%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `KNC`

* **Total Candidate Breakouts Filtered (Vetoed):** `1733`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `1051` (60.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `95`
* **Saved Capital Losses Avoided:** `+12,965.4%`
* **Missed Upside Forgone:** `-2,548.1%`
* **Net Veto Alpha:** `+10,417.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `674` | `38.9%` |
| `Core 1: Macro Bear Veto` | `483` | `27.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `386` | `22.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `122` | `7.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `53` | `3.1%` |
| `Core 4: Defensible Whale Dump` | `13` | `0.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*