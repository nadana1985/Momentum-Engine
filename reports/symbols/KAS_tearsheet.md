# Kronos V12: Institutional Symbol Tear Sheet — `KAS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.673`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-6.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.93x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.70%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-19.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`116.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.3% / -9.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-06-26 23:00` | `2024-06-30 23:00` | Live | `$0.1622` | `$0.1760` | **+8.50%** | **+8.16%** | +12.2% | -17.2% | `shelf_target_reclaim` |
| 2 | Book 4 | `2024-11-14 19:00` | `2024-11-15 15:00` | 20.0h | `$0.1494` | `$0.1270` | **-18.12%** | **-19.64%** | +0.9% | -15.2% | `structural_stop` |
| 3 | Book 2 | `2025-04-22 04:00` | `2025-04-29 04:00` | 168.0h | `$0.0895` | `$0.0944` | **+5.99%** | **+5.83%** | +22.0% | -2.0% | `time_cap` |
| 4 | Book 1 | `2026-09-07 05:00` | `2026-09-13 22:00` | 161.0h | `$0.0333` | `$0.0331` | **-1.14%** | **-1.14%** | +17.9% | -1.7% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.1%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-19.6%`** |
| `time_cap` | `1` | `100.0%` | **`+5.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `KAS`

* **Total Candidate Breakouts Filtered (Vetoed):** `648`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `449` (69.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `38`
* **Saved Capital Losses Avoided:** `+5,526.8%`
* **Missed Upside Forgone:** `-869.5%`
* **Net Veto Alpha:** `+4,657.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `562` | `86.7%` |
| `Core 1: Macro Bear Veto` | `81` | `12.5%` |
| `Core 4: Funding Rate Cap` | `4` | `0.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*