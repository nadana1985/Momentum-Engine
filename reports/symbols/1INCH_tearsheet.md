# Kronos V12: Institutional Symbol Tear Sheet — `1INCH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `26` (`26` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `26` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.567`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+159.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`4.92x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+6.12%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`42.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.5% / -6.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-01-26 17:00` | `2021-01-28 04:00` | 35.0h | `$2.4698` | `$2.9638` | **+64.30%** | **+51.49%** | +21.5% | -10.2% | `target_reclaim` |
| 2 | Book 2 | `2022-10-25 17:00` | `2022-10-28 02:00` | 57.0h | `$0.5912` | `$0.5870` | **-0.85%** | **-0.85%** | +5.2% | -2.2% | `fast_decay_cut` |
| 3 | Book 3 | `2023-01-22 20:00` | `2023-01-23 01:00` | 5.0h | `$0.5046` | `$0.5315` | **+5.34%** | **+5.20%** | +6.4% | -0.7% | `target_reclaim` |
| 4 | Book 3 | `2023-01-24 22:00` | `2023-01-25 00:00` | 2.0h | `$0.5046` | `$0.5462` | **+8.25%** | **+7.93%** | +12.2% | -1.6% | `target_reclaim` |
| 5 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$0.4791` | `$0.5451` | **+15.62%** | **+14.63%** | +21.5% | -3.5% | `time_cap` |
| 6 | Book 3 | `2023-03-31 07:00` | `2023-04-03 07:00` | 72.0h | `$0.5374` | `$0.5120` | **-4.73%** | **-4.84%** | +4.7% | -6.6% | `time_expiry` |
| 7 | Book 2 | `2023-07-12 00:00` | `2023-07-16 11:00` | 107.0h | `$0.3169` | `$0.4230` | **+39.65%** | **+34.19%** | +37.1% | -1.2% | `climax_top_harvest` |
| 8 | Book 5 (Shelf Absorption Squeeze) | `2023-07-15 15:00` | `2023-07-19 15:00` | Live | `$0.3419` | `$0.3709` | **+8.50%** | **+8.16%** | +19.2% | -25.5% | `shelf_target_reclaim` |
| 9 | Book 3 | `2023-07-17 16:00` | `2023-07-18 01:00` | 9.0h | `$0.4223` | `$0.3875` | **-8.23%** | **-8.59%** | +4.5% | -8.6% | `stop_loss` |
| 10 | Book 2 | `2023-09-21 01:00` | `2023-09-23 01:00` | 48.0h | `$0.2648` | `$0.2632` | **-0.67%** | **-0.67%** | +5.6% | -4.3% | `fast_decay_cut` |
| 11 | Book 3 | `2023-10-04 00:00` | `2023-10-07 00:00` | 72.0h | `$0.2514` | `$0.2564` | **+1.95%** | **+1.94%** | +3.0% | -1.8% | `time_expiry` |
| 12 | Book 2 | `2023-10-16 05:00` | `2023-10-18 05:00` | 48.0h | `$0.2543` | `$0.2530` | **-0.62%** | **-0.62%** | +1.0% | -3.4% | `fast_decay_cut` |
| 13 | Book 3 | `2023-11-09 16:00` | `2023-11-11 13:00` | 45.0h | `$0.3576` | `$0.3887` | **+8.70%** | **+8.34%** | +8.7% | -11.1% | `target_reclaim` |
| 14 | Book 3 | `2023-12-06 11:00` | `2023-12-06 19:00` | 8.0h | `$0.3633` | `$0.3831` | **+5.45%** | **+5.30%** | +5.6% | -0.9% | `target_reclaim` |
| 15 | Book 3 | `2024-01-03 12:00` | `2024-01-03 14:00` | 2.0h | `$0.4526` | `$0.4154` | **-8.23%** | **-8.59%** | +2.2% | -21.6% | `stop_loss` |
| 16 | Book 3 | `2024-03-14 13:00` | `2024-03-15 08:00` | 19.0h | `$0.6352` | `$0.5829` | **-8.23%** | **-8.59%** | +4.7% | -8.1% | `stop_loss` |
| 17 | Book 3 | `2024-05-23 20:00` | `2024-05-24 14:00` | 18.0h | `$0.3892` | `$0.4254` | **+9.29%** | **+8.88%** | +9.5% | -2.0% | `target_reclaim` |
| 18 | Book 4 | `2024-05-28 15:00` | `2024-05-30 19:00` | 52.0h | `$0.4399` | `$0.5278` | **+11.27%** | **+10.54%** | +20.8% | -0.7% | `target_reclaim` |
| 19 | Book 3 | `2024-09-30 16:00` | `2024-10-01 17:00` | 25.0h | `$0.2813` | `$0.2582` | **-8.23%** | **-8.59%** | +3.1% | -12.3% | `stop_loss` |
| 20 | Book 4 | `2024-11-18 14:00` | `2024-11-24 02:00` | 132.0h | `$0.3262` | `$0.3914` | **+31.57%** | **+26.65%** | +20.2% | -4.9% | `target_reclaim` |
| 21 | Book 3 | `2024-12-09 11:00` | `2024-12-09 20:00` | 9.0h | `$0.5364` | `$0.4922` | **-8.23%** | **-8.59%** | +4.6% | -13.3% | `stop_loss` |
| 22 | Book 3 | `2025-04-30 13:00` | `2025-04-30 20:00` | 7.0h | `$0.1986` | `$0.2069` | **+4.17%** | **+4.08%** | +4.5% | -0.6% | `target_reclaim` |
| 23 | Book 3 | `2025-05-14 17:00` | `2025-05-17 11:00` | 66.0h | `$0.2340` | `$0.2147` | **-8.23%** | **-8.59%** | +2.5% | -8.1% | `stop_loss` |
| 24 | Book 4 | `2025-07-11 00:00` | `2025-07-11 12:00` | 12.0h | `$0.2375` | `$0.2849` | **+32.29%** | **+28.59%** | +28.7% | -0.5% | `target_reclaim` |
| 25 | Book 2 | `2026-05-06 03:00` | `2026-05-07 15:00` | 36.0h | `$0.0993` | `$0.0964` | **-3.46%** | **-3.52%** | +-0.0% | -3.2% | `stall_bailout` |
| 26 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0836` | `$0.0882` | **+5.50%** | **+5.36%** | +16.7% | -9.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `11` | `100.0%` | **`+162.4%`** |
| `stop_loss` | `6` | `0.0%` | **`-51.5%`** |
| `fast_decay_cut` | `3` | `0.0%` | **`-2.1%`** |
| `time_expiry` | `2` | `50.0%` | **`-2.9%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.5%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+34.2%`** |
| `time_cap` | `1` | `100.0%` | **`+14.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `1INCH`

* **Total Candidate Breakouts Filtered (Vetoed):** `1780`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `1000` (56.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `362`
* **Saved Capital Losses Avoided:** `+12,592.6%`
* **Missed Upside Forgone:** `-14,400.8%`
* **Net Veto Alpha:** `+-1,808.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `1034` | `58.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `541` | `30.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `111` | `6.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `51` | `2.9%` |
| `Core 1: Macro Bear Veto` | `43` | `2.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*