# Kronos V12: Institutional Symbol Tear Sheet — `ROSE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `23` (`23` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `23` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`65.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.984`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+63.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.89x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+2.76%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`49.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.3% / -5.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2022-04-06 19:00` | `2022-04-06 23:00` | 4.0h | `$0.2641` | `$0.2423` | **-8.23%** | **-8.59%** | +3.1% | -10.6% | `stop_loss` |
| 2 | Book 3 | `2023-01-28 20:00` | `2023-01-29 01:00` | 5.0h | `$0.0558` | `$0.0586` | **+4.98%** | **+4.86%** | +5.1% | -0.1% | `target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2023-02-08 07:00` | `2023-02-12 07:00` | Live | `$0.0682` | `$0.0740` | **+8.50%** | **+8.16%** | +15.9% | -15.0% | `shelf_target_reclaim` |
| 4 | Book 3 | `2023-02-13 10:00` | `2023-02-14 21:00` | 35.0h | `$0.0717` | `$0.0790` | **+10.06%** | **+9.59%** | +11.1% | -7.5% | `target_reclaim` |
| 5 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$0.0548` | `$0.0622` | **+15.09%** | **+14.15%** | +25.5% | -2.9% | `time_cap` |
| 6 | Book 3 | `2023-04-19 08:00` | `2023-04-21 12:00` | 52.0h | `$0.0712` | `$0.0654` | **-8.23%** | **-8.59%** | +7.9% | -8.6% | `stop_loss` |
| 7 | Book 3 | `2023-07-14 18:00` | `2023-07-17 18:00` | 72.0h | `$0.0519` | `$0.0496` | **-4.38%** | **-4.47%** | +1.5% | -5.3% | `time_expiry` |
| 8 | Book 2 | `2023-10-23 19:00` | `2023-10-30 19:00` | 168.0h | `$0.0439` | `$0.0521` | **+19.73%** | **+18.09%** | +23.6% | -1.2% | `time_cap` |
| 9 | Book 3 | `2023-11-07 00:00` | `2023-11-07 15:00` | 15.0h | `$0.0693` | `$0.0636` | **-8.23%** | **-8.59%** | +2.6% | -8.6% | `stop_loss` |
| 10 | Book 3 | `2024-02-16 14:00` | `2024-02-19 07:00` | 65.0h | `$0.1195` | `$0.1285` | **+7.59%** | **+7.32%** | +8.8% | -4.2% | `target_reclaim` |
| 11 | Book 3 | `2024-03-08 15:00` | `2024-03-09 08:00` | 17.0h | `$0.1607` | `$0.1759` | **+9.45%** | **+9.03%** | +10.4% | -3.0% | `target_reclaim` |
| 12 | Book 4 | `2024-06-03 13:00` | `2024-06-10 18:00` | 173.0h | `$0.1037` | `$0.1244` | **+18.81%** | **+17.48%** | +20.4% | -3.0% | `target_reclaim` |
| 13 | Book 3 | `2024-06-11 06:00` | `2024-06-11 15:00` | 9.0h | `$0.1181` | `$0.1084` | **-8.23%** | **-8.59%** | +2.9% | -8.4% | `stop_loss` |
| 14 | Book 3 | `2024-06-13 15:00` | `2024-06-14 07:00` | 16.0h | `$0.1233` | `$0.1296` | **+5.10%** | **+4.97%** | +9.3% | -5.5% | `target_reclaim` |
| 15 | Book 3 | `2024-09-25 06:00` | `2024-09-26 19:00` | 37.0h | `$0.0742` | `$0.0773` | **+4.17%** | **+4.08%** | +4.8% | -3.4% | `target_reclaim` |
| 16 | Book 3 | `2024-09-28 21:00` | `2024-09-29 17:00` | 20.0h | `$0.0750` | `$0.0781` | **+4.17%** | **+4.08%** | +5.2% | -1.5% | `target_reclaim` |
| 17 | Book 3 | `2024-10-01 13:00` | `2024-10-01 17:00` | 4.0h | `$0.0752` | `$0.0690` | **-8.23%** | **-8.59%** | +4.0% | -9.7% | `stop_loss` |
| 18 | Book 3 | `2024-11-13 03:00` | `2024-11-16 03:00` | 72.0h | `$0.0767` | `$0.0805` | **+4.90%** | **+4.78%** | +9.5% | -6.1% | `time_expiry` |
| 19 | Book 3 | `2025-04-28 01:00` | `2025-04-28 07:00` | 6.0h | `$0.0287` | `$0.0300` | **+4.46%** | **+4.37%** | +4.8% | -3.0% | `target_reclaim` |
| 20 | Book 3 | `2025-05-03 07:00` | `2025-05-04 08:00` | 25.0h | `$0.0305` | `$0.0280` | **-8.23%** | **-8.59%** | +0.9% | -8.4% | `stop_loss` |
| 21 | Book 3 | `2025-05-15 07:00` | `2025-05-17 00:00` | 41.0h | `$0.0370` | `$0.0339` | **-8.23%** | **-8.59%** | +2.3% | -8.8% | `stop_loss` |
| 22 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0056` | `$0.0066` | **+18.00%** | **+16.55%** | +28.3% | -3.8% | `climax_whale_euphoria_harvest` |
| 23 | Book 3 | `2026-10-01 14:00` | `2026-10-04 14:00` | 72.0h | `$0.0084` | `$0.0085` | **+0.65%** | **+0.65%** | +5.3% | -5.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `9` | `100.0%` | **`+65.8%`** |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `time_expiry` | `3` | `66.7%` | **`+1.0%`** |
| `time_cap` | `2` | `100.0%` | **`+32.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `ROSE`

* **Total Candidate Breakouts Filtered (Vetoed):** `864`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `577` (66.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `60`
* **Saved Capital Losses Avoided:** `+6,835.8%`
* **Missed Upside Forgone:** `-1,493.9%`
* **Net Veto Alpha:** `+5,341.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `391` | `45.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `339` | `39.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `64` | `7.4%` |
| `Core 1: Macro Bear Veto` | `63` | `7.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `7` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*