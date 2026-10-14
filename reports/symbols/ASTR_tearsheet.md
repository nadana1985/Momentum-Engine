# Kronos V12: Institutional Symbol Tear Sheet — `ASTR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `22` (`22` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `22` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`59.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.504`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+36.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.44x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.65%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-15.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`72.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.4% / -9.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-02-15 04:00` | `2023-02-19 04:00` | Live | `$0.0840` | `$0.0911` | **+8.50%** | **+8.16%** | +26.4% | -28.9% | `shelf_target_reclaim` |
| 2 | Book 2 | `2023-04-10 10:00` | `2023-04-17 10:00` | 168.0h | `$0.0650` | `$0.0715` | **+10.79%** | **+10.29%** | +15.4% | -1.9% | `time_cap` |
| 3 | Book 4 | `2023-08-12 00:00` | `2023-08-17 21:00` | 141.0h | `$0.0600` | `$0.0510` | **-10.42%** | **-11.30%** | +5.4% | -23.7% | `structural_stop` |
| 4 | Book 4 | `2023-10-30 09:00` | `2023-11-06 09:00` | 168.0h | `$0.0547` | `$0.0570` | **+25.19%** | **+22.86%** | +5.0% | -6.1% | `stagnation_cut` |
| 5 | Book 3 | `2023-11-13 07:00` | `2023-11-13 23:00` | 16.0h | `$0.0751` | `$0.0689` | **-8.23%** | **-8.59%** | +2.3% | -9.9% | `stop_loss` |
| 6 | Book 3 | `2023-12-11 02:00` | `2023-12-11 07:00` | 5.0h | `$0.0666` | `$0.0744` | **+11.80%** | **+11.15%** | +13.3% | -1.1% | `target_reclaim` |
| 7 | Book 5 (Shelf Absorption Squeeze) | `2023-12-18 07:00` | `2023-12-22 07:00` | Live | `$0.1176` | `$0.1275` | **+8.50%** | **+8.16%** | +14.7% | -30.5% | `shelf_target_reclaim` |
| 8 | Book 3 | `2023-12-18 08:00` | `2023-12-18 09:00` | 1.0h | `$0.1176` | `$0.1079` | **-8.23%** | **-8.59%** | +12.2% | -14.2% | `stop_loss` |
| 9 | Book 3 | `2024-01-03 12:00` | `2024-01-03 16:00` | 4.0h | `$0.1607` | `$0.1747` | **+8.70%** | **+8.34%** | +11.2% | -13.9% | `target_reclaim` |
| 10 | Book 3 | `2024-06-07 18:00` | `2024-06-10 18:00` | 72.0h | `$0.0907` | `$0.0875` | **-3.52%** | **-3.58%** | +3.9% | -11.0% | `time_expiry` |
| 11 | Book 3 | `2024-11-11 05:00` | `2024-11-11 23:00` | 18.0h | `$0.0607` | `$0.0641` | **+5.47%** | **+5.32%** | +5.9% | -1.8% | `target_reclaim` |
| 12 | Book 3 | `2024-11-12 10:00` | `2024-11-14 15:00` | 53.0h | `$0.0607` | `$0.0557` | **-8.23%** | **-8.59%** | +5.7% | -8.6% | `stop_loss` |
| 13 | Book 3 | `2024-12-02 04:00` | `2024-12-03 05:00` | 25.0h | `$0.0808` | `$0.0861` | **+6.65%** | **+6.44%** | +7.6% | -6.2% | `target_reclaim` |
| 14 | Book 3 | `2025-05-12 18:00` | `2025-05-13 17:00` | 23.0h | `$0.0327` | `$0.0340` | **+4.17%** | **+4.08%** | +4.6% | -2.2% | `target_reclaim` |
| 15 | Book 3 | `2025-05-14 09:00` | `2025-05-15 13:00` | 28.0h | `$0.0332` | `$0.0304` | **-8.23%** | **-8.59%** | +1.8% | -8.4% | `stop_loss` |
| 16 | Book 3 | `2025-06-05 19:00` | `2025-06-07 07:00` | 36.0h | `$0.0267` | `$0.0278` | **+4.17%** | **+4.08%** | +4.2% | -4.6% | `target_reclaim` |
| 17 | Book 3 | `2025-07-01 18:00` | `2025-07-02 19:00` | 25.0h | `$0.0217` | `$0.0236` | **+8.70%** | **+8.34%** | +9.2% | -0.3% | `target_reclaim` |
| 18 | Book 3 | `2025-07-18 20:00` | `2025-07-20 05:00` | 33.0h | `$0.0255` | `$0.0265` | **+4.17%** | **+4.08%** | +4.6% | -2.2% | `target_reclaim` |
| 19 | Book 3 | `2025-09-22 00:00` | `2025-09-22 06:00` | 6.0h | `$0.0242` | `$0.0222` | **-8.23%** | **-8.59%** | +3.2% | -10.1% | `stop_loss` |
| 20 | Book 2 | `2026-05-05 01:00` | `2026-05-12 01:00` | 168.0h | `$0.0087` | `$0.0093` | **+7.14%** | **+6.93%** | +12.5% | -2.1% | `time_cap` |
| 21 | Book 3 | `2026-09-15 06:00` | `2026-09-16 10:00` | 28.0h | `$0.0068` | `$0.0062` | **-8.23%** | **-8.59%** | +7.9% | -8.4% | `stop_loss` |
| 22 | Book 4 | `2026-09-23 02:00` | `2026-10-11 00:00` | 430.0h | `$0.0073` | `$0.0069` | **-5.43%** | **-5.56%** | +7.6% | -11.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+51.8%`** |
| `stop_loss` | `6` | `0.0%` | **`-51.5%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `time_expiry` | `2` | `0.0%` | **`-9.1%`** |
| `time_cap` | `2` | `100.0%` | **`+17.2%`** |
| `stagnation_cut` | `1` | `100.0%` | **`+22.9%`** |
| `structural_stop` | `1` | `0.0%` | **`-11.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `ASTR`

* **Total Candidate Breakouts Filtered (Vetoed):** `658`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `397` (60.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `15`
* **Saved Capital Losses Avoided:** `+5,417.2%`
* **Missed Upside Forgone:** `-337.2%`
* **Net Veto Alpha:** `+5,080.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `435` | `66.1%` |
| `Core 1: Macro Bear Veto` | `160` | `24.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `37` | `5.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `26` | `4.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*