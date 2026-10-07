# Kronos V12: Institutional Symbol Tear Sheet — `MAGIC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `24` (`24` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `24` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`54.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.233`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+17.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.20x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.75%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-28.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.9% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-03-22 00:00` | `2023-03-23 13:00` | 37.0h | `$1.8340` | `$1.6831` | **-8.23%** | **-8.59%** | +6.0% | -13.2% | `stop_loss` |
| 2 | Book 3 | `2023-10-03 12:00` | `2023-10-06 12:00` | 72.0h | `$0.5370` | `$0.5533` | **+3.04%** | **+2.99%** | +6.3% | -6.9% | `time_expiry` |
| 3 | Book 3 | `2023-10-26 14:00` | `2023-10-26 23:00` | 9.0h | `$0.5561` | `$0.6045` | **+8.70%** | **+8.34%** | +9.0% | -1.1% | `target_reclaim` |
| 4 | Book 3 | `2023-10-31 12:00` | `2023-11-03 12:00` | 72.0h | `$0.5910` | `$0.5654` | **-4.34%** | **-4.43%** | +6.4% | -7.3% | `time_expiry` |
| 5 | Book 3 | `2023-11-11 22:00` | `2023-11-14 00:00` | 50.0h | `$0.6762` | `$0.6205` | **-8.23%** | **-8.59%** | +5.8% | -8.3% | `stop_loss` |
| 6 | Book 3 | `2023-12-07 08:00` | `2023-12-07 16:00` | 8.0h | `$0.8512` | `$0.9252` | **+8.70%** | **+8.34%** | +10.8% | -3.8% | `target_reclaim` |
| 7 | Book 3 | `2023-12-13 02:00` | `2023-12-16 02:00` | 72.0h | `$0.8944` | `$0.8703` | **-2.70%** | **-2.73%** | +4.4% | -5.8% | `time_expiry` |
| 8 | Book 3 | `2023-12-28 21:00` | `2023-12-31 21:00` | 72.0h | `$1.1275` | `$1.0944` | **-2.94%** | **-2.98%** | +1.9% | -6.8% | `time_expiry` |
| 9 | Book 3 | `2024-02-20 15:00` | `2024-02-23 15:00` | 72.0h | `$1.3382` | `$1.2281` | **-8.23%** | **-8.59%** | +3.6% | -8.7% | `stop_loss` |
| 10 | Book 3 | `2024-03-10 14:00` | `2024-03-13 08:00` | 66.0h | `$1.3789` | `$1.4988` | **+8.70%** | **+8.34%** | +10.3% | -7.4% | `target_reclaim` |
| 11 | Book 3 | `2024-09-18 15:00` | `2024-09-19 07:00` | 16.0h | `$0.3407` | `$0.3703` | **+8.70%** | **+8.34%** | +8.9% | -1.5% | `target_reclaim` |
| 12 | Book 3 | `2024-09-30 09:00` | `2024-10-01 17:00` | 32.0h | `$0.3824` | `$0.3509` | **-8.23%** | **-8.59%** | +5.9% | -9.2% | `stop_loss` |
| 13 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$0.3914` | `$0.3592` | **-8.23%** | **-8.59%** | +5.0% | -9.3% | `stop_loss` |
| 14 | Book 3 | `2024-11-19 05:00` | `2024-11-20 18:00` | 37.0h | `$0.4243` | `$0.3894` | **-8.23%** | **-8.59%** | +5.5% | -9.4% | `stop_loss` |
| 15 | Book 3 | `2024-12-02 08:00` | `2024-12-03 00:00` | 16.0h | `$0.5497` | `$0.5975` | **+8.70%** | **+8.34%** | +11.8% | -4.7% | `target_reclaim` |
| 16 | Book 3 | `2024-12-03 13:00` | `2024-12-03 20:00` | 7.0h | `$0.5696` | `$0.6191` | **+8.70%** | **+8.34%** | +9.3% | -3.4% | `target_reclaim` |
| 17 | Book 3 | `2024-12-09 07:00` | `2024-12-09 20:00` | 13.0h | `$0.6605` | `$0.6061` | **-8.23%** | **-8.59%** | +1.5% | -10.1% | `stop_loss` |
| 18 | Book 3 | `2025-04-19 18:00` | `2025-04-19 19:00` | 1.0h | `$0.1156` | `$0.1256` | **+8.70%** | **+8.34%** | +15.5% | -0.7% | `target_reclaim` |
| 19 | Book 3 | `2025-04-20 09:00` | `2025-04-20 14:00` | 5.0h | `$0.1317` | `$0.1432` | **+8.70%** | **+8.34%** | +34.4% | -4.3% | `target_reclaim` |
| 20 | Book 3 | `2025-04-23 16:00` | `2025-04-24 17:00` | 25.0h | `$0.1981` | `$0.2153` | **+8.70%** | **+8.34%** | +19.9% | -6.6% | `target_reclaim` |
| 21 | Book 3 | `2025-07-10 06:00` | `2025-07-11 00:00` | 18.0h | `$0.1802` | `$0.1959` | **+8.70%** | **+8.34%** | +8.7% | -5.6% | `target_reclaim` |
| 22 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0452` | `$0.0452` | **+0.06%** | **+0.06%** | +9.2% | -7.7% | `time_expiry` |
| 23 | Book 3 | `2026-08-30 23:00` | `2026-09-02 23:00` | 72.0h | `$0.0455` | `$0.0426` | **-6.40%** | **-6.62%** | +3.8% | -7.0% | `time_expiry` |
| 24 | Book 3 | `2026-09-30 06:00` | `2026-10-01 16:00` | 34.0h | `$0.0507` | `$0.0551` | **+8.70%** | **+8.34%** | +10.3% | -1.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `11` | `100.0%` | **`+91.7%`** |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `time_expiry` | `6` | `33.3%` | **`-13.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `MAGIC`

* **Total Candidate Breakouts Filtered (Vetoed):** `111`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `83` (74.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+1,056.4%`
* **Missed Upside Forgone:** `-465.1%`
* **Net Veto Alpha:** `+591.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `38` | `34.2%` |
| `Core 1: Macro Bear Veto` | `26` | `23.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `24` | `21.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `23` | `20.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*