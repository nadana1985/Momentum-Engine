# Kronos V12: Institutional Symbol Tear Sheet — `GPS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+24.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.28x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.16%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`nanh`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+28.2% / -18.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-06-20 10:00` | `2025-06-24 10:00` | Live | `$0.0245` | `$0.0266` | **+8.50%** | **+8.16%** | +41.8% | -11.3% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-02-09 07:00` | `2026-02-13 07:00` | Live | `$0.0110` | `$0.0119` | **+8.50%** | **+8.16%** | +20.0% | -17.9% | `shelf_target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2026-08-17 02:00` | `2026-08-21 02:00` | Live | `$0.0113` | `$0.0123` | **+8.50%** | **+8.16%** | +22.9% | -27.3% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `3` | `100.0%` | **`+24.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `GPS`

* **Total Candidate Breakouts Filtered (Vetoed):** `72`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `59` (81.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+1,338.3%`
* **Missed Upside Forgone:** `-455.6%`
* **Net Veto Alpha:** `+882.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `59` | `81.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `9` | `12.5%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `2.8%` |
| `Core 4: Whale Firewall` | `2` | `2.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*