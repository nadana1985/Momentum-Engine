# Kronos V12: Institutional Symbol Tear Sheet — `AIOT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.675`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+5.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.89%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`8.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+-7.8% / -33.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-18 13:00` | `2025-07-18 21:00` | 8.0h | `$0.2767` | `$0.3193` | **+15.41%** | **+14.33%** | +24.3% | -2.1% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-12-10 04:00` | `2025-12-14 04:00` | Live | `$0.2632` | `$0.2416` | **-8.20%** | **-8.56%** | +-40.0% | -65.0% | `shelf_stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+14.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `AIOT`

* **Total Candidate Breakouts Filtered (Vetoed):** `107`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `71` (66.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `52`
* **Saved Capital Losses Avoided:** `+1,986.0%`
* **Missed Upside Forgone:** `-3,223.4%`
* **Net Veto Alpha:** `+-1,237.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `52` | `48.6%` |
| `Core 1: Macro Bear Veto` | `40` | `37.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `8` | `7.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `6.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*