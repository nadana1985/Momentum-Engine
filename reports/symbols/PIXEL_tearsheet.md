# Kronos V12: Institutional Symbol Tear Sheet — `PIXEL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `16` (`15` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.501`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+25.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.28x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.67%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-15.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.4% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-05-30 07:00` | `2024-05-31 17:00` | 34.0h | `$0.3903` | `$0.4242` | **+8.70%** | **+8.34%** | +9.6% | -2.1% | `target_reclaim` |
| 2 | Book 3 | `2024-08-26 15:00` | `2024-08-27 21:00` | 30.0h | `$0.1573` | `$0.1444` | **-8.23%** | **-8.59%** | +1.6% | -11.1% | `stop_loss` |
| 3 | Book 3 | `2024-09-18 07:00` | `2024-09-19 00:00` | 17.0h | `$0.1342` | `$0.1459` | **+8.70%** | **+8.34%** | +9.7% | -5.7% | `target_reclaim` |
| 4 | Book 3 | `2024-09-26 00:00` | `2024-09-26 15:00` | 15.0h | `$0.1474` | `$0.1602` | **+8.70%** | **+8.34%** | +9.4% | -0.5% | `target_reclaim` |
| 5 | Book 3 | `2024-10-22 18:00` | `2024-10-23 10:00` | 16.0h | `$0.1809` | `$0.1660` | **-8.23%** | **-8.59%** | +12.0% | -8.2% | `stop_loss` |
| 6 | Book 3 | `2024-11-10 21:00` | `2024-11-11 00:00` | 3.0h | `$0.1876` | `$0.2039` | **+8.70%** | **+8.34%** | +8.7% | -0.0% | `target_reclaim` |
| 7 | Book 3 | `2024-11-12 10:00` | `2024-11-13 03:00` | 17.0h | `$0.1970` | `$0.1808` | **-8.23%** | **-8.59%** | +1.6% | -8.3% | `stop_loss` |
| 8 | Book 3 | `2024-11-17 02:00` | `2024-11-20 02:00` | 72.0h | `$0.2016` | `$0.1878` | **-6.82%** | **-7.06%** | +5.9% | -6.9% | `time_expiry` |
| 9 | Book 3 | `2024-11-26 11:00` | `2024-11-27 15:00` | 28.0h | `$0.2121` | `$0.2305` | **+8.70%** | **+8.34%** | +9.0% | -3.5% | `target_reclaim` |
| 10 | Book 3 | `2024-12-02 08:00` | `2024-12-02 21:00` | 13.0h | `$0.2414` | `$0.2624` | **+8.70%** | **+8.34%** | +9.0% | -4.7% | `target_reclaim` |
| 11 | Book 3 | `2024-12-03 14:00` | `2024-12-03 18:00` | 4.0h | `$0.2485` | `$0.2701` | **+8.70%** | **+8.34%** | +9.2% | -1.7% | `target_reclaim` |
| 12 | Book 3 | `2025-05-14 13:00` | `2025-05-15 06:00` | 17.0h | `$0.0598` | `$0.0549` | **-8.23%** | **-8.59%** | +2.3% | -9.5% | `stop_loss` |
| 13 | Book 3 | `2025-07-18 20:00` | `2025-07-20 16:00` | 44.0h | `$0.0419` | `$0.0455` | **+8.70%** | **+8.34%** | +9.6% | -2.1% | `target_reclaim` |
| 14 | Book 3 | `2026-09-25 02:00` | `2026-09-25 11:00` | 9.0h | `$0.0056` | `$0.0061` | **+8.70%** | **+8.34%** | +8.9% | -2.0% | `target_reclaim` |
| 15 | Book 3 | `2026-09-25 14:00` | `2026-09-28 14:00` | 72.0h | `$0.0060` | `$0.0055` | **-8.23%** | **-8.59%** | +4.6% | -9.4% | `stop_loss` |
| 16 | Book 3 | `2026-10-05 04:00` | `_Open Live_` | 46.7h | `$0.0062` | `$0.0061` | **-1.41%** | **-1.42%** | +3.4% | -2.1% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `9` | `100.0%` | **`+75.0%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `time_expiry` | `1` | `0.0%` | **`-7.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `PIXEL`

* **Total Candidate Breakouts Filtered (Vetoed):** `81`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `49` (60.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `16`
* **Saved Capital Losses Avoided:** `+650.8%`
* **Missed Upside Forgone:** `-977.3%`
* **Net Veto Alpha:** `+-326.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `44` | `54.3%` |
| `Core 1: Macro Bear Veto` | `25` | `30.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `7.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `7.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*