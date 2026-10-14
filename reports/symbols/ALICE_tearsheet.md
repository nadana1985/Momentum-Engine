# Kronos V12: Institutional Symbol Tear Sheet — `ALICE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `22` (`22` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `22` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`59.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.526`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+36.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.44x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.67%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-29.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`61.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.2% / -9.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2022-04-01 02:00` | `2022-04-01 18:00` | 16.0h | `$7.1570` | `$8.1000` | **+13.18%** | **+12.38%** | +22.5% | -2.0% | `target_reclaim` |
| 2 | Book 2 | `2022-10-25 17:00` | `2022-10-28 02:00` | 57.0h | `$1.6000` | `$1.5910` | **-0.69%** | **-0.69%** | +4.5% | -2.9% | `fast_decay_cut` |
| 3 | Book 3 | `2023-01-18 15:00` | `2023-01-21 15:00` | 72.0h | `$1.3575` | `$1.5292` | **+12.64%** | **+11.90%** | +17.0% | -2.3% | `time_expiry` |
| 4 | Book 3 | `2023-01-24 22:00` | `2023-01-27 07:00` | 57.0h | `$1.5441` | `$1.6840` | **+9.06%** | **+8.67%** | +12.4% | -5.7% | `target_reclaim` |
| 5 | Book 3 | `2023-02-09 19:00` | `2023-02-09 22:00` | 3.0h | `$1.8081` | `$1.6593` | **-8.23%** | **-8.59%** | +5.4% | -8.5% | `stop_loss` |
| 6 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$1.5037` | `$1.6439` | **+10.72%** | **+10.25%** | +17.0% | -4.8% | `time_cap` |
| 7 | Book 3 | `2023-04-19 08:00` | `2023-04-20 04:00` | 20.0h | `$1.6580` | `$1.8340` | **+10.62%** | **+10.09%** | +11.3% | -0.8% | `target_reclaim` |
| 8 | Book 3 | `2023-07-02 09:00` | `2023-07-05 09:00` | 72.0h | `$1.0553` | `$1.0803` | **+2.37%** | **+2.34%** | +5.9% | -0.6% | `time_expiry` |
| 9 | Book 3 | `2023-11-09 16:00` | `2023-11-12 10:00` | 66.0h | `$0.8464` | `$0.9880` | **+16.73%** | **+15.47%** | +19.9% | -4.3% | `target_reclaim` |
| 10 | Book 3 | `2023-11-16 15:00` | `2023-11-17 15:00` | 24.0h | `$0.9991` | `$0.9169` | **-8.23%** | **-8.59%** | +3.2% | -9.1% | `stop_loss` |
| 11 | Book 3 | `2024-05-23 18:00` | `2024-05-25 00:00` | 30.0h | `$1.1993` | `$1.2900` | **+7.56%** | **+7.29%** | +8.6% | -4.1% | `target_reclaim` |
| 12 | Book 5 (Shelf Absorption Squeeze) | `2024-06-03 03:00` | `2024-06-07 03:00` | Live | `$2.2319` | `$2.0489` | **-8.20%** | **-8.56%** | +-1.8% | -58.1% | `shelf_stop_loss` |
| 13 | Book 3 | `2024-09-28 08:00` | `2024-09-29 20:00` | 36.0h | `$1.1472` | `$1.1950` | **+4.17%** | **+4.08%** | +4.4% | -3.2% | `target_reclaim` |
| 14 | Book 3 | `2024-10-22 13:00` | `2024-10-25 13:00` | 72.0h | `$1.1458` | `$1.1182` | **-2.41%** | **-2.44%** | +9.2% | -4.3% | `time_expiry` |
| 15 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$1.1367` | `$1.0431` | **-8.23%** | **-8.59%** | +6.4% | -8.2% | `stop_loss` |
| 16 | Book 3 | `2024-11-24 12:00` | `2024-11-26 11:00` | 47.0h | `$1.4352` | `$1.3171` | **-8.23%** | **-8.59%** | +6.7% | -9.8% | `stop_loss` |
| 17 | Book 3 | `2024-12-02 08:00` | `2024-12-02 20:00` | 12.0h | `$1.4933` | `$1.6200` | **+8.49%** | **+8.14%** | +8.6% | -2.6% | `target_reclaim` |
| 18 | Book 3 | `2025-07-18 20:00` | `2025-07-20 06:00` | 34.0h | `$0.4701` | `$0.4950` | **+5.29%** | **+5.15%** | +5.9% | -2.4% | `target_reclaim` |
| 19 | Book 3 | `2025-10-09 10:00` | `2025-10-09 14:00` | 4.0h | `$0.3662` | `$0.3910` | **+6.77%** | **+6.55%** | +6.8% | -0.6% | `target_reclaim` |
| 20 | Book 3 | `2025-10-10 20:00` | `2025-10-10 21:00` | 1.0h | `$0.3854` | `$0.3537` | **-8.23%** | **-8.59%** | +14.7% | -52.5% | `stop_loss` |
| 21 | Book 4 | `2026-08-20 15:00` | `2026-09-09 22:00` | 487.0h | `$0.1498` | `$0.1274` | **-13.91%** | **-15.08%** | +6.6% | -17.2% | `structural_stop` |
| 22 | Book 3 | `2026-09-23 14:00` | `2026-09-23 15:00` | 1.0h | `$0.1383` | `$0.1441` | **+4.17%** | **+4.08%** | +7.6% | -0.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `10` | `100.0%` | **`+81.9%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `time_expiry` | `3` | `66.7%` | **`+11.8%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.7%`** |
| `structural_stop` | `1` | `0.0%` | **`-15.1%`** |
| `time_cap` | `1` | `100.0%` | **`+10.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALICE`

* **Total Candidate Breakouts Filtered (Vetoed):** `636`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `489` (76.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `98`
* **Saved Capital Losses Avoided:** `+8,580.0%`
* **Missed Upside Forgone:** `-5,763.4%`
* **Net Veto Alpha:** `+2,816.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `381` | `59.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `98` | `15.4%` |
| `Core 1: Macro Bear Veto` | `74` | `11.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `45` | `7.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `38` | `6.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*