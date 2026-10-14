# Kronos V12: Institutional Symbol Tear Sheet — `SPELL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `21` (`21` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `21` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`61.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.201`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+54.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.72x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+2.59%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-16.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`63.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.7% / -5.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-02-05 12:00` | `2023-02-08 12:00` | 72.0h | `$0.0008` | `$0.0008` | **+2.46%** | **+2.43%** | +6.0% | -3.0% | `time_expiry` |
| 2 | Book 4 | `2023-04-04 20:00` | `2023-04-11 20:00` | 168.0h | `$0.0008` | `$0.0008` | **-7.07%** | **-7.29%** | +4.4% | -10.1% | `stagnation_cut` |
| 3 | Book 4 | `2023-09-19 09:00` | `2023-10-02 18:00` | 321.0h | `$0.0006` | `$0.0005` | **-8.57%** | **-9.30%** | +12.9% | -17.1% | `structural_stop` |
| 4 | Book 3 | `2023-10-26 14:00` | `2023-10-27 21:00` | 31.0h | `$0.0005` | `$0.0005` | **+4.17%** | **+4.08%** | +4.6% | -1.7% | `target_reclaim` |
| 5 | Book 3 | `2023-10-31 15:00` | `2023-11-01 21:00` | 30.0h | `$0.0005` | `$0.0005` | **+7.78%** | **+7.49%** | +8.0% | -0.7% | `target_reclaim` |
| 6 | Book 3 | `2023-11-09 16:00` | `2023-11-10 09:00` | 17.0h | `$0.0005` | `$0.0005` | **+8.29%** | **+7.96%** | +9.3% | -6.1% | `target_reclaim` |
| 7 | Book 3 | `2023-11-25 04:00` | `2023-11-28 04:00` | 72.0h | `$0.0006` | `$0.0006` | **-2.16%** | **-2.19%** | +14.8% | -3.9% | `time_expiry` |
| 8 | Book 3 | `2024-05-28 12:00` | `2024-05-31 12:00` | 72.0h | `$0.0010` | `$0.0010` | **-1.54%** | **-1.55%** | +4.4% | -6.6% | `time_expiry` |
| 9 | Book 3 | `2024-07-21 18:00` | `2024-07-21 20:00` | 2.0h | `$0.0007` | `$0.0007` | **+4.17%** | **+4.08%** | +4.5% | -2.8% | `target_reclaim` |
| 10 | Book 3 | `2024-09-22 22:00` | `2024-09-23 03:00` | 5.0h | `$0.0005` | `$0.0006` | **+5.52%** | **+5.37%** | +5.6% | -0.6% | `target_reclaim` |
| 11 | Book 3 | `2024-10-15 11:00` | `2024-10-18 11:00` | 72.0h | `$0.0006` | `$0.0006` | **-1.66%** | **-1.68%** | +3.6% | -7.9% | `time_expiry` |
| 12 | Book 3 | `2024-11-10 01:00` | `2024-11-10 05:00` | 4.0h | `$0.0007` | `$0.0008` | **+17.12%** | **+15.80%** | +20.5% | -0.9% | `target_reclaim` |
| 13 | Book 3 | `2024-11-18 19:00` | `2024-11-21 19:00` | 72.0h | `$0.0008` | `$0.0008` | **-0.57%** | **-0.57%** | +5.9% | -7.1% | `time_expiry` |
| 14 | Book 5 (Shelf Absorption Squeeze) | `2025-01-17 21:00` | `2025-01-21 21:00` | Live | `$0.0009` | `$0.0010` | **+8.50%** | **+8.16%** | +105.5% | -16.3% | `shelf_target_reclaim` |
| 15 | Book 3 | `2025-01-19 11:00` | `2025-01-19 16:00` | 5.0h | `$0.0009` | `$0.0010` | **+7.52%** | **+7.26%** | +9.7% | -1.1% | `target_reclaim` |
| 16 | Book 5 (Shelf Absorption Squeeze) | `2025-01-23 17:00` | `2025-01-27 17:00` | Live | `$0.0009` | `$0.0010` | **+8.50%** | **+8.16%** | +92.8% | -12.5% | `shelf_target_reclaim` |
| 17 | Book 3 | `2025-07-18 20:00` | `2025-07-20 08:00` | 36.0h | `$0.0005` | `$0.0006` | **+4.17%** | **+4.08%** | +4.8% | -1.5% | `target_reclaim` |
| 18 | Book 3 | `2025-07-23 16:00` | `2025-07-26 16:00` | 72.0h | `$0.0005` | `$0.0005` | **+0.10%** | **+0.10%** | +2.3% | -7.1% | `time_expiry` |
| 19 | Book 3 | `2025-08-07 09:00` | `2025-08-10 09:00` | 72.0h | `$0.0005` | `$0.0005` | **-0.37%** | **-0.37%** | +4.3% | -1.7% | `time_expiry` |
| 20 | Book 2 | `2026-09-20 16:00` | `2026-09-22 04:00` | 36.0h | `$0.0001` | `$0.0001` | **-1.74%** | **-1.75%** | +0.4% | -5.7% | `stall_bailout` |
| 21 | Book 3 | `2026-09-23 14:00` | `2026-09-25 10:00` | 44.0h | `$0.0001` | `$0.0001` | **+4.17%** | **+4.08%** | +4.4% | -1.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `9` | `100.0%` | **`+60.2%`** |
| `time_expiry` | `7` | `28.6%` | **`-3.8%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-7.3%`** |
| `structural_stop` | `1` | `0.0%` | **`-9.3%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `SPELL`

* **Total Candidate Breakouts Filtered (Vetoed):** `173`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `126` (72.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+1,429.3%`
* **Missed Upside Forgone:** `-631.9%`
* **Net Veto Alpha:** `+797.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `63` | `36.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `48` | `27.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `35` | `20.2%` |
| `Core 1: Macro Bear Veto` | `24` | `13.9%` |
| `Core 0: Zero-Tolerance Data Firewall` | `3` | `1.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*