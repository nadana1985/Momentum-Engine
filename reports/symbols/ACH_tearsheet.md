# Kronos V12: Institutional Symbol Tear Sheet — `ACH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `23` (`23` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `23` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`56.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.956`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+57.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.77x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+2.48%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-23.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`47.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.4% / -6.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-04-03 09:00` | `2023-04-07 09:00` | Live | `$0.0344` | `$0.0373` | **+8.50%** | **+8.16%** | +17.7% | -15.9% | `shelf_target_reclaim` |
| 2 | Book 3 | `2023-11-12 00:00` | `2023-11-14 00:00` | 48.0h | `$0.0208` | `$0.0191` | **-8.23%** | **-8.59%** | +5.1% | -8.6% | `stop_loss` |
| 3 | Book 2 | `2024-01-29 16:00` | `2024-01-31 16:00` | 48.0h | `$0.0193` | `$0.0189` | **-1.94%** | **-1.96%** | +3.9% | -3.8% | `fast_decay_cut` |
| 4 | Book 4 | `2024-02-14 04:00` | `2024-02-20 05:00` | 145.0h | `$0.0200` | `$0.0240` | **+28.71%** | **+25.74%** | +27.3% | -1.1% | `target_reclaim` |
| 5 | Book 3 | `2024-02-29 13:00` | `2024-03-03 07:00` | 66.0h | `$0.0288` | `$0.0265` | **-8.23%** | **-8.59%** | +7.7% | -11.8% | `stop_loss` |
| 6 | Book 3 | `2024-03-12 08:00` | `2024-03-12 10:00` | 2.0h | `$0.0352` | `$0.0367` | **+4.17%** | **+4.08%** | +6.3% | -1.0% | `target_reclaim` |
| 7 | Book 3 | `2024-04-23 04:00` | `2024-04-26 04:00` | 72.0h | `$0.0352` | `$0.0351` | **-0.44%** | **-0.44%** | +6.2% | -6.2% | `time_expiry` |
| 8 | Book 3 | `2024-05-23 13:00` | `2024-05-26 13:00` | 72.0h | `$0.0298` | `$0.0291` | **-2.35%** | **-2.38%** | +3.6% | -5.3% | `time_expiry` |
| 9 | Book 3 | `2024-07-23 04:00` | `2024-07-26 04:00` | 72.0h | `$0.0238` | `$0.0253` | **+6.28%** | **+6.09%** | +8.9% | -4.4% | `time_expiry` |
| 10 | Book 3 | `2024-10-31 14:00` | `2024-11-02 02:00` | 36.0h | `$0.0202` | `$0.0191` | **-5.38%** | **-5.54%** | +0.8% | -7.7% | `stall_bailout` |
| 11 | Book 3 | `2024-11-14 23:00` | `2024-11-17 00:00` | 49.0h | `$0.0212` | `$0.0244` | **+15.03%** | **+14.00%** | +15.5% | -4.7% | `target_reclaim` |
| 12 | Book 3 | `2024-12-06 12:00` | `2024-12-09 08:00` | 68.0h | `$0.0364` | `$0.0334` | **-8.23%** | **-8.59%** | +6.0% | -9.5% | `stop_loss` |
| 13 | Book 5 (Shelf Absorption Squeeze) | `2025-01-27 01:00` | `2025-01-31 01:00` | Live | `$0.0270` | `$0.0293` | **+8.50%** | **+8.16%** | +99.0% | -15.3% | `shelf_target_reclaim` |
| 14 | Book 3 | `2025-01-27 07:00` | `2025-01-27 10:00` | 3.0h | `$0.0266` | `$0.0294` | **+10.72%** | **+10.18%** | +13.0% | -4.0% | `target_reclaim` |
| 15 | Book 3 | `2025-01-28 18:00` | `2025-01-29 06:00` | 12.0h | `$0.0305` | `$0.0341` | **+11.66%** | **+11.03%** | +21.9% | -4.1% | `target_reclaim` |
| 16 | Book 5 (Shelf Absorption Squeeze) | `2025-02-16 10:00` | `2025-02-20 10:00` | Live | `$0.0262` | `$0.0284` | **+8.50%** | **+8.16%** | +41.0% | -12.5% | `shelf_target_reclaim` |
| 17 | Book 3 | `2025-04-15 12:00` | `2025-04-15 15:00` | 3.0h | `$0.0274` | `$0.0285` | **+4.17%** | **+4.08%** | +4.5% | -2.0% | `target_reclaim` |
| 18 | Book 3 | `2025-04-21 02:00` | `2025-04-21 17:00` | 15.0h | `$0.0284` | `$0.0261` | **-8.23%** | **-8.59%** | +5.2% | -8.6% | `stop_loss` |
| 19 | Book 3 | `2025-04-27 12:00` | `2025-04-30 12:00` | 72.0h | `$0.0278` | `$0.0260` | **-6.17%** | **-6.37%** | +1.5% | -7.5% | `time_expiry` |
| 20 | Book 3 | `2025-05-12 18:00` | `2025-05-15 07:00` | 61.0h | `$0.0283` | `$0.0260` | **-8.23%** | **-8.59%** | +5.7% | -8.6% | `stop_loss` |
| 21 | Book 3 | `2025-07-18 20:00` | `2025-07-20 04:00` | 32.0h | `$0.0220` | `$0.0232` | **+5.66%** | **+5.51%** | +6.5% | -1.1% | `target_reclaim` |
| 22 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0045` | `$0.0049` | **+9.97%** | **+9.51%** | +20.4% | -5.9% | `target_reclaim` |
| 23 | Book 3 | `2026-09-28 06:00` | `2026-10-01 06:00` | 72.0h | `$0.0060` | `$0.0061` | **+1.99%** | **+1.97%** | +4.4% | -4.1% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+84.1%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `time_expiry` | `5` | `40.0%` | **`-1.1%`** |
| `shelf_target_reclaim` | `3` | `100.0%` | **`+24.5%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-2.0%`** |
| `stall_bailout` | `1` | `0.0%` | **`-5.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `ACH`

* **Total Candidate Breakouts Filtered (Vetoed):** `738`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `513` (69.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `78`
* **Saved Capital Losses Avoided:** `+6,428.6%`
* **Missed Upside Forgone:** `-2,212.4%`
* **Net Veto Alpha:** `+4,216.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `514` | `69.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `112` | `15.2%` |
| `Core 1: Macro Bear Veto` | `67` | `9.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `44` | `6.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*