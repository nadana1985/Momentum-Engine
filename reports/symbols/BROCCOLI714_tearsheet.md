# Kronos V12: Institutional Symbol Tear Sheet — `BROCCOLI714`
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
| **Cumulative Net Log Return** | **`+0.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.25%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`71.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+20.5% / -5.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-03 15:00` | `2026-09-06 14:00` | 71.0h | `$0.0186` | `$0.0186` | **+0.25%** | **+0.25%** | +20.5% | -5.5% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `BROCCOLI714`

* **Total Candidate Breakouts Filtered (Vetoed):** `45`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `32` (71.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `16`
* **Saved Capital Losses Avoided:** `+574.6%`
* **Missed Upside Forgone:** `-672.8%`
* **Net Veto Alpha:** `+-98.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `19` | `42.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `17` | `37.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `15.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `4.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*