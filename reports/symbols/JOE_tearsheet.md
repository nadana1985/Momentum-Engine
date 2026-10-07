# Kronos V12: Institutional Symbol Tear Sheet — `JOE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `16` (`16` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `16` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`68.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.082`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+43.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.54x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+2.71%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-25.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`30.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.1% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-10-02 18:00` | `2023-10-04 19:00` | 49.0h | `$0.2410` | `$0.2620` | **+8.70%** | **+8.34%** | +10.1% | -1.2% | `target_reclaim` |
| 2 | Book 3 | `2023-10-09 09:00` | `2023-10-11 02:00` | 41.0h | `$0.2498` | `$0.2292` | **-8.23%** | **-8.59%** | +1.4% | -8.7% | `stop_loss` |
| 3 | Book 3 | `2023-11-01 14:00` | `2023-11-01 18:00` | 4.0h | `$0.2521` | `$0.2740` | **+8.70%** | **+8.34%** | +9.2% | -0.2% | `target_reclaim` |
| 4 | Book 3 | `2023-11-09 16:00` | `2023-11-10 17:00` | 25.0h | `$0.2978` | `$0.3237` | **+8.70%** | **+8.34%** | +10.7% | -10.5% | `target_reclaim` |
| 5 | Book 3 | `2023-11-18 01:00` | `2023-11-18 07:00` | 6.0h | `$0.3763` | `$0.3453` | **-8.23%** | **-8.59%** | +3.3% | -8.8% | `stop_loss` |
| 6 | Book 3 | `2023-12-23 01:00` | `2023-12-24 22:00` | 45.0h | `$0.7069` | `$0.6487` | **-8.23%** | **-8.59%** | +2.6% | -8.1% | `stop_loss` |
| 7 | Book 3 | `2024-02-20 15:00` | `2024-02-23 15:00` | 72.0h | `$0.5146` | `$0.5149` | **+0.07%** | **+0.07%** | +3.5% | -7.3% | `time_expiry` |
| 8 | Book 3 | `2024-03-16 15:00` | `2024-03-16 23:00` | 8.0h | `$0.8532` | `$0.7830` | **-8.23%** | **-8.59%** | +2.8% | -9.4% | `stop_loss` |
| 9 | Book 3 | `2024-03-19 06:00` | `2024-03-19 12:00` | 6.0h | `$0.9942` | `$1.0807` | **+8.70%** | **+8.34%** | +11.3% | -2.9% | `target_reclaim` |
| 10 | Book 3 | `2024-10-09 21:00` | `2024-10-12 00:00` | 51.0h | `$0.3125` | `$0.3397` | **+8.70%** | **+8.34%** | +9.6% | -2.7% | `target_reclaim` |
| 11 | Book 3 | `2024-11-23 16:00` | `2024-11-24 20:00` | 28.0h | `$0.4281` | `$0.4653` | **+8.70%** | **+8.34%** | +9.8% | -4.2% | `target_reclaim` |
| 12 | Book 3 | `2024-11-28 19:00` | `2024-11-29 18:00` | 23.0h | `$0.5406` | `$0.5876` | **+8.70%** | **+8.34%** | +9.2% | -1.2% | `target_reclaim` |
| 13 | Book 3 | `2024-12-03 14:00` | `2024-12-03 21:00` | 7.0h | `$0.5541` | `$0.6023` | **+8.70%** | **+8.34%** | +10.0% | -3.1% | `target_reclaim` |
| 14 | Book 3 | `2025-04-27 15:00` | `2025-04-30 15:00` | 72.0h | `$0.1944` | `$0.1836` | **-5.57%** | **-5.73%** | +1.3% | -7.9% | `time_expiry` |
| 15 | Book 3 | `2026-09-20 02:00` | `2026-09-20 13:00` | 11.0h | `$0.0318` | `$0.0345` | **+8.70%** | **+8.34%** | +9.0% | -0.7% | `target_reclaim` |
| 16 | Book 3 | `2026-09-23 14:00` | `2026-09-25 02:00` | 36.0h | `$0.0349` | `$0.0379` | **+8.70%** | **+8.34%** | +9.4% | -3.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `10` | `100.0%` | **`+83.4%`** |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `time_expiry` | `2` | `50.0%` | **`-5.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `JOE`

* **Total Candidate Breakouts Filtered (Vetoed):** `161`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `104` (64.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `17`
* **Saved Capital Losses Avoided:** `+1,237.4%`
* **Missed Upside Forgone:** `-506.2%`
* **Net Veto Alpha:** `+731.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `70` | `43.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `36` | `22.4%` |
| `Core 1: Macro Bear Veto` | `33` | `20.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `22` | `13.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*