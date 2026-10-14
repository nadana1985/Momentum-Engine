# Kronos V12: Institutional Symbol Tear Sheet — `GMT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `24` (`24` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `24` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`58.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.662`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+46.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.59x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+1.93%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-26.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`40.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.7% / -6.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-01-24 22:00` | `2023-01-25 21:00` | 23.0h | `$0.5193` | `$0.5868` | **+13.00%** | **+12.22%** | +13.5% | -1.8% | `target_reclaim` |
| 2 | Book 3 | `2023-03-20 02:00` | `2023-03-21 07:00` | 29.0h | `$0.4336` | `$0.3979` | **-8.23%** | **-8.59%** | +3.8% | -9.6% | `stop_loss` |
| 3 | Book 2 | `2023-06-20 17:00` | `2023-06-27 17:00` | 168.0h | `$0.2073` | `$0.2287` | **+12.71%** | **+12.10%** | +19.3% | -3.0% | `time_cap` |
| 4 | Book 3 | `2023-07-14 16:00` | `2023-07-14 18:00` | 2.0h | `$0.2372` | `$0.2177` | **-8.23%** | **-8.59%** | +2.7% | -8.6% | `stop_loss` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2023-07-17 13:00` | `2023-07-21 13:00` | Live | `$0.2350` | `$0.2549` | **+8.50%** | **+8.16%** | +0.0% | -20.5% | `shelf_target_reclaim` |
| 6 | Book 3 | `2023-07-18 16:00` | `2023-07-21 16:00` | 72.0h | `$0.2363` | `$0.2281` | **-3.47%** | **-3.53%** | +4.2% | -4.2% | `time_expiry` |
| 7 | Book 3 | `2023-10-02 18:00` | `2023-10-05 18:00` | 72.0h | `$0.1561` | `$0.1493` | **-4.34%** | **-4.43%** | +3.3% | -5.3% | `time_expiry` |
| 8 | Book 3 | `2023-10-24 15:00` | `2023-10-24 16:00` | 1.0h | `$0.1547` | `$0.1618` | **+4.58%** | **+4.47%** | +7.9% | -0.5% | `target_reclaim` |
| 9 | Book 3 | `2023-11-18 07:00` | `2023-11-19 23:00` | 40.0h | `$0.2358` | `$0.2628` | **+11.45%** | **+10.84%** | +12.3% | -0.1% | `target_reclaim` |
| 10 | Book 3 | `2024-01-02 07:00` | `2024-01-02 15:00` | 8.0h | `$0.3424` | `$0.3570` | **+4.27%** | **+4.18%** | +4.3% | -0.9% | `target_reclaim` |
| 11 | Book 3 | `2024-01-03 07:00` | `2024-01-03 12:00` | 5.0h | `$0.3424` | `$0.3142` | **-8.23%** | **-8.59%** | +2.8% | -25.7% | `stop_loss` |
| 12 | Book 3 | `2024-01-08 02:00` | `2024-01-08 04:00` | 2.0h | `$0.3448` | `$0.3976` | **+15.30%** | **+14.23%** | +17.9% | -4.2% | `target_reclaim` |
| 13 | Book 3 | `2024-02-16 15:00` | `2024-02-17 00:00` | 9.0h | `$0.2681` | `$0.2793` | **+4.17%** | **+4.08%** | +4.6% | -0.8% | `target_reclaim` |
| 14 | Book 3 | `2024-02-20 15:00` | `2024-02-20 20:00` | 5.0h | `$0.2720` | `$0.2833` | **+4.17%** | **+4.08%** | +4.6% | -2.7% | `target_reclaim` |
| 15 | Book 3 | `2024-02-28 17:00` | `2024-02-29 02:00` | 9.0h | `$0.2674` | `$0.2911` | **+8.87%** | **+8.50%** | +12.4% | -7.2% | `target_reclaim` |
| 16 | Book 3 | `2024-03-29 07:00` | `2024-04-01 07:00` | 72.0h | `$0.3689` | `$0.3618` | **-1.93%** | **-1.95%** | +9.9% | -5.2% | `time_expiry` |
| 17 | Book 3 | `2024-06-03 21:00` | `2024-06-06 00:00` | 51.0h | `$0.2364` | `$0.2463` | **+4.17%** | **+4.08%** | +4.2% | -2.3% | `target_reclaim` |
| 18 | Book 4 | `2024-11-16 23:00` | `2024-11-23 13:00` | 158.0h | `$0.1628` | `$0.1953` | **+23.07%** | **+21.10%** | +25.0% | -7.9% | `target_reclaim` |
| 19 | Book 3 | `2025-05-03 00:00` | `2025-05-04 04:00` | 28.0h | `$0.0573` | `$0.0526` | **-8.23%** | **-8.59%** | +1.9% | -8.0% | `stop_loss` |
| 20 | Book 3 | `2025-05-15 07:00` | `2025-05-17 13:00` | 54.0h | `$0.0603` | `$0.0553` | **-8.23%** | **-8.59%** | +2.6% | -8.7% | `stop_loss` |
| 21 | Book 3 | `2025-07-18 20:00` | `2025-07-20 00:00` | 28.0h | `$0.0514` | `$0.0535` | **+4.17%** | **+4.08%** | +4.2% | -1.5% | `target_reclaim` |
| 22 | Book 3 | `2025-07-23 13:00` | `2025-07-25 15:00` | 50.0h | `$0.0519` | `$0.0476` | **-8.23%** | **-8.59%** | +5.3% | -8.6% | `stop_loss` |
| 23 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0068` | `$0.0071` | **+4.34%** | **+4.25%** | +15.1% | -2.7% | `target_reclaim` |
| 24 | Book 3 | `2026-10-07 01:00` | `2026-10-08 15:00` | 38.0h | `$0.0086` | `$0.0079` | **-8.23%** | **-8.59%** | +2.8% | -11.5% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `12` | `100.0%` | **`+96.1%`** |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `time_expiry` | `3` | `0.0%` | **`-9.9%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_cap` | `1` | `100.0%` | **`+12.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `GMT`

* **Total Candidate Breakouts Filtered (Vetoed):** `649`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `374` (57.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `63`
* **Saved Capital Losses Avoided:** `+4,880.2%`
* **Missed Upside Forgone:** `-2,658.4%`
* **Net Veto Alpha:** `+2,221.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `326` | `50.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `221` | `34.1%` |
| `Core 1: Macro Bear Veto` | `43` | `6.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `40` | `6.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `19` | `2.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*