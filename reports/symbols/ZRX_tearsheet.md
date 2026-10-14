# Kronos V12: Institutional Symbol Tear Sheet — `ZRX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `21` (`21` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `21` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.069`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+102.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.80x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.90%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-14.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`98.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.1% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-11 09:00` | `2021-09-04 00:00` | 567.0h | `$0.9926` | `$1.1911` | **+22.94%** | **+20.99%** | +21.4% | -8.5% | `target_reclaim` |
| 2 | Book 2 | `2023-01-09 00:00` | `2023-01-11 04:00` | 52.0h | `$0.1711` | `$0.1707` | **-0.33%** | **-0.33%** | +2.6% | -3.1% | `fast_decay_cut` |
| 3 | Book 3 | `2023-01-24 22:00` | `2023-01-27 22:00` | 72.0h | `$0.2179` | `$0.2390` | **+9.70%** | **+9.25%** | +12.1% | -3.6% | `time_expiry` |
| 4 | Book 4 | `2023-02-17 20:00` | `2023-03-01 13:00` | 281.0h | `$0.2651` | `$0.3181` | **+11.58%** | **+11.05%** | +20.2% | -7.1% | `target_reclaim` |
| 5 | Book 3 | `2023-03-03 01:00` | `2023-03-03 03:00` | 2.0h | `$0.2667` | `$0.2448` | **-8.23%** | **-8.59%** | +1.9% | -9.4% | `stop_loss` |
| 6 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.2133` | `$0.2488` | **+18.43%** | **+17.05%** | +19.0% | -4.0% | `time_cap` |
| 7 | Book 3 | `2023-04-06 00:00` | `2023-04-07 07:00` | 31.0h | `$0.3161` | `$0.2901` | **-8.23%** | **-8.59%** | +4.2% | -8.4% | `stop_loss` |
| 8 | Book 3 | `2023-07-06 00:00` | `2023-07-09 00:00` | 72.0h | `$0.2150` | `$0.2028` | **-5.70%** | **-5.86%** | +4.3% | -6.9% | `time_expiry` |
| 9 | Book 5 (Shelf Absorption Squeeze) | `2023-10-08 14:00` | `2023-10-12 14:00` | Live | `$0.1928` | `$0.2092` | **+8.50%** | **+8.16%** | +28.3% | -12.1% | `shelf_target_reclaim` |
| 10 | Book 4 | `2023-10-14 07:00` | `2023-10-16 11:00` | 52.0h | `$0.2082` | `$0.2499` | **+7.54%** | **+7.31%** | +20.3% | -1.2% | `target_reclaim` |
| 11 | Book 3 | `2023-10-18 19:00` | `2023-10-19 11:00` | 16.0h | `$0.2246` | `$0.2061` | **-8.23%** | **-8.59%** | +2.5% | -8.7% | `stop_loss` |
| 12 | Book 5 (Shelf Absorption Squeeze) | `2024-01-26 08:00` | `2024-01-30 08:00` | Live | `$0.3068` | `$0.3329` | **+8.50%** | **+8.16%** | +21.9% | -8.8% | `shelf_target_reclaim` |
| 13 | Book 3 | `2024-02-21 10:00` | `2024-02-22 07:00` | 21.0h | `$0.3384` | `$0.3576` | **+5.68%** | **+5.52%** | +6.0% | -1.4% | `target_reclaim` |
| 14 | Book 3 | `2024-02-28 17:00` | `2024-02-29 06:00` | 13.0h | `$0.3664` | `$0.3892` | **+6.22%** | **+6.03%** | +8.5% | -8.6% | `target_reclaim` |
| 15 | Book 3 | `2024-03-05 19:00` | `2024-03-06 11:00` | 16.0h | `$0.3861` | `$0.4472` | **+15.82%** | **+14.69%** | +18.0% | -16.1% | `target_reclaim` |
| 16 | Book 3 | `2024-07-28 15:00` | `2024-07-31 15:00` | 72.0h | `$0.3704` | `$0.3708` | **+0.10%** | **+0.10%** | +5.5% | -3.3% | `time_expiry` |
| 17 | Book 2 | `2024-09-13 16:00` | `2024-09-15 17:00` | 49.0h | `$0.2924` | `$0.2917` | **-0.30%** | **-0.30%** | +3.5% | -1.2% | `fast_decay_cut` |
| 18 | Book 3 | `2024-11-12 13:00` | `2024-11-12 22:00` | 9.0h | `$0.3537` | `$0.3825` | **+8.15%** | **+7.84%** | +8.7% | -0.6% | `target_reclaim` |
| 19 | Book 4 | `2025-09-03 15:00` | `2025-09-10 15:00` | 168.0h | `$0.2809` | `$0.2787` | **-1.25%** | **-1.25%** | +3.3% | -7.6% | `stagnation_cut` |
| 20 | Book 2 | `2026-05-06 03:00` | `2026-05-13 03:00` | 168.0h | `$0.1142` | `$0.1279` | **+13.32%** | **+12.58%** | +12.8% | -2.9% | `time_cap` |
| 21 | Book 3 | `2026-09-10 12:00` | `2026-09-12 06:00` | 42.0h | `$0.0989` | `$0.1067` | **+7.89%** | **+7.59%** | +8.2% | -1.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+81.0%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_expiry` | `3` | `66.7%` | **`+3.5%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-0.6%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `time_cap` | `2` | `100.0%` | **`+29.6%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-1.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZRX`

* **Total Candidate Breakouts Filtered (Vetoed):** `1079`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `742` (68.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `111`
* **Saved Capital Losses Avoided:** `+9,401.1%`
* **Missed Upside Forgone:** `-3,968.5%`
* **Net Veto Alpha:** `+5,432.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `402` | `37.3%` |
| `Core 1: Macro Bear Veto` | `260` | `24.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `190` | `17.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `167` | `15.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `60` | `5.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*