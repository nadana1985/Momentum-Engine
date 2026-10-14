# Kronos V12: Institutional Symbol Tear Sheet — `KAIA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.680`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+34.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.41x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.75%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-0.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`34.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.9% / -8.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-01-19 08:00` | `2025-01-20 00:00` | 16.0h | `$0.2216` | `$0.2033` | **-8.23%** | **-8.59%** | +6.6% | -8.1% | `stop_loss` |
| 2 | Book 4 | `2025-06-18 20:00` | `2025-06-20 07:00` | 35.0h | `$0.1668` | `$0.2002` | **+11.58%** | **+11.05%** | +20.3% | -1.6% | `target_reclaim` |
| 3 | Book 3 | `2025-07-17 20:00` | `2025-07-18 00:00` | 4.0h | `$0.1559` | `$0.1649` | **+5.74%** | **+5.58%** | +9.3% | -0.2% | `target_reclaim` |
| 4 | Book 3 | `2025-07-23 13:00` | `2025-07-26 13:00` | 72.0h | `$0.1678` | `$0.1665` | **-0.79%** | **-0.79%** | +2.7% | -7.8% | `time_expiry` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2026-01-23 15:00` | `2026-01-27 15:00` | Live | `$0.0625` | `$0.0678` | **+8.50%** | **+8.16%** | +18.4% | -33.0% | `shelf_target_reclaim` |
| 6 | Book 2 | `2026-08-20 08:00` | `2026-08-22 05:00` | 45.0h | `$0.0252` | `$0.0294` | **+20.67%** | **+19.11%** | +37.7% | -2.1% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+16.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.8%`** |
| `trail_stop` | `1` | `100.0%` | **`+19.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `KAIA`

* **Total Candidate Breakouts Filtered (Vetoed):** `297`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `234` (78.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `22`
* **Saved Capital Losses Avoided:** `+2,841.7%`
* **Missed Upside Forgone:** `-565.8%`
* **Net Veto Alpha:** `+2,275.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `231` | `77.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `49` | `16.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `9` | `3.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `8` | `2.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*