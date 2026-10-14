# Kronos V12: Institutional Symbol Tear Sheet — `SQD`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.549`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+4.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.05x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.35%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`25.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.7% / -25.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-29 15:00` | `2025-07-30 16:00` | 25.0h | `$0.1731` | `$0.1977` | **+14.17%** | **+13.25%** | +16.1% | -3.0% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-11-27 15:00` | `2025-12-01 15:00` | Live | `$0.0737` | `$0.0676` | **-8.20%** | **-8.56%** | +-2.8% | -47.9% | `shelf_stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+13.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `SQD`

* **Total Candidate Breakouts Filtered (Vetoed):** `114`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `101` (88.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `25`
* **Saved Capital Losses Avoided:** `+1,943.5%`
* **Missed Upside Forgone:** `-1,368.6%`
* **Net Veto Alpha:** `+574.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `112` | `98.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `2` | `1.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*