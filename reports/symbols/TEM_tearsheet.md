# Kronos V12: Institutional Symbol Tear Sheet — `TEM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-8.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-8.57%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`24.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.1% / -8.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-10-05 15:00` | `2026-10-06 15:00` | 24.0h | `$82.2351` | `$75.4812` | **-8.21%** | **-8.57%** | +7.1% | -8.7% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `TEM`

* **Total Candidate Breakouts Filtered (Vetoed):** `7`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `1` (14.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `1`
* **Saved Capital Losses Avoided:** `+6.3%`
* **Missed Upside Forgone:** `-23.4%`
* **Net Veto Alpha:** `+-17.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `7` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*