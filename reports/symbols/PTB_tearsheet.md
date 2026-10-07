# Kronos V12: Institutional Symbol Tear Sheet — `PTB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+18.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.20x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+18.49%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`24.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+41.9% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-19 17:00` | `2026-09-20 17:00` | 24.0h | `$0.0007` | `$0.0009` | **+20.32%** | **+18.49%** | +41.9% | -5.3% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `trail_stop` | `1` | `100.0%` | **`+18.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `PTB`

* **Total Candidate Breakouts Filtered (Vetoed):** `17`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `16` (94.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+445.0%`
* **Missed Upside Forgone:** `-146.6%`
* **Net Veto Alpha:** `+298.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `14` | `82.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `17.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*