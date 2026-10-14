# Kronos V12: Institutional Symbol Tear Sheet — `INIT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+39.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.48x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+7.84%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`15.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.2% / -7.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-01 05:00` | `2025-07-02 17:00` | 36.0h | `$0.4143` | `$0.4503` | **+8.70%** | **+8.34%** | +9.8% | -5.8% | `target_reclaim` |
| 2 | Book 3 | `2025-07-11 15:00` | `2025-07-12 01:00` | 10.0h | `$0.4911` | `$0.5338` | **+8.70%** | **+8.34%** | +11.8% | -2.8% | `target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2026-02-15 17:00` | `2026-02-19 17:00` | Live | `$0.0806` | `$0.0874` | **+8.50%** | **+8.16%** | +34.6% | -16.1% | `shelf_target_reclaim` |
| 4 | Book 3 | `2026-08-22 05:00` | `2026-08-22 08:00` | 3.0h | `$0.0542` | `$0.0583` | **+7.63%** | **+7.35%** | +12.3% | -9.9% | `target_reclaim` |
| 5 | Book 3 | `2026-09-29 19:00` | `2026-09-30 06:00` | 11.0h | `$0.0998` | `$0.1071` | **+7.27%** | **+7.02%** | +7.5% | -1.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+31.0%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `INIT`

* **Total Candidate Breakouts Filtered (Vetoed):** `52`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `38` (73.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+503.4%`
* **Missed Upside Forgone:** `-49.2%`
* **Net Veto Alpha:** `+454.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `23` | `44.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `14` | `26.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `12` | `23.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `3` | `5.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*