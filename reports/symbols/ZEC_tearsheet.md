# Kronos V12: Institutional Symbol Tear Sheet — `ZEC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `20` (`20` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `20` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`65.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.401`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+63.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.88x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.15%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`47.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.8% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-11 05:00` | `2021-08-23 03:00` | 286.0h | `$136.6447` | `$163.9736` | **+11.58%** | **+11.05%** | +20.3% | -4.4% | `target_reclaim` |
| 2 | Book 2 | `2023-10-20 08:00` | `2023-10-21 20:00` | 36.0h | `$25.7041` | `$25.6058` | **-0.42%** | **-0.42%** | +0.9% | -1.9% | `stall_bailout` |
| 3 | Book 4 | `2023-11-10 02:00` | `2023-11-17 02:00` | 168.0h | `$30.5357` | `$30.2146` | **-1.66%** | **-1.67%** | +4.3% | -9.2% | `stagnation_cut` |
| 4 | Book 3 | `2024-02-27 15:00` | `2024-02-28 17:00` | 26.0h | `$28.7040` | `$26.3417` | **-8.23%** | **-8.59%** | +3.5% | -11.0% | `stop_loss` |
| 5 | Book 3 | `2024-03-05 19:00` | `2024-03-07 01:00` | 30.0h | `$28.8154` | `$33.6400` | **+16.74%** | **+15.48%** | +17.7% | -10.4% | `target_reclaim` |
| 6 | Book 4 | `2024-07-13 05:00` | `2024-07-16 13:00` | 80.0h | `$25.0876` | `$30.1051` | **+9.32%** | **+8.96%** | +21.0% | -0.3% | `target_reclaim` |
| 7 | Book 3 | `2024-07-30 06:00` | `2024-07-31 22:00` | 40.0h | `$31.9392` | `$33.2700` | **+4.17%** | **+4.08%** | +4.3% | -3.2% | `target_reclaim` |
| 8 | Book 3 | `2024-08-03 01:00` | `2024-08-03 12:00` | 11.0h | `$32.1189` | `$33.8900` | **+5.51%** | **+5.37%** | +8.3% | -1.1% | `target_reclaim` |
| 9 | Book 3 | `2024-08-12 14:00` | `2024-08-12 17:00` | 3.0h | `$41.1360` | `$42.8500` | **+4.17%** | **+4.08%** | +4.4% | -1.7% | `target_reclaim` |
| 10 | Book 3 | `2024-10-29 05:00` | `2024-11-01 05:00` | 72.0h | `$36.3671` | `$36.9773` | **+1.68%** | **+1.66%** | +9.7% | -1.6% | `time_expiry` |
| 11 | Book 3 | `2024-11-12 03:00` | `2024-11-13 04:00` | 25.0h | `$42.2934` | `$38.8127` | **-8.23%** | **-8.59%** | +5.7% | -9.6% | `stop_loss` |
| 12 | Book 3 | `2024-11-26 10:00` | `2024-11-26 23:00` | 13.0h | `$45.0780` | `$50.6300` | **+12.32%** | **+11.61%** | +17.3% | -2.7% | `target_reclaim` |
| 13 | Book 3 | `2025-10-05 10:00` | `2025-10-05 18:00` | 8.0h | `$145.3689` | `$164.0200` | **+12.83%** | **+12.07%** | +14.1% | -1.2% | `target_reclaim` |
| 14 | Book 3 | `2025-10-09 02:00` | `2025-10-09 06:00` | 4.0h | `$165.3606` | `$177.7800` | **+7.51%** | **+7.24%** | +10.8% | -0.2% | `target_reclaim` |
| 15 | Book 3 | `2025-10-10 21:00` | `2025-10-10 22:00` | 1.0h | `$164.4943` | `$188.1500` | **+14.38%** | **+13.44%** | +45.7% | -10.4% | `target_reclaim` |
| 16 | Book 3 | `2025-10-27 20:00` | `2025-10-28 19:00` | 23.0h | `$336.3704` | `$308.6871` | **-8.23%** | **-8.59%** | +3.8% | -8.3% | `stop_loss` |
| 17 | Book 3 | `2026-09-10 12:00` | `2026-09-10 22:00` | 10.0h | `$1188.3414` | `$1090.5409` | **-8.23%** | **-8.59%** | +3.0% | -8.4% | `stop_loss` |
| 18 | Book 3 | `2026-09-19 17:00` | `2026-09-21 11:00` | 42.0h | `$1487.4144` | `$1549.3900` | **+4.17%** | **+4.08%** | +5.8% | -4.0% | `target_reclaim` |
| 19 | Book 3 | `2026-09-23 22:00` | `2026-09-26 21:00` | 71.0h | `$1490.0831` | `$1629.9400` | **+9.39%** | **+8.97%** | +14.0% | -2.4% | `target_reclaim` |
| 20 | Book 3 | `2026-09-28 19:00` | `2026-09-29 02:00` | 7.0h | `$1492.5214` | `$1369.6869` | **-8.23%** | **-8.59%** | +1.5% | -8.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `12` | `100.0%` | **`+106.4%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-1.7%`** |
| `stall_bailout` | `1` | `0.0%` | **`-0.4%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZEC`

* **Total Candidate Breakouts Filtered (Vetoed):** `1410`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `487` (34.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `192`
* **Saved Capital Losses Avoided:** `+5,430.9%`
* **Missed Upside Forgone:** `-5,508.2%`
* **Net Veto Alpha:** `+-77.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `674` | `47.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `434` | `30.8%` |
| `Core 4: Defensible Whale Dump` | `219` | `15.5%` |
| `Core 4: Whale Firewall` | `52` | `3.7%` |
| `Core 4: Funding Rate Cap` | `25` | `1.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `6` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*