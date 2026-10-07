# Kronos V12: Institutional Symbol Tear Sheet — `DODOX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `12` (`12` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `12` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.912`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+52.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.68x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.35%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`25.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.7% / -4.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-12-05 18:00` | `2023-12-06 01:00` | 7.0h | `$0.1562` | `$0.1697` | **+8.70%** | **+8.34%** | +10.8% | -1.4% | `target_reclaim` |
| 2 | Book 3 | `2023-12-26 17:00` | `2023-12-27 01:00` | 8.0h | `$0.2168` | `$0.2356` | **+8.70%** | **+8.34%** | +9.9% | -2.8% | `target_reclaim` |
| 3 | Book 3 | `2024-02-28 17:00` | `2024-02-29 01:00` | 8.0h | `$0.2123` | `$0.2308` | **+8.70%** | **+8.34%** | +11.3% | -7.1% | `target_reclaim` |
| 4 | Book 3 | `2024-03-03 07:00` | `2024-03-05 02:00` | 43.0h | `$0.2387` | `$0.2595` | **+8.70%** | **+8.34%** | +9.4% | -3.4% | `target_reclaim` |
| 5 | Book 3 | `2024-07-23 04:00` | `2024-07-26 04:00` | 72.0h | `$0.1205` | `$0.1246` | **+3.43%** | **+3.37%** | +4.6% | -7.1% | `time_expiry` |
| 6 | Book 3 | `2024-07-31 04:00` | `2024-07-31 10:00` | 6.0h | `$0.1260` | `$0.1370` | **+8.70%** | **+8.34%** | +9.8% | -0.4% | `target_reclaim` |
| 7 | Book 3 | `2024-11-12 10:00` | `2024-11-15 10:00` | 72.0h | `$0.1213` | `$0.1204` | **-0.73%** | **-0.73%** | +5.5% | -7.9% | `time_expiry` |
| 8 | Book 3 | `2024-12-02 11:00` | `2024-12-02 21:00` | 10.0h | `$0.1556` | `$0.1691` | **+8.70%** | **+8.34%** | +9.5% | -1.0% | `target_reclaim` |
| 9 | Book 3 | `2025-02-13 03:00` | `2025-02-13 12:00` | 9.0h | `$0.1133` | `$0.1040` | **-8.23%** | **-8.59%** | +8.1% | -8.1% | `stop_loss` |
| 10 | Book 3 | `2025-05-01 17:00` | `2025-05-03 10:00` | 41.0h | `$0.0513` | `$0.0471` | **-8.23%** | **-8.59%** | +3.8% | -8.3% | `stop_loss` |
| 11 | Book 3 | `2025-07-15 03:00` | `2025-07-15 16:00` | 13.0h | `$0.0429` | `$0.0466` | **+8.70%** | **+8.34%** | +12.7% | -0.6% | `target_reclaim` |
| 12 | Book 3 | `2025-07-17 16:00` | `2025-07-18 04:00` | 12.0h | `$0.0456` | `$0.0496` | **+8.70%** | **+8.34%** | +9.1% | -0.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+66.7%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `2` | `50.0%` | **`+2.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `DODOX`

* **Total Candidate Breakouts Filtered (Vetoed):** `102`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `52` (51.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `16`
* **Saved Capital Losses Avoided:** `+676.9%`
* **Missed Upside Forgone:** `-500.3%`
* **Net Veto Alpha:** `+176.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `63` | `61.8%` |
| `Core 1: Macro Bear Veto` | `17` | `16.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `16` | `15.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `5.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*