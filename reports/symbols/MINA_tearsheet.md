# Kronos V12: Institutional Symbol Tear Sheet — `MINA`
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
| **Cumulative Net Log Return** | **`+34.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.42x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+17.38%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`184.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.5% / -7.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-10-24 04:00` | `2023-10-28 04:00` | Live | `$0.5624` | `$0.6102` | **+8.50%** | **+8.16%** | +19.1% | -8.6% | `shelf_target_reclaim` |
| 2 | Book 4 | `2026-08-25 14:00` | `2026-09-02 06:00` | 184.0h | `$0.0609` | `$0.0731` | **+29.78%** | **+26.60%** | +20.0% | -7.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+26.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `MINA`

* **Total Candidate Breakouts Filtered (Vetoed):** `122`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `77` (63.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+988.7%`
* **Missed Upside Forgone:** `-204.0%`
* **Net Veto Alpha:** `+784.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `69` | `56.6%` |
| `Core 1: Macro Bear Veto` | `42` | `34.4%` |
| `Core 4: Funding Rate Cap` | `9` | `7.4%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*