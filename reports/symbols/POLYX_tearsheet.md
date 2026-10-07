# Kronos V12: Institutional Symbol Tear Sheet — `POLYX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.518`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+14.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.15x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.42%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-26.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`24.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.9% / -7.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-12-04 11:00` | `2023-12-04 23:00` | 12.0h | `$0.2078` | `$0.2259` | **+8.70%** | **+8.34%** | +19.6% | -9.3% | `target_reclaim` |
| 2 | Book 3 | `2024-01-06 08:00` | `2024-01-06 13:00` | 5.0h | `$0.1992` | `$0.2165` | **+8.70%** | **+8.34%** | +9.3% | -1.5% | `target_reclaim` |
| 3 | Book 3 | `2024-02-28 17:00` | `2024-02-29 12:00` | 19.0h | `$0.1856` | `$0.2018` | **+8.70%** | **+8.34%** | +9.4% | -6.4% | `target_reclaim` |
| 4 | Book 3 | `2024-03-05 16:00` | `2024-03-05 19:00` | 3.0h | `$0.2282` | `$0.2094` | **-8.23%** | **-8.59%** | +2.2% | -20.2% | `stop_loss` |
| 5 | Book 3 | `2024-03-31 21:00` | `2024-04-01 05:00` | 8.0h | `$0.6401` | `$0.5874` | **-8.23%** | **-8.59%** | +18.4% | -8.0% | `stop_loss` |
| 6 | Book 3 | `2024-07-23 04:00` | `2024-07-24 16:00` | 36.0h | `$0.2733` | `$0.2720` | **-0.48%** | **-0.48%** | +0.9% | -5.4% | `stall_bailout` |
| 7 | Book 3 | `2024-11-13 04:00` | `2024-11-14 23:00` | 43.0h | `$0.2533` | `$0.2324` | **-8.23%** | **-8.59%** | +5.3% | -8.4% | `stop_loss` |
| 8 | Book 3 | `2024-11-17 02:00` | `2024-11-18 03:00` | 25.0h | `$0.2862` | `$0.3111` | **+8.70%** | **+8.34%** | +8.9% | -4.5% | `target_reclaim` |
| 9 | Book 3 | `2024-11-20 03:00` | `2024-11-21 03:00` | 24.0h | `$0.2926` | `$0.3180` | **+8.70%** | **+8.34%** | +10.1% | -1.8% | `target_reclaim` |
| 10 | Book 3 | `2025-04-28 01:00` | `2025-05-01 01:00` | 72.0h | `$0.1543` | `$0.1524` | **-1.21%** | **-1.22%** | +5.1% | -5.0% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+41.7%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `stall_bailout` | `1` | `0.0%` | **`-0.5%`** |
| `time_expiry` | `1` | `0.0%` | **`-1.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `POLYX`

* **Total Candidate Breakouts Filtered (Vetoed):** `120`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `75` (62.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `14`
* **Saved Capital Losses Avoided:** `+932.7%`
* **Missed Upside Forgone:** `-410.8%`
* **Net Veto Alpha:** `+521.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `75` | `62.5%` |
| `Core 1: Macro Bear Veto` | `24` | `20.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `20` | `16.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*