# Kronos V12: Institutional Symbol Tear Sheet — `BAND`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `25` (`25` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `25` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.625`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+162.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`5.07x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+6.49%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-14.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`80.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.2% / -6.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-21 07:00` | `2021-09-04 07:00` | 336.0h | `$9.0561` | `$10.8673` | **+20.62%** | **+19.03%** | +20.2% | -10.4% | `target_reclaim` |
| 2 | Book 3 | `2022-03-27 13:00` | `2022-03-27 16:00` | 3.0h | `$4.1209` | `$4.2926` | **+4.17%** | **+4.08%** | +4.4% | -0.1% | `target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2022-06-09 14:00` | `2022-06-13 14:00` | Live | `$1.7026` | `$1.8473` | **+8.50%** | **+8.16%** | +12.0% | -36.4% | `shelf_target_reclaim` |
| 4 | Book 3 | `2023-01-22 15:00` | `2023-01-22 16:00` | 1.0h | `$1.9837` | `$2.0796` | **+4.84%** | **+4.72%** | +5.0% | -1.9% | `target_reclaim` |
| 5 | Book 3 | `2023-01-31 09:00` | `2023-02-02 03:00` | 42.0h | `$2.1396` | `$2.3388` | **+9.31%** | **+8.90%** | +9.8% | -7.3% | `target_reclaim` |
| 6 | Book 5 (Shelf Absorption Squeeze) | `2023-04-10 08:00` | `2023-04-14 08:00` | Live | `$1.7668` | `$1.9169` | **+8.50%** | **+8.16%** | +9.0% | -15.7% | `shelf_target_reclaim` |
| 7 | Book 5 (Shelf Absorption Squeeze) | `2023-07-20 09:00` | `2023-07-24 09:00` | Live | `$1.2561` | `$1.1531` | **-8.20%** | **-8.56%** | +-1.2% | -16.4% | `shelf_stop_loss` |
| 8 | Book 4 | `2023-10-15 15:00` | `2023-10-26 06:00` | 255.0h | `$1.3815` | `$1.6578` | **+3.59%** | **+3.47%** | +20.0% | -9.5% | `target_reclaim` |
| 9 | Book 3 | `2023-12-14 20:00` | `2023-12-15 14:00` | 18.0h | `$1.7646` | `$1.6193` | **-8.23%** | **-8.59%** | +1.5% | -8.1% | `stop_loss` |
| 10 | Book 3 | `2024-03-12 17:00` | `2024-03-15 17:00` | 72.0h | `$2.3999` | `$2.3813` | **-0.77%** | **-0.78%** | +13.2% | -7.0% | `time_expiry` |
| 11 | Book 3 | `2024-05-23 20:00` | `2024-05-23 21:00` | 1.0h | `$1.5210` | `$1.6120` | **+5.99%** | **+5.81%** | +6.2% | -1.0% | `target_reclaim` |
| 12 | Book 3 | `2024-11-10 20:00` | `2024-11-11 00:00` | 4.0h | `$1.2233` | `$1.2743` | **+4.17%** | **+4.08%** | +4.6% | -3.1% | `target_reclaim` |
| 13 | Book 3 | `2024-11-11 05:00` | `2024-11-11 10:00` | 5.0h | `$1.2240` | `$1.3094` | **+6.98%** | **+6.75%** | +9.2% | -0.1% | `target_reclaim` |
| 14 | Book 3 | `2024-11-13 06:00` | `2024-11-16 06:00` | 72.0h | `$1.1668` | `$1.2667` | **+8.56%** | **+8.22%** | +9.7% | -0.9% | `time_expiry` |
| 15 | Book 4 | `2024-11-16 07:00` | `2024-11-24 03:00` | 188.0h | `$1.2807` | `$1.5369` | **+48.49%** | **+40.73%** | +20.0% | -6.5% | `target_reclaim` |
| 16 | Book 3 | `2024-12-02 08:00` | `2024-12-02 20:00` | 12.0h | `$1.7606` | `$1.9137` | **+8.70%** | **+8.34%** | +11.3% | -0.7% | `target_reclaim` |
| 17 | Book 3 | `2025-01-27 00:00` | `2025-01-27 07:00` | 7.0h | `$1.2564` | `$1.1530` | **-8.23%** | **-8.59%** | +1.1% | -10.9% | `stop_loss` |
| 18 | Book 2 | `2025-04-19 15:00` | `2025-04-26 15:00` | 168.0h | `$0.7022` | `$0.8554` | **+26.31%** | **+23.80%** | +24.7% | -1.1% | `time_cap` |
| 19 | Book 3 | `2025-05-14 12:00` | `2025-05-15 14:00` | 26.0h | `$0.8755` | `$0.8034` | **-8.23%** | **-8.59%** | +1.9% | -8.7% | `stop_loss` |
| 20 | Book 3 | `2025-07-14 20:00` | `2025-07-15 23:00` | 27.0h | `$0.6783` | `$0.7066` | **+4.17%** | **+4.08%** | +4.7% | -3.4% | `target_reclaim` |
| 21 | Book 3 | `2025-07-22 04:00` | `2025-07-22 13:00` | 9.0h | `$0.7541` | `$0.7855` | **+4.17%** | **+4.08%** | +4.3% | -1.6% | `target_reclaim` |
| 22 | Book 4 | `2025-08-20 20:00` | `2025-08-22 15:00` | 43.0h | `$0.8774` | `$1.0529` | **+13.76%** | **+12.82%** | +23.0% | -8.2% | `target_reclaim` |
| 23 | Book 3 | `2026-08-30 23:00` | `2026-09-02 23:00` | 72.0h | `$0.1710` | `$0.1794` | **+4.89%** | **+4.78%** | +10.6% | -1.1% | `time_expiry` |
| 24 | Book 4 | `2026-09-21 23:00` | `2026-10-06 07:00` | 344.0h | `$0.2160` | `$0.2592` | **+14.10%** | **+13.33%** | +24.9% | -3.9% | `target_reclaim` |
| 25 | Book 3 | `2026-10-07 02:00` | `2026-10-10 02:00` | 72.0h | `$0.2304` | `$0.2400` | **+4.17%** | **+4.08%** | +4.5% | -7.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `15` | `100.0%` | **`+144.3%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_expiry` | `3` | `66.7%` | **`+12.2%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_cap` | `1` | `100.0%` | **`+23.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `BAND`

* **Total Candidate Breakouts Filtered (Vetoed):** `1167`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `767` (65.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `145`
* **Saved Capital Losses Avoided:** `+11,599.4%`
* **Missed Upside Forgone:** `-6,292.8%`
* **Net Veto Alpha:** `+5,306.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `462` | `39.6%` |
| `Core 1: Macro Bear Veto` | `273` | `23.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `173` | `14.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `150` | `12.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `109` | `9.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*