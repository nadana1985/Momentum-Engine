# Kronos V12: Institutional Symbol Tear Sheet — `POWER`
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
| **Cumulative Net Log Return** | **`+30.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.36x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+30.81%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`18.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+21.6% / -5.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2026-09-13 01:00` | `2026-09-13 19:00` | 18.0h | `$0.1003` | `$0.1204` | **+35.23%** | **+30.81%** | +21.6% | -5.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+30.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `POWER`

* **Total Candidate Breakouts Filtered (Vetoed):** `152`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `123` (80.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `99`
* **Saved Capital Losses Avoided:** `+5,240.8%`
* **Missed Upside Forgone:** `-5,602.5%`
* **Net Veto Alpha:** `+-361.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `152` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*