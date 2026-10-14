# Kronos V12: Institutional Symbol Tear Sheet — `FLNC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`2.028`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+4.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.38%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-4.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`84.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.2% / -11.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-06-01 15:00` | `2026-06-05 15:00` | Live | `$24.2512` | `$26.3126` | **+8.50%** | **+8.16%** | +6.4% | -24.6% | `shelf_target_reclaim` |
| 2 | Book 2 | `2026-08-25 08:00` | `2026-08-27 08:00` | 48.0h | `$11.5488` | `$11.3815` | **-1.76%** | **-1.78%** | +6.3% | -6.2% | `fast_decay_cut` |
| 3 | Book 2 | `2026-09-23 13:00` | `2026-09-28 13:00` | 120.0h | `$7.6190` | `$7.4813` | **-2.23%** | **-2.25%** | +5.8% | -4.8% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-4.0%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `FLNC`

* **Total Candidate Breakouts Filtered (Vetoed):** `5`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `5` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+101.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+101.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `5` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*