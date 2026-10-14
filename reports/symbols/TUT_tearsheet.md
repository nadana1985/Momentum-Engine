# Kronos V12: Institutional Symbol Tear Sheet — `TUT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+48.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.62x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+24.10%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`101.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.0% / -26.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-03-27 17:00` | `2025-03-31 17:00` | Live | `$0.0393` | `$0.0426` | **+8.50%** | **+8.16%** | +16.0% | -50.9% | `shelf_target_reclaim` |
| 2 | Book 4 | `2025-06-18 20:00` | `2025-06-23 01:00` | 101.0h | `$0.0358` | `$0.0430` | **+47.54%** | **+40.05%** | +22.0% | -2.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+40.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `TUT`

* **Total Candidate Breakouts Filtered (Vetoed):** `580`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `265` (45.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `166`
* **Saved Capital Losses Avoided:** `+3,480.8%`
* **Missed Upside Forgone:** `-18,260.5%`
* **Net Veto Alpha:** `+-14,779.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `408` | `70.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `172` | `29.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*