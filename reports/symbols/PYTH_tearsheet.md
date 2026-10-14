# Kronos V12: Institutional Symbol Tear Sheet — `PYTH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.122`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+22.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.25x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+7.34%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-19.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`156.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.4% / -13.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2024-01-25 07:00` | `2024-02-01 22:00` | 183.0h | `$0.3881` | `$0.4657` | **+38.67%** | **+33.52%** | +20.2% | -3.7% | `target_reclaim` |
| 2 | Book 4 | `2024-10-29 06:00` | `2024-11-03 15:00` | 129.0h | `$0.3755` | `$0.3191` | **-18.12%** | **-19.64%** | +9.8% | -15.1% | `structural_stop` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2025-08-28 14:00` | `2025-09-01 14:00` | Live | `$0.1732` | `$0.1879` | **+8.50%** | **+8.16%** | +7.2% | -22.5% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-19.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+33.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `PYTH`

* **Total Candidate Breakouts Filtered (Vetoed):** `512`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `355` (69.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `15`
* **Saved Capital Losses Avoided:** `+4,743.0%`
* **Missed Upside Forgone:** `-458.5%`
* **Net Veto Alpha:** `+4,284.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `290` | `56.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `221` | `43.2%` |
| `Core 4: Funding Rate Cap` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*