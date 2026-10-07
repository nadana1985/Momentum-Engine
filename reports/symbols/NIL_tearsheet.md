# Kronos V12: Institutional Symbol Tear Sheet — `NIL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+32.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.38x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+32.23%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`46.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+49.3% / -1.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-18 22:00` | `2026-09-20 20:00` | 46.0h | `$0.0460` | `$0.0635` | **+38.03%** | **+32.23%** | +49.3% | -1.6% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+32.2%`** |

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