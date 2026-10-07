# Kronos V12: Institutional Symbol Tear Sheet — `INIT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+33.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.40x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.34%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`14.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.0% / -5.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-01 05:00` | `2025-07-02 17:00` | 36.0h | `$0.4143` | `$0.4503` | **+8.70%** | **+8.34%** | +9.8% | -5.8% | `target_reclaim` |
| 2 | Book 3 | `2025-07-11 15:00` | `2025-07-12 01:00` | 10.0h | `$0.4911` | `$0.5338` | **+8.70%** | **+8.34%** | +11.8% | -2.8% | `target_reclaim` |
| 3 | Book 3 | `2026-08-22 05:00` | `2026-08-22 08:00` | 3.0h | `$0.0536` | `$0.0583` | **+8.70%** | **+8.34%** | +13.4% | -9.0% | `target_reclaim` |
| 4 | Book 3 | `2026-09-30 07:00` | `2026-09-30 16:00` | 9.0h | `$0.0985` | `$0.1071` | **+8.70%** | **+8.34%** | +8.9% | -2.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `INIT`

* **Total Candidate Breakouts Filtered (Vetoed):** `57`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `39` (68.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+503.8%`
* **Missed Upside Forgone:** `-49.2%`
* **Net Veto Alpha:** `+454.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `23` | `40.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `17` | `29.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `14` | `24.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `3` | `5.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*