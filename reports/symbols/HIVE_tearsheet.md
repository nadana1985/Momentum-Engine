# Kronos V12: Institutional Symbol Tear Sheet — `HIVE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.461`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+23.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.27x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.97%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`58.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.9% / -7.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-12-29 00:00` | `2025-01-02 00:00` | Live | `$0.4026` | `$0.4369` | **+8.50%** | **+8.16%** | +54.2% | -23.8% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-01-05 00:00` | `2025-01-09 00:00` | Live | `$0.4283` | `$0.4647` | **+8.50%** | **+8.16%** | +45.0% | -17.0% | `shelf_target_reclaim` |
| 3 | Book 3 | `2025-04-24 08:00` | `2025-04-24 23:00` | 15.0h | `$0.2396` | `$0.2496` | **+4.17%** | **+4.08%** | +4.3% | -0.5% | `target_reclaim` |
| 4 | Book 3 | `2025-05-04 00:00` | `2025-05-06 21:00` | 69.0h | `$0.2488` | `$0.2284` | **-8.23%** | **-8.59%** | +4.4% | -8.1% | `stop_loss` |
| 5 | Book 3 | `2025-07-23 21:00` | `2025-07-24 00:00` | 3.0h | `$0.2419` | `$0.2585` | **+6.85%** | **+6.62%** | +10.4% | -0.1% | `target_reclaim` |
| 6 | Book 3 | `2026-09-14 00:00` | `2026-09-15 00:00` | 24.0h | `$0.0484` | `$0.0548` | **+13.18%** | **+12.38%** | +28.3% | -0.2% | `target_reclaim` |
| 7 | Book 3 | `2026-09-15 07:00` | `2026-09-18 07:00` | 72.0h | `$0.0509` | `$0.0513` | **+0.69%** | **+0.69%** | +4.1% | -3.1% | `time_expiry` |
| 8 | Book 4 | `2026-09-26 05:00` | `2026-10-03 05:00` | 168.0h | `$0.0599` | `$0.0564` | **-7.46%** | **-7.71%** | +0.8% | -9.9% | `stagnation_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+23.1%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-7.7%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+0.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `HIVE`

* **Total Candidate Breakouts Filtered (Vetoed):** `54`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `47` (87.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `3`
* **Saved Capital Losses Avoided:** `+552.7%`
* **Missed Upside Forgone:** `-110.7%`
* **Net Veto Alpha:** `+442.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `23` | `42.6%` |
| `Core 1: Macro Bear Veto` | `21` | `38.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `13.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `5.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*