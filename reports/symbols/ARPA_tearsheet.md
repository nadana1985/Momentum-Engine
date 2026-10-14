# Kronos V12: Institutional Symbol Tear Sheet — `ARPA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `16` (`16` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `16` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`43.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.130`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+9.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.10x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.60%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-46.2%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`35.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.3% / -9.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2022-03-31 14:00` | `2022-04-01 02:00` | 12.0h | `$0.0881` | `$0.0809` | **-8.23%** | **-8.59%** | +1.7% | -9.4% | `stop_loss` |
| 2 | Book 3 | `2023-01-25 01:00` | `2023-01-25 19:00` | 18.0h | `$0.0334` | `$0.0348` | **+4.17%** | **+4.08%** | +4.6% | -1.2% | `target_reclaim` |
| 3 | Book 3 | `2023-01-30 19:00` | `2023-02-01 22:00` | 51.0h | `$0.0350` | `$0.0371` | **+5.95%** | **+5.78%** | +6.6% | -3.4% | `target_reclaim` |
| 4 | Book 2 | `2023-03-12 23:00` | `2023-03-17 02:00` | 99.0h | `$0.0344` | `$0.0462` | **+36.06%** | **+30.99%** | +42.6% | -4.4% | `climax_top_harvest` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2023-03-15 19:00` | `2023-03-19 19:00` | Live | `$0.0377` | `$0.0409` | **+8.50%** | **+8.16%** | +68.3% | -9.3% | `shelf_target_reclaim` |
| 6 | Book 3 | `2023-04-19 08:00` | `2023-04-21 19:00` | 59.0h | `$0.0419` | `$0.0385` | **-8.23%** | **-8.59%** | +8.9% | -9.8% | `stop_loss` |
| 7 | Book 3 | `2024-01-07 22:00` | `2024-01-08 02:00` | 4.0h | `$0.0613` | `$0.0562` | **-8.23%** | **-8.59%** | +1.9% | -9.0% | `stop_loss` |
| 8 | Book 3 | `2024-03-05 16:00` | `2024-03-05 19:00` | 3.0h | `$0.0695` | `$0.0638` | **-8.23%** | **-8.59%** | +6.0% | -17.1% | `stop_loss` |
| 9 | Book 3 | `2024-07-30 19:00` | `2024-08-01 16:00` | 45.0h | `$0.0420` | `$0.0385` | **-8.23%** | **-8.59%** | +2.9% | -9.8% | `stop_loss` |
| 10 | Book 5 (Shelf Absorption Squeeze) | `2024-10-20 20:00` | `2024-10-24 20:00` | Live | `$0.0521` | `$0.0478` | **-8.20%** | **-8.56%** | +-5.9% | -31.8% | `shelf_stop_loss` |
| 11 | Book 3 | `2024-11-26 11:00` | `2024-11-27 16:00` | 29.0h | `$0.0531` | `$0.0593` | **+11.70%** | **+11.06%** | +12.4% | -1.9% | `target_reclaim` |
| 12 | Book 3 | `2024-12-03 14:00` | `2024-12-03 17:00` | 3.0h | `$0.0641` | `$0.0692` | **+8.09%** | **+7.78%** | +14.3% | -0.6% | `target_reclaim` |
| 13 | Book 3 | `2025-07-02 03:00` | `2025-07-05 03:00` | 72.0h | `$0.0214` | `$0.0203` | **-4.85%** | **-4.97%** | +7.8% | -7.2% | `time_expiry` |
| 14 | Book 5 (Shelf Absorption Squeeze) | `2026-07-03 08:00` | `2026-07-07 08:00` | Live | `$0.0103` | `$0.0094` | **-8.20%** | **-8.56%** | +-5.5% | -26.6% | `shelf_stop_loss` |
| 15 | Book 3 | `2026-09-12 19:00` | `2026-09-12 22:00` | 3.0h | `$0.0104` | `$0.0095` | **-8.23%** | **-8.59%** | +4.4% | -8.3% | `stop_loss` |
| 16 | Book 3 | `2026-10-07 10:00` | `2026-10-10 07:00` | 69.0h | `$0.0109` | `$0.0127` | **+16.56%** | **+15.32%** | +26.2% | -5.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `6` | `0.0%` | **`-51.5%`** |
| `target_reclaim` | `5` | `100.0%` | **`+44.0%`** |
| `shelf_stop_loss` | `2` | `0.0%` | **`-17.1%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+31.0%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_expiry` | `1` | `0.0%` | **`-5.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `ARPA`

* **Total Candidate Breakouts Filtered (Vetoed):** `264`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `193` (73.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+2,749.3%`
* **Missed Upside Forgone:** `-694.2%`
* **Net Veto Alpha:** `+2,055.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `112` | `42.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `88` | `33.3%` |
| `Core 1: Macro Bear Veto` | `54` | `20.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `2.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `3` | `1.1%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*