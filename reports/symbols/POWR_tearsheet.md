# Kronos V12: Institutional Symbol Tear Sheet — `POWR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`83.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.481`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+12.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.13x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.06%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-25.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`21.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.8% / -9.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-12-12 10:00` | `2023-12-13 00:00` | 14.0h | `$0.3794` | `$0.4124` | **+8.70%** | **+8.34%** | +10.1% | -2.0% | `target_reclaim` |
| 2 | Book 3 | `2024-01-07 02:00` | `2024-01-07 05:00` | 3.0h | `$0.8896` | `$0.9670` | **+8.70%** | **+8.34%** | +9.2% | -1.9% | `target_reclaim` |
| 3 | Book 3 | `2024-01-07 08:00` | `2024-01-07 09:00` | 1.0h | `$0.9919` | `$0.7674` | **-22.64%** | **-25.67%** | +21.9% | -44.0% | `stop_loss` |
| 4 | Book 3 | `2024-03-11 00:00` | `2024-03-11 02:00` | 2.0h | `$0.3755` | `$0.4081` | **+8.70%** | **+8.34%** | +8.7% | -0.9% | `target_reclaim` |
| 5 | Book 3 | `2024-11-20 00:00` | `2024-11-23 00:00` | 72.0h | `$0.2563` | `$0.2685` | **+4.77%** | **+4.66%** | +5.5% | -6.1% | `time_expiry` |
| 6 | Book 3 | `2026-09-09 22:00` | `2026-09-11 10:00` | 36.0h | `$0.0474` | `$0.0515` | **+8.70%** | **+8.34%** | +9.5% | -0.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `stop_loss` | `1` | `0.0%` | **`-25.7%`** |
| `time_expiry` | `1` | `100.0%` | **`+4.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `POWR`

* **Total Candidate Breakouts Filtered (Vetoed):** `121`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `76` (62.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+1,188.4%`
* **Missed Upside Forgone:** `-1,255.0%`
* **Net Veto Alpha:** `+-66.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `49` | `40.5%` |
| `Core 1: Macro Bear Veto` | `39` | `32.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `17` | `14.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `16` | `13.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*