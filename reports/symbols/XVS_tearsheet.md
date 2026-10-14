# Kronos V12: Institutional Symbol Tear Sheet — `XVS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `14` (`14` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `14` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`42.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.026`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+1.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.01x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.08%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-33.7%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`67.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.4% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-09-29 23:00` | `2023-10-03 23:00` | Live | `$4.4832` | `$4.8642` | **+8.50%** | **+8.16%** | +8.9% | -10.7% | `shelf_target_reclaim` |
| 2 | Book 3 | `2023-10-26 14:00` | `2023-10-27 06:00` | 16.0h | `$5.3377` | `$5.6610` | **+6.06%** | **+5.88%** | +6.5% | -0.7% | `target_reclaim` |
| 3 | Book 3 | `2023-10-31 08:00` | `2023-11-03 08:00` | 72.0h | `$5.3377` | `$5.3286` | **-0.17%** | **-0.17%** | +5.7% | -6.1% | `time_expiry` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2023-11-05 06:00` | `2023-11-09 06:00` | Live | `$6.4989` | `$7.0513` | **+8.50%** | **+8.16%** | +15.7% | -14.6% | `shelf_target_reclaim` |
| 5 | Book 3 | `2023-12-24 14:00` | `2023-12-25 05:00` | 15.0h | `$11.0355` | `$12.5480` | **+13.71%** | **+12.84%** | +21.9% | -2.9% | `target_reclaim` |
| 6 | Book 3 | `2023-12-26 17:00` | `2023-12-29 01:00` | 56.0h | `$12.8064` | `$11.7524` | **-8.23%** | **-8.59%** | +6.4% | -8.2% | `stop_loss` |
| 7 | Book 3 | `2024-04-02 00:00` | `2024-04-02 10:00` | 10.0h | `$16.1414` | `$14.8130` | **-8.23%** | **-8.59%** | +2.7% | -8.4% | `stop_loss` |
| 8 | Book 3 | `2024-06-07 18:00` | `2024-06-10 18:00` | 72.0h | `$9.9853` | `$9.4832` | **-5.03%** | **-5.16%** | +13.0% | -6.5% | `time_expiry` |
| 9 | Book 3 | `2024-08-01 16:00` | `2024-08-03 15:00` | 47.0h | `$7.0539` | `$6.4734` | **-8.23%** | **-8.59%** | +8.9% | -9.9% | `stop_loss` |
| 10 | Book 3 | `2024-11-12 10:00` | `2024-11-12 22:00` | 12.0h | `$7.4232` | `$7.8190` | **+5.33%** | **+5.19%** | +7.3% | -1.5% | `target_reclaim` |
| 11 | Book 3 | `2024-12-02 17:00` | `2024-12-03 03:00` | 10.0h | `$9.8234` | `$10.3840` | **+5.71%** | **+5.55%** | +5.7% | -2.2% | `target_reclaim` |
| 12 | Book 3 | `2025-07-23 13:00` | `2025-07-26 13:00` | 72.0h | `$6.6668` | `$6.5655` | **-1.52%** | **-1.53%** | +3.8% | -7.9% | `time_expiry` |
| 13 | Book 3 | `2025-10-10 15:00` | `2025-10-10 20:00` | 5.0h | `$6.6634` | `$6.1150` | **-8.23%** | **-8.59%** | +3.0% | -12.4% | `stop_loss` |
| 14 | Book 4 | `2026-01-10 13:00` | `2026-01-28 02:00` | 421.0h | `$5.3751` | `$5.0784` | **-3.37%** | **-3.42%** | +8.4% | -8.2% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `target_reclaim` | `4` | `100.0%` | **`+29.5%`** |
| `time_expiry` | `3` | `0.0%` | **`-6.9%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `structural_stop` | `1` | `0.0%` | **`-3.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `XVS`

* **Total Candidate Breakouts Filtered (Vetoed):** `876`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `657` (75.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+6,401.9%`
* **Missed Upside Forgone:** `-589.3%`
* **Net Veto Alpha:** `+5,812.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `417` | `47.6%` |
| `Core 1: Macro Bear Veto` | `356` | `40.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `91` | `10.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `11` | `1.3%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*