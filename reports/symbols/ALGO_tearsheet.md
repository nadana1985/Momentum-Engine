# Kronos V12: Institutional Symbol Tear Sheet — `ALGO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `12` (`12` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `12` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`41.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`16.698`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+149.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`4.47x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+12.48%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`139.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.8% / -3.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-01-08 23:00` | `2023-01-10 11:00` | 36.0h | `$0.1996` | `$0.1989` | **-0.50%** | **-0.50%** | +4.4% | -1.6% | `fast_decay_cut` |
| 2 | Book 1 | `2023-01-13 20:00` | `2023-01-18 16:00` | 116.0h | `$0.2180` | `$0.2138` | **-2.48%** | **-2.52%** | +11.0% | -3.6% | `fast_decay_cut` |
| 3 | Book 2 | `2023-06-23 16:00` | `2023-06-26 01:00` | 57.0h | `$0.1328` | `$0.1313` | **-1.43%** | **-1.44%** | +6.1% | -1.8% | `fast_decay_cut` |
| 4 | Book 2 | `2023-07-13 17:00` | `2023-07-15 17:00` | 48.0h | `$0.1162` | `$0.1130` | **-3.36%** | **-3.41%** | +6.4% | -5.7% | `fast_decay_cut` |
| 5 | Book 2 | `2023-09-20 18:00` | `2023-09-25 17:00` | 119.0h | `$0.0989` | `$0.0982` | **-0.96%** | **-0.96%** | +4.3% | -3.5% | `fast_decay_cut` |
| 6 | Book 2 | `2023-10-23 22:00` | `2023-10-27 01:00` | 75.0h | `$0.0987` | `$0.0985` | **-0.34%** | **-0.34%** | +5.0% | -3.2% | `fast_decay_cut` |
| 7 | Book 1 | `2023-11-06 08:00` | `2023-11-07 22:00` | 38.0h | `$0.1240` | `$0.1233` | **-0.36%** | **-0.36%** | +4.9% | -4.6% | `fast_decay_cut` |
| 8 | Book 4 | `2023-11-11 10:00` | `2023-12-04 03:00` | 545.0h | `$0.1318` | `$0.1582` | **+37.84%** | **+32.89%** | +20.3% | -7.1% | `target_reclaim` |
| 9 | Book 4 | `2024-11-10 05:00` | `2024-11-15 13:00` | 128.0h | `$0.1422` | `$0.1707` | **+133.47%** | **+89.73%** | +21.4% | -2.6% | `target_reclaim` |
| 10 | Book 1 | `2025-04-21 05:00` | `2025-05-03 00:00` | 283.0h | `$0.2010` | `$0.2112` | **+6.40%** | **+6.19%** | +18.8% | -5.9% | `trail_stop` |
| 11 | Book 4 | `2025-07-11 01:00` | `2025-07-13 15:00` | 62.0h | `$0.2172` | `$0.2607` | **+28.36%** | **+25.46%** | +24.3% | -2.2% | `target_reclaim` |
| 12 | Book 2 | `2026-05-05 05:00` | `2026-05-12 05:00` | 168.0h | `$0.1194` | `$0.1253` | **+5.11%** | **+4.98%** | +14.7% | -2.9% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `7` | `0.0%` | **`-9.5%`** |
| `target_reclaim` | `3` | `100.0%` | **`+148.1%`** |
| `time_cap` | `1` | `100.0%` | **`+5.0%`** |
| `trail_stop` | `1` | `100.0%` | **`+6.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALGO`

* **Total Candidate Breakouts Filtered (Vetoed):** `1236`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `554` (44.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `338`
* **Saved Capital Losses Avoided:** `+6,396.4%`
* **Missed Upside Forgone:** `-12,381.0%`
* **Net Veto Alpha:** `+-5,984.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `916` | `74.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `226` | `18.3%` |
| `Core 1: Macro Bear Veto` | `79` | `6.4%` |
| `Core 4: Funding Rate Cap` | `15` | `1.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*