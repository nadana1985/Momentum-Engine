# Kronos V12: Institutional Symbol Tear Sheet — `VVV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.183`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+3.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.68%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-9.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`34.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.5% / -9.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-06-08 19:00` | `2025-06-12 19:00` | Live | `$2.7747` | `$3.0106` | **+8.50%** | **+8.16%** | +32.2% | -23.5% | `shelf_target_reclaim` |
| 2 | Book 2 | `2025-07-27 16:00` | `2025-07-29 16:00` | 48.0h | `$3.2311` | `$2.9651` | **-9.52%** | **-9.94%** | +12.7% | -9.1% | `initial_stop` |
| 3 | Book 4 | `2026-01-09 06:00` | `2026-01-10 01:00` | 19.0h | `$2.2504` | `$2.7004` | **+9.28%** | **+8.94%** | +21.3% | -1.5% | `target_reclaim` |
| 4 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$14.4956` | `$15.2100` | **+4.93%** | **+4.81%** | +12.8% | -3.0% | `target_reclaim` |
| 5 | Book 3 | `2026-09-21 15:00` | `2026-09-24 11:00` | 68.0h | `$30.9092` | `$28.3654` | **-8.23%** | **-8.59%** | +8.7% | -8.2% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+13.8%`** |
| `initial_stop` | `1` | `0.0%` | **`-9.9%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `VVV`

* **Total Candidate Breakouts Filtered (Vetoed):** `459`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `286` (62.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `107`
* **Saved Capital Losses Avoided:** `+3,896.5%`
* **Missed Upside Forgone:** `-3,834.4%`
* **Net Veto Alpha:** `+62.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `436` | `95.0%` |
| `Core 4: Defensible Whale Dump` | `15` | `3.3%` |
| `Core 4: Whale Firewall` | `7` | `1.5%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*