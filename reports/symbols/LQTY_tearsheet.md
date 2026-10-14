# Kronos V12: Institutional Symbol Tear Sheet — `LQTY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `23` (`23` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `23` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.120`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+66.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.94x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+2.88%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.9% / -9.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-09-20 03:00` | `2023-09-22 16:00` | 61.0h | `$0.8388` | `$0.8287` | **-1.41%** | **-1.42%** | +5.5% | -2.1% | `fast_decay_cut` |
| 2 | Book 3 | `2023-10-01 07:00` | `2023-10-02 08:00` | 25.0h | `$1.0533` | `$1.0972` | **+4.17%** | **+4.08%** | +5.5% | -4.6% | `target_reclaim` |
| 3 | Book 3 | `2023-10-02 18:00` | `2023-10-04 00:00` | 30.0h | `$1.0884` | `$0.9988` | **-8.23%** | **-8.59%** | +3.3% | -13.6% | `stop_loss` |
| 4 | Book 4 | `2023-10-05 08:00` | `2023-10-09 08:00` | 96.0h | `$1.1685` | `$1.4021` | **+22.63%** | **+20.73%** | +27.9% | -6.2% | `target_reclaim` |
| 5 | Book 3 | `2023-10-26 10:00` | `2023-10-26 11:00` | 1.0h | `$2.0456` | `$1.8773` | **-8.23%** | **-8.59%** | +11.9% | -12.3% | `stop_loss` |
| 6 | Book 3 | `2023-12-04 11:00` | `2023-12-07 11:00` | 72.0h | `$1.4864` | `$1.4863` | **-0.01%** | **-0.01%** | +10.2% | -3.8% | `time_expiry` |
| 7 | Book 3 | `2024-01-03 12:00` | `2024-01-03 13:00` | 1.0h | `$1.4707` | `$1.3496` | **-8.23%** | **-8.59%** | +6.8% | -32.9% | `stop_loss` |
| 8 | Book 3 | `2024-03-05 19:00` | `2024-03-08 00:00` | 53.0h | `$1.5519` | `$1.8127` | **+16.81%** | **+15.53%** | +17.8% | -11.0% | `target_reclaim` |
| 9 | Book 3 | `2024-03-10 14:00` | `2024-03-13 14:00` | 72.0h | `$1.7487` | `$1.9008` | **+8.70%** | **+8.34%** | +10.1% | -5.6% | `target_reclaim` |
| 10 | Book 3 | `2024-04-01 16:00` | `2024-04-02 02:00` | 10.0h | `$1.7686` | `$1.6231` | **-8.23%** | **-8.59%** | +5.2% | -9.3% | `stop_loss` |
| 11 | Book 3 | `2024-05-24 08:00` | `2024-05-25 04:00` | 20.0h | `$1.0882` | `$1.1526` | **+5.92%** | **+5.75%** | +7.4% | -0.7% | `target_reclaim` |
| 12 | Book 3 | `2024-05-30 07:00` | `2024-06-02 04:00` | 69.0h | `$1.0882` | `$1.1787` | **+8.32%** | **+7.99%** | +13.5% | -0.2% | `target_reclaim` |
| 13 | Book 3 | `2024-06-07 18:00` | `2024-06-10 18:00` | 72.0h | `$1.1260` | `$1.0589` | **-5.96%** | **-6.14%** | +6.9% | -7.0% | `time_expiry` |
| 14 | Book 5 (Shelf Absorption Squeeze) | `2024-08-23 18:00` | `2024-08-27 18:00` | Live | `$0.8120` | `$0.8810` | **+8.50%** | **+8.16%** | +22.5% | -26.3% | `shelf_target_reclaim` |
| 15 | Book 3 | `2024-11-10 21:00` | `2024-11-12 00:00` | 27.0h | `$1.0312` | `$1.1299` | **+9.57%** | **+9.14%** | +12.1% | -2.8% | `target_reclaim` |
| 16 | Book 3 | `2024-11-26 11:00` | `2024-11-27 04:00` | 17.0h | `$1.2623` | `$1.3903` | **+10.14%** | **+9.66%** | +10.5% | -3.2% | `target_reclaim` |
| 17 | Book 3 | `2024-12-03 14:00` | `2024-12-03 20:00` | 6.0h | `$1.5933` | `$1.7318` | **+8.70%** | **+8.34%** | +10.0% | -1.0% | `target_reclaim` |
| 18 | Book 5 (Shelf Absorption Squeeze) | `2024-12-07 05:00` | `2024-12-11 05:00` | Live | `$2.1797` | `$2.3649` | **+8.50%** | **+8.16%** | +21.1% | -37.5% | `shelf_target_reclaim` |
| 19 | Book 3 | `2024-12-09 21:00` | `2024-12-09 22:00` | 1.0h | `$2.0496` | `$2.2278` | **+8.70%** | **+8.34%** | +15.7% | -3.0% | `target_reclaim` |
| 20 | Book 5 (Shelf Absorption Squeeze) | `2025-01-14 03:00` | `2025-01-18 03:00` | Live | `$1.5508` | `$1.6827` | **+8.50%** | **+8.16%** | +28.8% | -19.6% | `shelf_target_reclaim` |
| 21 | Book 3 | `2025-05-15 10:00` | `2025-05-17 01:00` | 39.0h | `$0.9773` | `$0.8968` | **-8.23%** | **-8.59%** | +5.5% | -9.9% | `stop_loss` |
| 22 | Book 3 | `2025-06-12 20:00` | `2025-06-13 00:00` | 4.0h | `$1.0211` | `$0.9371` | **-8.23%** | **-8.59%** | +3.2% | -9.3% | `stop_loss` |
| 23 | Book 3 | `2025-07-12 12:00` | `2025-07-15 12:00` | 72.0h | `$1.1192` | `$1.1521` | **+2.94%** | **+2.89%** | +11.5% | -4.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `10` | `100.0%` | **`+97.9%`** |
| `stop_loss` | `6` | `0.0%` | **`-51.5%`** |
| `shelf_target_reclaim` | `3` | `100.0%` | **`+24.5%`** |
| `time_expiry` | `3` | `33.3%` | **`-3.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `LQTY`

* **Total Candidate Breakouts Filtered (Vetoed):** `544`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `343` (63.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `125`
* **Saved Capital Losses Avoided:** `+5,294.6%`
* **Missed Upside Forgone:** `-3,674.1%`
* **Net Veto Alpha:** `+1,620.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `200` | `36.8%` |
| `Core 1: Macro Bear Veto` | `184` | `33.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `132` | `24.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `26` | `4.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.2%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*