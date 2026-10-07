# Kronos V12: Institutional Symbol Tear Sheet — `ETHW`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `12` (`12` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `12` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.913`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+49.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.64x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.11%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`14.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.6% / -4.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-28 17:00` | `2024-02-29 02:00` | 9.0h | `$3.0240` | `$3.2870` | **+8.70%** | **+8.34%** | +11.4% | -6.1% | `target_reclaim` |
| 2 | Book 3 | `2024-03-05 19:00` | `2024-03-06 06:00` | 11.0h | `$3.8355` | `$4.1690` | **+8.70%** | **+8.34%** | +9.7% | -12.0% | `target_reclaim` |
| 3 | Book 3 | `2024-03-12 17:00` | `2024-03-13 01:00` | 8.0h | `$4.3038` | `$4.6780` | **+8.70%** | **+8.34%** | +8.8% | -0.6% | `target_reclaim` |
| 4 | Book 3 | `2024-03-29 18:00` | `2024-03-30 00:00` | 6.0h | `$4.8015` | `$5.2190` | **+8.70%** | **+8.34%** | +9.2% | -0.3% | `target_reclaim` |
| 5 | Book 3 | `2024-04-10 12:00` | `2024-04-11 04:00` | 16.0h | `$5.0168` | `$5.4530` | **+8.70%** | **+8.34%** | +9.4% | -0.8% | `target_reclaim` |
| 6 | Book 3 | `2024-07-24 21:00` | `2024-07-25 08:00` | 11.0h | `$2.6156` | `$2.4003` | **-8.23%** | **-8.59%** | +1.3% | -8.5% | `stop_loss` |
| 7 | Book 3 | `2024-11-10 21:00` | `2024-11-11 01:00` | 4.0h | `$3.3196` | `$3.6083` | **+8.70%** | **+8.34%** | +9.0% | -0.2% | `target_reclaim` |
| 8 | Book 3 | `2024-11-12 10:00` | `2024-11-14 23:00` | 61.0h | `$3.4537` | `$3.1694` | **-8.23%** | **-8.59%** | +6.7% | -9.4% | `stop_loss` |
| 9 | Book 3 | `2024-11-24 12:00` | `2024-11-25 09:00` | 21.0h | `$3.5163` | `$3.8221` | **+8.70%** | **+8.34%** | +8.7% | -1.4% | `target_reclaim` |
| 10 | Book 3 | `2024-12-09 08:00` | `2024-12-09 20:00` | 12.0h | `$4.8134` | `$4.4173` | **-8.23%** | **-8.59%** | +2.7% | -10.0% | `stop_loss` |
| 11 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.2603` | `$0.2829` | **+8.70%** | **+8.34%** | +17.0% | -0.1% | `target_reclaim` |
| 12 | Book 3 | `2026-09-23 20:00` | `2026-09-24 14:00` | 18.0h | `$0.2727` | `$0.2964` | **+8.70%** | **+8.34%** | +9.0% | -0.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `9` | `100.0%` | **`+75.0%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `ETHW`

* **Total Candidate Breakouts Filtered (Vetoed):** `107`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `49` (45.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `32`
* **Saved Capital Losses Avoided:** `+625.8%`
* **Missed Upside Forgone:** `-1,570.9%`
* **Net Veto Alpha:** `+-945.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `76` | `71.0%` |
| `Core 1: Macro Bear Veto` | `16` | `15.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `15` | `14.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*