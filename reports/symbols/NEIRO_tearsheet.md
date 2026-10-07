# Kronos V12: Institutional Symbol Tear Sheet — `NEIRO`
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
| **Cumulative Net Log Return** | **`+24.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.28x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+24.59%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`107.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+45.7% / -3.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2025-04-22 14:00` | `2025-04-27 01:00` | 107.0h | `$0.0002` | `$0.0002` | **+27.87%** | **+24.59%** | +45.7% | -3.1% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `trail_stop` | `1` | `100.0%` | **`+24.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `NEIRO`

* **Total Candidate Breakouts Filtered (Vetoed):** `52`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `39` (75.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+635.3%`
* **Missed Upside Forgone:** `-1,191.1%`
* **Net Veto Alpha:** `+-555.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `32` | `61.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `20` | `38.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*