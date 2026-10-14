# Kronos V12: Institutional Symbol Tear Sheet — `REZ`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.247`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+3.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.08%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-13.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`13.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.3% / -21.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-03-05 17:00` | `2025-03-09 17:00` | Live | `$0.0207` | `$0.0225` | **+8.50%** | **+8.16%** | +34.0% | -20.6% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-03-30 06:00` | `2025-04-03 06:00` | Live | `$0.0170` | `$0.0185` | **+8.50%** | **+8.16%** | +12.8% | -29.0% | `shelf_target_reclaim` |
| 3 | Book 4 | `2026-09-12 17:00` | `2026-09-13 06:00` | 13.0h | `$0.0040` | `$0.0034` | **-12.07%** | **-13.09%** | +8.0% | -15.3% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `structural_stop` | `1` | `0.0%` | **`-13.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `REZ`

* **Total Candidate Breakouts Filtered (Vetoed):** `144`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `55` (38.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+801.9%`
* **Missed Upside Forgone:** `-977.1%`
* **Net Veto Alpha:** `+-175.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `106` | `73.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `37` | `25.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*