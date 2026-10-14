# Kronos V12: Institutional Symbol Tear Sheet — `EUL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.566`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+5.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.47%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-10.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+22.3% / -13.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-02-14 16:00` | `2026-02-18 16:00` | Live | `$0.9228` | `$1.0012` | **+8.50%** | **+8.16%** | +18.9% | -14.2% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-07-25 03:00` | `2026-07-29 03:00` | Live | `$1.1918` | `$1.2931` | **+8.50%** | **+8.16%** | +57.4% | -13.8% | `shelf_target_reclaim` |
| 3 | Book 2 | `2026-08-21 14:00` | `2026-08-22 05:00` | 15.0h | `$1.3594` | `$1.2475` | **-9.38%** | **-9.79%** | +2.7% | -22.8% | `initial_stop` |
| 4 | Book 1 | `2026-08-26 06:00` | `2026-08-28 18:00` | 60.0h | `$1.3684` | `$1.3573` | **-0.63%** | **-0.63%** | +10.0% | -3.7% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.6%`** |
| `initial_stop` | `1` | `0.0%` | **`-9.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `EUL`

* **Total Candidate Breakouts Filtered (Vetoed):** `92`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `60` (65.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `16`
* **Saved Capital Losses Avoided:** `+1,486.2%`
* **Missed Upside Forgone:** `-1,021.2%`
* **Net Veto Alpha:** `+465.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `49` | `53.3%` |
| `Core 4: Defensible Whale Dump` | `43` | `46.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*