# Kronos V12: Institutional Symbol Tear Sheet — `KSM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `27` (`27` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `27` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.954`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+93.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.54x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.46%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-26.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`56.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.8% / -4.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-11 07:00` | `2021-08-16 11:00` | 124.0h | `$258.2368` | `$309.8841` | **+25.74%** | **+23.32%** | +21.4% | -4.3% | `target_reclaim` |
| 2 | Book 3 | `2022-03-28 23:00` | `2022-03-29 01:00` | 2.0h | `$166.2816` | `$173.2100` | **+4.17%** | **+4.08%** | +5.4% | -2.5% | `target_reclaim` |
| 3 | Book 2 | `2022-10-25 15:00` | `2022-10-27 20:00` | 53.0h | `$35.3782` | `$35.0621` | **-1.10%** | **-1.10%** | +5.4% | -2.1% | `fast_decay_cut` |
| 4 | Book 3 | `2023-01-14 09:00` | `2023-01-17 08:00` | 71.0h | `$30.4246` | `$33.7000` | **+10.77%** | **+10.22%** | +11.1% | -3.5% | `target_reclaim` |
| 5 | Book 3 | `2023-01-29 00:00` | `2023-01-29 23:00` | 23.0h | `$35.7331` | `$37.2900` | **+4.36%** | **+4.26%** | +4.4% | -0.3% | `target_reclaim` |
| 6 | Book 3 | `2023-02-05 12:00` | `2023-02-08 12:00` | 72.0h | `$35.7331` | `$36.3489` | **+1.72%** | **+1.71%** | +7.5% | -2.5% | `time_expiry` |
| 7 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$32.8920` | `$36.0796` | **+11.18%** | **+10.67%** | +15.5% | -5.7% | `time_cap` |
| 8 | Book 3 | `2023-07-02 08:00` | `2023-07-02 22:00` | 14.0h | `$25.4592` | `$26.5200` | **+4.17%** | **+4.08%** | +4.4% | -0.2% | `target_reclaim` |
| 9 | Book 3 | `2023-07-04 04:00` | `2023-07-07 00:00` | 68.0h | `$25.7664` | `$23.6458` | **-8.23%** | **-8.59%** | +1.7% | -8.1% | `stop_loss` |
| 10 | Book 2 | `2023-09-21 00:00` | `2023-09-22 12:00` | 36.0h | `$19.9197` | `$19.2617` | **-3.80%** | **-3.86%** | +0.3% | -4.3% | `stall_bailout` |
| 11 | Book 3 | `2023-09-22 16:00` | `2023-09-25 16:00` | 72.0h | `$18.8544` | `$18.8627` | **+0.04%** | **+0.04%** | +1.4% | -4.1% | `time_expiry` |
| 12 | Book 3 | `2023-10-02 18:00` | `2023-10-05 18:00` | 72.0h | `$18.9760` | `$18.0049` | **-5.12%** | **-5.25%** | +3.6% | -5.7% | `time_expiry` |
| 13 | Book 3 | `2023-11-13 02:00` | `2023-11-14 00:00` | 22.0h | `$26.2686` | `$24.1067` | **-8.23%** | **-8.59%** | +6.7% | -8.3% | `stop_loss` |
| 14 | Book 3 | `2023-12-25 21:00` | `2023-12-26 09:00` | 12.0h | `$56.6614` | `$62.2000` | **+9.77%** | **+9.33%** | +12.6% | -2.0% | `target_reclaim` |
| 15 | Book 3 | `2024-02-13 14:00` | `2024-02-13 21:00` | 7.0h | `$42.2784` | `$44.0400` | **+4.17%** | **+4.08%** | +4.5% | -0.8% | `target_reclaim` |
| 16 | Book 3 | `2024-02-29 16:00` | `2024-03-02 03:00` | 35.0h | `$50.4672` | `$52.5700` | **+4.17%** | **+4.08%** | +4.8% | -5.5% | `target_reclaim` |
| 17 | Book 3 | `2024-03-03 07:00` | `2024-03-03 16:00` | 9.0h | `$50.6674` | `$54.3500` | **+7.27%** | **+7.02%** | +7.5% | -4.1% | `target_reclaim` |
| 18 | Book 3 | `2024-03-08 16:00` | `2024-03-11 16:00` | 72.0h | `$50.3680` | `$54.2540` | **+7.72%** | **+7.43%** | +9.1% | -3.6% | `time_expiry` |
| 19 | Book 3 | `2024-03-15 03:00` | `2024-03-16 18:00` | 39.0h | `$52.4960` | `$48.1756` | **-8.23%** | **-8.59%** | +6.4% | -10.6% | `stop_loss` |
| 20 | Book 3 | `2024-05-19 12:00` | `2024-05-20 17:00` | 29.0h | `$29.9136` | `$31.1600` | **+4.17%** | **+4.08%** | +5.2% | -5.5% | `target_reclaim` |
| 21 | Book 3 | `2024-05-23 15:00` | `2024-05-24 15:00` | 24.0h | `$30.0206` | `$32.2900` | **+7.56%** | **+7.29%** | +7.8% | -6.1% | `target_reclaim` |
| 22 | Book 4 | `2024-11-22 23:00` | `2024-11-23 12:00` | 13.0h | `$23.4912` | `$28.1894` | **+37.09%** | **+31.03%** | +43.0% | -1.6% | `target_reclaim` |
| 23 | Book 3 | `2025-07-14 14:00` | `2025-07-16 07:00` | 41.0h | `$14.7984` | `$15.4150` | **+4.17%** | **+4.08%** | +6.9% | -4.4% | `target_reclaim` |
| 24 | Book 4 | `2025-09-13 12:00` | `2025-09-20 12:00` | 168.0h | `$16.9985` | `$15.9081` | **-8.25%** | **-8.55%** | +0.3% | -11.5% | `stagnation_cut` |
| 25 | Book 2 | `2026-05-04 00:00` | `2026-05-06 00:00` | 48.0h | `$4.9313` | `$4.8848` | **-1.11%** | **-1.12%** | +2.4% | -3.4% | `fast_decay_cut` |
| 26 | Book 3 | `2026-09-10 23:00` | `2026-09-13 23:00` | 72.0h | `$3.6763` | `$3.8344` | **+4.30%** | **+4.21%** | +7.7% | -1.2% | `time_expiry` |
| 27 | Book 4 | `2026-09-17 16:00` | `2026-09-24 16:00` | 168.0h | `$4.6800` | `$4.5322` | **-2.06%** | **-2.08%** | +3.1% | -11.0% | `stagnation_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `13` | `100.0%` | **`+117.0%`** |
| `time_expiry` | `5` | `80.0%` | **`+8.1%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-2.2%`** |
| `stagnation_cut` | `2` | `0.0%` | **`-10.6%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.9%`** |
| `time_cap` | `1` | `100.0%` | **`+10.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `KSM`

* **Total Candidate Breakouts Filtered (Vetoed):** `1059`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `555` (52.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `207`
* **Saved Capital Losses Avoided:** `+7,071.4%`
* **Missed Upside Forgone:** `-6,802.6%`
* **Net Veto Alpha:** `+268.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `511` | `48.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `344` | `32.5%` |
| `Core 1: Macro Bear Veto` | `83` | `7.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `80` | `7.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `41` | `3.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*