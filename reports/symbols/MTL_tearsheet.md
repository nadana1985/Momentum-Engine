# Kronos V12: Institutional Symbol Tear Sheet — `MTL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `28` (`28` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `28` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`67.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.971`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+69.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.00x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+2.48%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-35.8%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`31.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.6% / -7.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2022-03-30 01:00` | `2022-03-30 14:00` | 13.0h | `$1.8525` | `$2.0803` | **+12.30%** | **+11.60%** | +12.8% | -0.1% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2022-06-05 04:00` | `2022-06-09 04:00` | Live | `$1.3703` | `$1.4868` | **+8.50%** | **+8.16%** | +26.8% | -25.4% | `shelf_target_reclaim` |
| 3 | Book 2 | `2022-10-25 17:00` | `2022-10-27 20:00` | 51.0h | `$1.0152` | `$1.0033` | **-1.37%** | **-1.37%** | +3.4% | -2.4% | `fast_decay_cut` |
| 4 | Book 3 | `2023-02-05 12:00` | `2023-02-05 13:00` | 1.0h | `$0.9815` | `$1.0669` | **+8.70%** | **+8.34%** | +23.3% | -1.0% | `target_reclaim` |
| 5 | Book 3 | `2023-02-07 18:00` | `2023-02-09 03:00` | 33.0h | `$1.1160` | `$1.0241` | **-8.23%** | **-8.59%** | +6.3% | -8.6% | `stop_loss` |
| 6 | Book 5 (Shelf Absorption Squeeze) | `2023-02-19 00:00` | `2023-02-23 00:00` | Live | `$1.1634` | `$1.2623` | **+8.50%** | **+8.16%** | +28.5% | -13.0% | `shelf_target_reclaim` |
| 7 | Book 3 | `2023-02-19 23:00` | `2023-02-20 00:00` | 1.0h | `$1.6229` | `$1.7640` | **+8.70%** | **+8.34%** | +10.1% | -2.5% | `target_reclaim` |
| 8 | Book 3 | `2023-04-02 12:00` | `2023-04-05 12:00` | 72.0h | `$1.2447` | `$1.2631` | **+1.48%** | **+1.47%** | +2.6% | -6.8% | `time_expiry` |
| 9 | Book 3 | `2023-05-06 14:00` | `2023-05-06 22:00` | 8.0h | `$1.3058` | `$1.1983` | **-8.23%** | **-8.59%** | +2.7% | -8.7% | `stop_loss` |
| 10 | Book 5 (Shelf Absorption Squeeze) | `2023-06-03 14:00` | `2023-06-07 14:00` | Live | `$0.9986` | `$1.0834` | **+8.50%** | **+8.16%** | +111.9% | -10.6% | `shelf_target_reclaim` |
| 11 | Book 3 | `2023-07-12 15:00` | `2023-07-14 18:00` | 51.0h | `$1.4555` | `$1.3357` | **-8.23%** | **-8.59%** | +2.7% | -9.3% | `stop_loss` |
| 12 | Book 3 | `2023-10-18 02:00` | `2023-10-21 02:00` | 72.0h | `$1.2901` | `$1.2966` | **+0.50%** | **+0.50%** | +3.6% | -5.4% | `time_expiry` |
| 13 | Book 3 | `2023-11-12 00:00` | `2023-11-12 01:00` | 1.0h | `$1.8437` | `$2.0040` | **+8.70%** | **+8.34%** | +13.3% | -2.0% | `target_reclaim` |
| 14 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$1.5968` | `$1.6375` | **+2.55%** | **+2.52%** | +6.1% | -12.3% | `time_expiry` |
| 15 | Book 3 | `2024-02-20 15:00` | `2024-02-20 23:00` | 8.0h | `$1.5872` | `$1.7079` | **+7.60%** | **+7.33%** | +9.7% | -1.2% | `target_reclaim` |
| 16 | Book 3 | `2024-03-05 04:00` | `2024-03-05 05:00` | 1.0h | `$2.0303` | `$2.2068` | **+8.70%** | **+8.34%** | +22.6% | -1.5% | `target_reclaim` |
| 17 | Book 3 | `2024-03-05 19:00` | `2024-03-05 20:00` | 1.0h | `$2.1071` | `$2.2903` | **+8.70%** | **+8.34%** | +17.3% | -4.9% | `target_reclaim` |
| 18 | Book 5 (Shelf Absorption Squeeze) | `2024-03-06 02:00` | `2024-03-10 02:00` | Live | `$2.3954` | `$2.5990` | **+8.50%** | **+8.16%** | +20.6% | -32.8% | `shelf_target_reclaim` |
| 19 | Book 3 | `2024-03-07 00:00` | `2024-03-07 01:00` | 1.0h | `$2.6135` | `$2.7646` | **+5.78%** | **+5.62%** | +12.7% | -0.7% | `target_reclaim` |
| 20 | Book 3 | `2024-07-30 17:00` | `2024-08-01 15:00` | 46.0h | `$1.1304` | `$1.0374` | **-8.23%** | **-8.59%** | +2.3% | -9.4% | `stop_loss` |
| 21 | Book 2 | `2024-08-10 11:00` | `2024-08-12 06:00` | 43.0h | `$1.0153` | `$0.9318` | **-9.66%** | **-10.08%** | +2.2% | -8.6% | `initial_stop` |
| 22 | Book 3 | `2024-08-27 03:00` | `2024-08-27 22:00` | 19.0h | `$0.9752` | `$0.8949` | **-8.23%** | **-8.59%** | +1.9% | -8.5% | `stop_loss` |
| 23 | Book 3 | `2024-10-24 07:00` | `2024-10-25 23:00` | 40.0h | `$0.9927` | `$0.9110` | **-8.23%** | **-8.59%** | +1.5% | -13.2% | `stop_loss` |
| 24 | Book 4 | `2024-11-16 07:00` | `2024-11-23 07:00` | 168.0h | `$1.1571` | `$1.3886` | **+22.52%** | **+20.35%** | +20.2% | -4.7% | `target_reclaim` |
| 25 | Book 3 | `2024-12-02 08:00` | `2024-12-02 18:00` | 10.0h | `$1.4537` | `$1.5270` | **+5.04%** | **+4.92%** | +6.2% | -2.7% | `target_reclaim` |
| 26 | Book 3 | `2025-07-18 20:00` | `2025-07-20 00:00` | 28.0h | `$0.8013` | `$0.8347` | **+4.17%** | **+4.08%** | +4.9% | -1.7% | `target_reclaim` |
| 27 | Book 3 | `2026-09-13 15:00` | `2026-09-14 00:00` | 9.0h | `$0.2743` | `$0.2981` | **+8.70%** | **+8.34%** | +22.5% | -1.6% | `target_reclaim` |
| 28 | Book 3 | `2026-09-14 03:00` | `2026-09-14 09:00` | 6.0h | `$0.3719` | `$0.3413` | **-8.23%** | **-8.59%** | +8.9% | -9.8% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `12` | `100.0%` | **`+103.9%`** |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `shelf_target_reclaim` | `4` | `100.0%` | **`+32.6%`** |
| `time_expiry` | `3` | `100.0%` | **`+4.5%`** |
| `initial_stop` | `1` | `0.0%` | **`-10.1%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `MTL`

* **Total Candidate Breakouts Filtered (Vetoed):** `578`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `273` (47.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `96`
* **Saved Capital Losses Avoided:** `+3,227.1%`
* **Missed Upside Forgone:** `-3,532.5%`
* **Net Veto Alpha:** `+-305.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `400` | `69.2%` |
| `Core 1: Macro Bear Veto` | `82` | `14.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `46` | `8.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `38` | `6.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `12` | `2.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*