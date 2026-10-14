# Kronos V12: Institutional Symbol Tear Sheet — `SAND`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`42.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.462`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+40.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.50x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.75%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-5.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`70.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.7% / -4.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-07-07 00:00` | `2021-07-07 06:00` | 6.0h | `$0.3463` | `$0.4156` | **+6.10%** | **+5.88%** | +21.9% | -3.0% | `target_reclaim` |
| 2 | Book 2 | `2022-10-05 01:00` | `2022-10-06 13:00` | 36.0h | `$0.8724` | `$0.8502` | **-3.13%** | **-3.17%** | +0.3% | -4.5% | `stall_bailout` |
| 3 | Book 2 | `2023-07-13 16:00` | `2023-07-15 16:00` | 48.0h | `$0.4568` | `$0.4506` | **-1.57%** | **-1.58%** | +6.4% | -5.6% | `fast_decay_cut` |
| 4 | Book 1 | `2023-11-06 11:00` | `2023-11-07 23:00` | 36.0h | `$0.3921` | `$0.3870` | **-1.03%** | **-1.04%** | +2.8% | -4.8% | `fast_decay_cut` |
| 5 | Book 4 | `2024-11-16 11:00` | `2024-11-23 08:00` | 165.0h | `$0.3367` | `$0.4040` | **+32.61%** | **+25.11%** | +20.2% | -4.2% | `target_reclaim` |
| 6 | Book 2 | `2026-09-03 15:00` | `2026-09-05 03:00` | 36.0h | `$0.0402` | `$0.0392` | **-3.18%** | **-3.22%** | +0.9% | -5.5% | `stall_bailout` |
| 7 | Book 2 | `2026-09-18 00:00` | `2026-09-25 00:00` | 168.0h | `$0.0372` | `$0.0432` | **+19.71%** | **+18.28%** | +22.4% | -1.9% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-2.6%`** |
| `stall_bailout` | `2` | `0.0%` | **`-6.4%`** |
| `target_reclaim` | `2` | `100.0%` | **`+31.0%`** |
| `time_cap` | `1` | `100.0%` | **`+18.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `SAND`

* **Total Candidate Breakouts Filtered (Vetoed):** `1005`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `583` (58.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `361`
* **Saved Capital Losses Avoided:** `+9,226.8%`
* **Missed Upside Forgone:** `-23,893.8%`
* **Net Veto Alpha:** `+-14,666.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `492` | `49.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `450` | `44.8%` |
| `Core 1: Macro Bear Veto` | `49` | `4.9%` |
| `Core 4: Funding Rate Cap` | `14` | `1.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*