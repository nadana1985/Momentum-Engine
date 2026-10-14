# Kronos V12: Institutional Symbol Tear Sheet — `TRX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.854`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+38.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.47x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.86%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-10.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`229.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.4% / -2.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-05 14:00` | `2021-08-11 12:00` | 142.0h | `$0.0694` | `$0.0833` | **+39.76%** | **+34.34%** | +20.0% | -1.0% | `target_reclaim` |
| 2 | Book 1 | `2022-03-31 06:00` | `2022-04-02 11:00` | 53.0h | `$0.0770` | `$0.0747` | **-5.11%** | **-5.22%** | +3.5% | -7.4% | `fast_decay_cut` |
| 3 | Book 4 | `2022-08-08 08:00` | `2022-08-15 08:00` | 168.0h | `$0.0709` | `$0.0688` | **-1.73%** | **-1.74%** | +2.1% | -4.5% | `stagnation_cut` |
| 4 | Book 2 | `2022-10-26 08:00` | `2022-10-30 22:00` | 110.0h | `$0.0631` | `$0.0629` | **-0.33%** | **-0.34%** | +2.7% | -1.0% | `stagnation_cut` |
| 5 | Book 2 | `2022-11-04 14:00` | `2022-11-07 14:00` | 72.0h | `$0.0636` | `$0.0619` | **-2.69%** | **-2.73%** | +2.8% | -2.8% | `stagnation_cut` |
| 6 | Book 4 | `2023-01-13 23:00` | `2023-02-12 22:00` | 719.0h | `$0.0602` | `$0.0635` | **+3.51%** | **+3.46%** | +19.0% | -2.4% | `time_expiry` |
| 7 | Book 3 | `2024-01-03 12:00` | `2024-01-06 12:00` | 72.0h | `$0.1033` | `$0.1034` | **+0.13%** | **+0.13%** | +5.3% | -1.7% | `time_expiry` |
| 8 | Book 3 | `2024-11-25 22:00` | `2024-11-28 22:00` | 72.0h | `$0.1937` | `$0.2028` | **+4.68%** | **+4.57%** | +5.1% | -4.0% | `time_expiry` |
| 9 | Book 4 | `2026-01-03 21:00` | `2026-01-10 21:00` | 168.0h | `$0.2949` | `$0.2994` | **+1.11%** | **+1.11%** | +2.1% | -1.4% | `stagnation_cut` |
| 10 | Book 4 | `2026-03-11 20:00` | `2026-04-10 19:00` | 719.0h | `$0.2917` | `$0.3163` | **+5.16%** | **+5.06%** | +11.2% | -1.2% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stagnation_cut` | `4` | `25.0%` | **`-3.7%`** |
| `time_expiry` | `4` | `100.0%` | **`+13.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-5.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+34.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `TRX`

* **Total Candidate Breakouts Filtered (Vetoed):** `1550`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `498` (32.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `95`
* **Saved Capital Losses Avoided:** `+3,452.1%`
* **Missed Upside Forgone:** `-2,886.6%`
* **Net Veto Alpha:** `+565.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `930` | `60.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `494` | `31.9%` |
| `Core 4: Defensible Whale Dump` | `60` | `3.9%` |
| `Core 4: Funding Rate Cap` | `27` | `1.7%` |
| `Core 4: Whale Firewall` | `23` | `1.5%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `16` | `1.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*