# Kronos V12: Institutional Symbol Tear Sheet — `TLM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `17` (`17` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `17` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`58.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.494`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+53.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.70x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.12%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`46.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.0% / -7.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-07-14 18:00` | `2023-07-17 18:00` | 72.0h | `$0.0119` | `$0.0114` | **-4.11%** | **-4.20%** | +2.4% | -5.8% | `time_expiry` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2023-08-06 09:00` | `2023-08-10 09:00` | Live | `$0.0109` | `$0.0118` | **+8.50%** | **+8.16%** | +15.0% | -26.2% | `shelf_target_reclaim` |
| 3 | Book 3 | `2023-10-02 18:00` | `2023-10-05 18:00` | 72.0h | `$0.0101` | `$0.0098` | **-2.92%** | **-2.96%** | +2.8% | -5.5% | `time_expiry` |
| 4 | Book 3 | `2023-11-12 00:00` | `2023-11-13 01:00` | 25.0h | `$0.0134` | `$0.0144` | **+7.29%** | **+7.04%** | +8.0% | -0.4% | `target_reclaim` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2023-11-26 10:00` | `2023-11-30 10:00` | Live | `$0.0152` | `$0.0165` | **+8.50%** | **+8.16%** | +4.8% | -16.0% | `shelf_target_reclaim` |
| 6 | Book 3 | `2023-12-23 03:00` | `2023-12-23 09:00` | 6.0h | `$0.0167` | `$0.0176` | **+4.93%** | **+4.82%** | +7.0% | -0.0% | `target_reclaim` |
| 7 | Book 3 | `2024-02-16 15:00` | `2024-02-18 09:00` | 42.0h | `$0.0155` | `$0.0163` | **+5.20%** | **+5.07%** | +6.8% | -3.7% | `target_reclaim` |
| 8 | Book 3 | `2024-03-14 13:00` | `2024-03-15 03:00` | 14.0h | `$0.0286` | `$0.0262` | **-8.23%** | **-8.59%** | +4.0% | -9.3% | `stop_loss` |
| 9 | Book 3 | `2024-09-20 17:00` | `2024-09-21 21:00` | 28.0h | `$0.0109` | `$0.0114` | **+4.17%** | **+4.08%** | +5.1% | -0.8% | `target_reclaim` |
| 10 | Book 3 | `2024-11-10 20:00` | `2024-11-11 02:00` | 6.0h | `$0.0111` | `$0.0118` | **+5.83%** | **+5.66%** | +6.3% | -4.4% | `target_reclaim` |
| 11 | Book 3 | `2024-11-12 10:00` | `2024-11-15 04:00` | 66.0h | `$0.0111` | `$0.0102` | **-8.23%** | **-8.59%** | +5.7% | -9.1% | `stop_loss` |
| 12 | Book 4 | `2024-11-17 10:00` | `2024-11-24 03:00` | 161.0h | `$0.0123` | `$0.0148` | **+38.17%** | **+33.14%** | +21.8% | -12.6% | `target_reclaim` |
| 13 | Book 3 | `2024-11-24 12:00` | `2024-11-24 22:00` | 10.0h | `$0.0135` | `$0.0146` | **+8.70%** | **+8.34%** | +12.1% | -2.4% | `target_reclaim` |
| 14 | Book 3 | `2024-12-09 09:00` | `2024-12-09 20:00` | 11.0h | `$0.0187` | `$0.0172` | **-8.23%** | **-8.59%** | +4.5% | -8.7% | `stop_loss` |
| 15 | Book 3 | `2025-05-15 13:00` | `2025-05-18 13:00` | 72.0h | `$0.0060` | `$0.0059` | **-1.19%** | **-1.19%** | +5.3% | -7.1% | `time_expiry` |
| 16 | Book 3 | `2025-07-14 14:00` | `2025-07-16 00:00` | 34.0h | `$0.0052` | `$0.0054` | **+4.17%** | **+4.08%** | +4.6% | -5.9% | `target_reclaim` |
| 17 | Book 3 | `2026-09-28 05:00` | `2026-10-01 05:00` | 72.0h | `$0.0016` | `$0.0015` | **-1.37%** | **-1.38%** | +2.3% | -5.7% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+72.2%`** |
| `time_expiry` | `4` | `0.0%` | **`-9.7%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `TLM`

* **Total Candidate Breakouts Filtered (Vetoed):** `380`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `153` (40.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `60`
* **Saved Capital Losses Avoided:** `+1,825.1%`
* **Missed Upside Forgone:** `-1,673.0%`
* **Net Veto Alpha:** `+152.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `309` | `81.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `36` | `9.5%` |
| `Core 1: Macro Bear Veto` | `21` | `5.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `14` | `3.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*