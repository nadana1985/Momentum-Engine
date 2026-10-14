# Kronos V12: Institutional Symbol Tear Sheet — `CGPT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`62.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.436`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+37.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.45x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.63%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-21.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.4% / -9.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-01-10 09:00` | `2025-01-14 09:00` | Live | `$0.3202` | `$0.3474` | **+8.50%** | **+8.16%** | +34.3% | -40.7% | `shelf_target_reclaim` |
| 2 | Book 2 | `2025-04-21 13:00` | `2025-04-26 07:00` | 114.0h | `$0.0804` | `$0.1069` | **+40.58%** | **+35.08%** | +38.1% | -3.4% | `climax_top_harvest` |
| 3 | Book 3 | `2025-05-12 14:00` | `2025-05-12 18:00` | 4.0h | `$0.1374` | `$0.1261` | **-8.23%** | **-8.59%** | +5.6% | -9.2% | `stop_loss` |
| 4 | Book 3 | `2025-05-23 12:00` | `2025-05-25 07:00` | 43.0h | `$0.1376` | `$0.1263` | **-8.23%** | **-8.59%** | +4.7% | -8.4% | `stop_loss` |
| 5 | Book 3 | `2025-07-01 05:00` | `2025-07-02 13:00` | 32.0h | `$0.0901` | `$0.0939` | **+4.17%** | **+4.08%** | +5.1% | -4.5% | `target_reclaim` |
| 6 | Book 3 | `2025-07-14 06:00` | `2025-07-15 04:00` | 22.0h | `$0.1098` | `$0.1007` | **-8.23%** | **-8.59%** | +2.7% | -8.1% | `stop_loss` |
| 7 | Book 3 | `2025-07-17 19:00` | `2025-07-18 01:00` | 6.0h | `$0.1130` | `$0.1177` | **+4.17%** | **+4.08%** | +4.4% | -2.2% | `target_reclaim` |
| 8 | Book 3 | `2026-09-29 01:00` | `2026-09-30 16:00` | 39.0h | `$0.0207` | `$0.0232` | **+12.04%** | **+11.37%** | +12.2% | -0.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+19.5%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+35.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `CGPT`

* **Total Candidate Breakouts Filtered (Vetoed):** `107`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `92` (86.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+1,812.2%`
* **Missed Upside Forgone:** `-279.6%`
* **Net Veto Alpha:** `+1,532.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `84` | `78.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `19` | `17.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `3.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*