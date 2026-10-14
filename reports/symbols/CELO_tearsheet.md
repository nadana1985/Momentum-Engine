# Kronos V12: Institutional Symbol Tear Sheet — `CELO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `28` (`28` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `28` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.248`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+86.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.37x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.09%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-19.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`40.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.6% / -7.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-31 11:00` | `2022-11-02 11:00` | 48.0h | `$0.7429` | `$0.7022` | **-6.73%** | **-6.92%** | +3.0% | -6.6% | `fast_decay_cut` |
| 2 | Book 2 | `2022-12-15 05:00` | `2022-12-16 23:00` | 42.0h | `$0.5764` | `$0.5290` | **-10.13%** | **-10.57%** | +5.0% | -8.6% | `initial_stop` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2022-12-15 07:00` | `2022-12-19 07:00` | Live | `$0.5290` | `$0.5740` | **+8.50%** | **+8.16%** | +3.5% | -21.9% | `shelf_target_reclaim` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2022-12-25 00:00` | `2022-12-29 00:00` | Live | `$0.4812` | `$0.5221` | **+8.50%** | **+8.16%** | +1.3% | -14.1% | `shelf_target_reclaim` |
| 5 | Book 3 | `2023-01-24 22:00` | `2023-01-26 04:00` | 30.0h | `$0.6846` | `$0.7730` | **+12.92%** | **+12.15%** | +13.8% | -3.6% | `target_reclaim` |
| 6 | Book 4 | `2023-02-20 02:00` | `2023-02-24 16:00` | 110.0h | `$0.8903` | `$0.7568` | **-18.12%** | **-19.64%** | +3.8% | -15.1% | `structural_stop` |
| 7 | Book 3 | `2023-03-31 00:00` | `2023-03-31 09:00` | 9.0h | `$0.6408` | `$0.7060` | **+10.17%** | **+9.69%** | +10.6% | -1.1% | `target_reclaim` |
| 8 | Book 5 (Shelf Absorption Squeeze) | `2023-07-02 12:00` | `2023-07-06 12:00` | Live | `$0.5023` | `$0.5450` | **+8.50%** | **+8.16%** | +12.6% | -14.1% | `shelf_target_reclaim` |
| 9 | Book 3 | `2023-07-05 08:00` | `2023-07-06 14:00` | 30.0h | `$0.5324` | `$0.4886` | **-8.23%** | **-8.59%** | +1.2% | -8.2% | `stop_loss` |
| 10 | Book 5 (Shelf Absorption Squeeze) | `2023-07-31 15:00` | `2023-08-04 15:00` | Live | `$0.4784` | `$0.5191` | **+8.50%** | **+8.16%** | +2.9% | -29.6% | `shelf_target_reclaim` |
| 11 | Book 2 | `2023-10-16 05:00` | `2023-10-17 13:00` | 32.0h | `$0.4311` | `$0.4070` | **-6.18%** | **-6.36%** | +1.8% | -6.3% | `initial_stop` |
| 12 | Book 4 | `2023-11-01 19:00` | `2023-11-02 10:00` | 15.0h | `$0.5178` | `$0.6213` | **+13.96%** | **+13.16%** | +20.7% | -0.3% | `target_reclaim` |
| 13 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$0.5513` | `$0.5825` | **+5.67%** | **+5.51%** | +9.6% | -6.4% | `time_expiry` |
| 14 | Book 3 | `2023-12-26 17:00` | `2023-12-27 14:00` | 21.0h | `$0.7001` | `$0.7610` | **+8.70%** | **+8.34%** | +17.1% | -3.2% | `target_reclaim` |
| 15 | Book 3 | `2024-02-20 09:00` | `2024-02-22 21:00` | 60.0h | `$0.7489` | `$0.7910` | **+5.62%** | **+5.47%** | +6.2% | -6.4% | `target_reclaim` |
| 16 | Book 3 | `2024-02-28 17:00` | `2024-02-29 07:00` | 14.0h | `$0.8424` | `$0.9770` | **+15.97%** | **+14.82%** | +19.5% | -5.5% | `target_reclaim` |
| 17 | Book 3 | `2024-03-12 08:00` | `2024-03-14 04:00` | 44.0h | `$1.5484` | `$1.4209` | **-8.23%** | **-8.59%** | +3.3% | -8.1% | `stop_loss` |
| 18 | Book 3 | `2024-09-30 00:00` | `2024-10-01 05:00` | 29.0h | `$0.6605` | `$0.6950` | **+5.23%** | **+5.10%** | +6.0% | -4.8% | `target_reclaim` |
| 19 | Book 3 | `2024-10-01 16:00` | `2024-10-02 02:00` | 10.0h | `$0.6687` | `$0.7200` | **+7.68%** | **+7.40%** | +8.1% | -2.9% | `target_reclaim` |
| 20 | Book 3 | `2024-10-13 15:00` | `2024-10-14 07:00` | 16.0h | `$0.7661` | `$0.8310` | **+8.47%** | **+8.13%** | +11.2% | -0.5% | `target_reclaim` |
| 21 | Book 3 | `2025-07-08 09:00` | `2025-07-08 23:00` | 14.0h | `$0.2899` | `$0.3020` | **+4.17%** | **+4.08%** | +4.5% | -0.7% | `target_reclaim` |
| 22 | Book 3 | `2025-07-14 15:00` | `2025-07-15 23:00` | 32.0h | `$0.3293` | `$0.3430` | **+4.17%** | **+4.08%** | +4.2% | -4.0% | `target_reclaim` |
| 23 | Book 3 | `2025-07-23 21:00` | `2025-07-26 21:00` | 72.0h | `$0.3453` | `$0.3561` | **+3.14%** | **+3.09%** | +4.6% | -5.0% | `time_expiry` |
| 24 | Book 3 | `2025-08-14 21:00` | `2025-08-17 21:00` | 72.0h | `$0.3322` | `$0.3421` | **+2.99%** | **+2.95%** | +7.5% | -3.4% | `time_expiry` |
| 25 | Book 3 | `2025-10-27 23:00` | `2025-10-30 13:00` | 62.0h | `$0.2540` | `$0.2331` | **-8.23%** | **-8.59%** | +3.1% | -9.1% | `stop_loss` |
| 26 | Book 3 | `2026-09-23 20:00` | `2026-09-26 00:00` | 52.0h | `$0.0894` | `$0.0972` | **+8.70%** | **+8.34%** | +10.1% | -2.3% | `target_reclaim` |
| 27 | Book 3 | `2026-09-28 03:00` | `2026-09-29 00:00` | 21.0h | `$0.0914` | `$0.0993` | **+8.70%** | **+8.34%** | +11.2% | -2.5% | `target_reclaim` |
| 28 | Book 3 | `2026-09-30 00:00` | `2026-10-03 00:00` | 72.0h | `$0.0988` | `$0.1012` | **+2.42%** | **+2.39%** | +6.2% | -4.2% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `13` | `100.0%` | **`+109.1%`** |
| `time_expiry` | `4` | `100.0%` | **`+13.9%`** |
| `shelf_target_reclaim` | `4` | `100.0%` | **`+32.6%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `initial_stop` | `2` | `0.0%` | **`-16.9%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-6.9%`** |
| `structural_stop` | `1` | `0.0%` | **`-19.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CELO`

* **Total Candidate Breakouts Filtered (Vetoed):** `787`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `468` (59.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `43`
* **Saved Capital Losses Avoided:** `+8,719.7%`
* **Missed Upside Forgone:** `-1,194.3%`
* **Net Veto Alpha:** `+7,525.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `364` | `46.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `193` | `24.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `167` | `21.2%` |
| `Core 1: Macro Bear Veto` | `54` | `6.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `9` | `1.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*