# Kronos V12: Institutional Symbol Tear Sheet — `UMA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `22` (`22` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `22` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`81.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`6.782`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+109.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`3.00x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.99%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`47.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.7% / -7.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-09-09 10:00` | `2023-09-13 10:00` | Live | `$1.3588` | `$1.4743` | **+8.50%** | **+8.16%** | +1.4% | -14.4% | `shelf_target_reclaim` |
| 2 | Book 3 | `2023-10-03 11:00` | `2023-10-04 23:00` | 36.0h | `$1.3725` | `$1.3546` | **-1.31%** | **-1.32%** | +1.0% | -4.8% | `stall_bailout` |
| 3 | Book 3 | `2023-10-16 13:00` | `2023-10-16 14:00` | 1.0h | `$1.6284` | `$1.7020` | **+4.52%** | **+4.42%** | +9.2% | -0.1% | `target_reclaim` |
| 4 | Book 3 | `2023-11-07 15:00` | `2023-11-08 16:00` | 25.0h | `$1.5542` | `$1.6390` | **+5.46%** | **+5.31%** | +5.5% | -1.3% | `target_reclaim` |
| 5 | Book 3 | `2023-11-09 16:00` | `2023-11-10 00:00` | 8.0h | `$1.5542` | `$1.6670` | **+7.26%** | **+7.01%** | +8.9% | -6.4% | `target_reclaim` |
| 6 | Book 4 | `2023-11-10 07:00` | `2023-11-28 16:00` | 441.0h | `$1.7496` | `$2.0995` | **+15.65%** | **+14.50%** | +22.7% | -7.8% | `target_reclaim` |
| 7 | Book 3 | `2023-11-28 19:00` | `2023-11-29 11:00` | 16.0h | `$1.9191` | `$2.0860` | **+8.70%** | **+8.34%** | +9.3% | -3.2% | `target_reclaim` |
| 8 | Book 3 | `2023-12-11 02:00` | `2023-12-11 23:00` | 21.0h | `$1.9909` | `$2.1570` | **+8.34%** | **+8.01%** | +11.5% | -10.0% | `target_reclaim` |
| 9 | Book 5 (Shelf Absorption Squeeze) | `2024-05-08 19:00` | `2024-05-12 19:00` | Live | `$3.3755` | `$3.6624` | **+8.50%** | **+8.16%** | +18.7% | -14.4% | `shelf_target_reclaim` |
| 10 | Book 5 (Shelf Absorption Squeeze) | `2024-07-26 05:00` | `2024-07-30 05:00` | Live | `$2.3248` | `$2.5225` | **+8.50%** | **+8.16%** | +5.6% | -40.9% | `shelf_target_reclaim` |
| 11 | Book 3 | `2024-09-22 16:00` | `2024-09-23 21:00` | 29.0h | `$2.3359` | `$2.4980` | **+6.94%** | **+6.71%** | +7.5% | -2.2% | `target_reclaim` |
| 12 | Book 3 | `2024-10-01 20:00` | `2024-10-02 02:00` | 6.0h | `$2.6807` | `$2.9650` | **+10.60%** | **+10.08%** | +11.0% | -1.1% | `target_reclaim` |
| 13 | Book 3 | `2024-11-24 12:00` | `2024-11-25 08:00` | 20.0h | `$2.7436` | `$3.0300` | **+10.44%** | **+9.93%** | +10.9% | -1.1% | `target_reclaim` |
| 14 | Book 3 | `2024-12-09 08:00` | `2024-12-09 20:00` | 12.0h | `$3.8346` | `$3.5190` | **-8.23%** | **-8.59%** | +6.4% | -8.7% | `stop_loss` |
| 15 | Book 3 | `2025-04-23 15:00` | `2025-04-25 06:00` | 39.0h | `$1.1616` | `$1.2100` | **+4.17%** | **+4.08%** | +4.5% | -1.8% | `target_reclaim` |
| 16 | Book 3 | `2025-04-26 13:00` | `2025-04-29 13:00` | 72.0h | `$1.1884` | `$1.1960` | **+0.64%** | **+0.64%** | +5.3% | -5.4% | `time_expiry` |
| 17 | Book 5 (Shelf Absorption Squeeze) | `2025-06-06 15:00` | `2025-06-10 15:00` | Live | `$1.2310` | `$1.3356` | **+8.50%** | **+8.16%** | +18.5% | -25.4% | `shelf_target_reclaim` |
| 18 | Book 3 | `2025-06-09 11:00` | `2025-06-09 12:00` | 1.0h | `$1.5777` | `$1.6740` | **+6.10%** | **+5.92%** | +17.5% | -1.4% | `target_reclaim` |
| 19 | Book 3 | `2025-07-17 20:00` | `2025-07-18 00:00` | 4.0h | `$1.1933` | `$1.2430` | **+4.17%** | **+4.08%** | +4.8% | -0.4% | `target_reclaim` |
| 20 | Book 3 | `2025-07-18 20:00` | `2025-07-20 15:00` | 43.0h | `$1.2181` | `$1.3070` | **+7.30%** | **+7.04%** | +8.0% | -3.9% | `target_reclaim` |
| 21 | Book 2 | `2026-09-19 16:00` | `2026-09-21 05:00` | 37.0h | `$0.3936` | `$0.3918` | **-0.48%** | **-0.48%** | +0.8% | -5.3% | `stall_bailout` |
| 22 | Book 3 | `2026-10-07 02:00` | `2026-10-08 17:00` | 39.0h | `$0.4086` | `$0.3750` | **-8.23%** | **-8.59%** | +2.8% | -9.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `13` | `100.0%` | **`+95.4%`** |
| `shelf_target_reclaim` | `4` | `100.0%` | **`+32.6%`** |
| `stall_bailout` | `2` | `0.0%` | **`-1.8%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+0.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `UMA`

* **Total Candidate Breakouts Filtered (Vetoed):** `430`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `228` (53.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `33`
* **Saved Capital Losses Avoided:** `+2,389.3%`
* **Missed Upside Forgone:** `-1,350.9%`
* **Net Veto Alpha:** `+1,038.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `169` | `39.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `121` | `28.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `94` | `21.9%` |
| `Core 1: Macro Bear Veto` | `43` | `10.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `3` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*