# Kronos V12: Institutional Symbol Tear Sheet — `GRIFFAIN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.903`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+67.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.96x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+6.70%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`35.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.5% / -11.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-01-03 15:00` | `2025-01-07 15:00` | Live | `$0.3923` | `$0.4256` | **+8.50%** | **+8.16%** | +51.2% | -46.1% | `shelf_target_reclaim` |
| 2 | Book 3 | `2025-04-27 01:00` | `2025-04-28 06:00` | 29.0h | `$0.0630` | `$0.0732` | **+16.23%** | **+15.04%** | +17.6% | -7.6% | `target_reclaim` |
| 3 | Book 3 | `2025-05-01 19:00` | `2025-05-04 03:00` | 56.0h | `$0.0684` | `$0.0627` | **-8.23%** | **-8.59%** | +8.1% | -9.0% | `stop_loss` |
| 4 | Book 3 | `2025-05-15 23:00` | `2025-05-16 20:00` | 21.0h | `$0.1067` | `$0.0979` | **-8.23%** | **-8.59%** | +7.6% | -8.1% | `stop_loss` |
| 5 | Book 3 | `2026-08-22 05:00` | `2026-08-22 07:00` | 2.0h | `$0.0127` | `$0.0138` | **+8.70%** | **+8.34%** | +10.4% | -16.3% | `target_reclaim` |
| 6 | Book 3 | `2026-09-12 09:00` | `2026-09-12 14:00` | 5.0h | `$0.0132` | `$0.0148` | **+11.96%** | **+11.29%** | +14.3% | -5.9% | `target_reclaim` |
| 7 | Book 3 | `2026-09-12 21:00` | `2026-09-12 22:00` | 1.0h | `$0.0153` | `$0.0160` | **+4.83%** | **+4.72%** | +8.5% | -0.9% | `target_reclaim` |
| 8 | Book 4 | `2026-09-16 18:00` | `2026-09-22 14:00` | 140.0h | `$0.0137` | `$0.0164` | **+16.51%** | **+15.46%** | +21.1% | -6.4% | `target_reclaim` |
| 9 | Book 3 | `2026-09-28 09:00` | `2026-09-28 21:00` | 12.0h | `$0.0161` | `$0.0170` | **+5.56%** | **+5.41%** | +7.5% | -0.2% | `target_reclaim` |
| 10 | Book 3 | `2026-10-07 12:00` | `2026-10-09 19:00` | 55.0h | `$0.0160` | `$0.0188` | **+17.11%** | **+15.79%** | +49.0% | -11.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `7` | `100.0%` | **`+76.1%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `GRIFFAIN`

* **Total Candidate Breakouts Filtered (Vetoed):** `92`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `72` (78.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+1,342.4%`
* **Missed Upside Forgone:** `-741.4%`
* **Net Veto Alpha:** `+601.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `52` | `56.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `20` | `21.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `17` | `18.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `3.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*