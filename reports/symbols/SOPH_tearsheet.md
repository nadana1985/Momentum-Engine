# Kronos V12: Institutional Symbol Tear Sheet — `SOPH`
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
| **Cumulative Net Log Return** | **`+16.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.16%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`nanh`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+37.6% / -26.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-12-19 18:00` | `2025-12-23 18:00` | Live | `$0.0139` | `$0.0151` | **+8.50%** | **+8.16%** | +8.1% | -21.0% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-09-07 09:00` | `2026-09-11 09:00` | Live | `$0.0046` | `$0.0050` | **+8.50%** | **+8.16%** | +67.1% | -32.8% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `SOPH`

* **Total Candidate Breakouts Filtered (Vetoed):** `22`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `19` (86.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+324.9%`
* **Missed Upside Forgone:** `-413.0%`
* **Net Veto Alpha:** `+-88.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `13` | `59.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `5` | `22.7%` |
| `Core 4: Funding Rate Cap` | `3` | `13.6%` |
| `Core 4: Whale Firewall` | `1` | `4.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*