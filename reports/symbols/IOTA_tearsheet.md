# Kronos V12: Institutional Symbol Tear Sheet — `IOTA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`9.698`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+99.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.70x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+14.18%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`131.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.4% / -3.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2022-03-28 05:00` | `2022-03-29 17:00` | 36.0h | `$0.9078` | `$0.8569` | **-9.88%** | **-10.32%** | +-0.2% | -7.6% | `fast_decay_cut` |
| 2 | Book 2 | `2022-10-25 17:00` | `2022-10-27 17:00` | 48.0h | `$0.2556` | `$0.2545` | **-0.56%** | **-0.56%** | +3.4% | -1.7% | `fast_decay_cut` |
| 3 | Book 2 | `2023-07-13 15:00` | `2023-07-18 11:00` | 116.0h | `$0.1869` | `$0.1859` | **-0.53%** | **-0.54%** | +5.3% | -4.1% | `fast_decay_cut` |
| 4 | Book 4 | `2023-11-09 22:00` | `2023-11-29 12:00` | 470.0h | `$0.1762` | `$0.2114` | **+11.58%** | **+11.05%** | +25.1% | -5.8% | `target_reclaim` |
| 5 | Book 4 | `2024-11-16 07:00` | `2024-11-18 16:00` | 57.0h | `$0.1597` | `$0.1917` | **+95.97%** | **+70.52%** | +23.4% | -5.0% | `target_reclaim` |
| 6 | Book 2 | `2025-04-22 19:00` | `2025-04-29 19:00` | 168.0h | `$0.1845` | `$0.2094` | **+14.71%** | **+13.80%** | +30.7% | -1.4% | `time_cap` |
| 7 | Book 4 | `2025-07-13 06:00` | `2025-07-14 04:00` | 22.0h | `$0.2014` | `$0.2417` | **+16.36%** | **+15.29%** | +20.4% | -0.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `3` | `0.0%` | **`-11.4%`** |
| `target_reclaim` | `3` | `100.0%` | **`+96.9%`** |
| `time_cap` | `1` | `100.0%` | **`+13.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `IOTA`

* **Total Candidate Breakouts Filtered (Vetoed):** `1056`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `437` (41.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `332`
* **Saved Capital Losses Avoided:** `+5,908.1%`
* **Missed Upside Forgone:** `-16,016.6%`
* **Net Veto Alpha:** `+-10,108.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `712` | `67.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `266` | `25.2%` |
| `Core 1: Macro Bear Veto` | `65` | `6.2%` |
| `Core 4: Funding Rate Cap` | `9` | `0.9%` |
| `Core 4: Defensible Whale Dump` | `3` | `0.3%` |
| `Core 4: Whale Firewall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*