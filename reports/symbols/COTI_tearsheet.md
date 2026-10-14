# Kronos V12: Institutional Symbol Tear Sheet — `COTI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`44.4%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.893`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+34.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.41x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.78%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-7.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`60.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.7% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-19 22:00` | `2021-08-21 01:00` | 27.0h | `$0.2601` | `$0.3122` | **+22.46%** | **+20.59%** | +20.2% | -4.9% | `target_reclaim` |
| 2 | Book 2 | `2022-10-25 11:00` | `2022-10-28 02:00` | 63.0h | `$0.1029` | `$0.1015` | **-1.54%** | **-1.55%** | +4.6% | -1.6% | `fast_decay_cut` |
| 3 | Book 2 | `2022-12-26 10:00` | `2022-12-28 05:00` | 43.0h | `$0.0589` | `$0.0568` | **-4.29%** | **-4.37%** | +1.7% | -4.0% | `breakeven_ratchet` |
| 4 | Book 1 | `2023-01-13 19:00` | `2023-01-18 16:00` | 117.0h | `$0.0697` | `$0.0685` | **-1.67%** | **-1.68%** | +11.1% | -7.1% | `fast_decay_cut` |
| 5 | Book 4 | `2023-01-25 09:00` | `2023-01-26 05:00` | 20.0h | `$0.0990` | `$0.1188` | **+11.58%** | **+11.05%** | +21.2% | -3.1% | `target_reclaim` |
| 6 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$0.0723` | `$0.0762` | **+6.17%** | **+6.01%** | +14.8% | -4.9% | `time_cap` |
| 7 | Book 1 | `2023-11-04 05:00` | `2023-11-05 21:00` | 40.0h | `$0.0505` | `$0.0499` | **-1.91%** | **-1.93%** | +1.9% | -2.7% | `fast_decay_cut` |
| 8 | Book 5 (Shelf Absorption Squeeze) | `2026-07-27 20:00` | `2026-07-31 20:00` | Live | `$0.0110` | `$0.0119` | **+8.50%** | **+8.16%** | +59.1% | -22.1% | `shelf_target_reclaim` |
| 9 | Book 2 | `2026-08-21 12:00` | `2026-08-21 19:00` | 7.0h | `$0.0108` | `$0.0106` | **-2.22%** | **-2.24%** | +15.9% | -4.9% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `3` | `0.0%` | **`-5.2%`** |
| `breakeven_ratchet` | `2` | `0.0%` | **`-6.6%`** |
| `target_reclaim` | `2` | `100.0%` | **`+31.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_cap` | `1` | `100.0%` | **`+6.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `COTI`

* **Total Candidate Breakouts Filtered (Vetoed):** `743`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `471` (63.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `136`
* **Saved Capital Losses Avoided:** `+6,663.0%`
* **Missed Upside Forgone:** `-6,467.0%`
* **Net Veto Alpha:** `+196.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `419` | `56.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `216` | `29.1%` |
| `Core 1: Macro Bear Veto` | `89` | `12.0%` |
| `Core 4: Funding Rate Cap` | `17` | `2.3%` |
| `Core 4: Defensible Whale Dump` | `2` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*