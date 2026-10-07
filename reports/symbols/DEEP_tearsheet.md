# Kronos V12: Institutional Symbol Tear Sheet — `DEEP`
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
| **Cumulative Net Log Return** | **`+12.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.14x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+12.68%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`133.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+42.1% / -1.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-03 11:00` | `2026-05-09 00:00` | 133.0h | `$0.0290` | `$0.0330` | **+13.52%** | **+12.68%** | +42.1% | -1.5% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `trail_stop` | `1` | `100.0%` | **`+12.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `DEEP`

* **Total Candidate Breakouts Filtered (Vetoed):** `52`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (46.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+267.8%`
* **Missed Upside Forgone:** `-113.2%`
* **Net Veto Alpha:** `+154.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `26` | `50.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `13` | `25.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `15.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `5` | `9.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*