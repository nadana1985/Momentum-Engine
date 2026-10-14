# Kronos V12: Institutional Symbol Tear Sheet — `YGG`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `19` (`19` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `19` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`73.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.131`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+43.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.54x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+2.29%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-25.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`20.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.3% / -3.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-10-02 18:00` | `2023-10-02 19:00` | 1.0h | `$0.2284` | `$0.2379` | **+4.17%** | **+4.08%** | +9.3% | -0.4% | `target_reclaim` |
| 2 | Book 3 | `2023-11-12 00:00` | `2023-11-12 07:00` | 7.0h | `$0.3911` | `$0.4251` | **+8.70%** | **+8.34%** | +10.6% | -0.8% | `target_reclaim` |
| 3 | Book 3 | `2023-11-12 23:00` | `2023-11-13 14:00` | 15.0h | `$0.4174` | `$0.3831` | **-8.23%** | **-8.59%** | +6.5% | -9.2% | `stop_loss` |
| 4 | Book 3 | `2023-12-18 07:00` | `2023-12-18 10:00` | 3.0h | `$0.3869` | `$0.3551` | **-8.23%** | **-8.59%** | +1.5% | -8.0% | `stop_loss` |
| 5 | Book 3 | `2023-12-27 18:00` | `2023-12-28 14:00` | 20.0h | `$0.4768` | `$0.4376` | **-8.23%** | **-8.59%** | +2.9% | -8.8% | `stop_loss` |
| 6 | Book 3 | `2024-01-05 01:00` | `2024-01-05 02:00` | 1.0h | `$0.5257` | `$0.5714` | **+8.70%** | **+8.34%** | +8.7% | -1.5% | `target_reclaim` |
| 7 | Book 3 | `2024-02-20 15:00` | `2024-02-23 15:00` | 72.0h | `$0.5145` | `$0.5201` | **+1.09%** | **+1.09%** | +5.1% | -4.7% | `time_expiry` |
| 8 | Book 3 | `2024-05-23 20:00` | `2024-05-25 01:00` | 29.0h | `$0.8487` | `$0.9700` | **+14.29%** | **+13.36%** | +15.6% | -4.2% | `target_reclaim` |
| 9 | Book 3 | `2024-05-28 04:00` | `2024-05-29 05:00` | 25.0h | `$0.9606` | `$1.0218` | **+6.38%** | **+6.18%** | +7.8% | -1.6% | `target_reclaim` |
| 10 | Book 3 | `2024-09-26 00:00` | `2024-09-26 16:00` | 16.0h | `$0.4571` | `$0.4868` | **+6.50%** | **+6.30%** | +10.0% | -1.3% | `target_reclaim` |
| 11 | Book 3 | `2024-09-26 20:00` | `2024-09-27 04:00` | 8.0h | `$0.4716` | `$0.4913` | **+4.17%** | **+4.08%** | +5.7% | -0.5% | `target_reclaim` |
| 12 | Book 3 | `2024-12-02 04:00` | `2024-12-02 18:00` | 14.0h | `$0.6516` | `$0.7012` | **+7.61%** | **+7.34%** | +7.7% | -4.2% | `target_reclaim` |
| 13 | Book 3 | `2025-04-21 18:00` | `2025-04-22 21:00` | 27.0h | `$0.1868` | `$0.1946` | **+4.17%** | **+4.08%** | +4.2% | -3.4% | `target_reclaim` |
| 14 | Book 3 | `2025-04-27 04:00` | `2025-04-28 20:00` | 40.0h | `$0.1985` | `$0.2068` | **+4.17%** | **+4.08%** | +4.2% | -4.1% | `target_reclaim` |
| 15 | Book 3 | `2025-07-14 08:00` | `2025-07-15 04:00` | 20.0h | `$0.1782` | `$0.1635` | **-8.23%** | **-8.59%** | +2.0% | -8.1% | `stop_loss` |
| 16 | Book 3 | `2025-07-17 01:00` | `2025-07-17 09:00` | 8.0h | `$0.1787` | `$0.1861` | **+4.17%** | **+4.08%** | +5.2% | -0.6% | `target_reclaim` |
| 17 | Book 3 | `2025-07-18 19:00` | `2025-07-20 05:00` | 34.0h | `$0.1839` | `$0.1916` | **+4.17%** | **+4.08%** | +5.5% | -4.0% | `target_reclaim` |
| 18 | Book 3 | `2025-07-22 08:00` | `2025-07-22 22:00` | 14.0h | `$0.1881` | `$0.2006` | **+6.65%** | **+6.44%** | +7.1% | -0.3% | `target_reclaim` |
| 19 | Book 2 | `2026-05-03 17:00` | `2026-05-05 05:00` | 36.0h | `$0.0455` | `$0.0440` | **-4.00%** | **-4.06%** | +0.3% | -5.6% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `13` | `100.0%` | **`+80.8%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `stall_bailout` | `1` | `0.0%` | **`-4.1%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `YGG`

* **Total Candidate Breakouts Filtered (Vetoed):** `235`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `168` (71.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `15`
* **Saved Capital Losses Avoided:** `+2,007.3%`
* **Missed Upside Forgone:** `-404.7%`
* **Net Veto Alpha:** `+1,602.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `145` | `61.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `43` | `18.3%` |
| `Core 1: Macro Bear Veto` | `27` | `11.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `20` | `8.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*