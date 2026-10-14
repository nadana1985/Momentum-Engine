# Kronos V12: Institutional Symbol Tear Sheet — `EDEN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.500`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+28.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.33x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+7.09%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-11.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`31.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+70.0% / -10.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-05-17 13:00` | `2026-05-21 13:00` | Live | `$0.0484` | `$0.0525` | **+8.50%** | **+8.16%** | +232.2% | -21.8% | `shelf_target_reclaim` |
| 2 | Book 2 | `2026-08-26 03:00` | `2026-08-28 11:00` | 56.0h | `$0.0548` | `$0.0722` | **+36.35%** | **+31.55%** | +39.3% | -4.6% | `climax_top_harvest` |
| 3 | Book 2 | `2026-09-17 10:00` | `2026-09-17 11:00` | 1.0h | `$0.0539` | `$0.0494` | **-9.27%** | **-9.68%** | +0.8% | -8.0% | `initial_stop` |
| 4 | Book 1 | `2026-09-22 01:00` | `2026-09-23 14:00` | 37.0h | `$0.0602` | `$0.0589` | **-1.65%** | **-1.67%** | +7.9% | -6.3% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `1` | `100.0%` | **`+31.6%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.7%`** |
| `initial_stop` | `1` | `0.0%` | **`-9.7%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `EDEN`

* **Total Candidate Breakouts Filtered (Vetoed):** `87`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `81` (93.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `52`
* **Saved Capital Losses Avoided:** `+2,568.6%`
* **Missed Upside Forgone:** `-2,510.9%`
* **Net Veto Alpha:** `+57.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `85` | `97.7%` |
| `Core 4: Defensible Whale Dump` | `2` | `2.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*