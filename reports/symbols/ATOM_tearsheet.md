# Kronos V12: Institutional Symbol Tear Sheet — `ATOM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `19` (`19` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `19` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`31.6%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.346`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+15.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.17x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.83%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-30.5%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`99.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.6% / -4.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-03-28 00:00` | `2022-03-31 00:00` | 72.0h | `$30.5662` | `$30.1006` | **-1.52%** | **-1.54%** | +3.7% | -4.8% | `stagnation_cut` |
| 2 | Book 2 | `2022-10-25 17:00` | `2022-11-01 17:00` | 168.0h | `$12.3127` | `$14.1027` | **+14.54%** | **+13.57%** | +17.7% | -3.5% | `time_cap` |
| 3 | Book 2 | `2023-01-12 20:00` | `2023-01-19 20:00` | 168.0h | `$12.2135` | `$12.0448` | **-1.49%** | **-1.50%** | +10.3% | -6.7% | `time_cap` |
| 4 | Book 1 | `2023-04-17 02:00` | `2023-04-18 14:00` | 36.0h | `$12.9353` | `$12.6064` | **-3.05%** | **-3.10%** | +0.1% | -6.0% | `stall_bailout` |
| 5 | Book 2 | `2023-04-26 12:00` | `2023-04-26 19:00` | 7.0h | `$11.3994` | `$10.4973` | **-7.91%** | **-8.24%** | +-0.0% | -8.7% | `initial_stop` |
| 6 | Book 2 | `2023-06-21 01:00` | `2023-06-28 01:00` | 168.0h | `$8.9102` | `$9.3216` | **+4.62%** | **+4.51%** | +9.3% | -1.9% | `time_cap` |
| 7 | Book 2 | `2023-07-13 16:00` | `2023-07-20 16:00` | 168.0h | `$9.5268` | `$9.2448` | **-2.96%** | **-3.00%** | +8.0% | -4.7% | `time_cap` |
| 8 | Book 2 | `2023-09-18 10:00` | `2023-09-21 13:00` | 75.0h | `$7.3754` | `$7.3566` | **-0.26%** | **-0.26%** | +2.8% | -3.4% | `stagnation_cut` |
| 9 | Book 2 | `2023-10-10 07:00` | `2023-10-10 20:00` | 13.0h | `$7.2060` | `$6.6129` | **-8.23%** | **-8.59%** | +1.6% | -8.6% | `initial_stop` |
| 10 | Book 2 | `2023-10-16 05:00` | `2023-10-17 12:00` | 31.0h | `$6.7178` | `$6.4665` | **-3.74%** | **-3.81%** | +1.3% | -3.6% | `initial_stop` |
| 11 | Book 2 | `2023-10-30 21:00` | `2023-11-02 21:00` | 72.0h | `$7.9869` | `$7.7805` | **-2.58%** | **-2.62%** | +3.2% | -5.9% | `stagnation_cut` |
| 12 | Book 1 | `2024-09-21 23:00` | `2024-09-23 11:00` | 36.0h | `$4.7278` | `$4.5546` | **-3.79%** | **-3.86%** | +-0.0% | -5.2% | `stall_bailout` |
| 13 | Book 2 | `2024-11-05 14:00` | `2024-11-12 14:00` | 168.0h | `$4.1413` | `$5.3257` | **+28.60%** | **+25.15%** | +41.0% | -1.9% | `time_cap` |
| 14 | Book 2 | `2025-05-08 03:00` | `2025-05-15 03:00` | 168.0h | `$4.2867` | `$5.0354` | **+17.47%** | **+16.10%** | +28.2% | -1.2% | `time_cap` |
| 15 | Book 2 | `2025-07-11 01:00` | `2025-07-14 14:00` | 85.0h | `$4.6867` | `$4.6384` | **-1.03%** | **-1.04%** | +3.5% | -4.2% | `stagnation_cut` |
| 16 | Book 2 | `2026-05-04 02:00` | `2026-05-05 14:00` | 36.0h | `$1.9218` | `$1.8903` | **-1.64%** | **-1.65%** | +0.1% | -3.3% | `stall_bailout` |
| 17 | Book 2 | `2026-08-21 02:00` | `2026-08-28 02:00` | 168.0h | `$1.5288` | `$1.5332` | **+0.28%** | **+0.28%** | +12.6% | -5.9% | `time_cap` |
| 18 | Book 1 | `2026-09-08 15:00` | `2026-09-11 19:00` | 76.0h | `$1.8115` | `$1.6429` | **-5.98%** | **-6.16%** | +12.3% | -9.8% | `fast_decay_cut` |
| 19 | Book 2 | `2026-09-18 21:00` | `2026-09-25 21:00` | 168.0h | `$1.7333` | `$1.7586` | **+1.46%** | **+1.45%** | +7.5% | -3.9% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `8` | `75.0%` | **`+56.6%`** |
| `stagnation_cut` | `4` | `0.0%` | **`-5.4%`** |
| `initial_stop` | `3` | `0.0%` | **`-20.6%`** |
| `stall_bailout` | `3` | `0.0%` | **`-8.6%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-6.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ATOM`

* **Total Candidate Breakouts Filtered (Vetoed):** `251`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `139` (55.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `42`
* **Saved Capital Losses Avoided:** `+1,782.1%`
* **Missed Upside Forgone:** `-1,143.4%`
* **Net Veto Alpha:** `+638.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `142` | `56.6%` |
| `Core 1: Macro Bear Veto` | `99` | `39.4%` |
| `Core 4: Defensible Whale Dump` | `5` | `2.0%` |
| `Core 4: Funding Rate Cap` | `5` | `2.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*