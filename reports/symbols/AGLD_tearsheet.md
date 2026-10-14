# Kronos V12: Institutional Symbol Tear Sheet — `AGLD`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `18` (`18` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `18` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`55.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.273`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+15.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.17x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.86%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-16.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.2% / -8.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-09 16:00` | `2024-02-12 16:00` | 72.0h | `$1.2739` | `$1.2685` | **-0.42%** | **-0.43%** | +4.2% | -3.1% | `time_expiry` |
| 2 | Book 3 | `2024-03-03 07:00` | `2024-03-04 05:00` | 22.0h | `$1.5450` | `$1.6682` | **+7.97%** | **+7.67%** | +10.3% | -3.4% | `target_reclaim` |
| 3 | Book 3 | `2024-03-05 19:00` | `2024-03-05 20:00` | 1.0h | `$1.5508` | `$1.4020` | **-9.60%** | **-10.09%** | +2.8% | -18.1% | `stop_loss` |
| 4 | Book 3 | `2024-05-23 13:00` | `2024-05-24 15:00` | 26.0h | `$1.0889` | `$1.1343` | **+4.17%** | **+4.08%** | +4.4% | -5.1% | `target_reclaim` |
| 5 | Book 3 | `2024-06-06 10:00` | `2024-06-07 08:00` | 22.0h | `$1.6412` | `$1.7405` | **+6.05%** | **+5.88%** | +6.5% | -1.6% | `target_reclaim` |
| 6 | Book 3 | `2024-10-22 12:00` | `2024-10-25 12:00` | 72.0h | `$1.1207` | `$1.0779` | **-3.82%** | **-3.89%** | +6.7% | -7.8% | `time_expiry` |
| 7 | Book 3 | `2024-11-13 08:00` | `2024-11-13 10:00` | 2.0h | `$2.4502` | `$2.2486` | **-8.23%** | **-8.59%** | +12.7% | -12.6% | `stop_loss` |
| 8 | Book 3 | `2024-12-23 00:00` | `2024-12-24 00:00` | 24.0h | `$1.5059` | `$1.7191` | **+14.16%** | **+13.24%** | +17.4% | -4.4% | `target_reclaim` |
| 9 | Book 3 | `2024-12-28 02:00` | `2024-12-29 00:00` | 22.0h | `$1.8744` | `$1.7201` | **-8.23%** | **-8.59%** | +2.7% | -8.0% | `stop_loss` |
| 10 | Book 3 | `2025-05-12 15:00` | `2025-05-14 05:00` | 38.0h | `$0.9925` | `$1.1208` | **+12.93%** | **+12.16%** | +14.2% | -2.9% | `target_reclaim` |
| 11 | Book 3 | `2025-05-14 08:00` | `2025-05-14 11:00` | 3.0h | `$1.0765` | `$1.1295` | **+4.92%** | **+4.81%** | +5.1% | -0.4% | `target_reclaim` |
| 12 | Book 3 | `2025-05-14 21:00` | `2025-05-15 07:00` | 10.0h | `$1.0765` | `$0.9879` | **-8.23%** | **-8.59%** | +1.2% | -8.9% | `stop_loss` |
| 13 | Book 3 | `2025-06-04 12:00` | `2025-06-05 00:00` | 12.0h | `$0.8418` | `$0.8769` | **+4.17%** | **+4.08%** | +5.8% | -0.7% | `target_reclaim` |
| 14 | Book 5 (Shelf Absorption Squeeze) | `2026-02-21 15:00` | `2026-02-25 15:00` | Live | `$0.2514` | `$0.2728` | **+8.50%** | **+8.16%** | +23.9% | -24.1% | `shelf_target_reclaim` |
| 15 | Book 5 (Shelf Absorption Squeeze) | `2026-06-26 13:00` | `2026-06-30 13:00` | Live | `$0.1559` | `$0.1692` | **+8.50%** | **+8.16%** | +27.4% | -15.8% | `shelf_target_reclaim` |
| 16 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.1677` | `$0.1747` | **+4.17%** | **+4.08%** | +11.7% | -4.4% | `target_reclaim` |
| 17 | Book 3 | `2026-09-14 12:00` | `2026-09-17 12:00` | 72.0h | `$0.1755` | `$0.1735` | **-1.19%** | **-1.19%** | +1.5% | -7.4% | `time_expiry` |
| 18 | Book 4 | `2026-09-22 23:00` | `2026-10-08 15:00` | 376.0h | `$0.2157` | `$0.1899` | **-14.48%** | **-15.43%** | +6.4% | -14.7% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+56.0%`** |
| `stop_loss` | `4` | `0.0%` | **`-35.9%`** |
| `time_expiry` | `3` | `0.0%` | **`-5.5%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `structural_stop` | `1` | `0.0%` | **`-15.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `AGLD`

* **Total Candidate Breakouts Filtered (Vetoed):** `206`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `148` (71.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+2,077.7%`
* **Missed Upside Forgone:** `-1,395.2%`
* **Net Veto Alpha:** `+682.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `101` | `49.0%` |
| `Core 1: Macro Bear Veto` | `52` | `25.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `32` | `15.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `21` | `10.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*