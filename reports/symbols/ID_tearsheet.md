# Kronos V12: Institutional Symbol Tear Sheet — `ID`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `22` (`22` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `22` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`45.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.777`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-19.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.82x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.90%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-59.2%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`40.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.1% / -6.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-10-24 15:00` | `2023-10-25 01:00` | 10.0h | `$0.1944` | `$0.2025` | **+4.17%** | **+4.08%** | +4.3% | -2.9% | `target_reclaim` |
| 2 | Book 3 | `2023-11-14 00:00` | `2023-11-14 18:00` | 18.0h | `$0.2659` | `$0.2441` | **-8.23%** | **-8.59%** | +3.9% | -12.6% | `stop_loss` |
| 3 | Book 3 | `2023-11-30 09:00` | `2023-11-30 14:00` | 5.0h | `$0.3053` | `$0.2802` | **-8.23%** | **-8.59%** | +9.4% | -9.9% | `stop_loss` |
| 4 | Book 3 | `2024-02-18 02:00` | `2024-02-18 23:00` | 21.0h | `$0.6001` | `$0.6251` | **+4.17%** | **+4.08%** | +5.8% | -1.4% | `target_reclaim` |
| 5 | Book 3 | `2024-02-20 15:00` | `2024-02-23 15:00` | 72.0h | `$0.6275` | `$0.6020` | **-4.07%** | **-4.15%** | +6.0% | -5.8% | `time_expiry` |
| 6 | Book 3 | `2024-03-18 06:00` | `2024-03-19 01:00` | 19.0h | `$1.6643` | `$1.5273` | **-8.23%** | **-8.59%** | +4.3% | -9.8% | `stop_loss` |
| 7 | Book 3 | `2024-07-21 18:00` | `2024-07-24 18:00` | 72.0h | `$0.4629` | `$0.4552` | **-1.66%** | **-1.67%** | +5.5% | -1.8% | `time_expiry` |
| 8 | Book 2 | `2024-08-11 01:00` | `2024-08-12 07:00` | 30.0h | `$0.3851` | `$0.3534` | **-9.75%** | **-10.18%** | +4.8% | -8.3% | `initial_stop` |
| 9 | Book 3 | `2024-08-14 13:00` | `2024-08-17 13:00` | 72.0h | `$0.3716` | `$0.3558` | **-4.25%** | **-4.34%** | +2.4% | -7.5% | `time_expiry` |
| 10 | Book 3 | `2024-10-25 07:00` | `2024-10-25 23:00` | 16.0h | `$0.4212` | `$0.3866` | **-8.23%** | **-8.59%** | +2.0% | -12.8% | `stop_loss` |
| 11 | Book 3 | `2024-11-12 10:00` | `2024-11-15 04:00` | 66.0h | `$0.4280` | `$0.3928` | **-8.23%** | **-8.59%** | +7.8% | -8.4% | `stop_loss` |
| 12 | Book 4 | `2024-11-16 18:00` | `2024-11-27 15:00` | 261.0h | `$0.4557` | `$0.5468` | **+24.29%** | **+22.12%** | +21.9% | -10.8% | `target_reclaim` |
| 13 | Book 3 | `2024-12-02 08:00` | `2024-12-03 05:00` | 21.0h | `$0.5484` | `$0.5961` | **+8.70%** | **+8.34%** | +9.5% | -1.8% | `target_reclaim` |
| 14 | Book 3 | `2025-04-28 01:00` | `2025-04-28 08:00` | 7.0h | `$0.1898` | `$0.2062` | **+8.70%** | **+8.34%** | +14.7% | -0.8% | `target_reclaim` |
| 15 | Book 3 | `2025-05-03 09:00` | `2025-05-04 19:00` | 34.0h | `$0.2102` | `$0.1929` | **-8.23%** | **-8.59%** | +0.6% | -8.4% | `stop_loss` |
| 16 | Book 3 | `2025-05-12 18:00` | `2025-05-12 21:00` | 3.0h | `$0.2245` | `$0.2339` | **+4.17%** | **+4.08%** | +5.2% | -3.2% | `target_reclaim` |
| 17 | Book 3 | `2025-05-15 04:00` | `2025-05-15 14:00` | 10.0h | `$0.2280` | `$0.2093` | **-8.23%** | **-8.59%** | +1.0% | -8.3% | `stop_loss` |
| 18 | Book 3 | `2025-07-14 14:00` | `2025-07-16 00:00` | 34.0h | `$0.1751` | `$0.1824` | **+4.17%** | **+4.08%** | +4.3% | -5.4% | `target_reclaim` |
| 19 | Book 3 | `2025-07-17 16:00` | `2025-07-18 02:00` | 10.0h | `$0.1769` | `$0.1842` | **+4.17%** | **+4.08%** | +4.6% | -1.4% | `target_reclaim` |
| 20 | Book 3 | `2025-07-18 19:00` | `2025-07-20 15:00` | 44.0h | `$0.1790` | `$0.1898` | **+6.06%** | **+5.89%** | +6.4% | -3.1% | `target_reclaim` |
| 21 | Book 3 | `2025-09-22 06:00` | `2025-09-25 03:00` | 69.0h | `$0.1605` | `$0.1473` | **-8.23%** | **-8.59%** | +1.1% | -8.3% | `stop_loss` |
| 22 | Book 3 | `2026-08-22 05:00` | `2026-08-22 08:00` | 3.0h | `$0.0321` | `$0.0334` | **+4.17%** | **+4.08%** | +8.0% | -6.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `10` | `100.0%` | **`+69.2%`** |
| `stop_loss` | `8` | `0.0%` | **`-68.7%`** |
| `time_expiry` | `3` | `0.0%` | **`-10.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-10.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ID`

* **Total Candidate Breakouts Filtered (Vetoed):** `298`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `164` (55.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `22`
* **Saved Capital Losses Avoided:** `+2,055.5%`
* **Missed Upside Forgone:** `-887.9%`
* **Net Veto Alpha:** `+1,167.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `241` | `80.9%` |
| `Core 1: Macro Bear Veto` | `26` | `8.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `25` | `8.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `2.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*