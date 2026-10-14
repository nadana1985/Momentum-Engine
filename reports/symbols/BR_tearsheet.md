# Kronos V12: Institutional Symbol Tear Sheet — `BR`
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
| **Mean Peak MFE / Max MAE** | **`+22.4% / -15.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-05-03 11:00` | `2025-05-07 11:00` | Live | `$0.0572` | `$0.0621` | **+8.50%** | **+8.16%** | +34.4% | -20.4% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-12-13 16:00` | `2025-12-17 16:00` | Live | `$0.0588` | `$0.0638` | **+8.50%** | **+8.16%** | +17.0% | -9.5% | `shelf_target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2026-06-16 06:00` | `2026-06-20 06:00` | Live | `$0.1407` | `$0.1526` | **+8.50%** | **+8.16%** | +15.9% | -17.3% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `3` | `100.0%` | **`+24.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `BR`

* **Total Candidate Breakouts Filtered (Vetoed):** `213`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `182` (85.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `25`
* **Saved Capital Losses Avoided:** `+3,152.0%`
* **Missed Upside Forgone:** `-2,185.5%`
* **Net Veto Alpha:** `+966.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `194` | `91.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `6` | `2.8%` |
| `Core 4: Defensible Whale Dump` | `6` | `2.8%` |
| `Core 4: Whale Firewall` | `6` | `2.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*