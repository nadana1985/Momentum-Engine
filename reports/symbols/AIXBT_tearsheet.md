# Kronos V12: Institutional Symbol Tear Sheet — `AIXBT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.608`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-17.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.84x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.72%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-37.1%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`22.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.9% / -8.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-01-10 09:00` | `2025-01-14 09:00` | Live | `$0.5247` | `$0.5693` | **+8.50%** | **+8.16%** | +67.5% | -25.9% | `shelf_target_reclaim` |
| 2 | Book 3 | `2025-04-24 02:00` | `2025-04-24 16:00` | 14.0h | `$0.1050` | `$0.1094` | **+4.17%** | **+4.08%** | +7.2% | -3.6% | `target_reclaim` |
| 3 | Book 3 | `2025-04-25 12:00` | `2025-04-25 16:00` | 4.0h | `$0.1343` | `$0.1233` | **-8.23%** | **-8.59%** | +4.9% | -8.5% | `stop_loss` |
| 4 | Book 3 | `2025-04-26 11:00` | `2025-04-26 15:00` | 4.0h | `$0.1489` | `$0.1578` | **+5.96%** | **+5.79%** | +6.7% | -4.6% | `target_reclaim` |
| 5 | Book 3 | `2025-06-16 16:00` | `2025-06-17 00:00` | 8.0h | `$0.1763` | `$0.1618` | **-8.23%** | **-8.59%** | +3.1% | -8.3% | `stop_loss` |
| 6 | Book 3 | `2025-06-30 01:00` | `2025-07-01 12:00` | 35.0h | `$0.1362` | `$0.1250` | **-8.23%** | **-8.59%** | +1.1% | -8.7% | `stop_loss` |
| 7 | Book 3 | `2025-07-14 05:00` | `2025-07-14 15:00` | 10.0h | `$0.1645` | `$0.1509` | **-8.23%** | **-8.59%** | +5.0% | -8.6% | `stop_loss` |
| 8 | Book 3 | `2025-07-17 12:00` | `2025-07-19 14:00` | 50.0h | `$0.1734` | `$0.1592` | **-8.23%** | **-8.59%** | +4.1% | -8.2% | `stop_loss` |
| 9 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0191` | `$0.0208` | **+8.97%** | **+8.59%** | +23.0% | -0.6% | `target_reclaim` |
| 10 | Book 3 | `2026-09-28 14:00` | `2026-10-01 14:00` | 72.0h | `$0.0225` | `$0.0223` | **-0.85%** | **-0.85%** | +6.3% | -2.6% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `target_reclaim` | `3` | `100.0%` | **`+18.5%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `AIXBT`

* **Total Candidate Breakouts Filtered (Vetoed):** `76`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `65` (85.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+920.4%`
* **Missed Upside Forgone:** `-719.4%`
* **Net Veto Alpha:** `+201.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `40` | `52.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `23` | `30.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `10` | `13.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `3.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*