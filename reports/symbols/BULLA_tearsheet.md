# Kronos V12: Institutional Symbol Tear Sheet — `BULLA`
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
| **Cumulative Net Log Return** | **`+16.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.16%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`nanh`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+600.0% / -48.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-12-28 15:00` | `2026-01-01 15:00` | Live | `$0.0361` | `$0.0392` | **+8.50%** | **+8.16%** | +52.6% | -29.5% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-01-25 10:00` | `2026-01-29 10:00` | Live | `$0.0354` | `$0.0384` | **+8.50%** | **+8.16%** | +1147.4% | -68.2% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `BULLA`

* **Total Candidate Breakouts Filtered (Vetoed):** `129`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `120` (93.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `50`
* **Saved Capital Losses Avoided:** `+5,259.4%`
* **Missed Upside Forgone:** `-4,994.4%`
* **Net Veto Alpha:** `+264.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `124` | `96.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `5` | `3.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*