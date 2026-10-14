# Kronos V12: Institutional Symbol Tear Sheet — `FLOW`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `19` (`19` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `19` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`78.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.975`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+110.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`3.01x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+5.80%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-15.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`51.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.3% / -4.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-01-24 21:00` | `2023-01-27 21:00` | 72.0h | `$1.1221` | `$1.0773` | **-3.99%** | **-4.08%** | +4.0% | -7.0% | `time_expiry` |
| 2 | Book 2 | `2023-03-12 23:00` | `2023-03-19 23:00` | 168.0h | `$0.9333` | `$1.0733` | **+18.30%** | **+17.05%** | +18.7% | -2.6% | `time_cap` |
| 3 | Book 3 | `2023-04-14 15:00` | `2023-04-15 11:00` | 20.0h | `$1.0147` | `$1.0570` | **+4.17%** | **+4.08%** | +4.4% | -0.6% | `target_reclaim` |
| 4 | Book 3 | `2023-04-17 15:00` | `2023-04-18 11:00` | 20.0h | `$1.0176` | `$1.0600` | **+4.17%** | **+4.08%** | +4.9% | -0.4% | `target_reclaim` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2023-07-01 15:00` | `2023-07-05 15:00` | Live | `$0.6146` | `$0.6668` | **+8.50%** | **+8.16%** | +11.5% | -15.1% | `shelf_target_reclaim` |
| 6 | Book 3 | `2023-11-14 18:00` | `2023-11-14 22:00` | 4.0h | `$0.6081` | `$0.6610` | **+8.70%** | **+8.34%** | +9.7% | -0.3% | `target_reclaim` |
| 7 | Book 3 | `2023-12-11 02:00` | `2023-12-11 18:00` | 16.0h | `$0.7958` | `$0.7303` | **-8.23%** | **-8.59%** | +2.5% | -12.2% | `stop_loss` |
| 8 | Book 3 | `2023-12-26 17:00` | `2023-12-27 12:00` | 19.0h | `$0.9034` | `$0.9820` | **+8.70%** | **+8.34%** | +9.7% | -2.0% | `target_reclaim` |
| 9 | Book 3 | `2024-02-12 06:00` | `2024-02-12 15:00` | 9.0h | `$0.8016` | `$0.8350` | **+4.17%** | **+4.08%** | +4.4% | -0.3% | `target_reclaim` |
| 10 | Book 3 | `2024-02-17 14:00` | `2024-02-20 14:00` | 72.0h | `$0.9094` | `$0.9217` | **+1.35%** | **+1.34%** | +7.4% | -1.5% | `time_expiry` |
| 11 | Book 3 | `2024-02-28 17:00` | `2024-02-29 08:00` | 15.0h | `$0.9510` | `$1.0810` | **+13.67%** | **+12.81%** | +17.0% | -6.0% | `target_reclaim` |
| 12 | Book 3 | `2024-03-11 00:00` | `2024-03-11 04:00` | 4.0h | `$1.3533` | `$1.4710` | **+8.70%** | **+8.34%** | +10.5% | -2.2% | `target_reclaim` |
| 13 | Book 3 | `2024-05-23 13:00` | `2024-05-26 13:00` | 72.0h | `$0.9130` | `$0.9257` | **+1.39%** | **+1.38%** | +5.4% | -4.5% | `time_expiry` |
| 14 | Book 3 | `2024-07-21 18:00` | `2024-07-21 20:00` | 2.0h | `$0.6221` | `$0.6480` | **+4.17%** | **+4.08%** | +4.3% | -1.0% | `target_reclaim` |
| 15 | Book 3 | `2024-07-25 01:00` | `2024-07-26 02:00` | 25.0h | `$0.6256` | `$0.6700` | **+7.10%** | **+6.86%** | +10.9% | -4.3% | `target_reclaim` |
| 16 | Book 4 | `2024-11-16 01:00` | `2024-11-23 00:00` | 167.0h | `$0.6410` | `$0.7692` | **+54.60%** | **+45.00%** | +20.9% | -2.0% | `target_reclaim` |
| 17 | Book 3 | `2025-04-28 00:00` | `2025-04-28 10:00` | 10.0h | `$0.3917` | `$0.4080` | **+4.17%** | **+4.08%** | +5.2% | -1.5% | `target_reclaim` |
| 18 | Book 3 | `2025-05-15 06:00` | `2025-05-17 16:00` | 58.0h | `$0.4321` | `$0.3966` | **-8.23%** | **-8.59%** | +1.1% | -8.1% | `stop_loss` |
| 19 | Book 4 | `2025-08-31 03:00` | `2025-09-07 03:00` | 168.0h | `$0.4316` | `$0.4024` | **-6.27%** | **-6.49%** | +4.9% | -9.6% | `stagnation_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `11` | `100.0%` | **`+110.1%`** |
| `time_expiry` | `3` | `66.7%` | **`-1.4%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-6.5%`** |
| `time_cap` | `1` | `100.0%` | **`+17.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `FLOW`

* **Total Candidate Breakouts Filtered (Vetoed):** `632`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `357` (56.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `99`
* **Saved Capital Losses Avoided:** `+4,001.1%`
* **Missed Upside Forgone:** `-3,386.8%`
* **Net Veto Alpha:** `+614.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `327` | `51.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `106` | `16.8%` |
| `Core 1: Macro Bear Veto` | `82` | `13.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `75` | `11.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `42` | `6.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*