# Kronos V12: Institutional Symbol Tear Sheet — `ENS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`20.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.750`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.94%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`70.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.2% / -5.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-24 10:00` | `2022-10-27 20:00` | 82.0h | `$17.5528` | `$17.3046` | **-1.41%** | **-1.42%** | +6.7% | -5.4% | `fast_decay_cut` |
| 2 | Book 2 | `2022-11-04 14:00` | `2022-11-06 14:00` | 48.0h | `$17.7773` | `$17.3844` | **-2.21%** | **-2.23%** | +4.1% | -3.7% | `fast_decay_cut` |
| 3 | Book 2 | `2023-01-16 17:00` | `2023-01-18 15:00` | 46.0h | `$15.0515` | `$13.8128` | **-8.23%** | **-8.59%** | +2.2% | -10.7% | `initial_stop` |
| 4 | Book 1 | `2023-01-20 23:00` | `2023-01-22 20:00` | 45.0h | `$15.1989` | `$14.1695` | **-6.44%** | **-6.66%** | +1.9% | -7.4% | `fast_decay_cut` |
| 5 | Book 2 | `2025-04-22 14:00` | `2025-04-28 01:00` | 131.0h | `$15.6400` | `$18.0233` | **+15.24%** | **+14.18%** | +35.9% | -2.1% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `3` | `0.0%` | **`-10.3%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `trail_stop` | `1` | `100.0%` | **`+14.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ENS`

* **Total Candidate Breakouts Filtered (Vetoed):** `135`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `84` (62.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+1,032.5%`
* **Missed Upside Forgone:** `-740.0%`
* **Net Veto Alpha:** `+292.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `81` | `60.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `50` | `37.0%` |
| `Core 4: Funding Rate Cap` | `4` | `3.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*