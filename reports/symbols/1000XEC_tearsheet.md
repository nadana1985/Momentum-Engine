# Kronos V12: Institutional Symbol Tear Sheet — `1000XEC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`69.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.592`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+57.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.78x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.41%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-6.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.4% / -4.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-01-14 09:00` | `2023-01-15 00:00` | 15.0h | `$0.0280` | `$0.0304` | **+8.70%** | **+8.34%** | +10.8% | -2.4% | `target_reclaim` |
| 2 | Book 3 | `2023-01-18 16:00` | `2023-01-21 16:00` | 72.0h | `$0.0287` | `$0.0306` | **+6.65%** | **+6.44%** | +8.1% | -3.1% | `time_expiry` |
| 3 | Book 3 | `2023-09-18 21:00` | `2023-09-21 21:00` | 72.0h | `$0.0252` | `$0.0238` | **-5.59%** | **-5.76%** | +8.1% | -6.1% | `time_expiry` |
| 4 | Book 3 | `2023-10-26 14:00` | `2023-10-29 14:00` | 72.0h | `$0.0269` | `$0.0283` | **+5.20%** | **+5.07%** | +6.3% | -1.6% | `time_expiry` |
| 5 | Book 3 | `2023-11-09 16:00` | `2023-11-09 23:00` | 7.0h | `$0.0283` | `$0.0307` | **+8.70%** | **+8.34%** | +15.6% | -7.9% | `target_reclaim` |
| 6 | Book 3 | `2023-12-11 02:00` | `2023-12-11 03:00` | 1.0h | `$0.0343` | `$0.0373` | **+8.70%** | **+8.34%** | +9.5% | -7.0% | `target_reclaim` |
| 7 | Book 3 | `2023-12-29 01:00` | `2023-12-29 13:00` | 12.0h | `$0.0368` | `$0.0399` | **+8.70%** | **+8.34%** | +9.6% | -2.7% | `target_reclaim` |
| 8 | Book 3 | `2024-04-09 08:00` | `2024-04-12 08:00` | 72.0h | `$0.0725` | `$0.0695` | **-4.24%** | **-4.33%** | +3.4% | -6.5% | `time_expiry` |
| 9 | Book 3 | `2024-05-23 13:00` | `2024-05-26 13:00` | 72.0h | `$0.0491` | `$0.0486` | **-1.05%** | **-1.05%** | +3.7% | -5.5% | `time_expiry` |
| 10 | Book 3 | `2024-11-17 18:00` | `2024-11-20 18:00` | 72.0h | `$0.0435` | `$0.0429` | **-1.34%** | **-1.35%** | +7.2% | -2.2% | `time_expiry` |
| 11 | Book 3 | `2024-12-02 08:00` | `2024-12-03 00:00` | 16.0h | `$0.0479` | `$0.0521` | **+8.70%** | **+8.34%** | +9.0% | -2.0% | `target_reclaim` |
| 12 | Book 3 | `2024-12-03 13:00` | `2024-12-03 22:00` | 9.0h | `$0.0495` | `$0.0538` | **+8.70%** | **+8.34%** | +11.3% | -4.7% | `target_reclaim` |
| 13 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0067` | `$0.0073` | **+8.70%** | **+8.34%** | +19.1% | -2.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `7` | `100.0%` | **`+58.4%`** |
| `time_expiry` | `6` | `33.3%` | **`-1.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000XEC`

* **Total Candidate Breakouts Filtered (Vetoed):** `164`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `95` (57.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `24`
* **Saved Capital Losses Avoided:** `+1,069.6%`
* **Missed Upside Forgone:** `-1,108.2%`
* **Net Veto Alpha:** `+-38.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `61` | `37.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `55` | `33.5%` |
| `Core 1: Macro Bear Veto` | `36` | `22.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `11` | `6.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*