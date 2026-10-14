# Kronos V12: Institutional Symbol Tear Sheet — `SFP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.887`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-3.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.34%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-11.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`70.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.3% / -9.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-23 09:00` | `2021-09-07 14:00` | 365.0h | `$1.4957` | `$1.3419` | **-12.46%** | **-13.16%** | +18.7% | -25.7% | `structural_stop` |
| 2 | Book 4 | `2022-11-13 16:00` | `2022-11-14 04:00` | 12.0h | `$0.5079` | `$0.6094` | **+5.10%** | **+4.98%** | +29.6% | -13.7% | `target_reclaim` |
| 3 | Book 3 | `2023-01-14 09:00` | `2023-01-16 02:00` | 41.0h | `$0.4579` | `$0.4770` | **+4.17%** | **+4.08%** | +4.6% | -8.8% | `target_reclaim` |
| 4 | Book 3 | `2023-01-28 13:00` | `2023-01-29 15:00` | 26.0h | `$0.4836` | `$0.5038` | **+4.17%** | **+4.08%** | +4.3% | -1.3% | `target_reclaim` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2023-01-31 17:00` | `2023-02-04 17:00` | Live | `$0.5158` | `$0.5597` | **+8.50%** | **+8.16%** | +14.5% | -20.2% | `shelf_target_reclaim` |
| 6 | Book 3 | `2023-06-22 16:00` | `2023-06-25 16:00` | 72.0h | `$0.4583` | `$0.4583` | **-0.01%** | **-0.01%** | +4.8% | -2.7% | `time_expiry` |
| 7 | Book 3 | `2024-11-12 09:00` | `2024-11-13 04:00` | 19.0h | `$0.7373` | `$0.6766` | **-8.23%** | **-8.59%** | +4.6% | -9.9% | `stop_loss` |
| 8 | Book 3 | `2024-12-01 02:00` | `2024-12-01 13:00` | 11.0h | `$0.7427` | `$0.7790` | **+4.89%** | **+4.77%** | +6.5% | -1.2% | `target_reclaim` |
| 9 | Book 3 | `2025-05-20 11:00` | `2025-05-23 11:00` | 72.0h | `$0.5438` | `$0.5484` | **+0.86%** | **+0.85%** | +5.9% | -4.1% | `time_expiry` |
| 10 | Book 3 | `2025-09-24 15:00` | `2025-09-25 07:00` | 16.0h | `$0.5207` | `$0.4778` | **-8.23%** | **-8.59%** | +9.1% | -8.3% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+17.9%`** |
| `time_expiry` | `2` | `50.0%` | **`+0.8%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-13.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `SFP`

* **Total Candidate Breakouts Filtered (Vetoed):** `997`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `740` (74.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `100`
* **Saved Capital Losses Avoided:** `+11,356.3%`
* **Missed Upside Forgone:** `-3,414.7%`
* **Net Veto Alpha:** `+7,941.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `412` | `41.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `379` | `38.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `131` | `13.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `47` | `4.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `21` | `2.1%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `3` | `0.3%` |
| `Core 4: Defensible Whale Dump` | `3` | `0.3%` |
| `Core 3: Min Turnover Velocity` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*