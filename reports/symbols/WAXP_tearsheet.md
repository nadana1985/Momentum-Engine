# Kronos V12: Institutional Symbol Tear Sheet — `WAXP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `11` (`11` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`54.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.004`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+31.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.37x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.84%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-19.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`95.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.4% / -8.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$0.0674` | `$0.0691` | **+2.57%** | **+2.54%** | +8.1% | -17.8% | `time_expiry` |
| 2 | Book 3 | `2023-12-26 17:00` | `2023-12-29 17:00` | 72.0h | `$0.0673` | `$0.0702` | **+4.29%** | **+4.20%** | +13.4% | -6.6% | `time_expiry` |
| 3 | Book 4 | `2024-02-20 23:00` | `2024-02-28 13:00` | 182.0h | `$0.0647` | `$0.0776` | **+26.29%** | **+23.77%** | +25.0% | -7.1% | `target_reclaim` |
| 4 | Book 3 | `2024-03-01 07:00` | `2024-03-03 07:00` | 48.0h | `$0.0863` | `$0.0792` | **-8.23%** | **-8.59%** | +3.9% | -16.8% | `stop_loss` |
| 5 | Book 3 | `2024-05-30 06:00` | `2024-06-02 06:00` | 72.0h | `$0.0658` | `$0.0643` | **-2.26%** | **-2.29%** | +1.8% | -3.2% | `time_expiry` |
| 6 | Book 3 | `2024-08-26 20:00` | `2024-08-27 22:00` | 26.0h | `$0.0333` | `$0.0305` | **-8.23%** | **-8.59%** | +2.2% | -8.9% | `stop_loss` |
| 7 | Book 4 | `2024-11-18 15:00` | `2024-11-24 04:00` | 133.0h | `$0.0422` | `$0.0507` | **+24.85%** | **+22.45%** | +22.2% | -8.7% | `target_reclaim` |
| 8 | Book 3 | `2024-11-26 10:00` | `2024-11-27 20:00` | 34.0h | `$0.0526` | `$0.0553` | **+4.99%** | **+4.87%** | +7.0% | -4.6% | `target_reclaim` |
| 9 | Book 3 | `2025-05-30 00:00` | `2025-05-31 00:00` | 24.0h | `$0.0223` | `$0.0205` | **-8.23%** | **-8.59%** | +5.5% | -8.8% | `stop_loss` |
| 10 | Book 3 | `2025-07-22 04:00` | `2025-07-22 09:00` | 5.0h | `$0.0238` | `$0.0249` | **+4.60%** | **+4.50%** | +9.0% | -0.0% | `target_reclaim` |
| 11 | Book 4 | `2026-09-25 00:00` | `2026-10-11 00:00` | 384.0h | `$0.0061` | `$0.0058` | **-2.96%** | **-3.05%** | +16.4% | -10.1% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+55.6%`** |
| `time_expiry` | `4` | `50.0%` | **`+1.4%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `WAXP`

* **Total Candidate Breakouts Filtered (Vetoed):** `477`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `162` (34.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `119`
* **Saved Capital Losses Avoided:** `+1,571.2%`
* **Missed Upside Forgone:** `-3,403.4%`
* **Net Veto Alpha:** `+-1,832.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `359` | `75.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `49` | `10.3%` |
| `Core 1: Macro Bear Veto` | `42` | `8.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `27` | `5.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*