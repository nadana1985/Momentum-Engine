# Kronos V12: Institutional Symbol Tear Sheet — `STRK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.488`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+4.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.10%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`38.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.0% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-15 03:00` | `2025-05-15 14:00` | 11.0h | `$0.1727` | `$0.1585` | **-8.23%** | **-8.59%** | +1.8% | -8.1% | `stop_loss` |
| 2 | Book 3 | `2025-07-18 20:00` | `2025-07-21 14:00` | 66.0h | `$0.1369` | `$0.1556` | **+13.64%** | **+12.78%** | +14.2% | -2.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `STRK`

* **Total Candidate Breakouts Filtered (Vetoed):** `98`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `79` (80.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `14`
* **Saved Capital Losses Avoided:** `+1,125.5%`
* **Missed Upside Forgone:** `-403.4%`
* **Net Veto Alpha:** `+722.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `57` | `58.2%` |
| `Core 1: Macro Bear Veto` | `41` | `41.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*