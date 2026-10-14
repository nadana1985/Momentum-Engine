# Kronos V12: Institutional Symbol Tear Sheet — `VELODROME`
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
| **Cumulative Net Log Return** | **`+35.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.43x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+17.81%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`140.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.0% / -0.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-08-24 06:00` | `2026-09-03 19:00` | 253.0h | `$0.0206` | `$0.0247` | **+24.24%** | **+22.07%** | +22.1% | -1.7% | `target_reclaim` |
| 2 | Book 3 | `2026-09-10 12:00` | `2026-09-11 15:00` | 27.0h | `$0.0231` | `$0.0265` | **+14.51%** | **+13.55%** | +16.0% | -0.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+35.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `VELODROME`

* **Total Candidate Breakouts Filtered (Vetoed):** `90`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `58` (64.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+694.6%`
* **Missed Upside Forgone:** `-234.2%`
* **Net Veto Alpha:** `+460.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `38` | `42.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `23` | `25.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `15` | `16.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `8.9%` |
| `Core 3: Min Turnover Velocity` | `6` | `6.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*