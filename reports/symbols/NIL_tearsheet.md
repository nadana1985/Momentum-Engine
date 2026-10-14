# Kronos V12: Institutional Symbol Tear Sheet — `NIL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+52.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.70x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+17.61%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`46.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+40.4% / -23.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-05-07 14:00` | `2026-05-11 14:00` | Live | `$0.0591` | `$0.0641` | **+8.50%** | **+8.16%** | +19.2% | -28.9% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-05-23 20:00` | `2026-05-27 20:00` | Live | `$0.0560` | `$0.0608` | **+8.50%** | **+8.16%** | +52.7% | -38.3% | `shelf_target_reclaim` |
| 3 | Book 2 | `2026-09-18 22:00` | `2026-09-20 20:00` | 46.0h | `$0.0460` | `$0.0635` | **+43.09%** | **+36.52%** | +49.3% | -1.6% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+36.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `NIL`

* **Total Candidate Breakouts Filtered (Vetoed):** `40`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `32` (80.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+629.8%`
* **Missed Upside Forgone:** `-661.3%`
* **Net Veto Alpha:** `+-31.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `23` | `57.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `17` | `42.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*