# Kronos V12: Institutional Symbol Tear Sheet — `ANKR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `23` (`23` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `23` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`56.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.107`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+8.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.09x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.36%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-26.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`32.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.8% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2022-04-04 09:00` | `2022-04-06 00:00` | 39.0h | `$0.0938` | `$0.0861` | **-8.23%** | **-8.59%** | +3.3% | -10.0% | `stop_loss` |
| 2 | Book 3 | `2023-02-08 15:00` | `2023-02-09 02:00` | 11.0h | `$0.0304` | `$0.0330` | **+8.70%** | **+8.34%** | +9.8% | -4.2% | `target_reclaim` |
| 3 | Book 3 | `2023-02-09 15:00` | `2023-02-09 22:00` | 7.0h | `$0.0313` | `$0.0288` | **-8.23%** | **-8.59%** | +3.8% | -11.4% | `stop_loss` |
| 4 | Book 3 | `2023-02-21 21:00` | `2023-02-22 03:00` | 6.0h | `$0.0453` | `$0.0492` | **+8.70%** | **+8.34%** | +11.7% | -3.4% | `target_reclaim` |
| 5 | Book 3 | `2023-04-02 10:00` | `2023-04-03 20:00` | 34.0h | `$0.0357` | `$0.0327` | **-8.23%** | **-8.59%** | +1.7% | -8.0% | `stop_loss` |
| 6 | Book 3 | `2023-06-25 03:00` | `2023-06-26 21:00` | 42.0h | `$0.0259` | `$0.0238` | **-8.23%** | **-8.59%** | +4.6% | -8.1% | `stop_loss` |
| 7 | Book 3 | `2023-10-04 00:00` | `2023-10-07 00:00` | 72.0h | `$0.0191` | `$0.0198` | **+3.93%** | **+3.85%** | +7.0% | -3.5% | `time_expiry` |
| 8 | Book 3 | `2023-10-31 15:00` | `2023-11-01 12:00` | 21.0h | `$0.0214` | `$0.0232` | **+8.70%** | **+8.34%** | +10.9% | -0.1% | `target_reclaim` |
| 9 | Book 3 | `2023-11-09 16:00` | `2023-11-10 02:00` | 10.0h | `$0.0237` | `$0.0258` | **+8.70%** | **+8.34%** | +10.7% | -8.2% | `target_reclaim` |
| 10 | Book 3 | `2023-11-14 18:00` | `2023-11-17 18:00` | 72.0h | `$0.0248` | `$0.0252` | **+1.98%** | **+1.96%** | +8.3% | -3.2% | `time_expiry` |
| 11 | Book 3 | `2023-12-06 05:00` | `2023-12-09 05:00` | 72.0h | `$0.0272` | `$0.0292` | **+7.14%** | **+6.90%** | +7.9% | -3.9% | `time_expiry` |
| 12 | Book 3 | `2023-12-19 09:00` | `2023-12-22 09:00` | 72.0h | `$0.0294` | `$0.0293` | **-0.45%** | **-0.45%** | +10.1% | -5.3% | `time_expiry` |
| 13 | Book 3 | `2024-02-28 17:00` | `2024-02-29 08:00` | 15.0h | `$0.0330` | `$0.0359` | **+8.70%** | **+8.34%** | +10.0% | -8.1% | `target_reclaim` |
| 14 | Book 3 | `2024-03-03 07:00` | `2024-03-03 08:00` | 1.0h | `$0.0348` | `$0.0378` | **+8.70%** | **+8.34%** | +24.8% | -0.0% | `target_reclaim` |
| 15 | Book 3 | `2024-03-04 17:00` | `2024-03-05 19:00` | 26.0h | `$0.0397` | `$0.0364` | **-8.23%** | **-8.59%** | +5.4% | -23.7% | `stop_loss` |
| 16 | Book 3 | `2024-03-14 13:00` | `2024-03-15 08:00` | 19.0h | `$0.0536` | `$0.0492` | **-8.23%** | **-8.59%** | +8.2% | -8.2% | `stop_loss` |
| 17 | Book 3 | `2024-03-26 15:00` | `2024-03-27 02:00` | 11.0h | `$0.0572` | `$0.0621` | **+8.70%** | **+8.34%** | +10.1% | -5.4% | `target_reclaim` |
| 18 | Book 3 | `2024-04-02 02:00` | `2024-04-02 13:00` | 11.0h | `$0.0607` | `$0.0557` | **-8.23%** | **-8.59%** | +2.9% | -8.1% | `stop_loss` |
| 19 | Book 3 | `2024-08-26 17:00` | `2024-08-27 21:00` | 28.0h | `$0.0265` | `$0.0243` | **-8.23%** | **-8.59%** | +1.7% | -8.6% | `stop_loss` |
| 20 | Book 3 | `2024-12-02 08:00` | `2024-12-02 21:00` | 13.0h | `$0.0402` | `$0.0437` | **+8.70%** | **+8.34%** | +9.9% | -0.9% | `target_reclaim` |
| 21 | Book 3 | `2025-04-28 01:00` | `2025-05-01 01:00` | 72.0h | `$0.0191` | `$0.0199` | **+4.45%** | **+4.36%** | +7.9% | -0.4% | `time_expiry` |
| 22 | Book 3 | `2026-09-03 03:00` | `2026-09-03 12:00` | 9.0h | `$0.0045` | `$0.0041` | **-8.23%** | **-8.59%** | +4.3% | -8.6% | `stop_loss` |
| 23 | Book 3 | `2026-09-29 01:00` | `2026-10-02 01:00` | 72.0h | `$0.0048` | `$0.0049` | **+2.33%** | **+2.30%** | +4.5% | -0.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `9` | `0.0%` | **`-77.3%`** |
| `target_reclaim` | `8` | `100.0%` | **`+66.7%`** |
| `time_expiry` | `6` | `83.3%` | **`+18.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `ANKR`

* **Total Candidate Breakouts Filtered (Vetoed):** `237`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `134` (56.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `36`
* **Saved Capital Losses Avoided:** `+1,825.0%`
* **Missed Upside Forgone:** `-1,460.4%`
* **Net Veto Alpha:** `+364.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `86` | `36.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `53` | `22.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `49` | `20.7%` |
| `Core 1: Macro Bear Veto` | `37` | `15.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `12` | `5.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*