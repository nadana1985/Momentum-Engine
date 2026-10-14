# Kronos V12: Institutional Symbol Tear Sheet — `PROMPT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+16.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.54%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`47.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+43.5% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-12 15:00` | `2025-07-13 14:00` | 23.0h | `$0.1422` | `$0.1546` | **+8.70%** | **+8.34%** | +8.9% | -1.1% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-08-23 08:00` | `2025-08-27 08:00` | Live | `$0.1650` | `$0.1791` | **+8.50%** | **+8.16%** | +109.5% | -14.1% | `shelf_target_reclaim` |
| 3 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0220` | `$0.0220` | **+0.12%** | **+0.12%** | +12.0% | -3.3% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+0.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `PROMPT`

* **Total Candidate Breakouts Filtered (Vetoed):** `192`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `175` (91.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `24`
* **Saved Capital Losses Avoided:** `+4,277.9%`
* **Missed Upside Forgone:** `-1,756.0%`
* **Net Veto Alpha:** `+2,521.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `186` | `96.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `3` | `1.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*