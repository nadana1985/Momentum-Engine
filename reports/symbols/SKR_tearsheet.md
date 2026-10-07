# Kronos V12: Institutional Symbol Tear Sheet — `SKR`
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
| **Cumulative Net Log Return** | **`+30.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.36x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+30.54%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`15.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+79.7% / -14.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-30 05:00` | `2026-08-30 20:00` | 15.0h | `$0.0135` | `$0.0205` | **+35.71%** | **+30.54%** | +79.7% | -14.4% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `trail_stop` | `1` | `100.0%` | **`+30.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `SKR`

* **Total Candidate Breakouts Filtered (Vetoed):** `6`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `6` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+93.4%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+93.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `6` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*