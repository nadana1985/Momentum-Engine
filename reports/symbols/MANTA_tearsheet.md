# Kronos V12: Institutional Symbol Tear Sheet — `MANTA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `11` (`11` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`54.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.877`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.39%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.4% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-23 14:00` | `2024-02-24 01:00` | 11.0h | `$3.0451` | `$2.7944` | **-8.23%** | **-8.59%** | +2.8% | -9.2% | `stop_loss` |
| 2 | Book 3 | `2024-03-14 08:00` | `2024-03-15 03:00` | 19.0h | `$3.6203` | `$3.3223` | **-8.23%** | **-8.59%** | +1.5% | -12.8% | `stop_loss` |
| 3 | Book 3 | `2024-05-29 16:00` | `2024-06-01 16:00` | 72.0h | `$1.7580` | `$1.7500` | **-0.46%** | **-0.46%** | +2.5% | -3.4% | `time_expiry` |
| 4 | Book 3 | `2024-07-22 14:00` | `2024-07-24 15:00` | 49.0h | `$1.0267` | `$0.9422` | **-8.23%** | **-8.59%** | +2.8% | -8.1% | `stop_loss` |
| 5 | Book 3 | `2024-12-02 04:00` | `2024-12-02 23:00` | 19.0h | `$1.1376` | `$1.2365` | **+8.70%** | **+8.34%** | +11.8% | -3.7% | `target_reclaim` |
| 6 | Book 3 | `2025-04-24 13:00` | `2025-04-24 22:00` | 9.0h | `$0.2182` | `$0.2273` | **+4.17%** | **+4.08%** | +4.3% | -4.7% | `target_reclaim` |
| 7 | Book 3 | `2025-04-27 07:00` | `2025-04-28 07:00` | 24.0h | `$0.2354` | `$0.2452` | **+4.17%** | **+4.08%** | +4.6% | -6.2% | `target_reclaim` |
| 8 | Book 3 | `2025-07-17 01:00` | `2025-07-17 11:00` | 10.0h | `$0.2381` | `$0.2480` | **+4.17%** | **+4.08%** | +4.5% | -2.1% | `target_reclaim` |
| 9 | Book 3 | `2025-07-18 15:00` | `2025-07-20 15:00` | 48.0h | `$0.2436` | `$0.2583` | **+6.03%** | **+5.85%** | +7.3% | -6.0% | `target_reclaim` |
| 10 | Book 3 | `2025-07-22 08:00` | `2025-07-23 17:00` | 33.0h | `$0.2436` | `$0.2236` | **-8.23%** | **-8.59%** | +6.5% | -8.3% | `stop_loss` |
| 11 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0591` | `$0.0616` | **+4.17%** | **+4.08%** | +11.2% | -3.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+30.5%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `MANTA`

* **Total Candidate Breakouts Filtered (Vetoed):** `435`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `241` (55.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+4,544.4%`
* **Missed Upside Forgone:** `-486.9%`
* **Net Veto Alpha:** `+4,057.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `381` | `87.6%` |
| `Core 1: Macro Bear Veto` | `37` | `8.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `17` | `3.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*