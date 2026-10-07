# Kronos V12: Institutional Symbol Tear Sheet — `XVG`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.437`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-29.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.74x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.97%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-27.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`39.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.8% / -9.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-10-02 18:00` | `2023-10-05 18:00` | 72.0h | `$0.0035` | `$0.0033` | **-5.90%** | **-6.08%** | +3.7% | -7.6% | `time_expiry` |
| 2 | Book 3 | `2023-12-31 22:00` | `2024-01-03 12:00` | 62.0h | `$0.0039` | `$0.0036` | **-8.23%** | **-8.59%** | +7.1% | -21.0% | `stop_loss` |
| 3 | Book 3 | `2024-08-26 17:00` | `2024-08-27 22:00` | 29.0h | `$0.0041` | `$0.0037` | **-8.23%** | **-8.59%** | +2.0% | -8.8% | `stop_loss` |
| 4 | Book 3 | `2025-04-28 01:00` | `2025-04-28 12:00` | 11.0h | `$0.0050` | `$0.0054` | **+8.70%** | **+8.34%** | +8.9% | -1.9% | `target_reclaim` |
| 5 | Book 3 | `2025-04-29 17:00` | `2025-04-30 13:00` | 20.0h | `$0.0056` | `$0.0051` | **-8.23%** | **-8.59%** | +1.6% | -9.1% | `stop_loss` |
| 6 | Book 3 | `2025-05-14 08:00` | `2025-05-14 15:00` | 7.0h | `$0.0078` | `$0.0072` | **-8.23%** | **-8.59%** | +7.3% | -8.6% | `stop_loss` |
| 7 | Book 3 | `2025-07-18 10:00` | `2025-07-20 06:00` | 44.0h | `$0.0074` | `$0.0081` | **+8.70%** | **+8.34%** | +10.7% | -7.5% | `target_reclaim` |
| 8 | Book 3 | `2026-09-05 13:00` | `2026-09-08 13:00` | 72.0h | `$0.0028` | `$0.0029` | **+2.26%** | **+2.24%** | +8.6% | -4.5% | `time_expiry` |
| 9 | Book 3 | `2026-09-09 22:00` | `2026-09-09 23:00` | 1.0h | `$0.0031` | `$0.0028` | **-11.60%** | **-12.33%** | +2.8% | -16.6% | `stop_loss` |
| 10 | Book 3 | `2026-09-28 06:00` | `2026-10-01 06:00` | 72.0h | `$0.0032` | `$0.0033` | **+4.25%** | **+4.16%** | +5.8% | -5.5% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `5` | `0.0%` | **`-46.7%`** |
| `time_expiry` | `3` | `66.7%` | **`+0.3%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `XVG`

* **Total Candidate Breakouts Filtered (Vetoed):** `133`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `76` (57.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `48`
* **Saved Capital Losses Avoided:** `+1,111.8%`
* **Missed Upside Forgone:** `-1,749.0%`
* **Net Veto Alpha:** `+-637.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `63` | `47.4%` |
| `Core 1: Macro Bear Veto` | `31` | `23.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `31` | `23.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `8` | `6.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*