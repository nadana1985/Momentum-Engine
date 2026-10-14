# Kronos V12: Institutional Symbol Tear Sheet — `TURBO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `15` (`15` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.200`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+55.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.75x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.72%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-19.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`31.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.9% / -11.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-06-19 22:00` | `2024-06-23 22:00` | Live | `$0.0046` | `$0.0050` | **+8.50%** | **+8.16%** | +29.6% | -41.5% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2024-07-19 19:00` | `2024-07-23 19:00` | Live | `$0.0051` | `$0.0055` | **+8.50%** | **+8.16%** | +36.5% | -31.9% | `shelf_target_reclaim` |
| 3 | Book 4 | `2024-09-17 17:00` | `2024-09-19 16:00` | 47.0h | `$0.0054` | `$0.0064` | **+11.03%** | **+10.53%** | +23.8% | -9.2% | `target_reclaim` |
| 4 | Book 3 | `2024-10-10 09:00` | `2024-10-11 19:00` | 34.0h | `$0.0064` | `$0.0074` | **+14.40%** | **+13.46%** | +14.7% | -5.1% | `target_reclaim` |
| 5 | Book 3 | `2024-12-09 21:00` | `2024-12-09 22:00` | 1.0h | `$0.0092` | `$0.0105` | **+14.20%** | **+13.28%** | +23.3% | -4.3% | `target_reclaim` |
| 6 | Book 3 | `2024-12-12 10:00` | `2024-12-13 15:00` | 29.0h | `$0.0126` | `$0.0116` | **-8.23%** | **-8.59%** | +3.2% | -8.8% | `stop_loss` |
| 7 | Book 4 | `2025-04-24 16:00` | `2025-04-24 21:00` | 5.0h | `$0.0051` | `$0.0043` | **-10.01%** | **-10.85%** | +0.3% | -15.6% | `structural_stop` |
| 8 | Book 3 | `2025-05-06 10:00` | `2025-05-08 16:00` | 54.0h | `$0.0054` | `$0.0062` | **+14.45%** | **+13.50%** | +16.6% | -6.4% | `target_reclaim` |
| 9 | Book 3 | `2025-06-11 22:00` | `2025-06-12 20:00` | 22.0h | `$0.0043` | `$0.0039` | **-8.23%** | **-8.59%** | +0.7% | -10.4% | `stop_loss` |
| 10 | Book 4 | `2025-07-13 18:00` | `2025-07-14 04:00` | 10.0h | `$0.0045` | `$0.0055` | **+23.71%** | **+21.63%** | +20.7% | -3.9% | `target_reclaim` |
| 11 | Book 3 | `2025-08-18 01:00` | `2025-08-19 19:00` | 42.0h | `$0.0044` | `$0.0040` | **-8.23%** | **-8.59%** | +1.9% | -8.0% | `stop_loss` |
| 12 | Book 3 | `2025-10-28 02:00` | `2025-10-30 04:00` | 50.0h | `$0.0025` | `$0.0023` | **-8.23%** | **-8.59%** | +2.5% | -8.3% | `stop_loss` |
| 13 | Book 5 (Shelf Absorption Squeeze) | `2025-11-27 19:00` | `2025-12-01 19:00` | Live | `$0.0021` | `$0.0023` | **+8.50%** | **+8.16%** | +22.5% | -19.8% | `shelf_target_reclaim` |
| 14 | Book 2 | `2026-05-05 07:00` | `2026-05-07 14:00` | 55.0h | `$0.0013` | `$0.0013` | **-1.24%** | **-1.25%** | +5.8% | -2.2% | `fast_decay_cut` |
| 15 | Book 3 | `2026-09-23 15:00` | `2026-09-24 14:00` | 23.0h | `$0.0010` | `$0.0011` | **+5.44%** | **+5.30%** | +5.7% | -1.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+77.7%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `shelf_target_reclaim` | `3` | `100.0%` | **`+24.5%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-10.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `TURBO`

* **Total Candidate Breakouts Filtered (Vetoed):** `823`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `477` (58.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `185`
* **Saved Capital Losses Avoided:** `+5,947.3%`
* **Missed Upside Forgone:** `-5,957.3%`
* **Net Veto Alpha:** `+-10.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `671` | `81.5%` |
| `Core 1: Macro Bear Veto` | `79` | `9.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `41` | `5.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `32` | `3.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*