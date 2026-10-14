# Kronos V12: Institutional Symbol Tear Sheet — `HMSTR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.942`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+16.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.34%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`40.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+21.7% / -19.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-11-09 11:00` | `2024-11-13 11:00` | Live | `$0.0039` | `$0.0042` | **+8.50%** | **+8.16%** | +37.1% | -20.1% | `shelf_target_reclaim` |
| 2 | Book 3 | `2025-01-07 15:00` | `2025-01-08 00:00` | 9.0h | `$0.0032` | `$0.0029` | **-8.23%** | **-8.59%** | +1.8% | -8.1% | `stop_loss` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2025-12-18 07:00` | `2025-12-22 07:00` | Live | `$0.0002` | `$0.0003` | **+8.50%** | **+8.16%** | +29.7% | -22.6% | `shelf_target_reclaim` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2026-07-04 03:00` | `2026-07-08 03:00` | Live | `$0.0003` | `$0.0003` | **+8.50%** | **+8.16%** | +37.7% | -41.9% | `shelf_target_reclaim` |
| 5 | Book 3 | `2026-09-23 14:00` | `2026-09-26 14:00` | 72.0h | `$0.0002` | `$0.0002` | **+0.79%** | **+0.79%** | +1.9% | -6.1% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `3` | `100.0%` | **`+24.5%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+0.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `HMSTR`

* **Total Candidate Breakouts Filtered (Vetoed):** `58`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `45` (77.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `23`
* **Saved Capital Losses Avoided:** `+892.8%`
* **Missed Upside Forgone:** `-1,161.8%`
* **Net Veto Alpha:** `+-268.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `46` | `79.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `10` | `17.2%` |
| `Core 3: Min Turnover Velocity` | `1` | `1.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `1.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*