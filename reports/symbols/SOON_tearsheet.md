# Kronos V12: Institutional Symbol Tear Sheet — `SOON`
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
| **Average Trade Duration** | **`9.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.1% / -0.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-08-05 20:00` | `2025-08-06 05:00` | 9.0h | `$0.1548` | `$0.1682` | **+8.70%** | **+8.34%** | +11.1% | -0.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `SOON`

* **Total Candidate Breakouts Filtered (Vetoed):** `66`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `35` (53.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `44`
* **Saved Capital Losses Avoided:** `+713.1%`
* **Missed Upside Forgone:** `-3,035.5%`
* **Net Veto Alpha:** `+-2,322.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `26` | `39.4%` |
| `Core 1: Macro Bear Veto` | `22` | `33.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `10` | `15.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `10.6%` |
| `Core 3: Min Turnover Velocity` | `1` | `1.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*