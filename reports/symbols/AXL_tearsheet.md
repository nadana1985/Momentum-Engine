# Kronos V12: Institutional Symbol Tear Sheet — `AXL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `11` (`11` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`45.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.560`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+12.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.13x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.09%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-5.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`46.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.9% / -10.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-08-26 08:00` | `2024-08-27 10:00` | 26.0h | `$0.6341` | `$0.5819` | **-8.23%** | **-8.59%** | +1.4% | -8.4% | `stop_loss` |
| 2 | Book 3 | `2024-12-02 08:00` | `2024-12-02 21:00` | 13.0h | `$0.9414` | `$1.0233` | **+8.70%** | **+8.34%** | +10.7% | -0.6% | `target_reclaim` |
| 3 | Book 3 | `2024-12-03 13:00` | `2024-12-03 20:00` | 7.0h | `$1.0018` | `$1.0889` | **+8.70%** | **+8.34%** | +10.2% | -2.0% | `target_reclaim` |
| 4 | Book 3 | `2024-12-05 01:00` | `2024-12-08 01:00` | 72.0h | `$1.0284` | `$1.0316` | **+0.31%** | **+0.31%** | +7.3% | -2.8% | `time_expiry` |
| 5 | Book 3 | `2025-05-12 18:00` | `2025-05-15 18:00` | 72.0h | `$0.4026` | `$0.3827` | **-4.93%** | **-5.06%** | +6.5% | -7.6% | `time_expiry` |
| 6 | Book 5 (Shelf Absorption Squeeze) | `2025-06-10 05:00` | `2025-06-14 05:00` | Live | `$0.4426` | `$0.4802` | **+8.50%** | **+8.16%** | +4.5% | -33.8% | `shelf_target_reclaim` |
| 7 | Book 3 | `2025-07-12 04:00` | `2025-07-15 04:00` | 72.0h | `$0.3543` | `$0.3457` | **-2.42%** | **-2.45%** | +5.6% | -4.1% | `time_expiry` |
| 8 | Book 3 | `2025-07-25 03:00` | `2025-07-28 03:00` | 72.0h | `$0.4186` | `$0.4068` | **-2.83%** | **-2.87%** | +7.3% | -4.4% | `time_expiry` |
| 9 | Book 5 (Shelf Absorption Squeeze) | `2025-12-09 22:00` | `2025-12-13 22:00` | Live | `$0.1222` | `$0.1326` | **+8.50%** | **+8.16%** | +21.2% | -47.1% | `shelf_target_reclaim` |
| 10 | Book 3 | `2026-09-01 12:00` | `2026-09-04 12:00` | 72.0h | `$0.0420` | `$0.0418` | **-0.37%** | **-0.37%** | +4.6% | -2.5% | `time_expiry` |
| 11 | Book 2 | `2026-09-15 02:00` | `2026-09-15 10:00` | 8.0h | `$0.0462` | `$0.0454` | **-2.01%** | **-2.02%** | +18.4% | -2.8% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `5` | `20.0%` | **`-10.4%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `breakeven_ratchet` | `1` | `0.0%` | **`-2.0%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `AXL`

* **Total Candidate Breakouts Filtered (Vetoed):** `426`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `260` (61.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+4,045.8%`
* **Missed Upside Forgone:** `-260.5%`
* **Net Veto Alpha:** `+3,785.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `379` | `89.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `25` | `5.9%` |
| `Core 1: Macro Bear Veto` | `19` | `4.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*