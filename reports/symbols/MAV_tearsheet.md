# Kronos V12: Institutional Symbol Tear Sheet — `MAV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `19` (`19` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `19` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`47.4%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.961`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-3.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.16%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-18.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`21.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.8% / -7.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-10-02 14:00` | `2023-10-03 17:00` | 27.0h | `$0.2757` | `$0.2530` | **-8.23%** | **-8.59%** | +5.5% | -8.8% | `stop_loss` |
| 2 | Book 3 | `2023-10-26 21:00` | `2023-10-29 21:00` | 72.0h | `$0.2368` | `$0.2350` | **-0.76%** | **-0.76%** | +5.4% | -7.8% | `time_expiry` |
| 3 | Book 3 | `2023-11-14 18:00` | `2023-11-15 04:00` | 10.0h | `$0.2731` | `$0.2969` | **+8.70%** | **+8.34%** | +10.3% | -4.3% | `target_reclaim` |
| 4 | Book 3 | `2023-12-04 11:00` | `2023-12-04 23:00` | 12.0h | `$0.3126` | `$0.3398` | **+8.70%** | **+8.34%** | +17.0% | -12.1% | `target_reclaim` |
| 5 | Book 3 | `2023-12-07 09:00` | `2023-12-07 12:00` | 3.0h | `$0.3342` | `$0.3633` | **+8.70%** | **+8.34%** | +9.4% | -1.3% | `target_reclaim` |
| 6 | Book 3 | `2023-12-17 16:00` | `2023-12-18 07:00` | 15.0h | `$0.3870` | `$0.3551` | **-8.23%** | **-8.59%** | +3.4% | -10.9% | `stop_loss` |
| 7 | Book 3 | `2024-01-03 12:00` | `2024-01-03 13:00` | 1.0h | `$0.4129` | `$0.4488` | **+8.70%** | **+8.34%** | +25.7% | -19.1% | `target_reclaim` |
| 8 | Book 3 | `2024-01-19 04:00` | `2024-01-20 17:00` | 37.0h | `$0.5457` | `$0.5007` | **-8.23%** | **-8.59%** | +3.5% | -8.2% | `stop_loss` |
| 9 | Book 3 | `2024-02-01 01:00` | `2024-02-01 17:00` | 16.0h | `$0.6658` | `$0.7237` | **+8.70%** | **+8.34%** | +12.1% | -1.5% | `target_reclaim` |
| 10 | Book 3 | `2024-03-03 07:00` | `2024-03-05 17:00` | 58.0h | `$0.6799` | `$0.6239` | **-8.23%** | **-8.59%** | +8.4% | -8.3% | `stop_loss` |
| 11 | Book 3 | `2024-04-03 00:00` | `2024-04-03 13:00` | 13.0h | `$0.6986` | `$0.6411` | **-8.23%** | **-8.59%** | +4.3% | -8.7% | `stop_loss` |
| 12 | Book 3 | `2024-09-25 23:00` | `2024-09-26 17:00` | 18.0h | `$0.2187` | `$0.2377` | **+8.70%** | **+8.34%** | +8.9% | -1.2% | `target_reclaim` |
| 13 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$0.1786` | `$0.1639` | **-8.23%** | **-8.59%** | +3.1% | -9.7% | `stop_loss` |
| 14 | Book 3 | `2024-12-02 08:00` | `2024-12-03 06:00` | 22.0h | `$0.2848` | `$0.3095` | **+8.70%** | **+8.34%** | +9.3% | -3.4% | `target_reclaim` |
| 15 | Book 3 | `2024-12-05 01:00` | `2024-12-06 00:00` | 23.0h | `$0.2910` | `$0.3163` | **+8.70%** | **+8.34%** | +8.9% | -1.9% | `target_reclaim` |
| 16 | Book 3 | `2024-12-08 05:00` | `2024-12-09 20:00` | 39.0h | `$0.3039` | `$0.2789` | **-8.23%** | **-8.59%** | +5.6% | -12.8% | `stop_loss` |
| 17 | Book 3 | `2025-05-13 03:00` | `2025-05-13 16:00` | 13.0h | `$0.0734` | `$0.0798` | **+8.70%** | **+8.34%** | +9.9% | -0.2% | `target_reclaim` |
| 18 | Book 3 | `2025-07-01 09:00` | `2025-07-01 10:00` | 1.0h | `$0.0716` | `$0.0657` | **-8.23%** | **-8.59%** | +11.6% | -10.4% | `stop_loss` |
| 19 | Book 3 | `2025-07-28 05:00` | `2025-07-28 12:00` | 7.0h | `$0.0562` | `$0.0516` | **-8.23%** | **-8.59%** | +4.4% | -10.3% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `9` | `0.0%` | **`-77.3%`** |
| `target_reclaim` | `9` | `100.0%` | **`+75.0%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `MAV`

* **Total Candidate Breakouts Filtered (Vetoed):** `112`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `79` (70.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+1,172.7%`
* **Missed Upside Forgone:** `-119.6%`
* **Net Veto Alpha:** `+1,053.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `58` | `51.8%` |
| `Core 1: Macro Bear Veto` | `26` | `23.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `15` | `13.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `13` | `11.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*