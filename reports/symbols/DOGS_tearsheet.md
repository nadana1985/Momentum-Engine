# Kronos V12: Institutional Symbol Tear Sheet — `DOGS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `12` (`12` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `12` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.893`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+23.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.26x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.92%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`40.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.4% / -8.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-11-10 04:00` | `2024-11-10 21:00` | 17.0h | `$0.0008` | `$0.0007` | **-8.23%** | **-8.59%** | +4.7% | -12.9% | `stop_loss` |
| 2 | Book 3 | `2024-12-02 04:00` | `2024-12-05 04:00` | 72.0h | `$0.0007` | `$0.0008` | **+7.87%** | **+7.58%** | +12.2% | -6.3% | `time_expiry` |
| 3 | Book 3 | `2024-12-09 21:00` | `2024-12-09 22:00` | 1.0h | `$0.0008` | `$0.0007` | **-8.23%** | **-8.59%** | +4.2% | -20.5% | `stop_loss` |
| 4 | Book 3 | `2025-04-24 08:00` | `2025-04-24 11:00` | 3.0h | `$0.0001` | `$0.0001` | **+4.17%** | **+4.08%** | +5.3% | -0.5% | `target_reclaim` |
| 5 | Book 3 | `2025-04-25 15:00` | `2025-04-26 01:00` | 10.0h | `$0.0001` | `$0.0002` | **+4.17%** | **+4.08%** | +7.5% | -0.8% | `target_reclaim` |
| 6 | Book 3 | `2025-04-27 04:00` | `2025-04-30 04:00` | 72.0h | `$0.0001` | `$0.0001` | **+1.15%** | **+1.15%** | +6.1% | -5.7% | `time_expiry` |
| 7 | Book 3 | `2025-05-02 12:00` | `2025-05-03 16:00` | 28.0h | `$0.0002` | `$0.0001` | **-8.23%** | **-8.59%** | +3.4% | -8.3% | `stop_loss` |
| 8 | Book 3 | `2025-07-18 20:00` | `2025-07-20 16:00` | 44.0h | `$0.0002` | `$0.0002` | **+11.54%** | **+10.92%** | +14.1% | -1.2% | `target_reclaim` |
| 9 | Book 5 (Shelf Absorption Squeeze) | `2026-05-05 02:00` | `2026-05-09 02:00` | Live | `$0.0001` | `$0.0001` | **+8.50%** | **+8.16%** | +48.8% | -16.1% | `shelf_target_reclaim` |
| 10 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0000` | `$0.0000` | **+4.17%** | **+4.08%** | +18.3% | -9.9% | `target_reclaim` |
| 11 | Book 4 | `2026-08-31 18:00` | `2026-09-07 18:00` | 168.0h | `$0.0000` | `$0.0000` | **+0.87%** | **+0.87%** | +1.6% | -14.0% | `stagnation_cut` |
| 12 | Book 3 | `2026-09-09 22:00` | `2026-09-11 03:00` | 29.0h | `$0.0000` | `$0.0000` | **+8.18%** | **+7.86%** | +10.9% | -5.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+31.0%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_expiry` | `2` | `100.0%` | **`+8.7%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stagnation_cut` | `1` | `100.0%` | **`+0.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `DOGS`

* **Total Candidate Breakouts Filtered (Vetoed):** `51`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `42` (82.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+713.3%`
* **Missed Upside Forgone:** `-595.5%`
* **Net Veto Alpha:** `+117.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `23` | `45.1%` |
| `Core 1: Macro Bear Veto` | `12` | `23.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `9` | `17.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `13.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*