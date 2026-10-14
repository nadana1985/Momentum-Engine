# Kronos V12: Institutional Symbol Tear Sheet — `ONT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `23` (`23` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `23` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`73.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`6.994`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+160.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`4.97x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+6.97%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-13.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`66.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.8% / -6.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-01-14 08:00` | `2021-01-18 08:00` | 96.0h | `$0.5844` | `$0.7013` | **+14.80%** | **+13.95%** | +22.5% | -2.8% | `target_reclaim` |
| 2 | Book 4 | `2021-08-13 07:00` | `2021-08-24 00:00` | 257.0h | `$1.0201` | `$1.2242` | **+14.62%** | **+13.79%** | +26.2% | -7.6% | `target_reclaim` |
| 3 | Book 3 | `2022-03-25 16:00` | `2022-03-26 21:00` | 29.0h | `$0.5499` | `$0.5728` | **+4.17%** | **+4.08%** | +5.1% | -1.7% | `target_reclaim` |
| 4 | Book 3 | `2022-04-01 02:00` | `2022-04-03 00:00` | 46.0h | `$0.6210` | `$0.6949` | **+11.90%** | **+11.24%** | +13.4% | -0.3% | `target_reclaim` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2022-06-02 10:00` | `2022-06-06 10:00` | Live | `$0.2890` | `$0.3135` | **+8.50%** | **+8.16%** | +0.2% | -39.4% | `shelf_target_reclaim` |
| 6 | Book 3 | `2023-01-18 16:00` | `2023-01-20 20:00` | 52.0h | `$0.1854` | `$0.2024` | **+9.17%** | **+8.77%** | +10.7% | -0.4% | `target_reclaim` |
| 7 | Book 5 (Shelf Absorption Squeeze) | `2023-04-06 07:00` | `2023-04-10 07:00` | Live | `$0.2435` | `$0.2642` | **+8.50%** | **+8.16%** | +21.1% | -11.2% | `shelf_target_reclaim` |
| 8 | Book 3 | `2023-06-28 07:00` | `2023-06-28 19:00` | 12.0h | `$0.1935` | `$0.1776` | **-8.23%** | **-8.59%** | +2.6% | -11.0% | `stop_loss` |
| 9 | Book 3 | `2023-07-01 21:00` | `2023-07-04 21:00` | 72.0h | `$0.2099` | `$0.1999` | **-4.74%** | **-4.86%** | +1.7% | -6.7% | `time_expiry` |
| 10 | Book 4 | `2023-10-26 22:00` | `2023-11-01 21:00` | 143.0h | `$0.1892` | `$0.2270` | **+22.53%** | **+20.65%** | +20.8% | -3.4% | `target_reclaim` |
| 11 | Book 3 | `2023-11-03 01:00` | `2023-11-03 13:00` | 12.0h | `$0.2087` | `$0.2269` | **+8.70%** | **+8.34%** | +10.4% | -1.7% | `target_reclaim` |
| 12 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$0.2243` | `$0.2320` | **+3.45%** | **+3.39%** | +9.9% | -10.6% | `time_expiry` |
| 13 | Book 3 | `2024-02-28 17:00` | `2024-02-29 08:00` | 15.0h | `$0.2486` | `$0.2852` | **+14.74%** | **+13.75%** | +17.1% | -2.1% | `target_reclaim` |
| 14 | Book 3 | `2024-03-05 19:00` | `2024-03-06 20:00` | 25.0h | `$0.2919` | `$0.3260` | **+11.67%** | **+11.04%** | +14.0% | -12.6% | `target_reclaim` |
| 15 | Book 3 | `2024-03-08 15:00` | `2024-03-09 09:00` | 18.0h | `$0.3449` | `$0.3630` | **+5.24%** | **+5.11%** | +5.3% | -1.1% | `target_reclaim` |
| 16 | Book 3 | `2024-04-23 00:00` | `2024-04-23 01:00` | 1.0h | `$0.4564` | `$0.4796` | **+5.08%** | **+4.96%** | +13.9% | -0.1% | `target_reclaim` |
| 17 | Book 3 | `2024-07-23 17:00` | `2024-07-26 17:00` | 72.0h | `$0.1980` | `$0.1965` | **-0.75%** | **-0.75%** | +4.4% | -7.8% | `time_expiry` |
| 18 | Book 4 | `2024-11-15 21:00` | `2024-11-23 01:00` | 172.0h | `$0.2085` | `$0.2502` | **+46.00%** | **+38.94%** | +22.1% | -0.5% | `target_reclaim` |
| 19 | Book 3 | `2025-04-28 00:00` | `2025-05-01 00:00` | 72.0h | `$0.1548` | `$0.1542` | **-0.41%** | **-0.41%** | +3.4% | -5.7% | `time_expiry` |
| 20 | Book 3 | `2025-05-15 07:00` | `2025-05-18 07:00` | 72.0h | `$0.1563` | `$0.1508` | **-3.48%** | **-3.54%** | +3.0% | -6.1% | `time_expiry` |
| 21 | Book 3 | `2025-07-15 03:00` | `2025-07-15 16:00` | 13.0h | `$0.1397` | `$0.1461` | **+4.61%** | **+4.51%** | +4.6% | -0.4% | `target_reclaim` |
| 22 | Book 5 (Shelf Absorption Squeeze) | `2025-12-27 11:00` | `2025-12-31 11:00` | Live | `$0.0627` | `$0.0681` | **+8.50%** | **+8.16%** | +12.0% | -11.0% | `shelf_target_reclaim` |
| 23 | Book 3 | `2026-08-28 02:00` | `2026-08-30 23:00` | 69.0h | `$0.0575` | `$0.0528` | **-8.23%** | **-8.59%** | +3.4% | -10.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `13` | `100.0%` | **`+159.1%`** |
| `time_expiry` | `5` | `20.0%` | **`-6.2%`** |
| `shelf_target_reclaim` | `3` | `100.0%` | **`+24.5%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ONT`

* **Total Candidate Breakouts Filtered (Vetoed):** `1392`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `826` (59.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `99`
* **Saved Capital Losses Avoided:** `+11,542.5%`
* **Missed Upside Forgone:** `-2,688.6%`
* **Net Veto Alpha:** `+8,854.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `668` | `48.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `462` | `33.2%` |
| `Core 1: Macro Bear Veto` | `162` | `11.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `83` | `6.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `17` | `1.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*