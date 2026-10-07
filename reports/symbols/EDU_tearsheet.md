# Kronos V12: Institutional Symbol Tear Sheet — `EDU`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `16` (`16` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `16` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`43.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.747`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-15.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.85x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.00%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-25.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.6% / -7.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-10-03 15:00` | `2023-10-06 15:00` | 72.0h | `$0.4449` | `$0.4351` | **-2.20%** | **-2.23%** | +1.3% | -5.6% | `time_expiry` |
| 2 | Book 3 | `2023-11-13 14:00` | `2023-11-14 18:00` | 28.0h | `$0.5497` | `$0.5045` | **-8.23%** | **-8.59%** | +7.4% | -9.0% | `stop_loss` |
| 3 | Book 3 | `2023-11-30 07:00` | `2023-12-03 07:00` | 72.0h | `$0.6442` | `$0.6405` | **-0.57%** | **-0.57%** | +3.5% | -2.1% | `time_expiry` |
| 4 | Book 3 | `2023-12-07 07:00` | `2023-12-07 09:00` | 2.0h | `$0.7001` | `$0.6425` | **-8.23%** | **-8.59%** | +9.6% | -8.2% | `stop_loss` |
| 5 | Book 3 | `2023-12-07 15:00` | `2023-12-08 11:00` | 20.0h | `$0.7060` | `$0.7674` | **+8.70%** | **+8.34%** | +10.9% | -3.1% | `target_reclaim` |
| 6 | Book 3 | `2023-12-10 09:00` | `2023-12-11 02:00` | 17.0h | `$0.7080` | `$0.6498` | **-8.23%** | **-8.59%** | +2.5% | -14.5% | `stop_loss` |
| 7 | Book 3 | `2024-02-20 14:00` | `2024-02-22 18:00` | 52.0h | `$0.7918` | `$0.8607` | **+8.70%** | **+8.34%** | +9.2% | -6.5% | `target_reclaim` |
| 8 | Book 3 | `2024-02-23 04:00` | `2024-02-26 04:00` | 72.0h | `$0.8285` | `$0.8477` | **+2.32%** | **+2.29%** | +5.6% | -3.5% | `time_expiry` |
| 9 | Book 3 | `2024-03-05 16:00` | `2024-03-05 19:00` | 3.0h | `$0.8775` | `$0.8053` | **-8.23%** | **-8.59%** | +5.6% | -19.3% | `stop_loss` |
| 10 | Book 3 | `2024-05-26 06:00` | `2024-05-27 05:00` | 23.0h | `$0.9892` | `$1.0752` | **+8.70%** | **+8.34%** | +13.5% | -2.8% | `target_reclaim` |
| 11 | Book 3 | `2024-09-27 19:00` | `2024-09-28 02:00` | 7.0h | `$0.6604` | `$0.7178` | **+8.70%** | **+8.34%** | +9.2% | -1.1% | `target_reclaim` |
| 12 | Book 3 | `2025-01-18 05:00` | `2025-01-19 08:00` | 27.0h | `$0.5869` | `$0.5386` | **-8.23%** | **-8.59%** | +2.0% | -10.5% | `stop_loss` |
| 13 | Book 3 | `2025-04-28 11:00` | `2025-04-29 21:00` | 34.0h | `$0.1552` | `$0.1424` | **-8.23%** | **-8.59%** | +10.4% | -9.7% | `stop_loss` |
| 14 | Book 3 | `2025-05-13 02:00` | `2025-05-15 05:00` | 51.0h | `$0.1771` | `$0.1625` | **-8.23%** | **-8.59%** | +8.3% | -8.6% | `stop_loss` |
| 15 | Book 3 | `2025-07-22 04:00` | `2025-07-23 07:00` | 27.0h | `$0.1486` | `$0.1615` | **+8.70%** | **+8.34%** | +11.8% | -0.8% | `target_reclaim` |
| 16 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0404` | `$0.0416` | **+3.06%** | **+3.01%** | +11.3% | -8.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `target_reclaim` | `5` | `100.0%` | **`+41.7%`** |
| `time_expiry` | `4` | `50.0%` | **`+2.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `EDU`

* **Total Candidate Breakouts Filtered (Vetoed):** `147`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `82` (55.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+1,245.6%`
* **Missed Upside Forgone:** `-1,118.9%`
* **Net Veto Alpha:** `+126.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `52` | `35.4%` |
| `Core 1: Macro Bear Veto` | `43` | `29.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `30` | `20.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `22` | `15.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*