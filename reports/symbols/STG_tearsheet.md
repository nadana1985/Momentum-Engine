# Kronos V12: Institutional Symbol Tear Sheet — `STG`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `18` (`18` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `18` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`72.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`8.271`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+94.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.58x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+5.26%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-7.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`99.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.7% / -7.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-01-09 00:00` | `2023-01-16 00:00` | 168.0h | `$0.3734` | `$0.4701` | **+30.85%** | **+27.43%** | +29.3% | -1.1% | `time_cap` |
| 2 | Book 4 | `2023-01-22 05:00` | `2023-01-22 07:00` | 2.0h | `$0.5705` | `$0.6845` | **+11.06%** | **+10.33%** | +20.4% | -1.4% | `target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2023-02-01 20:00` | `2023-02-05 20:00` | Live | `$0.6435` | `$0.6982` | **+8.50%** | **+8.16%** | +92.7% | -11.5% | `shelf_target_reclaim` |
| 4 | Book 3 | `2023-02-03 02:00` | `2023-02-03 16:00` | 14.0h | `$0.7105` | `$0.7699` | **+8.37%** | **+8.03%** | +12.8% | -4.7% | `target_reclaim` |
| 5 | Book 3 | `2023-04-07 18:00` | `2023-04-10 18:00` | 72.0h | `$0.7900` | `$0.8418` | **+6.56%** | **+6.35%** | +8.8% | -6.7% | `time_expiry` |
| 6 | Book 3 | `2023-07-05 10:00` | `2023-07-08 10:00` | 72.0h | `$0.6075` | `$0.5984` | **-1.50%** | **-1.51%** | +3.4% | -5.8% | `time_expiry` |
| 7 | Book 5 (Shelf Absorption Squeeze) | `2023-08-10 00:00` | `2023-08-14 00:00` | Live | `$0.6342` | `$0.6882` | **+8.50%** | **+8.16%** | +1.1% | -29.9% | `shelf_target_reclaim` |
| 8 | Book 4 | `2023-11-09 23:00` | `2023-12-09 22:00` | 719.0h | `$0.5609` | `$0.5626` | **-1.18%** | **-1.19%** | +14.4% | -10.9% | `time_expiry` |
| 9 | Book 5 (Shelf Absorption Squeeze) | `2024-05-30 07:00` | `2024-06-03 07:00` | Live | `$0.6472` | `$0.7022` | **+8.50%** | **+8.16%** | +8.0% | -28.4% | `shelf_target_reclaim` |
| 10 | Book 2 | `2024-08-10 16:00` | `2024-08-13 09:00` | 65.0h | `$0.3374` | `$0.3315` | **-2.07%** | **-2.09%** | +18.0% | -1.8% | `breakeven_ratchet` |
| 11 | Book 2 | `2024-09-15 04:00` | `2024-09-17 04:00` | 48.0h | `$0.3032` | `$0.2905` | **-4.94%** | **-5.05%** | +5.4% | -5.9% | `fast_decay_cut` |
| 12 | Book 5 (Shelf Absorption Squeeze) | `2024-11-09 00:00` | `2024-11-13 00:00` | Live | `$0.3116` | `$0.3381` | **+8.50%** | **+8.16%** | +10.8% | -14.6% | `shelf_target_reclaim` |
| 13 | Book 3 | `2024-12-02 08:00` | `2024-12-02 22:00` | 14.0h | `$0.3764` | `$0.4040` | **+7.34%** | **+7.08%** | +7.5% | -0.7% | `target_reclaim` |
| 14 | Book 3 | `2025-07-14 15:00` | `2025-07-17 15:00` | 72.0h | `$0.1700` | `$0.1732` | **+1.85%** | **+1.84%** | +3.3% | -2.8% | `time_expiry` |
| 15 | Book 3 | `2025-07-18 20:00` | `2025-07-20 11:00` | 39.0h | `$0.1705` | `$0.1779` | **+4.31%** | **+4.22%** | +4.3% | -0.4% | `target_reclaim` |
| 16 | Book 3 | `2025-08-10 20:00` | `2025-08-11 02:00` | 6.0h | `$0.1813` | `$0.1895` | **+4.55%** | **+4.45%** | +8.9% | -4.2% | `target_reclaim` |
| 17 | Book 3 | `2025-08-12 05:00` | `2025-08-15 05:00` | 72.0h | `$0.1817` | `$0.1761` | **-3.13%** | **-3.18%** | +7.2% | -6.1% | `time_expiry` |
| 18 | Book 3 | `2025-09-25 03:00` | `2025-09-26 04:00` | 25.0h | `$0.1807` | `$0.1905` | **+5.43%** | **+5.28%** | +7.6% | -5.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+39.4%`** |
| `time_expiry` | `5` | `40.0%` | **`+2.3%`** |
| `shelf_target_reclaim` | `4` | `100.0%` | **`+32.6%`** |
| `breakeven_ratchet` | `1` | `0.0%` | **`-2.1%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-5.1%`** |
| `time_cap` | `1` | `100.0%` | **`+27.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `STG`

* **Total Candidate Breakouts Filtered (Vetoed):** `844`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `558` (66.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `65`
* **Saved Capital Losses Avoided:** `+9,523.5%`
* **Missed Upside Forgone:** `-1,813.1%`
* **Net Veto Alpha:** `+7,710.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `373` | `44.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `258` | `30.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `117` | `13.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `88` | `10.4%` |
| `Core 4: Defensible Whale Dump` | `8` | `0.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*