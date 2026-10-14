# Kronos V12: Institutional Symbol Tear Sheet — `DOT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `21` (`21` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `21` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.016`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+103.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.82x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.93%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-15.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`91.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.7% / -4.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-11 06:00` | `2021-08-17 01:00` | 139.0h | `$21.5613` | `$25.8736` | **+11.58%** | **+11.05%** | +22.3% | -7.6% | `target_reclaim` |
| 2 | Book 2 | `2022-03-27 20:00` | `2022-04-03 20:00` | 168.0h | `$21.6961` | `$23.0313` | **+6.63%** | **+6.43%** | +9.9% | -5.2% | `time_cap` |
| 3 | Book 2 | `2022-10-25 15:00` | `2022-11-01 15:00` | 168.0h | `$6.1644` | `$6.4937` | **+6.55%** | **+6.38%** | +10.8% | -1.1% | `time_cap` |
| 4 | Book 1 | `2022-11-04 22:00` | `2022-11-06 22:00` | 48.0h | `$7.0827` | `$6.8947` | **-4.18%** | **-4.26%** | +2.3% | -2.8% | `fast_decay_cut` |
| 5 | Book 1 | `2023-01-11 23:00` | `2023-01-14 06:00` | 55.0h | `$5.1418` | `$6.1702` | **+30.21%** | **+26.42%** | +28.0% | -2.6% | `target_reclaim` |
| 6 | Book 2 | `2023-03-14 12:00` | `2023-03-15 16:00` | 28.0h | `$6.3639` | `$5.8401` | **-8.65%** | **-9.02%** | +2.7% | -9.3% | `initial_stop` |
| 7 | Book 1 | `2023-03-18 00:00` | `2023-03-19 12:00` | 36.0h | `$6.6827` | `$6.4159` | **-3.96%** | **-4.05%** | +0.3% | -6.0% | `stall_bailout` |
| 8 | Book 2 | `2023-06-21 01:00` | `2023-06-28 01:00` | 168.0h | `$4.7087` | `$5.0434` | **+8.07%** | **+7.79%** | +11.3% | -1.4% | `time_cap` |
| 9 | Book 2 | `2023-10-01 10:00` | `2023-10-04 00:00` | 62.0h | `$4.1945` | `$4.0019` | **-5.11%** | **-5.23%** | +2.4% | -5.9% | `initial_stop` |
| 10 | Book 2 | `2023-10-16 05:00` | `2023-10-17 13:00` | 32.0h | `$3.8065` | `$3.6457` | **-4.82%** | **-4.93%** | +2.5% | -4.9% | `initial_stop` |
| 11 | Book 2 | `2023-10-21 14:00` | `2023-10-28 14:00` | 168.0h | `$3.8697` | `$4.1566` | **+8.37%** | **+8.07%** | +15.0% | -1.8% | `time_cap` |
| 12 | Book 1 | `2023-11-06 22:00` | `2023-11-08 10:00` | 36.0h | `$5.0015` | `$4.9476` | **-0.86%** | **-0.86%** | +0.2% | -5.6% | `stall_bailout` |
| 13 | Book 4 | `2023-11-09 16:00` | `2023-11-12 10:00` | 66.0h | `$4.8703` | `$5.7469` | **+11.11%** | **+10.22%** | +20.3% | -2.0% | `climax_whale_euphoria_harvest` |
| 14 | Book 3 | `2024-02-28 17:00` | `2024-02-28 18:00` | 1.0h | `$7.6763` | `$8.1950` | **+6.76%** | **+6.54%** | +13.8% | -0.0% | `target_reclaim` |
| 15 | Book 3 | `2024-03-05 19:00` | `2024-03-06 06:00` | 11.0h | `$8.4204` | `$9.7420` | **+15.69%** | **+14.58%** | +18.2% | -4.4% | `target_reclaim` |
| 16 | Book 3 | `2024-03-08 15:00` | `2024-03-09 11:00` | 20.0h | `$10.0317` | `$10.9040` | **+8.70%** | **+8.34%** | +9.4% | -0.7% | `target_reclaim` |
| 17 | Book 3 | `2024-03-12 17:00` | `2024-03-13 09:00` | 16.0h | `$10.3307` | `$11.2290` | **+8.70%** | **+8.34%** | +9.7% | -2.7% | `target_reclaim` |
| 18 | Book 3 | `2024-03-15 03:00` | `2024-03-16 22:00` | 43.0h | `$10.5666` | `$9.6969` | **-8.23%** | **-8.59%** | +4.5% | -8.0% | `stop_loss` |
| 19 | Book 4 | `2024-11-16 01:00` | `2024-11-22 02:00` | 145.0h | `$5.2078` | `$6.2494` | **+48.47%** | **+40.71%** | +20.1% | -0.9% | `target_reclaim` |
| 20 | Book 2 | `2025-06-09 21:00` | `2025-06-13 00:00` | 75.0h | `$4.1463` | `$3.8457` | **-7.93%** | **-8.24%** | +4.7% | -10.7% | `initial_stop` |
| 21 | Book 1 | `2025-07-11 05:00` | `2025-07-29 16:00` | 443.0h | `$3.9879` | `$3.8504` | **-6.02%** | **-6.18%** | +17.3% | -4.9% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `7` | `100.0%` | **`+116.0%`** |
| `initial_stop` | `4` | `0.0%` | **`-27.4%`** |
| `time_cap` | `4` | `100.0%` | **`+28.7%`** |
| `stall_bailout` | `2` | `0.0%` | **`-4.9%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-4.3%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+10.2%`** |
| `breakeven_ratchet` | `1` | `0.0%` | **`-6.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `DOT`

* **Total Candidate Breakouts Filtered (Vetoed):** `630`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `316` (50.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `95`
* **Saved Capital Losses Avoided:** `+3,777.5%`
* **Missed Upside Forgone:** `-2,496.3%`
* **Net Veto Alpha:** `+1,281.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `472` | `74.9%` |
| `Core 1: Macro Bear Veto` | `132` | `21.0%` |
| `Core 4: Funding Rate Cap` | `26` | `4.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*