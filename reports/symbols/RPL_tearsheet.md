# Kronos V12: Institutional Symbol Tear Sheet — `RPL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.066`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+2.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.21%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-12.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`35.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.5% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-10-22 13:00` | `2024-10-25 13:00` | 72.0h | `$11.3114` | `$11.0832` | **-2.02%** | **-2.04%** | +2.4% | -7.4% | `time_expiry` |
| 2 | Book 3 | `2024-11-10 21:00` | `2024-11-12 16:00` | 43.0h | `$11.5488` | `$10.5983` | **-8.23%** | **-8.59%** | +8.3% | -8.6% | `stop_loss` |
| 3 | Book 3 | `2024-12-02 08:00` | `2024-12-03 06:00` | 22.0h | `$13.6390` | `$14.8250` | **+8.70%** | **+8.34%** | +9.5% | -3.8% | `target_reclaim` |
| 4 | Book 3 | `2024-12-03 14:00` | `2024-12-03 18:00` | 4.0h | `$14.2158` | `$15.4520` | **+8.70%** | **+8.34%** | +9.4% | -1.5% | `target_reclaim` |
| 5 | Book 3 | `2025-02-11 17:00` | `2025-02-11 18:00` | 1.0h | `$9.8210` | `$9.0127` | **-8.23%** | **-8.59%** | +2.4% | -8.2% | `stop_loss` |
| 6 | Book 3 | `2025-04-24 03:00` | `2025-04-25 05:00` | 26.0h | `$4.2716` | `$4.6430` | **+8.70%** | **+8.34%** | +11.4% | -0.9% | `target_reclaim` |
| 7 | Book 3 | `2025-04-27 01:00` | `2025-04-30 01:00` | 72.0h | `$4.3240` | `$4.2883` | **-0.83%** | **-0.83%** | +5.3% | -2.8% | `time_expiry` |
| 8 | Book 3 | `2025-06-12 11:00` | `2025-06-13 01:00` | 14.0h | `$6.3434` | `$5.8213` | **-8.23%** | **-8.59%** | +6.9% | -8.6% | `stop_loss` |
| 9 | Book 3 | `2025-07-12 00:00` | `2025-07-15 00:00` | 72.0h | `$5.8319` | `$5.6788` | **-2.63%** | **-2.66%** | +6.4% | -3.9% | `time_expiry` |
| 10 | Book 3 | `2025-08-10 03:00` | `2025-08-11 04:00` | 25.0h | `$8.3628` | `$9.0900` | **+8.70%** | **+8.34%** | +12.7% | -3.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_expiry` | `3` | `0.0%` | **`-5.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `RPL`

* **Total Candidate Breakouts Filtered (Vetoed):** `89`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `51` (57.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+642.0%`
* **Missed Upside Forgone:** `-713.9%`
* **Net Veto Alpha:** `+-71.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `46` | `51.7%` |
| `Core 1: Macro Bear Veto` | `30` | `33.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `13` | `14.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*