# Kronos V12: Institutional Symbol Tear Sheet — `MAGMA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+24.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.28x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.16%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`nanh`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+50.0% / -38.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-01-07 06:00` | `2026-01-11 06:00` | Live | `$0.1306` | `$0.1417` | **+8.50%** | **+8.16%** | +21.8% | -37.5% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-03-04 03:00` | `2026-03-08 03:00` | Live | `$0.1219` | `$0.1322` | **+8.50%** | **+8.16%** | +6.4% | -35.5% | `shelf_target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2026-03-21 17:00` | `2026-03-25 17:00` | Live | `$0.1096` | `$0.1189` | **+8.50%** | **+8.16%** | +122.0% | -41.8% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `3` | `100.0%` | **`+24.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `MAGMA`

* **Total Candidate Breakouts Filtered (Vetoed):** `43`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (79.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `15`
* **Saved Capital Losses Avoided:** `+1,008.0%`
* **Missed Upside Forgone:** `-598.2%`
* **Net Veto Alpha:** `+409.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `36` | `83.7%` |
| `Core 4: Whale Firewall` | `6` | `14.0%` |
| `Core 4: Defensible Whale Dump` | `1` | `2.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*