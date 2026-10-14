# Kronos V12: Institutional Symbol Tear Sheet — `AVAX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `17` (`17` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `17` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`70.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`11.171`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+308.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`21.83x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+18.14%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-11.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`123.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.0% / -5.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-01-05 00:00` | `2021-01-06 05:00` | 29.0h | `$3.7817` | `$4.5380` | **+193.49%** | **+115.23%** | +23.2% | -8.4% | `target_reclaim` |
| 2 | Book 4 | `2021-08-13 06:00` | `2021-08-16 17:00` | 83.0h | `$17.5032` | `$21.0039` | **+76.41%** | **+58.27%** | +20.9% | -2.6% | `target_reclaim` |
| 3 | Book 2 | `2022-10-25 17:00` | `2022-11-01 17:00` | 168.0h | `$16.9834` | `$18.6163` | **+11.84%** | **+11.30%** | +16.6% | -3.5% | `time_cap` |
| 4 | Book 1 | `2022-11-05 15:00` | `2022-11-07 15:00` | 48.0h | `$19.9868` | `$18.5326` | **-11.26%** | **-11.92%** | +3.1% | -11.7% | `fast_decay_cut` |
| 5 | Book 1 | `2023-01-11 18:00` | `2023-01-14 00:00` | 54.0h | `$13.9448` | `$16.7337` | **+33.12%** | **+28.96%** | +23.4% | -10.8% | `target_reclaim` |
| 6 | Book 2 | `2023-04-26 10:00` | `2023-04-26 19:00` | 9.0h | `$17.9578` | `$16.4799` | **-8.50%** | **-8.88%** | +1.5% | -8.1% | `initial_stop` |
| 7 | Book 2 | `2023-06-20 18:00` | `2023-06-27 18:00` | 168.0h | `$11.8435` | `$13.2668` | **+14.19%** | **+13.40%** | +15.6% | -1.7% | `time_cap` |
| 8 | Book 2 | `2023-07-13 17:00` | `2023-07-20 17:00` | 168.0h | `$14.0460` | `$13.7914` | **-1.96%** | **-1.98%** | +13.9% | -3.7% | `time_cap` |
| 9 | Book 2 | `2023-10-21 07:00` | `2023-10-28 07:00` | 168.0h | `$9.4646` | `$10.8428` | **+16.73%** | **+15.62%** | +21.2% | -1.1% | `time_cap` |
| 10 | Book 1 | `2023-11-01 19:00` | `2023-11-12 08:00` | 253.0h | `$12.0140` | `$18.4927` | **+64.38%** | **+50.40%** | +58.8% | -5.0% | `climax_top_harvest` |
| 11 | Book 3 | `2024-02-29 22:00` | `2024-03-02 23:00` | 49.0h | `$39.8273` | `$43.9950` | **+10.46%** | **+9.95%** | +12.3% | -0.5% | `target_reclaim` |
| 12 | Book 3 | `2024-03-19 22:00` | `2024-03-22 22:00` | 72.0h | `$54.4187` | `$52.0944` | **-4.27%** | **-4.36%** | +6.9% | -7.3% | `time_expiry` |
| 13 | Book 3 | `2024-11-12 10:00` | `2024-11-15 10:00` | 72.0h | `$33.1586` | `$32.1215` | **-3.13%** | **-3.18%** | +9.6% | -7.8% | `time_expiry` |
| 14 | Book 3 | `2024-12-05 01:00` | `2024-12-08 01:00` | 72.0h | `$51.2339` | `$51.4131` | **+0.35%** | **+0.35%** | +4.8% | -5.6% | `time_expiry` |
| 15 | Book 2 | `2025-04-21 08:00` | `2025-04-28 08:00` | 168.0h | `$20.7628` | `$22.1824` | **+7.81%** | **+7.56%** | +11.1% | -6.5% | `time_cap` |
| 16 | Book 1 | `2025-07-15 22:00` | `2025-07-17 23:00` | 49.0h | `$22.3136` | `$23.9404` | **+12.38%** | **+11.75%** | +9.1% | -3.1% | `target_reclaim` |
| 17 | Book 1 | `2026-09-19 01:00` | `2026-10-08 15:00` | 470.0h | `$8.7187` | `$10.0488` | **+17.16%** | **+15.85%** | +37.7% | -5.1% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+224.2%`** |
| `time_cap` | `5` | `80.0%` | **`+45.9%`** |
| `time_expiry` | `3` | `33.3%` | **`-7.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.9%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-11.9%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+50.4%`** |
| `trail_stop` | `1` | `100.0%` | **`+15.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `AVAX`

* **Total Candidate Breakouts Filtered (Vetoed):** `868`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `378` (43.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `505`
* **Saved Capital Losses Avoided:** `+5,357.7%`
* **Missed Upside Forgone:** `-25,996.2%`
* **Net Veto Alpha:** `+-20,638.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `770` | `88.7%` |
| `Core 1: Macro Bear Veto` | `68` | `7.8%` |
| `Core 4: Funding Rate Cap` | `29` | `3.3%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*