# Kronos V12: Institutional Symbol Tear Sheet — `SXT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+32.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.38x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.44%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`41.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.0% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-23 18:00` | `2025-07-23 19:00` | 1.0h | `$0.1117` | `$0.1214` | **+8.70%** | **+8.34%** | +11.6% | -4.0% | `target_reclaim` |
| 2 | Book 3 | `2025-08-05 14:00` | `2025-08-07 22:00` | 56.0h | `$0.0813` | `$0.0884` | **+8.70%** | **+8.34%** | +9.1% | -2.8% | `target_reclaim` |
| 3 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0077` | `$0.0079` | **+2.28%** | **+2.25%** | +10.8% | -17.9% | `time_expiry` |
| 4 | Book 3 | `2026-08-30 23:00` | `2026-08-31 06:00` | 7.0h | `$0.0082` | `$0.0089` | **+8.70%** | **+8.34%** | +9.6% | -0.5% | `target_reclaim` |
| 5 | Book 3 | `2026-09-23 14:00` | `2026-09-26 14:00` | 72.0h | `$0.0090` | `$0.0095` | **+5.08%** | **+4.95%** | +9.0% | -1.3% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+25.0%`** |
| `time_expiry` | `2` | `100.0%` | **`+7.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `SXT`

* **Total Candidate Breakouts Filtered (Vetoed):** `30`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `27` (90.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+368.7%`
* **Missed Upside Forgone:** `-169.4%`
* **Net Veto Alpha:** `+199.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `17` | `56.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `23.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `6` | `20.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*