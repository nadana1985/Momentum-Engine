# Kronos V12: Institutional Symbol Tear Sheet — `NMR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `19` (`19` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `19` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`52.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.090`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+6.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.33%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-30.6%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`45.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.9% / -7.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-11-09 16:00` | `2023-11-10 22:00` | 30.0h | `$14.3843` | `$15.1900` | **+5.60%** | **+5.45%** | +6.1% | -9.6% | `target_reclaim` |
| 2 | Book 3 | `2024-03-05 16:00` | `2024-03-05 19:00` | 3.0h | `$34.1872` | `$31.3736` | **-8.23%** | **-8.59%** | +4.4% | -16.6% | `stop_loss` |
| 3 | Book 3 | `2024-03-10 14:00` | `2024-03-12 08:00` | 42.0h | `$46.3772` | `$42.5604` | **-8.23%** | **-8.59%** | +4.4% | -8.8% | `stop_loss` |
| 4 | Book 3 | `2024-05-23 13:00` | `2024-05-26 13:00` | 72.0h | `$27.9126` | `$28.2602` | **+1.25%** | **+1.24%** | +4.4% | -4.5% | `time_expiry` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2024-08-19 19:00` | `2024-08-23 19:00` | Live | `$15.1920` | `$16.4833` | **+8.50%** | **+8.16%** | +24.7% | -21.9% | `shelf_target_reclaim` |
| 6 | Book 3 | `2024-09-20 18:00` | `2024-09-23 03:00` | 57.0h | `$14.9510` | `$15.5740` | **+4.17%** | **+4.08%** | +5.2% | -2.2% | `target_reclaim` |
| 7 | Book 3 | `2024-09-30 15:00` | `2024-10-01 16:00` | 25.0h | `$16.0784` | `$14.7551` | **-8.23%** | **-8.59%** | +3.3% | -8.4% | `stop_loss` |
| 8 | Book 3 | `2024-11-10 21:00` | `2024-11-11 01:00` | 4.0h | `$15.9294` | `$16.7700` | **+5.28%** | **+5.14%** | +5.6% | -2.7% | `target_reclaim` |
| 9 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$15.9294` | `$14.6184` | **-8.23%** | **-8.59%** | +3.7% | -8.4% | `stop_loss` |
| 10 | Book 4 | `2024-11-19 18:00` | `2024-11-28 19:00` | 217.0h | `$17.1727` | `$20.6073` | **+30.47%** | **+26.51%** | +28.4% | -11.5% | `target_reclaim` |
| 11 | Book 3 | `2024-12-02 08:00` | `2024-12-02 21:00` | 13.0h | `$20.4672` | `$22.2470` | **+8.70%** | **+8.34%** | +10.9% | -1.1% | `target_reclaim` |
| 12 | Book 3 | `2025-05-23 15:00` | `2025-05-25 00:00` | 33.0h | `$9.2445` | `$8.4837` | **-8.23%** | **-8.59%** | +1.9% | -9.2% | `stop_loss` |
| 13 | Book 3 | `2025-05-30 23:00` | `2025-05-31 08:00` | 9.0h | `$9.3510` | `$8.5814` | **-8.23%** | **-8.59%** | +6.0% | -9.5% | `stop_loss` |
| 14 | Book 3 | `2025-07-18 15:00` | `2025-07-19 18:00` | 27.0h | `$8.4909` | `$8.9050` | **+4.88%** | **+4.76%** | +7.2% | -0.6% | `target_reclaim` |
| 15 | Book 3 | `2025-07-30 11:00` | `2025-08-02 11:00` | 72.0h | `$8.4909` | `$8.0319` | **-5.41%** | **-5.56%** | +7.8% | -6.0% | `time_expiry` |
| 16 | Book 3 | `2025-09-21 09:00` | `2025-09-22 02:00` | 17.0h | `$16.7411` | `$15.3633` | **-8.23%** | **-8.59%** | +2.2% | -8.9% | `stop_loss` |
| 17 | Book 4 | `2026-04-23 07:00` | `2026-04-30 07:00` | 168.0h | `$9.3790` | `$8.7868` | **-3.96%** | **-4.02%** | +4.5% | -6.9% | `stagnation_cut` |
| 18 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$8.5814` | `$8.9460` | **+4.25%** | **+4.16%** | +10.5% | -1.8% | `target_reclaim` |
| 19 | Book 3 | `2026-10-07 13:00` | `2026-10-08 00:00` | 11.0h | `$14.4003` | `$15.6170` | **+8.45%** | **+8.11%** | +8.6% | -0.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+66.6%`** |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `time_expiry` | `2` | `50.0%` | **`-4.3%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-4.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `NMR`

* **Total Candidate Breakouts Filtered (Vetoed):** `221`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `129` (58.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `37`
* **Saved Capital Losses Avoided:** `+1,690.5%`
* **Missed Upside Forgone:** `-1,344.5%`
* **Net Veto Alpha:** `+346.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `137` | `62.0%` |
| `Core 1: Macro Bear Veto` | `58` | `26.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `20` | `9.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `2.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*