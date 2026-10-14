# Kronos V12: Institutional Symbol Tear Sheet — `POWR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`85.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.583`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+31.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.38x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.56%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-12.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`14.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+42.9% / -8.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-12-12 10:00` | `2023-12-13 00:00` | 14.0h | `$0.3794` | `$0.4124` | **+8.70%** | **+8.34%** | +10.1% | -2.0% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2024-01-03 12:00` | `2024-01-07 12:00` | Live | `$0.3645` | `$0.3955` | **+8.50%** | **+8.16%** | +205.1% | -18.2% | `shelf_target_reclaim` |
| 3 | Book 3 | `2024-01-07 08:00` | `2024-01-07 09:00` | 1.0h | `$0.8683` | `$0.7674` | **-11.62%** | **-12.36%** | +39.2% | -36.0% | `stop_loss` |
| 4 | Book 3 | `2024-03-10 14:00` | `2024-03-10 19:00` | 5.0h | `$0.3899` | `$0.4081` | **+4.67%** | **+4.56%** | +5.1% | -1.4% | `target_reclaim` |
| 5 | Book 3 | `2024-11-14 03:00` | `2024-11-14 06:00` | 3.0h | `$0.2265` | `$0.2373` | **+4.77%** | **+4.66%** | +5.7% | -0.1% | `target_reclaim` |
| 6 | Book 3 | `2024-11-20 18:00` | `2024-11-23 09:00` | 63.0h | `$0.2423` | `$0.2786` | **+14.97%** | **+13.95%** | +15.1% | -0.7% | `target_reclaim` |
| 7 | Book 4 | `2026-09-13 00:00` | `2026-09-13 01:00` | 1.0h | `$0.0713` | `$0.0856` | **+4.83%** | **+4.61%** | +20.3% | -1.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+36.1%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-12.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `POWR`

* **Total Candidate Breakouts Filtered (Vetoed):** `243`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `174` (71.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+2,205.2%`
* **Missed Upside Forgone:** `-1,255.0%`
* **Net Veto Alpha:** `+950.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `170` | `70.0%` |
| `Core 1: Macro Bear Veto` | `39` | `16.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `17` | `7.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `16` | `6.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*