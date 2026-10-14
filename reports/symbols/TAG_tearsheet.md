# Kronos V12: Institutional Symbol Tear Sheet — `TAG`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+18.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.20x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+9.27%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`235.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.8% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-03-13 06:00` | `2026-04-01 18:00` | 468.0h | `$0.0006` | `$0.0007` | **+3.67%** | **+3.54%** | +21.2% | -12.0% | `target_reclaim` |
| 2 | Book 3 | `2026-09-20 08:00` | `2026-09-20 11:00` | 3.0h | `$0.0007` | `$0.0009` | **+16.19%** | **+15.00%** | +18.4% | -0.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+18.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `TAG`

* **Total Candidate Breakouts Filtered (Vetoed):** `107`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `104` (97.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+1,737.3%`
* **Missed Upside Forgone:** `-610.3%`
* **Net Veto Alpha:** `+1,127.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `98` | `91.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `6.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `0.9%` |
| `Core 3: Min Turnover Velocity` | `1` | `0.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*