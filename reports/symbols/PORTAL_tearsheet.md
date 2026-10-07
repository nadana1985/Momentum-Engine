# Kronos V12: Institutional Symbol Tear Sheet — `PORTAL`
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
| **Cumulative Net Log Return** | **`+5.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.05x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.14%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`300.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+26.7% / -5.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2024-09-19 03:00` | `2024-10-01 15:00` | 300.0h | `$0.2923` | `$0.3027` | **+5.27%** | **+5.14%** | +26.7% | -5.7% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `trail_stop` | `1` | `100.0%` | **`+5.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `PORTAL`

* **Total Candidate Breakouts Filtered (Vetoed):** `59`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `39` (66.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `15`
* **Saved Capital Losses Avoided:** `+759.6%`
* **Missed Upside Forgone:** `-874.9%`
* **Net Veto Alpha:** `+-115.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `39` | `66.1%` |
| `Core 1: Macro Bear Veto` | `20` | `33.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*