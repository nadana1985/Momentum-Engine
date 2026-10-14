# Kronos V12: Institutional Symbol Tear Sheet — `LINK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`46.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.571`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+25.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.28x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.92%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-27.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`135.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.6% / -6.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-03 00:00` | `2021-08-10 00:00` | 168.0h | `$24.1742` | `$23.9620` | **-0.20%** | **-0.20%** | +4.2% | -8.7% | `stagnation_cut` |
| 2 | Book 4 | `2023-02-09 08:00` | `2023-02-13 02:00` | 90.0h | `$7.7326` | `$6.6520` | **-13.47%** | **-14.52%** | +0.7% | -14.8% | `structural_stop` |
| 3 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$6.5684` | `$7.0633` | **+8.08%** | **+7.79%** | +11.1% | -3.0% | `time_cap` |
| 4 | Book 1 | `2023-07-03 02:00` | `2023-07-04 14:00` | 36.0h | `$6.6426` | `$6.4937` | **-1.12%** | **-1.12%** | +0.7% | -3.2% | `stall_bailout` |
| 5 | Book 4 | `2023-07-13 18:00` | `2023-07-20 10:00` | 160.0h | `$6.8162` | `$8.1795` | **+15.62%** | **+14.68%** | +20.1% | -5.7% | `target_reclaim` |
| 6 | Book 4 | `2023-09-18 10:00` | `2023-09-30 06:00` | 284.0h | `$6.7872` | `$8.1446` | **+13.12%** | **+12.32%** | +20.0% | -4.1% | `target_reclaim` |
| 7 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$14.8030` | `$14.7361` | **-0.45%** | **-0.45%** | +9.1% | -7.7% | `time_expiry` |
| 8 | Book 3 | `2023-12-30 08:00` | `2024-01-02 08:00` | 72.0h | `$15.0789` | `$15.9800` | **+5.98%** | **+5.80%** | +6.7% | -2.2% | `time_expiry` |
| 9 | Book 3 | `2024-03-03 07:00` | `2024-03-05 19:00` | 60.0h | `$20.1711` | `$18.5111` | **-8.23%** | **-8.59%** | +4.6% | -18.9% | `stop_loss` |
| 10 | Book 1 | `2024-11-09 22:00` | `2024-11-13 02:00` | 76.0h | `$13.7994` | `$13.7206` | **-0.58%** | **-0.58%** | +11.4% | -2.4% | `fast_decay_cut` |
| 11 | Book 1 | `2025-04-23 04:00` | `2025-05-06 11:00` | 319.0h | `$14.7347` | `$13.2658` | **-16.90%** | **-18.31%** | +4.2% | -10.3% | `initial_stop` |
| 12 | Book 4 | `2025-07-13 01:00` | `2025-07-18 00:00` | 119.0h | `$15.1837` | `$18.2205` | **+18.21%** | **+16.95%** | +21.8% | -0.9% | `target_reclaim` |
| 13 | Book 4 | `2026-08-15 16:00` | `2026-08-21 07:00` | 135.0h | `$9.6234` | `$11.5481` | **+11.75%** | **+11.21%** | +23.2% | -3.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+55.2%`** |
| `time_expiry` | `2` | `50.0%` | **`+5.4%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.6%`** |
| `initial_stop` | `1` | `0.0%` | **`-18.3%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-0.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.1%`** |
| `structural_stop` | `1` | `0.0%` | **`-14.5%`** |
| `time_cap` | `1` | `100.0%` | **`+7.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `LINK`

* **Total Candidate Breakouts Filtered (Vetoed):** `600`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `382` (63.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `55`
* **Saved Capital Losses Avoided:** `+4,345.0%`
* **Missed Upside Forgone:** `-1,567.0%`
* **Net Veto Alpha:** `+2,778.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `361` | `60.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `206` | `34.3%` |
| `Core 4: Funding Rate Cap` | `20` | `3.3%` |
| `Core 4: Whale Firewall` | `9` | `1.5%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `0.3%` |
| `Core 4: Defensible Whale Dump` | `2` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*