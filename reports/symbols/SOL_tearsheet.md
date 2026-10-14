# Kronos V12: Institutional Symbol Tear Sheet — `SOL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.627`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-20.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.81x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.30%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-33.1%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`112.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.4% / -8.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2022-11-05 00:00` | `2022-11-07 22:00` | 70.0h | `$35.0073` | `$29.6818` | **-20.15%** | **-22.54%** | +10.8% | -20.0% | `initial_stop` |
| 2 | Book 4 | `2023-07-11 06:00` | `2023-07-13 18:00` | 60.0h | `$22.1772` | `$26.6127` | **+15.08%** | **+14.20%** | +21.2% | -3.7% | `target_reclaim` |
| 3 | Book 3 | `2023-11-16 21:00` | `2023-11-19 21:00` | 72.0h | `$58.6723` | `$61.1926` | **+4.30%** | **+4.21%** | +5.3% | -7.8% | `time_expiry` |
| 4 | Book 3 | `2024-03-05 17:00` | `2024-03-05 19:00` | 2.0h | `$128.2213` | `$117.6687` | **-8.23%** | **-8.59%** | +6.0% | -18.9% | `stop_loss` |
| 5 | Book 3 | `2024-03-19 02:00` | `2024-03-19 22:00` | 20.0h | `$185.2089` | `$169.9662` | **-8.23%** | **-8.59%** | +2.6% | -10.3% | `stop_loss` |
| 6 | Book 1 | `2025-04-20 01:00` | `2025-04-21 13:00` | 36.0h | `$142.0743` | `$136.7572` | **-5.50%** | **-5.66%** | +0.8% | -4.6% | `stall_bailout` |
| 7 | Book 4 | `2025-05-08 20:00` | `2025-05-30 16:00` | 524.0h | `$163.0442` | `$156.6347` | **-4.84%** | **-4.94%** | +15.1% | -4.3% | `structural_stop` |
| 8 | Book 1 | `2025-07-10 22:00` | `2025-07-13 22:00` | 72.0h | `$165.0616` | `$160.2883` | **-5.17%** | **-5.29%** | +1.9% | -4.5% | `stagnation_bailout` |
| 9 | Book 4 | `2026-08-21 02:00` | `2026-08-27 14:00` | 156.0h | `$89.3839` | `$107.2606` | **+17.65%** | **+16.46%** | +20.7% | -2.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+30.7%`** |
| `initial_stop` | `1` | `0.0%` | **`-22.5%`** |
| `stall_bailout` | `1` | `0.0%` | **`-5.7%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-5.3%`** |
| `structural_stop` | `1` | `0.0%` | **`-4.9%`** |
| `time_expiry` | `1` | `100.0%` | **`+4.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `SOL`

* **Total Candidate Breakouts Filtered (Vetoed):** `289`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `143` (49.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `71`
* **Saved Capital Losses Avoided:** `+2,062.6%`
* **Missed Upside Forgone:** `-2,335.3%`
* **Net Veto Alpha:** `+-272.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `178` | `61.6%` |
| `Core 1: Macro Bear Veto` | `75` | `26.0%` |
| `Core 4: Funding Rate Cap` | `30` | `10.4%` |
| `Core 4: Defensible Whale Dump` | `5` | `1.7%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*