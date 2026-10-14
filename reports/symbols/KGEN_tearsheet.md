# Kronos V12: Institutional Symbol Tear Sheet — `KGEN`
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
| **Cumulative Net Log Return** | **`+15.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.17x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+7.78%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`140.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+22.4% / -6.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-01-14 08:00` | `2026-01-22 00:00` | 184.0h | `$0.2624` | `$0.3149` | **+8.26%** | **+7.92%** | +23.8% | -8.6% | `target_reclaim` |
| 2 | Book 4 | `2026-05-10 17:00` | `2026-05-14 17:00` | 96.0h | `$0.2143` | `$0.2572` | **+7.89%** | **+7.64%** | +21.0% | -5.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+15.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `KGEN`

* **Total Candidate Breakouts Filtered (Vetoed):** `366`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `231` (63.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `64`
* **Saved Capital Losses Avoided:** `+2,915.3%`
* **Missed Upside Forgone:** `-1,870.5%`
* **Net Veto Alpha:** `+1,044.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `364` | `99.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `0.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*