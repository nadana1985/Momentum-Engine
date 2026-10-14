# Kronos V12: Institutional Symbol Tear Sheet — `ARIA`
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
| **Cumulative Net Log Return** | **`+16.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.10%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+30.7% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-27 02:00` | `2026-08-27 03:00` | 1.0h | `$0.0351` | `$0.0397` | **+12.88%** | **+12.11%** | +53.9% | -5.1% | `target_reclaim` |
| 2 | Book 3 | `2026-09-23 14:00` | `2026-09-25 18:00` | 52.0h | `$0.0366` | `$0.0381` | **+4.17%** | **+4.08%** | +7.6% | -7.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+16.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ARIA`

* **Total Candidate Breakouts Filtered (Vetoed):** `426`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `120` (28.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `310`
* **Saved Capital Losses Avoided:** `+2,136.2%`
* **Missed Upside Forgone:** `-13,272.3%`
* **Net Veto Alpha:** `+-11,136.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `422` | `99.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `0.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*