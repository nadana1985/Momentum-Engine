# Kronos V12: Institutional Symbol Tear Sheet — `AIOT`
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
| **Cumulative Net Log Return** | **`+8.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.09x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.34%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`8.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.1% / -7.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-18 13:00` | `2025-07-18 21:00` | 8.0h | `$0.2938` | `$0.3193` | **+8.70%** | **+8.34%** | +17.1% | -7.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `AIOT`

* **Total Candidate Breakouts Filtered (Vetoed):** `84`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `48` (57.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `52`
* **Saved Capital Losses Avoided:** `+1,124.6%`
* **Missed Upside Forgone:** `-3,223.4%`
* **Net Veto Alpha:** `+-2,098.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `40` | `47.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `29` | `34.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `8` | `9.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `8.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*