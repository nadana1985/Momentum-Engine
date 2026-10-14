# Kronos V12: Institutional Symbol Tear Sheet — `CTK`
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
| **Cumulative Net Log Return** | **`+21.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.23x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+10.49%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`1.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.3% / -15.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-06-29 07:00` | `2025-07-03 07:00` | Live | `$0.3020` | `$0.3277` | **+8.50%** | **+8.16%** | +4.6% | -17.2% | `shelf_target_reclaim` |
| 2 | Book 4 | `2026-10-12 14:00` | `2026-10-12 15:00` | 1.0h | `$0.1502` | `$0.1727` | **+13.68%** | **+12.82%** | +17.9% | -13.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `CTK`

* **Total Candidate Breakouts Filtered (Vetoed):** `132`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `124` (93.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `24`
* **Saved Capital Losses Avoided:** `+1,786.9%`
* **Missed Upside Forgone:** `-589.4%`
* **Net Veto Alpha:** `+1,197.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `78` | `59.1%` |
| `Core 1: Macro Bear Veto` | `49` | `37.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `3.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*