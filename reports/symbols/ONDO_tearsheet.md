# Kronos V12: Institutional Symbol Tear Sheet — `ONDO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.855`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+17.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.19x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.41%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`172.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.3% / -6.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-10-29 04:00` | `2024-11-01 04:00` | 72.0h | `$0.7332` | `$0.6929` | **-5.51%** | **-5.66%** | +2.5% | -7.6% | `stagnation_cut` |
| 2 | Book 2 | `2024-11-06 01:00` | `2024-11-13 01:00` | 168.0h | `$0.6620` | `$0.8636` | **+30.47%** | **+26.60%** | +45.6% | -1.6% | `time_cap` |
| 3 | Book 2 | `2025-01-03 15:00` | `2025-01-07 15:00` | 96.0h | `$1.5692` | `$1.4401` | **-8.23%** | **-8.59%** | +4.6% | -10.8% | `initial_stop` |
| 4 | Book 1 | `2025-07-10 16:00` | `2025-07-30 11:00` | 475.0h | `$0.8630` | `$0.9285` | **+10.96%** | **+10.40%** | +35.6% | -2.5% | `trail_stop` |
| 5 | Book 1 | `2026-09-21 10:00` | `2026-09-23 15:00` | 53.0h | `$0.4507` | `$0.4098` | **-5.54%** | **-5.70%** | +3.0% | -11.0% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-5.7%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-5.7%`** |
| `time_cap` | `1` | `100.0%` | **`+26.6%`** |
| `trail_stop` | `1` | `100.0%` | **`+10.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `ONDO`

* **Total Candidate Breakouts Filtered (Vetoed):** `56`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `35` (62.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+400.0%`
* **Missed Upside Forgone:** `-292.1%`
* **Net Veto Alpha:** `+107.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `34` | `60.7%` |
| `Core 4: Funding Rate Cap` | `22` | `39.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*