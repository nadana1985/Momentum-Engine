# Kronos V12: Institutional Symbol Tear Sheet — `SNX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `29` (`29` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `29` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`69.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.961`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+128.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`3.62x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.44%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`53.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.9% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-19 18:00` | `2021-09-07 14:00` | 452.0h | `$12.3565` | `$10.7299` | **-15.92%** | **-17.08%** | +17.8% | -21.1% | `structural_stop` |
| 2 | Book 3 | `2022-03-31 16:00` | `2022-03-31 17:00` | 1.0h | `$6.5817` | `$7.1540` | **+8.70%** | **+8.34%** | +10.3% | -0.6% | `target_reclaim` |
| 3 | Book 2 | `2022-10-25 17:00` | `2022-10-28 07:00` | 62.0h | `$2.3388` | `$2.3212` | **-0.89%** | **-0.90%** | +7.7% | -2.5% | `fast_decay_cut` |
| 4 | Book 3 | `2023-02-05 12:00` | `2023-02-06 15:00` | 27.0h | `$2.6199` | `$2.7910` | **+6.53%** | **+6.32%** | +10.0% | -6.2% | `target_reclaim` |
| 5 | Book 3 | `2023-02-08 16:00` | `2023-02-09 19:00` | 27.0h | `$2.6110` | `$2.3961` | **-8.23%** | **-8.59%** | +5.2% | -8.2% | `stop_loss` |
| 6 | Book 5 (Shelf Absorption Squeeze) | `2023-02-28 14:00` | `2023-03-04 14:00` | Live | `$2.6919` | `$2.9207` | **+8.50%** | **+8.16%** | +15.9% | -32.2% | `shelf_target_reclaim` |
| 7 | Book 3 | `2023-03-03 01:00` | `2023-03-04 02:00` | 25.0h | `$2.6998` | `$2.9930` | **+10.86%** | **+10.31%** | +10.9% | -5.5% | `target_reclaim` |
| 8 | Book 2 | `2023-10-16 05:00` | `2023-10-18 20:00` | 63.0h | `$1.9238` | `$1.9142` | **-0.55%** | **-0.55%** | +2.5% | -2.9% | `fast_decay_cut` |
| 9 | Book 2 | `2023-10-23 22:00` | `2023-10-30 22:00` | 168.0h | `$2.2416` | `$2.3112` | **+3.11%** | **+3.06%** | +10.2% | -3.5% | `time_cap` |
| 10 | Book 3 | `2023-11-09 16:00` | `2023-11-10 02:00` | 10.0h | `$2.3402` | `$2.6940` | **+15.12%** | **+14.08%** | +17.2% | -3.9% | `target_reclaim` |
| 11 | Book 3 | `2023-11-14 18:00` | `2023-11-15 15:00` | 21.0h | `$2.4987` | `$2.8170` | **+12.74%** | **+11.99%** | +15.9% | -2.9% | `target_reclaim` |
| 12 | Book 3 | `2023-11-17 15:00` | `2023-11-17 18:00` | 3.0h | `$2.7885` | `$3.0310` | **+8.70%** | **+8.34%** | +8.8% | -0.6% | `target_reclaim` |
| 13 | Book 3 | `2023-11-21 17:00` | `2023-11-21 20:00` | 3.0h | `$3.1170` | `$3.3880` | **+8.70%** | **+8.34%** | +13.6% | -0.2% | `target_reclaim` |
| 14 | Book 3 | `2023-11-22 12:00` | `2023-11-25 06:00` | 66.0h | `$3.4767` | `$3.7790` | **+8.70%** | **+8.34%** | +8.8% | -3.9% | `target_reclaim` |
| 15 | Book 3 | `2024-02-20 15:00` | `2024-02-23 15:00` | 72.0h | `$3.5324` | `$3.6269` | **+2.67%** | **+2.64%** | +6.2% | -4.0% | `time_expiry` |
| 16 | Book 3 | `2024-02-24 15:00` | `2024-02-24 19:00` | 4.0h | `$3.8208` | `$3.9800` | **+4.17%** | **+4.08%** | +5.2% | -0.4% | `target_reclaim` |
| 17 | Book 3 | `2024-05-22 04:00` | `2024-05-23 12:00` | 32.0h | `$2.8570` | `$2.9760` | **+4.17%** | **+4.08%** | +4.4% | -1.9% | `target_reclaim` |
| 18 | Book 3 | `2024-05-29 15:00` | `2024-06-01 15:00` | 72.0h | `$2.9162` | `$2.9356` | **+0.67%** | **+0.66%** | +2.7% | -5.9% | `time_expiry` |
| 19 | Book 3 | `2024-08-24 21:00` | `2024-08-26 18:00` | 45.0h | `$1.6445` | `$1.5091` | **-8.23%** | **-8.59%** | +2.1% | -8.3% | `stop_loss` |
| 20 | Book 3 | `2024-09-28 09:00` | `2024-10-01 09:00` | 72.0h | `$1.6666` | `$1.5990` | **-4.05%** | **-4.14%** | +2.5% | -6.2% | `time_expiry` |
| 21 | Book 4 | `2024-11-22 23:00` | `2024-11-25 09:00` | 58.0h | `$1.9059` | `$2.2870` | **+39.40%** | **+33.10%** | +24.5% | -1.3% | `target_reclaim` |
| 22 | Book 3 | `2024-11-28 11:00` | `2024-11-30 06:00` | 43.0h | `$2.2623` | `$2.4590` | **+8.70%** | **+8.34%** | +9.3% | -0.4% | `target_reclaim` |
| 23 | Book 3 | `2024-12-09 04:00` | `2024-12-09 20:00` | 16.0h | `$3.2504` | `$2.9829` | **-8.23%** | **-8.59%** | +2.0% | -14.4% | `stop_loss` |
| 24 | Book 3 | `2025-05-15 01:00` | `2025-05-15 23:00` | 22.0h | `$0.8783` | `$0.8060` | **-8.23%** | **-8.59%** | +2.2% | -8.9% | `stop_loss` |
| 25 | Book 3 | `2025-08-14 12:00` | `2025-08-16 00:00` | 36.0h | `$0.6623` | `$0.7280` | **+9.92%** | **+9.46%** | +12.3% | -3.5% | `target_reclaim` |
| 26 | Book 4 | `2025-09-24 21:00` | `2025-09-26 15:00` | 42.0h | `$0.8483` | `$1.0179` | **+32.31%** | **+28.53%** | +34.5% | -8.8% | `target_reclaim` |
| 27 | Book 3 | `2025-10-07 16:00` | `2025-10-10 00:00` | 56.0h | `$1.1300` | `$1.2570` | **+11.24%** | **+10.65%** | +15.0% | -6.4% | `target_reclaim` |
| 28 | Book 3 | `2025-10-10 15:00` | `2025-10-10 20:00` | 5.0h | `$1.3119` | `$1.2039` | **-8.23%** | **-8.59%** | +4.4% | -9.2% | `stop_loss` |
| 29 | Book 3 | `2026-08-23 04:00` | `2026-08-23 11:00` | 7.0h | `$0.2160` | `$0.2281` | **+5.60%** | **+5.45%** | +6.3% | -0.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `16` | `100.0%` | **`+179.8%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `time_expiry` | `3` | `66.7%` | **`-0.8%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-1.4%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-17.1%`** |
| `time_cap` | `1` | `100.0%` | **`+3.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `SNX`

* **Total Candidate Breakouts Filtered (Vetoed):** `1478`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `922` (62.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `279`
* **Saved Capital Losses Avoided:** `+16,319.8%`
* **Missed Upside Forgone:** `-9,229.8%`
* **Net Veto Alpha:** `+7,090.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `632` | `42.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `495` | `33.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `144` | `9.7%` |
| `Core 1: Macro Bear Veto` | `140` | `9.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `67` | `4.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*