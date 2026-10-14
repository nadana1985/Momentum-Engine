# Kronos V12: Institutional Symbol Tear Sheet — `ACU`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.938`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+8.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.69%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`39.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+36.1% / -18.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-01-23 02:00` | `2026-01-27 02:00` | Live | `$0.1372` | `$0.1488` | **+8.50%** | **+8.16%** | +58.8% | -38.5% | `shelf_target_reclaim` |
| 2 | Book 4 | `2026-08-10 14:00` | `2026-08-13 05:00` | 63.0h | `$0.0961` | `$0.1153` | **+8.79%** | **+8.49%** | +44.3% | -7.9% | `target_reclaim` |
| 3 | Book 3 | `2026-08-28 02:00` | `2026-08-28 18:00` | 16.0h | `$0.1311` | `$0.1203` | **-8.23%** | **-8.59%** | +5.2% | -9.8% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `ACU`

* **Total Candidate Breakouts Filtered (Vetoed):** `298`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `199` (66.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `102`
* **Saved Capital Losses Avoided:** `+3,323.2%`
* **Missed Upside Forgone:** `-3,362.5%`
* **Net Veto Alpha:** `+-39.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `246` | `82.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `51` | `17.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*