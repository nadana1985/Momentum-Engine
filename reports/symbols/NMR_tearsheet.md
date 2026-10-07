# Kronos V12: Institutional Symbol Tear Sheet — `NMR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `14` (`14` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `14` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`42.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.532`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-30.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.74x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.17%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-55.9%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`31.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.1% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-11-09 16:00` | `2023-11-10 22:00` | 30.0h | `$13.9748` | `$15.1900` | **+8.70%** | **+8.34%** | +9.2% | -7.0% | `target_reclaim` |
| 2 | Book 3 | `2023-11-19 12:00` | `2023-11-22 12:00` | 72.0h | `$15.3732` | `$15.4513` | **+0.51%** | **+0.51%** | +8.5% | -6.8% | `time_expiry` |
| 3 | Book 3 | `2023-12-26 17:00` | `2023-12-27 08:00` | 15.0h | `$16.2472` | `$17.6600` | **+8.70%** | **+8.34%** | +9.7% | -0.5% | `target_reclaim` |
| 4 | Book 3 | `2023-12-29 00:00` | `2023-12-29 11:00` | 11.0h | `$16.8360` | `$18.3000` | **+8.70%** | **+8.34%** | +9.2% | -1.8% | `target_reclaim` |
| 5 | Book 3 | `2024-03-05 16:00` | `2024-03-05 19:00` | 3.0h | `$34.1872` | `$31.3736` | **-8.23%** | **-8.59%** | +4.4% | -16.6% | `stop_loss` |
| 6 | Book 3 | `2024-03-10 14:00` | `2024-03-12 08:00` | 42.0h | `$46.3772` | `$42.5604` | **-8.23%** | **-8.59%** | +4.4% | -8.8% | `stop_loss` |
| 7 | Book 3 | `2024-05-23 13:00` | `2024-05-26 13:00` | 72.0h | `$28.0738` | `$28.2602` | **+0.66%** | **+0.66%** | +3.8% | -5.1% | `time_expiry` |
| 8 | Book 3 | `2024-09-30 18:00` | `2024-10-01 17:00` | 23.0h | `$15.9767` | `$14.6618` | **-8.23%** | **-8.59%** | +3.9% | -12.6% | `stop_loss` |
| 9 | Book 3 | `2024-11-12 10:00` | `2024-11-13 20:00` | 34.0h | `$15.4284` | `$14.1586` | **-8.23%** | **-8.59%** | +7.0% | -8.1% | `stop_loss` |
| 10 | Book 3 | `2024-12-02 08:00` | `2024-12-02 21:00` | 13.0h | `$20.4672` | `$22.2470` | **+8.70%** | **+8.34%** | +10.9% | -1.1% | `target_reclaim` |
| 11 | Book 3 | `2025-05-23 15:00` | `2025-05-24 23:00` | 32.0h | `$9.3187` | `$8.5518` | **-8.23%** | **-8.59%** | +1.1% | -8.3% | `stop_loss` |
| 12 | Book 3 | `2025-05-30 17:00` | `2025-05-31 03:00` | 10.0h | `$9.7566` | `$8.9536` | **-8.23%** | **-8.59%** | +5.8% | -9.0% | `stop_loss` |
| 13 | Book 3 | `2025-07-29 20:00` | `2025-08-01 20:00` | 72.0h | `$8.6958` | `$8.2932` | **-4.63%** | **-4.74%** | +5.3% | -6.6% | `time_expiry` |
| 14 | Book 3 | `2025-09-21 12:00` | `2025-09-22 02:00` | 14.0h | `$16.6115` | `$15.2444` | **-8.23%** | **-8.59%** | +1.5% | -8.2% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `time_expiry` | `3` | `66.7%` | **`-3.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `NMR`

* **Total Candidate Breakouts Filtered (Vetoed):** `140`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `90` (64.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+1,292.6%`
* **Missed Upside Forgone:** `-1,144.0%`
* **Net Veto Alpha:** `+148.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `63` | `45.0%` |
| `Core 1: Macro Bear Veto` | `51` | `36.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `20` | `14.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `4.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*