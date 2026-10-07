# Kronos V12: Institutional Symbol Tear Sheet — `CFG`
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
| **Cumulative Net Log Return** | **`+40.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.49x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+40.09%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`114.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+57.7% / -4.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-04 07:00` | `2026-05-09 01:00` | 114.0h | `$0.2217` | `$0.3310` | **+49.32%** | **+40.09%** | +57.7% | -4.4% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+40.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `CFG`

* **Total Candidate Breakouts Filtered (Vetoed):** `26`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `19` (73.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `6`
* **Saved Capital Losses Avoided:** `+268.9%`
* **Missed Upside Forgone:** `-176.2%`
* **Net Veto Alpha:** `+92.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `18` | `69.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `8` | `30.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*