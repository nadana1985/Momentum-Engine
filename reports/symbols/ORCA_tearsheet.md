# Kronos V12: Institutional Symbol Tear Sheet — `ORCA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+27.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.32x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.88%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`189.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+24.3% / -17.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-03-21 05:00` | `2025-03-25 05:00` | Live | `$2.3110` | `$2.5075` | **+8.50%** | **+8.16%** | +16.0% | -32.6% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-02-17 01:00` | `2026-02-21 01:00` | Live | `$0.9283` | `$1.0072` | **+8.50%** | **+8.16%** | +39.1% | -17.3% | `shelf_target_reclaim` |
| 3 | Book 4 | `2026-04-25 15:00` | `2026-04-26 02:00` | 11.0h | `$1.2659` | `$1.5191` | **+2.41%** | **+2.36%** | +22.0% | -13.3% | `target_reclaim` |
| 4 | Book 4 | `2026-08-22 05:00` | `2026-09-06 12:00` | 367.0h | `$1.2459` | `$1.4950` | **+9.45%** | **+8.85%** | +20.2% | -5.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `target_reclaim` | `2` | `100.0%` | **`+11.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ORCA`

* **Total Candidate Breakouts Filtered (Vetoed):** `170`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `79` (46.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `126`
* **Saved Capital Losses Avoided:** `+1,133.8%`
* **Missed Upside Forgone:** `-5,060.2%`
* **Net Veto Alpha:** `+-3,926.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `158` | `92.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `11` | `6.5%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*