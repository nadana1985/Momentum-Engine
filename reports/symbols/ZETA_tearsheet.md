# Kronos V12: Institutional Symbol Tear Sheet — `ZETA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`69.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.937`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+32.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.38x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.48%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.9% / -7.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-09-18 05:00` | `2024-09-18 08:00` | 3.0h | `$0.5521` | `$0.5894` | **+6.75%** | **+6.53%** | +10.9% | -1.4% | `target_reclaim` |
| 2 | Book 3 | `2024-09-20 07:00` | `2024-09-21 03:00` | 20.0h | `$0.6378` | `$0.5853` | **-8.23%** | **-8.59%** | +2.2% | -8.6% | `stop_loss` |
| 3 | Book 3 | `2024-09-27 11:00` | `2024-09-27 14:00` | 3.0h | `$0.6810` | `$0.7102` | **+4.29%** | **+4.20%** | +7.0% | -0.1% | `target_reclaim` |
| 4 | Book 3 | `2024-09-30 04:00` | `2024-10-01 15:00` | 35.0h | `$0.6810` | `$0.6249` | **-8.23%** | **-8.59%** | +4.0% | -9.8% | `stop_loss` |
| 5 | Book 3 | `2024-10-23 11:00` | `2024-10-23 14:00` | 3.0h | `$0.6997` | `$0.7316` | **+4.55%** | **+4.45%** | +6.2% | -0.6% | `target_reclaim` |
| 6 | Book 3 | `2024-12-02 08:00` | `2024-12-04 00:00` | 40.0h | `$0.7933` | `$0.9185` | **+15.78%** | **+14.65%** | +19.2% | -1.9% | `target_reclaim` |
| 7 | Book 3 | `2024-12-04 16:00` | `2024-12-07 16:00` | 72.0h | `$0.8758` | `$0.9254` | **+5.66%** | **+5.50%** | +7.7% | -4.8% | `time_expiry` |
| 8 | Book 5 (Shelf Absorption Squeeze) | `2025-03-22 08:00` | `2025-03-26 08:00` | Live | `$0.2718` | `$0.2949` | **+8.50%** | **+8.16%** | +36.8% | -35.9% | `shelf_target_reclaim` |
| 9 | Book 3 | `2025-04-26 13:00` | `2025-04-29 12:00` | 71.0h | `$0.2595` | `$0.2823` | **+8.79%** | **+8.43%** | +10.4% | -6.5% | `target_reclaim` |
| 10 | Book 3 | `2025-07-15 00:00` | `2025-07-17 13:00` | 61.0h | `$0.2116` | `$0.2296` | **+8.52%** | **+8.18%** | +8.5% | -2.5% | `target_reclaim` |
| 11 | Book 3 | `2025-07-22 14:00` | `2025-07-23 21:00` | 31.0h | `$0.2303` | `$0.2113` | **-8.23%** | **-8.59%** | +6.5% | -8.2% | `stop_loss` |
| 12 | Book 3 | `2025-10-28 20:00` | `2025-10-30 15:00` | 43.0h | `$0.1198` | `$0.1099` | **-8.23%** | **-8.59%** | +2.3% | -8.7% | `stop_loss` |
| 13 | Book 3 | `2026-09-15 14:00` | `2026-09-18 13:00` | 71.0h | `$0.0344` | `$0.0367` | **+6.67%** | **+6.45%** | +7.0% | -6.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `7` | `100.0%` | **`+52.9%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+5.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZETA`

* **Total Candidate Breakouts Filtered (Vetoed):** `290`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `181` (62.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `10`
* **Saved Capital Losses Avoided:** `+3,505.8%`
* **Missed Upside Forgone:** `-372.9%`
* **Net Veto Alpha:** `+3,132.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `235` | `81.0%` |
| `Core 1: Macro Bear Veto` | `24` | `8.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `24` | `8.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `2.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*