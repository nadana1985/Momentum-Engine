# Kronos V12: Institutional Symbol Tear Sheet — `STEEM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `14` (`14` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `14` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`64.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.867`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+39.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.48x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.80%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-15.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`62.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.1% / -6.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-12-10 09:00` | `2023-12-11 02:00` | 17.0h | `$0.2630` | `$0.2414` | **-8.23%** | **-8.59%** | +5.9% | -14.1% | `stop_loss` |
| 2 | Book 3 | `2024-01-03 11:00` | `2024-01-03 12:00` | 1.0h | `$0.2577` | `$0.2365` | **-8.23%** | **-8.59%** | +3.5% | -23.4% | `stop_loss` |
| 3 | Book 4 | `2024-02-21 05:00` | `2024-02-28 05:00` | 168.0h | `$0.2531` | `$0.2558` | **+1.41%** | **+1.41%** | +1.8% | -6.6% | `stagnation_cut` |
| 4 | Book 3 | `2024-02-28 17:00` | `2024-02-29 00:00` | 7.0h | `$0.2405` | `$0.2594` | **+7.87%** | **+7.57%** | +11.7% | -1.8% | `target_reclaim` |
| 5 | Book 3 | `2024-03-05 19:00` | `2024-03-06 02:00` | 7.0h | `$0.2561` | `$0.3011` | **+17.57%** | **+16.19%** | +21.0% | -2.4% | `target_reclaim` |
| 6 | Book 3 | `2024-03-10 14:00` | `2024-03-11 21:00` | 31.0h | `$0.3272` | `$0.3556` | **+8.70%** | **+8.34%** | +9.4% | -3.9% | `target_reclaim` |
| 7 | Book 3 | `2024-03-15 03:00` | `2024-03-16 18:00` | 39.0h | `$0.3297` | `$0.3026` | **-8.23%** | **-8.59%** | +3.6% | -9.8% | `stop_loss` |
| 8 | Book 3 | `2024-05-31 05:00` | `2024-06-03 05:00` | 72.0h | `$0.2776` | `$0.2673` | **-3.71%** | **-3.78%** | +1.8% | -4.6% | `time_expiry` |
| 9 | Book 3 | `2024-11-10 21:00` | `2024-11-10 22:00` | 1.0h | `$0.1814` | `$0.1896` | **+4.51%** | **+4.41%** | +4.8% | -1.2% | `target_reclaim` |
| 10 | Book 3 | `2024-11-14 15:00` | `2024-11-16 00:00` | 33.0h | `$0.1814` | `$0.1955` | **+7.77%** | **+7.49%** | +9.0% | -0.9% | `target_reclaim` |
| 11 | Book 4 | `2024-11-16 01:00` | `2024-11-24 00:00` | 191.0h | `$0.1998` | `$0.2398` | **+35.29%** | **+30.94%** | +20.3% | -1.0% | `target_reclaim` |
| 12 | Book 3 | `2024-11-28 08:00` | `2024-11-29 19:00` | 35.0h | `$0.2545` | `$0.2651` | **+4.17%** | **+4.08%** | +4.2% | -1.5% | `target_reclaim` |
| 13 | Book 4 | `2025-07-20 15:00` | `2025-07-29 20:00` | 221.0h | `$0.1567` | `$0.1376` | **-14.74%** | **-15.72%** | +9.6% | -12.5% | `structural_stop` |
| 14 | Book 3 | `2026-09-24 03:00` | `2026-09-26 00:00` | 45.0h | `$0.0644` | `$0.0671` | **+4.17%** | **+4.08%** | +6.6% | -5.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+83.1%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `stagnation_cut` | `1` | `100.0%` | **`+1.4%`** |
| `structural_stop` | `1` | `0.0%` | **`-15.7%`** |
| `time_expiry` | `1` | `0.0%` | **`-3.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `STEEM`

* **Total Candidate Breakouts Filtered (Vetoed):** `571`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `250` (43.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `35`
* **Saved Capital Losses Avoided:** `+2,821.3%`
* **Missed Upside Forgone:** `-909.6%`
* **Net Veto Alpha:** `+1,911.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `434` | `76.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `107` | `18.7%` |
| `Core 1: Macro Bear Veto` | `17` | `3.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `12` | `2.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*