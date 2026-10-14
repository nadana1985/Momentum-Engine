# Kronos V12: Institutional Symbol Tear Sheet — `ENS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.770`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-7.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.93x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.49%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-13.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`79.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.3% / -10.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-01-20 23:00` | `2023-01-22 20:00` | 45.0h | `$15.1989` | `$14.1695` | **-9.62%** | **-10.08%** | +1.9% | -7.4% | `fast_decay_cut` |
| 2 | Book 4 | `2023-11-10 01:00` | `2023-11-14 18:00` | 113.0h | `$9.4672` | `$8.0471` | **-12.71%** | **-13.78%** | +1.0% | -17.7% | `structural_stop` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2024-11-27 22:00` | `2024-12-01 22:00` | Live | `$29.9626` | `$32.5094` | **+8.50%** | **+8.16%** | +42.5% | -9.5% | `shelf_target_reclaim` |
| 4 | Book 2 | `2025-04-22 14:00` | `2025-04-28 01:00` | 131.0h | `$15.6400` | `$18.0233` | **+18.00%** | **+16.75%** | +35.9% | -2.1% | `trail_stop` |
| 5 | Book 4 | `2026-09-01 05:00` | `2026-09-02 10:00` | 29.0h | `$6.3064` | `$5.3605` | **-7.83%** | **-8.49%** | +0.2% | -15.2% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `structural_stop` | `2` | `0.0%` | **`-22.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-10.1%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `trail_stop` | `1` | `100.0%` | **`+16.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `ENS`

* **Total Candidate Breakouts Filtered (Vetoed):** `522`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `369` (70.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+3,963.1%`
* **Missed Upside Forgone:** `-740.0%`
* **Net Veto Alpha:** `+3,223.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `351` | `67.2%` |
| `Core 1: Macro Bear Veto` | `162` | `31.0%` |
| `Core 4: Funding Rate Cap` | `5` | `1.0%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `4` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*