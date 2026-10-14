# Kronos V12: Institutional Symbol Tear Sheet — `GRASS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+42.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.53x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+10.65%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`86.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+46.2% / -15.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2025-05-18 07:00` | `2025-05-21 16:00` | 81.0h | `$2.1218` | `$2.5461` | **+11.58%** | **+11.05%** | +20.6% | -13.3% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-11-18 16:00` | `2025-11-22 16:00` | Live | `$0.3157` | `$0.3425` | **+8.50%** | **+8.16%** | +89.9% | -15.4% | `shelf_target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2026-05-21 21:00` | `2026-05-25 21:00` | Live | `$0.3778` | `$0.4099` | **+8.50%** | **+8.16%** | +52.1% | -25.1% | `shelf_target_reclaim` |
| 4 | Book 4 | `2026-09-21 20:00` | `2026-09-25 16:00` | 92.0h | `$0.4329` | `$0.5195` | **+17.80%** | **+15.22%** | +22.0% | -8.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `target_reclaim` | `2` | `100.0%` | **`+26.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `GRASS`

* **Total Candidate Breakouts Filtered (Vetoed):** `307`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `265` (86.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+4,413.2%`
* **Missed Upside Forgone:** `-750.8%`
* **Net Veto Alpha:** `+3,662.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `221` | `72.0%` |
| `Core 1: Macro Bear Veto` | `86` | `28.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*