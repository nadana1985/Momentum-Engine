# Kronos V12: Institutional Symbol Tear Sheet — `BEL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `22` (`22` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `22` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.690`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-31.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.73x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.44%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-52.3%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`25.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.8% / -8.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-01-14 09:00` | `2023-01-17 09:00` | 72.0h | `$0.4865` | `$0.5051` | **+3.83%** | **+3.76%** | +8.7% | -4.2% | `time_expiry` |
| 2 | Book 3 | `2023-01-24 21:00` | `2023-01-26 17:00` | 44.0h | `$0.5399` | `$0.5868` | **+8.70%** | **+8.34%** | +12.7% | -6.7% | `target_reclaim` |
| 3 | Book 3 | `2023-02-08 16:00` | `2023-02-09 21:00` | 29.0h | `$0.6104` | `$0.5602` | **-8.23%** | **-8.59%** | +5.8% | -9.4% | `stop_loss` |
| 4 | Book 3 | `2023-04-10 11:00` | `2023-04-13 11:00` | 72.0h | `$0.6965` | `$0.6628` | **-4.84%** | **-4.96%** | +2.5% | -7.7% | `time_expiry` |
| 5 | Book 3 | `2023-04-19 08:00` | `2023-04-20 16:00` | 32.0h | `$0.7877` | `$0.7229` | **-8.23%** | **-8.59%** | +5.2% | -9.9% | `stop_loss` |
| 6 | Book 3 | `2023-07-07 18:00` | `2023-07-09 00:00` | 30.0h | `$0.6998` | `$0.7606` | **+8.70%** | **+8.34%** | +10.2% | -2.2% | `target_reclaim` |
| 7 | Book 3 | `2023-07-18 08:00` | `2023-07-21 08:00` | 72.0h | `$0.7228` | `$0.7033` | **-2.69%** | **-2.72%** | +1.5% | -4.4% | `time_expiry` |
| 8 | Book 3 | `2023-12-11 02:00` | `2023-12-12 01:00` | 23.0h | `$0.6871` | `$0.7469` | **+8.70%** | **+8.34%** | +9.4% | -10.9% | `target_reclaim` |
| 9 | Book 3 | `2024-02-20 15:00` | `2024-02-22 11:00` | 44.0h | `$0.6798` | `$0.7389` | **+8.70%** | **+8.34%** | +9.2% | -5.0% | `target_reclaim` |
| 10 | Book 3 | `2024-02-28 17:00` | `2024-02-29 01:00` | 8.0h | `$0.7309` | `$0.7945` | **+8.70%** | **+8.34%** | +10.8% | -7.0% | `target_reclaim` |
| 11 | Book 3 | `2024-03-05 19:00` | `2024-03-05 20:00` | 1.0h | `$0.8090` | `$0.7424` | **-8.23%** | **-8.59%** | +11.0% | -16.4% | `stop_loss` |
| 12 | Book 3 | `2024-06-07 17:00` | `2024-06-07 18:00` | 1.0h | `$0.9762` | `$0.8959` | **-8.23%** | **-8.59%** | +1.7% | -17.8% | `stop_loss` |
| 13 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$0.5708` | `$0.5238` | **-8.23%** | **-8.59%** | +3.0% | -10.7% | `stop_loss` |
| 14 | Book 3 | `2024-11-20 11:00` | `2024-11-21 10:00` | 23.0h | `$0.6007` | `$0.6529` | **+8.70%** | **+8.34%** | +8.9% | -5.6% | `target_reclaim` |
| 15 | Book 3 | `2024-11-22 12:00` | `2024-11-22 13:00` | 1.0h | `$0.7000` | `$0.6424` | **-8.23%** | **-8.59%** | +8.7% | -9.5% | `stop_loss` |
| 16 | Book 3 | `2025-01-29 14:00` | `2025-01-29 19:00` | 5.0h | `$0.6427` | `$0.6986` | **+8.70%** | **+8.34%** | +12.0% | -2.0% | `target_reclaim` |
| 17 | Book 3 | `2025-02-02 18:00` | `2025-02-03 01:00` | 7.0h | `$0.7461` | `$0.6847` | **-8.23%** | **-8.59%** | +6.4% | -11.5% | `stop_loss` |
| 18 | Book 3 | `2025-02-04 05:00` | `2025-02-04 08:00` | 3.0h | `$0.8181` | `$0.7507` | **-8.23%** | **-8.59%** | +5.3% | -17.7% | `stop_loss` |
| 19 | Book 3 | `2025-02-10 15:00` | `2025-02-10 21:00` | 6.0h | `$0.8782` | `$0.9546` | **+8.70%** | **+8.34%** | +11.1% | -0.4% | `target_reclaim` |
| 20 | Book 3 | `2025-07-23 17:00` | `2025-07-24 06:00` | 13.0h | `$0.2902` | `$0.2663` | **-8.23%** | **-8.59%** | +2.0% | -8.6% | `stop_loss` |
| 21 | Book 3 | `2025-07-28 17:00` | `2025-07-30 10:00` | 41.0h | `$0.2918` | `$0.2678` | **-8.23%** | **-8.59%** | +1.7% | -8.2% | `stop_loss` |
| 22 | Book 3 | `2025-09-22 02:00` | `2025-09-22 06:00` | 4.0h | `$0.2516` | `$0.2309` | **-8.23%** | **-8.59%** | +1.3% | -11.9% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `11` | `0.0%` | **`-94.5%`** |
| `target_reclaim` | `8` | `100.0%` | **`+66.7%`** |
| `time_expiry` | `3` | `33.3%` | **`-3.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `BEL`

* **Total Candidate Breakouts Filtered (Vetoed):** `259`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `168` (64.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `50`
* **Saved Capital Losses Avoided:** `+2,917.0%`
* **Missed Upside Forgone:** `-2,467.3%`
* **Net Veto Alpha:** `+449.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `70` | `27.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `59` | `22.8%` |
| `Core 1: Macro Bear Veto` | `57` | `22.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `57` | `22.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `16` | `6.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*