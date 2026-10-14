# Kronos V12: Institutional Symbol Tear Sheet — `C98`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `25` (`25` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `25` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`52.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.350`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+28.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.33x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.15%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-30.3%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`43.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.3% / -7.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2022-03-28 23:00` | `2022-03-29 12:00` | 13.0h | `$1.6231` | `$1.6913` | **+4.20%** | **+4.11%** | +4.6% | -2.9% | `target_reclaim` |
| 2 | Book 2 | `2022-10-28 13:00` | `2022-11-01 13:00` | 96.0h | `$0.3206` | `$0.3150` | **-2.15%** | **-2.17%** | +16.0% | -2.1% | `breakeven_ratchet` |
| 3 | Book 3 | `2023-01-14 09:00` | `2023-01-17 09:00` | 72.0h | `$0.2217` | `$0.2194` | **-1.04%** | **-1.05%** | +4.2% | -7.9% | `time_expiry` |
| 4 | Book 3 | `2023-01-25 00:00` | `2023-01-25 15:00` | 15.0h | `$0.2275` | `$0.2381` | **+4.66%** | **+4.56%** | +4.7% | -2.7% | `target_reclaim` |
| 5 | Book 3 | `2023-02-09 22:00` | `2023-02-12 22:00` | 72.0h | `$0.2494` | `$0.2576` | **+3.27%** | **+3.22%** | +8.9% | -5.8% | `time_expiry` |
| 6 | Book 3 | `2023-07-05 10:00` | `2023-07-07 00:00` | 38.0h | `$0.1609` | `$0.1477` | **-8.23%** | **-8.59%** | +5.1% | -9.4% | `stop_loss` |
| 7 | Book 2 | `2023-07-13 16:00` | `2023-07-15 16:00` | 48.0h | `$0.1557` | `$0.1533` | **-1.84%** | **-1.86%** | +4.5% | -5.1% | `fast_decay_cut` |
| 8 | Book 5 (Shelf Absorption Squeeze) | `2023-08-08 10:00` | `2023-08-12 10:00` | Live | `$0.1466` | `$0.1591` | **+8.50%** | **+8.16%** | +7.7% | -27.5% | `shelf_target_reclaim` |
| 9 | Book 3 | `2023-11-03 00:00` | `2023-11-06 00:00` | 72.0h | `$0.1679` | `$0.1808` | **+7.71%** | **+7.43%** | +8.2% | -3.6% | `time_expiry` |
| 10 | Book 3 | `2023-11-09 13:00` | `2023-11-09 15:00` | 2.0h | `$0.1917` | `$0.2020` | **+5.39%** | **+5.25%** | +5.4% | -0.3% | `target_reclaim` |
| 11 | Book 3 | `2023-12-04 11:00` | `2023-12-05 00:00` | 13.0h | `$0.1842` | `$0.1972` | **+7.04%** | **+6.80%** | +9.3% | -5.0% | `target_reclaim` |
| 12 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$0.2041` | `$0.2189` | **+7.22%** | **+6.97%** | +12.2% | -6.4% | `time_expiry` |
| 13 | Book 3 | `2023-12-26 17:00` | `2023-12-29 00:00` | 55.0h | `$0.2953` | `$0.2710` | **-8.23%** | **-8.59%** | +7.3% | -9.2% | `stop_loss` |
| 14 | Book 3 | `2024-02-28 17:00` | `2024-02-28 20:00` | 3.0h | `$0.3502` | `$0.3806` | **+8.70%** | **+8.34%** | +13.9% | -8.0% | `target_reclaim` |
| 15 | Book 3 | `2024-03-03 07:00` | `2024-03-05 16:00` | 57.0h | `$0.3973` | `$0.3646` | **-8.23%** | **-8.59%** | +4.3% | -10.8% | `stop_loss` |
| 16 | Book 3 | `2024-06-07 18:00` | `2024-06-07 19:00` | 1.0h | `$0.2639` | `$0.2421` | **-8.23%** | **-8.59%** | +3.3% | -15.2% | `stop_loss` |
| 17 | Book 3 | `2024-10-23 14:00` | `2024-10-25 23:00` | 57.0h | `$0.1275` | `$0.1170` | **-8.23%** | **-8.59%** | +2.5% | -13.7% | `stop_loss` |
| 18 | Book 3 | `2024-11-13 04:00` | `2024-11-16 04:00` | 72.0h | `$0.1259` | `$0.1388` | **+10.18%** | **+9.70%** | +11.1% | -2.3% | `time_expiry` |
| 19 | Book 4 | `2024-11-23 07:00` | `2024-11-29 13:00` | 150.0h | `$0.1636` | `$0.1964` | **+45.34%** | **+38.46%** | +23.5% | -4.1% | `target_reclaim` |
| 20 | Book 3 | `2024-12-03 13:00` | `2024-12-03 15:00` | 2.0h | `$0.2191` | `$0.2282` | **+4.17%** | **+4.08%** | +8.3% | -2.5% | `target_reclaim` |
| 21 | Book 3 | `2025-05-14 08:00` | `2025-05-15 05:00` | 21.0h | `$0.0736` | `$0.0676` | **-8.23%** | **-8.59%** | +3.5% | -8.5% | `stop_loss` |
| 22 | Book 3 | `2025-07-14 14:00` | `2025-07-15 18:00` | 28.0h | `$0.0538` | `$0.0560` | **+4.17%** | **+4.08%** | +4.2% | -5.9% | `target_reclaim` |
| 23 | Book 3 | `2025-09-22 05:00` | `2025-09-22 06:00` | 1.0h | `$0.0503` | `$0.0462` | **-8.23%** | **-8.59%** | +2.8% | -11.7% | `stop_loss` |
| 24 | Book 3 | `2026-09-26 18:00` | `2026-09-28 03:00` | 33.0h | `$0.0173` | `$0.0158` | **-8.23%** | **-8.59%** | +5.0% | -8.3% | `stop_loss` |
| 25 | Book 3 | `2026-10-07 02:00` | `2026-10-08 16:00` | 38.0h | `$0.0169` | `$0.0155` | **-8.23%** | **-8.59%** | +3.1% | -9.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `9` | `0.0%` | **`-77.3%`** |
| `target_reclaim` | `8` | `100.0%` | **`+75.7%`** |
| `time_expiry` | `5` | `80.0%` | **`+26.3%`** |
| `breakeven_ratchet` | `1` | `0.0%` | **`-2.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.9%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `C98`

* **Total Candidate Breakouts Filtered (Vetoed):** `620`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `316` (51.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `117`
* **Saved Capital Losses Avoided:** `+4,935.6%`
* **Missed Upside Forgone:** `-3,024.7%`
* **Net Veto Alpha:** `+1,910.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `454` | `73.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `82` | `13.2%` |
| `Core 1: Macro Bear Veto` | `42` | `6.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `41` | `6.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*