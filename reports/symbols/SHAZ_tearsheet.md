# Kronos V12: Institutional Symbol Tear Sheet — `SHAZ`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.636`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+6.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.07x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.59%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-10.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`60.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.6% / -17.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-07-22 09:00` | `2026-07-26 09:00` | Live | `$64.3632` | `$69.8341` | **+8.50%** | **+8.16%** | +5.1% | -44.8% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-08-12 12:00` | `2026-08-16 12:00` | Live | `$56.6996` | `$61.5191` | **+8.50%** | **+8.16%** | +31.1% | -13.6% | `shelf_target_reclaim` |
| 3 | Book 2 | `2026-09-08 12:00` | `2026-09-10 12:00` | 48.0h | `$56.8618` | `$54.3638` | **-4.64%** | **-4.75%** | +5.6% | -4.5% | `fast_decay_cut` |
| 4 | Book 3 | `2026-09-23 13:00` | `2026-09-26 13:00` | 72.0h | `$57.9094` | `$54.9622` | **-5.09%** | **-5.22%** | +8.5% | -7.9% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-4.7%`** |
| `time_expiry` | `1` | `0.0%` | **`-5.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `SHAZ`

* **Total Candidate Breakouts Filtered (Vetoed):** `4`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `3` (75.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+58.4%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+58.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `3` | `75.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `25.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*