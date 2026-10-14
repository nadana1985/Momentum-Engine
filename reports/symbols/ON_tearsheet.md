# Kronos V12: Institutional Symbol Tear Sheet — `ON`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+13.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.14x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.62%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+21.3% / -29.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-03-27 11:00` | `2026-03-31 11:00` | Live | `$0.1166` | `$0.1266` | **+8.50%** | **+8.16%** | +19.4% | -47.8% | `shelf_target_reclaim` |
| 2 | Book 4 | `2026-07-19 14:00` | `2026-07-20 16:00` | 26.0h | `$0.1196` | `$0.1435` | **+5.20%** | **+5.08%** | +23.1% | -10.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+5.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `ON`

* **Total Candidate Breakouts Filtered (Vetoed):** `422`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `293` (69.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `277`
* **Saved Capital Losses Avoided:** `+7,311.6%`
* **Missed Upside Forgone:** `-20,306.8%`
* **Net Veto Alpha:** `+-12,995.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `422` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*