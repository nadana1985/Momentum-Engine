# Kronos V12: Institutional Symbol Tear Sheet — `CKB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `16` (`16` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `16` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`62.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.539`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+24.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.27x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.50%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-18.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`23.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.4% / -7.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-03-20 10:00` | `2023-03-24 10:00` | Live | `$0.0049` | `$0.0053` | **+8.50%** | **+8.16%** | +27.1% | -15.5% | `shelf_target_reclaim` |
| 2 | Book 3 | `2023-10-02 18:00` | `2023-10-05 18:00` | 72.0h | `$0.0027` | `$0.0027` | **-1.55%** | **-1.56%** | +2.1% | -5.6% | `time_expiry` |
| 3 | Book 3 | `2023-12-10 09:00` | `2023-12-10 20:00` | 11.0h | `$0.0035` | `$0.0036` | **+4.17%** | **+4.08%** | +4.6% | -0.3% | `target_reclaim` |
| 4 | Book 3 | `2024-03-05 19:00` | `2024-03-06 03:00` | 8.0h | `$0.0174` | `$0.0189` | **+8.70%** | **+8.34%** | +9.0% | -13.1% | `target_reclaim` |
| 5 | Book 3 | `2024-03-09 10:00` | `2024-03-10 01:00` | 15.0h | `$0.0216` | `$0.0235` | **+8.70%** | **+8.34%** | +8.9% | -0.5% | `target_reclaim` |
| 6 | Book 3 | `2024-03-12 08:00` | `2024-03-13 21:00` | 37.0h | `$0.0234` | `$0.0215` | **-8.23%** | **-8.59%** | +5.5% | -8.7% | `stop_loss` |
| 7 | Book 5 (Shelf Absorption Squeeze) | `2024-04-06 08:00` | `2024-04-10 08:00` | Live | `$0.0200` | `$0.0217` | **+8.50%** | **+8.16%** | +74.9% | -17.1% | `shelf_target_reclaim` |
| 8 | Book 3 | `2024-04-11 02:00` | `2024-04-11 12:00` | 10.0h | `$0.0320` | `$0.0294` | **-8.23%** | **-8.59%** | +3.4% | -8.6% | `stop_loss` |
| 9 | Book 3 | `2024-06-04 20:00` | `2024-06-04 21:00` | 1.0h | `$0.0177` | `$0.0184` | **+4.17%** | **+4.08%** | +4.9% | -0.6% | `target_reclaim` |
| 10 | Book 3 | `2024-06-05 05:00` | `2024-06-07 06:00` | 49.0h | `$0.0179` | `$0.0192` | **+7.50%** | **+7.24%** | +7.5% | -3.6% | `target_reclaim` |
| 11 | Book 3 | `2024-06-07 16:00` | `2024-06-07 18:00` | 2.0h | `$0.0189` | `$0.0173` | **-8.23%** | **-8.59%** | +3.0% | -20.1% | `stop_loss` |
| 12 | Book 3 | `2024-07-22 16:00` | `2024-07-25 02:00` | 58.0h | `$0.0123` | `$0.0113` | **-8.23%** | **-8.59%** | +3.7% | -9.0% | `stop_loss` |
| 13 | Book 3 | `2024-09-13 16:00` | `2024-09-13 22:00` | 6.0h | `$0.0128` | `$0.0137` | **+7.39%** | **+7.13%** | +8.5% | -0.3% | `target_reclaim` |
| 14 | Book 3 | `2024-09-30 23:00` | `2024-10-01 17:00` | 18.0h | `$0.0166` | `$0.0152` | **-8.23%** | **-8.59%** | +4.2% | -9.4% | `stop_loss` |
| 15 | Book 3 | `2024-12-02 08:00` | `2024-12-03 06:00` | 22.0h | `$0.0165` | `$0.0178` | **+7.58%** | **+7.31%** | +8.7% | -7.8% | `target_reclaim` |
| 16 | Book 3 | `2026-09-20 14:00` | `2026-09-21 03:00` | 13.0h | `$0.0012` | `$0.0012` | **+5.82%** | **+5.66%** | +7.1% | -0.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+52.2%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `time_expiry` | `1` | `0.0%` | **`-1.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CKB`

* **Total Candidate Breakouts Filtered (Vetoed):** `498`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `255` (51.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `120`
* **Saved Capital Losses Avoided:** `+3,114.7%`
* **Missed Upside Forgone:** `-4,082.2%`
* **Net Veto Alpha:** `+-967.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `203` | `40.8%` |
| `Core 1: Macro Bear Veto` | `131` | `26.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `120` | `24.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `44` | `8.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*