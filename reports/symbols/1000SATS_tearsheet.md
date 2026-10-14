# Kronos V12: Institutional Symbol Tear Sheet — `1000SATS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `12` (`12` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `12` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.234`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+10.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.11x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.91%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-16.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`21.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.2% / -8.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-20 01:00` | `2024-02-20 15:00` | 14.0h | `$0.0005` | `$0.0005` | **-8.23%** | **-8.59%** | +6.1% | -11.9% | `stop_loss` |
| 2 | Book 3 | `2024-02-28 17:00` | `2024-02-29 06:00` | 13.0h | `$0.0005` | `$0.0006` | **+13.99%** | **+13.10%** | +14.4% | -10.0% | `target_reclaim` |
| 3 | Book 3 | `2024-02-29 21:00` | `2024-03-02 01:00` | 28.0h | `$0.0005` | `$0.0006` | **+14.19%** | **+13.27%** | +18.6% | -4.9% | `target_reclaim` |
| 4 | Book 3 | `2024-05-23 12:00` | `2024-05-23 20:00` | 8.0h | `$0.0003` | `$0.0003` | **-8.23%** | **-8.59%** | +4.9% | -9.7% | `stop_loss` |
| 5 | Book 4 | `2024-08-22 04:00` | `2024-08-23 19:00` | 39.0h | `$0.0003` | `$0.0004` | **+13.83%** | **+13.00%** | +20.3% | -7.1% | `target_reclaim` |
| 6 | Book 3 | `2024-11-11 05:00` | `2024-11-12 10:00` | 29.0h | `$0.0003` | `$0.0003` | **-8.23%** | **-8.59%** | +4.2% | -14.8% | `stop_loss` |
| 7 | Book 3 | `2024-12-03 19:00` | `2024-12-03 22:00` | 3.0h | `$0.0003` | `$0.0003` | **+4.17%** | **+4.08%** | +5.0% | -0.1% | `target_reclaim` |
| 8 | Book 3 | `2025-04-27 16:00` | `2025-04-30 16:00` | 72.0h | `$0.0000` | `$0.0000` | **-3.42%** | **-3.48%** | +3.9% | -6.8% | `time_expiry` |
| 9 | Book 3 | `2025-05-15 09:00` | `2025-05-15 22:00` | 13.0h | `$0.0001` | `$0.0001` | **-8.23%** | **-8.59%** | +4.0% | -10.8% | `stop_loss` |
| 10 | Book 3 | `2025-07-18 20:00` | `2025-07-18 22:00` | 2.0h | `$0.0000` | `$0.0001` | **+10.25%** | **+9.76%** | +11.1% | -2.2% | `target_reclaim` |
| 11 | Book 3 | `2026-08-22 05:00` | `2026-08-23 04:00` | 23.0h | `$0.0000` | `$0.0000` | **-8.23%** | **-8.59%** | +13.2% | -18.3% | `stop_loss` |
| 12 | Book 3 | `2026-09-26 20:00` | `2026-09-27 07:00` | 11.0h | `$0.0000` | `$0.0000` | **+4.17%** | **+4.08%** | +5.0% | -0.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+57.3%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `time_expiry` | `1` | `0.0%` | **`-3.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000SATS`

* **Total Candidate Breakouts Filtered (Vetoed):** `168`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `157` (93.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `22`
* **Saved Capital Losses Avoided:** `+3,053.8%`
* **Missed Upside Forgone:** `-1,015.0%`
* **Net Veto Alpha:** `+2,038.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `120` | `71.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `39` | `23.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `4.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `1.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*