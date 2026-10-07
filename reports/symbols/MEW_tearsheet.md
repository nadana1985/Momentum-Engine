# Kronos V12: Institutional Symbol Tear Sheet — `MEW`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `15` (`15` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.680`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-22.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.80x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.48%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-21.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`33.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.9% / -6.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-07-24 14:00` | `2024-07-24 17:00` | 3.0h | `$0.0080` | `$0.0073` | **-8.23%** | **-8.59%** | +2.7% | -8.2% | `stop_loss` |
| 2 | Book 3 | `2024-09-22 00:00` | `2024-09-22 16:00` | 16.0h | `$0.0050` | `$0.0046` | **-8.23%** | **-8.59%** | +2.2% | -8.1% | `stop_loss` |
| 3 | Book 3 | `2024-10-08 06:00` | `2024-10-08 23:00` | 17.0h | `$0.0068` | `$0.0062` | **-8.23%** | **-8.59%** | +4.4% | -8.1% | `stop_loss` |
| 4 | Book 3 | `2024-10-19 07:00` | `2024-10-21 06:00` | 47.0h | `$0.0088` | `$0.0096` | **+8.70%** | **+8.34%** | +19.2% | -5.7% | `target_reclaim` |
| 5 | Book 3 | `2024-10-21 12:00` | `2024-10-24 02:00` | 62.0h | `$0.0091` | `$0.0099` | **+8.70%** | **+8.34%** | +11.5% | -4.6% | `target_reclaim` |
| 6 | Book 3 | `2024-10-26 01:00` | `2024-10-26 08:00` | 7.0h | `$0.0097` | `$0.0105` | **+8.70%** | **+8.34%** | +8.9% | -1.1% | `target_reclaim` |
| 7 | Book 3 | `2024-11-14 11:00` | `2024-11-14 22:00` | 11.0h | `$0.0113` | `$0.0103` | **-8.23%** | **-8.59%** | +6.2% | -9.8% | `stop_loss` |
| 8 | Book 3 | `2024-11-18 11:00` | `2024-11-20 01:00` | 38.0h | `$0.0116` | `$0.0106` | **-8.23%** | **-8.59%** | +2.2% | -8.5% | `stop_loss` |
| 9 | Book 3 | `2025-04-27 04:00` | `2025-04-30 04:00` | 72.0h | `$0.0028` | `$0.0029` | **+5.65%** | **+5.49%** | +8.2% | -4.8% | `time_expiry` |
| 10 | Book 3 | `2025-05-03 17:00` | `2025-05-06 10:00` | 65.0h | `$0.0028` | `$0.0026` | **-8.23%** | **-8.59%** | +3.6% | -8.9% | `stop_loss` |
| 11 | Book 3 | `2025-05-13 02:00` | `2025-05-13 16:00` | 14.0h | `$0.0037` | `$0.0040` | **+8.70%** | **+8.34%** | +10.9% | -2.1% | `target_reclaim` |
| 12 | Book 3 | `2025-05-23 11:00` | `2025-05-23 22:00` | 11.0h | `$0.0043` | `$0.0040` | **-8.23%** | **-8.59%** | +9.1% | -8.3% | `stop_loss` |
| 13 | Book 3 | `2025-07-14 20:00` | `2025-07-16 10:00` | 38.0h | `$0.0031` | `$0.0033` | **+8.70%** | **+8.34%** | +9.1% | -4.3% | `target_reclaim` |
| 14 | Book 3 | `2026-08-25 09:00` | `2026-08-26 14:00` | 29.0h | `$0.0004` | `$0.0004` | **-8.23%** | **-8.59%** | +2.5% | -8.7% | `stop_loss` |
| 15 | Book 3 | `2026-09-30 11:00` | `2026-10-03 11:00` | 72.0h | `$0.0005` | `$0.0005` | **-0.71%** | **-0.71%** | +3.5% | -6.7% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `8` | `0.0%` | **`-68.7%`** |
| `target_reclaim` | `5` | `100.0%` | **`+41.7%`** |
| `time_expiry` | `2` | `50.0%` | **`+4.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `MEW`

* **Total Candidate Breakouts Filtered (Vetoed):** `114`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `61` (53.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `26`
* **Saved Capital Losses Avoided:** `+864.4%`
* **Missed Upside Forgone:** `-922.1%`
* **Net Veto Alpha:** `+-57.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `57` | `50.0%` |
| `Core 1: Macro Bear Veto` | `30` | `26.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `25` | `21.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `1.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*