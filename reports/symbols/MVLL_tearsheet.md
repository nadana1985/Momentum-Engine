# Kronos V12: Institutional Symbol Tear Sheet — `MVLL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-14.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.87x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-7.04%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`11.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.3% / -16.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-20 19:00` | `2026-08-21 14:00` | 19.0h | `$34.6464` | `$31.7950` | **-5.47%** | **-5.62%** | +3.1% | -13.5% | `initial_stop` |
| 2 | Book 2 | `2026-10-06 13:00` | `2026-10-06 16:00` | 3.0h | `$43.5486` | `$39.9646` | **-8.12%** | **-8.47%** | +5.5% | -19.9% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-14.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `MVLL`

* **Total Candidate Breakouts Filtered (Vetoed):** `3`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `3` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+58.5%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+58.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `3` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*