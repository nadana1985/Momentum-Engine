# Kronos V12: Institutional Symbol Tear Sheet — `RSR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `22` (`22` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `22` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`81.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.173`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+109.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.97x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.95%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`23.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.6% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2022-03-28 23:00` | `2022-03-29 12:00` | 13.0h | `$0.0158` | `$0.0172` | **+8.70%** | **+8.34%** | +8.7% | -3.0% | `target_reclaim` |
| 2 | Book 3 | `2023-01-14 09:00` | `2023-01-16 01:00` | 40.0h | `$0.0037` | `$0.0040` | **+8.70%** | **+8.34%** | +8.8% | -3.6% | `target_reclaim` |
| 3 | Book 3 | `2023-01-18 15:00` | `2023-01-20 21:00` | 54.0h | `$0.0037` | `$0.0041` | **+8.70%** | **+8.34%** | +12.9% | -7.1% | `target_reclaim` |
| 4 | Book 3 | `2023-04-02 15:00` | `2023-04-04 12:00` | 45.0h | `$0.0042` | `$0.0046` | **+8.70%** | **+8.34%** | +8.9% | -5.3% | `target_reclaim` |
| 5 | Book 3 | `2023-10-31 15:00` | `2023-11-01 19:00` | 28.0h | `$0.0020` | `$0.0022` | **+8.70%** | **+8.34%** | +8.9% | -2.4% | `target_reclaim` |
| 6 | Book 3 | `2023-11-07 15:00` | `2023-11-08 16:00` | 25.0h | `$0.0024` | `$0.0026` | **+8.70%** | **+8.34%** | +9.4% | -3.5% | `target_reclaim` |
| 7 | Book 3 | `2023-11-09 16:00` | `2023-11-09 17:00` | 1.0h | `$0.0024` | `$0.0026` | **+8.70%** | **+8.34%** | +17.9% | -0.1% | `target_reclaim` |
| 8 | Book 3 | `2023-11-12 00:00` | `2023-11-14 00:00` | 48.0h | `$0.0027` | `$0.0025` | **-8.23%** | **-8.59%** | +6.8% | -9.0% | `stop_loss` |
| 9 | Book 3 | `2023-12-11 01:00` | `2023-12-11 02:00` | 1.0h | `$0.0029` | `$0.0027` | **-8.23%** | **-8.59%** | +2.0% | -14.4% | `stop_loss` |
| 10 | Book 3 | `2024-02-20 15:00` | `2024-02-22 05:00` | 38.0h | `$0.0027` | `$0.0029` | **+8.70%** | **+8.34%** | +9.6% | -2.4% | `target_reclaim` |
| 11 | Book 3 | `2024-02-28 17:00` | `2024-02-28 18:00` | 1.0h | `$0.0031` | `$0.0033` | **+8.70%** | **+8.34%** | +19.9% | -5.1% | `target_reclaim` |
| 12 | Book 3 | `2024-03-03 07:00` | `2024-03-03 08:00` | 1.0h | `$0.0037` | `$0.0040` | **+8.70%** | **+8.34%** | +12.1% | -1.6% | `target_reclaim` |
| 13 | Book 3 | `2024-03-04 17:00` | `2024-03-05 13:00` | 20.0h | `$0.0041` | `$0.0045` | **+8.70%** | **+8.34%** | +11.9% | -1.4% | `target_reclaim` |
| 14 | Book 3 | `2024-03-05 19:00` | `2024-03-05 23:00` | 4.0h | `$0.0042` | `$0.0045` | **+8.70%** | **+8.34%** | +10.0% | -13.8% | `target_reclaim` |
| 15 | Book 3 | `2024-03-14 13:00` | `2024-03-15 15:00` | 26.0h | `$0.0067` | `$0.0073` | **+8.70%** | **+8.34%** | +9.4% | -7.0% | `target_reclaim` |
| 16 | Book 3 | `2024-03-22 12:00` | `2024-03-22 17:00` | 5.0h | `$0.0077` | `$0.0084` | **+8.70%** | **+8.34%** | +9.3% | -0.4% | `target_reclaim` |
| 17 | Book 3 | `2024-05-20 01:00` | `2024-05-20 07:00` | 6.0h | `$0.0081` | `$0.0088` | **+8.70%** | **+8.34%** | +10.2% | -1.3% | `target_reclaim` |
| 18 | Book 3 | `2024-05-21 01:00` | `2024-05-22 05:00` | 28.0h | `$0.0091` | `$0.0084` | **-8.23%** | **-8.59%** | +2.3% | -8.0% | `stop_loss` |
| 19 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$0.0071` | `$0.0065` | **-8.23%** | **-8.59%** | +8.7% | -8.8% | `stop_loss` |
| 20 | Book 3 | `2024-11-24 15:00` | `2024-11-24 22:00` | 7.0h | `$0.0083` | `$0.0090` | **+8.70%** | **+8.34%** | +9.9% | -2.0% | `target_reclaim` |
| 21 | Book 3 | `2025-04-27 15:00` | `2025-04-29 06:00` | 39.0h | `$0.0088` | `$0.0096` | **+8.70%** | **+8.34%** | +8.8% | -4.4% | `target_reclaim` |
| 22 | Book 3 | `2025-08-14 12:00` | `2025-08-17 12:00` | 72.0h | `$0.0091` | `$0.0093` | **+1.62%** | **+1.61%** | +4.1% | -5.1% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `17` | `100.0%` | **`+141.7%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `RSR`

* **Total Candidate Breakouts Filtered (Vetoed):** `342`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `200` (58.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `50`
* **Saved Capital Losses Avoided:** `+2,825.0%`
* **Missed Upside Forgone:** `-2,298.0%`
* **Net Veto Alpha:** `+527.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `89` | `26.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `86` | `25.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `76` | `22.2%` |
| `Core 1: Macro Bear Veto` | `67` | `19.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `24` | `7.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*