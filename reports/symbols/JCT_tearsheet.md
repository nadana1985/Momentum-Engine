# Kronos V12: Institutional Symbol Tear Sheet — `JCT`
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
| **Cumulative Net Log Return** | **`+14.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.16x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+7.28%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`1.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.6% / -1.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-10-08 22:00` | `2026-10-08 23:00` | 1.0h | `$0.0024` | `$0.0025` | **+4.17%** | **+4.08%** | +12.0% | -1.3% | `target_reclaim` |
| 2 | Book 3 | `2026-10-10 07:00` | `2026-10-10 09:00` | 2.0h | `$0.0026` | `$0.0029` | **+11.04%** | **+10.48%** | +19.3% | -1.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+14.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `JCT`

* **Total Candidate Breakouts Filtered (Vetoed):** `165`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `151` (91.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+4,181.4%`
* **Missed Upside Forgone:** `-1,141.6%`
* **Net Veto Alpha:** `+3,039.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `154` | `93.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `11` | `6.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*