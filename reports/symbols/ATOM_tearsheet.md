# Kronos V12: Institutional Symbol Tear Sheet — `ATOM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `23` (`23` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `23` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`43.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.250`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+69.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.99x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.00%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-26.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`92.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.5% / -4.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 17:00` | `2022-11-01 17:00` | 168.0h | `$12.3127` | `$14.1027` | **+15.83%** | **+14.78%** | +17.7% | -3.5% | `time_cap` |
| 2 | Book 1 | `2023-04-17 02:00` | `2023-04-18 14:00` | 36.0h | `$12.9353` | `$12.6064` | **-2.51%** | **-2.55%** | +0.1% | -6.0% | `stall_bailout` |
| 3 | Book 2 | `2023-04-26 12:00` | `2023-04-26 19:00` | 7.0h | `$11.3994` | `$10.4973` | **-8.24%** | **-8.59%** | +-0.0% | -8.7% | `initial_stop` |
| 4 | Book 2 | `2023-06-21 01:00` | `2023-06-28 01:00` | 168.0h | `$8.9102` | `$9.3216` | **+5.22%** | **+5.10%** | +9.3% | -1.9% | `time_cap` |
| 5 | Book 2 | `2023-07-13 16:00` | `2023-07-20 16:00` | 168.0h | `$9.5268` | `$9.2448` | **-3.19%** | **-3.24%** | +8.0% | -4.7% | `time_cap` |
| 6 | Book 2 | `2023-09-18 10:00` | `2023-09-21 13:00` | 75.0h | `$7.3754` | `$7.3566` | **-0.29%** | **-0.29%** | +2.8% | -3.4% | `stagnation_cut` |
| 7 | Book 2 | `2023-10-10 07:00` | `2023-10-10 20:00` | 13.0h | `$7.2060` | `$6.6129` | **-9.22%** | **-9.62%** | +1.6% | -8.6% | `initial_stop` |
| 8 | Book 2 | `2023-10-16 05:00` | `2023-10-17 12:00` | 31.0h | `$6.7178` | `$6.4665` | **-4.28%** | **-4.36%** | +1.3% | -3.6% | `breakeven_ratchet` |
| 9 | Book 2 | `2023-10-30 21:00` | `2023-11-02 21:00` | 72.0h | `$7.9869` | `$7.7805` | **-2.69%** | **-2.73%** | +3.2% | -5.9% | `stagnation_cut` |
| 10 | Book 4 | `2023-11-09 17:00` | `2023-11-13 10:00` | 89.0h | `$8.6580` | `$10.3896` | **+11.58%** | **+11.05%** | +21.9% | -1.8% | `target_reclaim` |
| 11 | Book 3 | `2024-02-29 21:00` | `2024-03-02 04:00` | 31.0h | `$11.3945` | `$11.9170` | **+4.59%** | **+4.48%** | +5.3% | -3.4% | `target_reclaim` |
| 12 | Book 3 | `2024-03-05 19:00` | `2024-03-06 05:00` | 10.0h | `$11.3945` | `$12.3540` | **+8.42%** | **+8.08%** | +12.5% | -6.9% | `target_reclaim` |
| 13 | Book 1 | `2024-09-21 23:00` | `2024-09-23 11:00` | 36.0h | `$4.7278` | `$4.5546` | **-3.96%** | **-4.06%** | +-0.0% | -5.2% | `stall_bailout` |
| 14 | Book 1 | `2024-09-26 15:00` | `2024-09-29 22:00` | 79.0h | `$5.0646` | `$5.0224` | **-1.18%** | **-1.19%** | +2.5% | -2.7% | `stagnation_bailout` |
| 15 | Book 2 | `2024-11-05 14:00` | `2024-11-12 14:00` | 168.0h | `$4.1413` | `$5.3257` | **+33.81%** | **+29.73%** | +41.0% | -1.9% | `time_cap` |
| 16 | Book 4 | `2024-11-16 20:00` | `2024-11-22 12:00` | 136.0h | `$5.8818` | `$7.0582` | **+35.83%** | **+31.35%** | +21.4% | -5.3% | `target_reclaim` |
| 17 | Book 2 | `2025-05-08 03:00` | `2025-05-15 03:00` | 168.0h | `$4.2867` | `$5.0354` | **+19.43%** | **+17.91%** | +28.2% | -1.2% | `time_cap` |
| 18 | Book 2 | `2025-07-11 01:00` | `2025-07-14 14:00` | 85.0h | `$4.6867` | `$4.6384` | **-1.05%** | **-1.05%** | +3.5% | -4.2% | `stagnation_cut` |
| 19 | Book 1 | `2025-07-18 03:00` | `2025-07-23 17:00` | 134.0h | `$5.0275` | `$4.6982` | **-9.95%** | **-10.41%** | +5.8% | -7.6% | `fast_decay_cut` |
| 20 | Book 2 | `2026-05-04 02:00` | `2026-05-05 14:00` | 36.0h | `$1.9218` | `$1.8903` | **-1.83%** | **-1.85%** | +0.1% | -3.3% | `stall_bailout` |
| 21 | Book 2 | `2026-08-21 02:00` | `2026-08-28 02:00` | 168.0h | `$1.5288` | `$1.5332` | **+0.32%** | **+0.32%** | +12.6% | -5.9% | `time_cap` |
| 22 | Book 1 | `2026-09-08 15:00` | `2026-09-11 19:00` | 76.0h | `$1.8115` | `$1.6429` | **-5.14%** | **-5.31%** | +12.3% | -9.8% | `fast_decay_cut` |
| 23 | Book 2 | `2026-09-18 21:00` | `2026-09-25 21:00` | 168.0h | `$1.7333` | `$1.7586` | **+1.49%** | **+1.48%** | +7.5% | -3.9% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `7` | `85.7%` | **`+66.1%`** |
| `target_reclaim` | `4` | `100.0%` | **`+55.0%`** |
| `stagnation_cut` | `3` | `0.0%` | **`-4.1%`** |
| `stall_bailout` | `3` | `0.0%` | **`-8.5%`** |
| `initial_stop` | `2` | `0.0%` | **`-18.2%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-15.7%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-1.2%`** |
| `breakeven_ratchet` | `1` | `0.0%` | **`-4.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `ATOM`

* **Total Candidate Breakouts Filtered (Vetoed):** `355`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `238` (67.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `42`
* **Saved Capital Losses Avoided:** `+3,059.8%`
* **Missed Upside Forgone:** `-1,143.4%`
* **Net Veto Alpha:** `+1,916.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `198` | `55.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `146` | `41.1%` |
| `Core 4: Defensible Whale Dump` | `5` | `1.4%` |
| `Core 4: Funding Rate Cap` | `5` | `1.4%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*