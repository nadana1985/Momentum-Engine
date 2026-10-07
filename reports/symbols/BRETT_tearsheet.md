# Kronos V12: Institutional Symbol Tear Sheet — `BRETT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.909`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.34%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.9% / -6.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-09-21 10:00` | `2024-09-24 10:00` | 72.0h | `$0.0783` | `$0.0817` | **+4.30%** | **+4.21%** | +7.5% | -2.7% | `time_expiry` |
| 2 | Book 3 | `2025-07-14 14:00` | `2025-07-15 03:00` | 13.0h | `$0.0559` | `$0.0513` | **-8.23%** | **-8.59%** | +4.2% | -9.2% | `stop_loss` |
| 3 | Book 3 | `2025-07-18 18:00` | `2025-07-20 15:00` | 45.0h | `$0.0577` | `$0.0628` | **+8.70%** | **+8.34%** | +9.7% | -5.8% | `target_reclaim` |
| 4 | Book 3 | `2025-09-19 03:00` | `2025-09-21 09:00` | 54.0h | `$0.0547` | `$0.0502` | **-8.23%** | **-8.59%** | +2.8% | -8.2% | `stop_loss` |
| 5 | Book 3 | `2026-05-12 10:00` | `2026-05-14 02:00` | 40.0h | `$0.0099` | `$0.0091` | **-8.23%** | **-8.59%** | +6.8% | -9.1% | `stop_loss` |
| 6 | Book 3 | `2026-09-23 15:00` | `2026-09-25 11:00` | 44.0h | `$0.0053` | `$0.0057` | **+8.70%** | **+8.34%** | +17.9% | -2.5% | `target_reclaim` |
| 7 | Book 3 | `2026-09-28 05:00` | `2026-10-01 05:00` | 72.0h | `$0.0058` | `$0.0059` | **+2.56%** | **+2.53%** | +6.7% | -6.7% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `time_expiry` | `2` | `100.0%` | **`+6.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `BRETT`

* **Total Candidate Breakouts Filtered (Vetoed):** `114`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `59` (51.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `33`
* **Saved Capital Losses Avoided:** `+769.4%`
* **Missed Upside Forgone:** `-963.1%`
* **Net Veto Alpha:** `+-193.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `70` | `61.4%` |
| `Core 1: Macro Bear Veto` | `24` | `21.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `16` | `14.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `4` | `3.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*