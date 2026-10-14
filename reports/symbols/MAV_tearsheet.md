# Kronos V12: Institutional Symbol Tear Sheet — `MAV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `19` (`19` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `19` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`52.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.121`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+9.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.10x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.49%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-34.4%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`25.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.7% / -8.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-10-02 14:00` | `2023-10-03 12:00` | 22.0h | `$0.2839` | `$0.2606` | **-8.23%** | **-8.59%** | +2.4% | -8.4% | `stop_loss` |
| 2 | Book 3 | `2023-10-26 21:00` | `2023-10-29 21:00` | 72.0h | `$0.2316` | `$0.2350` | **+1.45%** | **+1.44%** | +7.7% | -5.7% | `time_expiry` |
| 3 | Book 3 | `2023-11-14 00:00` | `2023-11-14 05:00` | 5.0h | `$0.2802` | `$0.2969` | **+5.94%** | **+5.77%** | +7.4% | -1.8% | `target_reclaim` |
| 4 | Book 3 | `2023-12-04 11:00` | `2023-12-04 23:00` | 12.0h | `$0.2946` | `$0.3398` | **+15.33%** | **+14.27%** | +24.2% | -6.8% | `target_reclaim` |
| 5 | Book 3 | `2023-12-17 16:00` | `2023-12-18 07:00` | 15.0h | `$0.3870` | `$0.3551` | **-8.23%** | **-8.59%** | +3.4% | -10.9% | `stop_loss` |
| 6 | Book 3 | `2024-01-03 12:00` | `2024-01-03 13:00` | 1.0h | `$0.4180` | `$0.4488` | **+7.38%** | **+7.12%** | +24.2% | -20.1% | `target_reclaim` |
| 7 | Book 5 (Shelf Absorption Squeeze) | `2024-01-16 07:00` | `2024-01-20 07:00` | Live | `$0.5176` | `$0.5616` | **+8.50%** | **+8.16%** | +30.3% | -13.8% | `shelf_target_reclaim` |
| 8 | Book 3 | `2024-01-19 04:00` | `2024-01-20 17:00` | 37.0h | `$0.5457` | `$0.5007` | **-8.23%** | **-8.59%** | +3.5% | -8.2% | `stop_loss` |
| 9 | Book 3 | `2024-02-01 01:00` | `2024-02-01 17:00` | 16.0h | `$0.6642` | `$0.7237` | **+8.96%** | **+8.58%** | +12.3% | -1.3% | `target_reclaim` |
| 10 | Book 3 | `2024-03-03 07:00` | `2024-03-05 19:00` | 60.0h | `$0.6767` | `$0.6210` | **-8.23%** | **-8.59%** | +8.9% | -30.2% | `stop_loss` |
| 11 | Book 3 | `2024-04-03 00:00` | `2024-04-03 17:00` | 17.0h | `$0.6906` | `$0.6338` | **-8.23%** | **-8.59%** | +5.5% | -8.3% | `stop_loss` |
| 12 | Book 3 | `2024-09-29 07:00` | `2024-09-30 23:00` | 40.0h | `$0.2323` | `$0.2132` | **-8.23%** | **-8.59%** | +6.1% | -8.1% | `stop_loss` |
| 13 | Book 3 | `2024-11-12 09:00` | `2024-11-12 10:00` | 1.0h | `$0.1858` | `$0.1705` | **-8.23%** | **-8.59%** | +4.8% | -9.3% | `stop_loss` |
| 14 | Book 4 | `2024-11-27 16:00` | `2024-11-30 12:00` | 68.0h | `$0.2481` | `$0.2977` | **+25.56%** | **+23.17%** | +20.2% | -2.2% | `target_reclaim` |
| 15 | Book 3 | `2024-12-02 08:00` | `2024-12-03 06:00` | 22.0h | `$0.2848` | `$0.3095` | **+8.70%** | **+8.34%** | +9.3% | -3.4% | `target_reclaim` |
| 16 | Book 3 | `2024-12-04 16:00` | `2024-12-06 00:00` | 32.0h | `$0.2987` | `$0.3163` | **+5.88%** | **+5.71%** | +6.1% | -4.5% | `target_reclaim` |
| 17 | Book 3 | `2025-05-12 18:00` | `2025-05-13 16:00` | 22.0h | `$0.0766` | `$0.0798` | **+4.17%** | **+4.08%** | +5.3% | -4.4% | `target_reclaim` |
| 18 | Book 3 | `2025-07-01 09:00` | `2025-07-01 10:00` | 1.0h | `$0.0716` | `$0.0657` | **-8.23%** | **-8.59%** | +11.6% | -10.4% | `stop_loss` |
| 19 | Book 3 | `2025-07-28 01:00` | `2025-07-28 11:00` | 10.0h | `$0.0582` | `$0.0534` | **-8.23%** | **-8.59%** | +10.5% | -8.3% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `9` | `0.0%` | **`-77.3%`** |
| `target_reclaim` | `8` | `100.0%` | **`+77.0%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `MAV`

* **Total Candidate Breakouts Filtered (Vetoed):** `555`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `347` (62.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `54`
* **Saved Capital Losses Avoided:** `+5,292.1%`
* **Missed Upside Forgone:** `-1,224.8%`
* **Net Veto Alpha:** `+4,067.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `388` | `69.9%` |
| `Core 1: Macro Bear Veto` | `110` | `19.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `42` | `7.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `15` | `2.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*