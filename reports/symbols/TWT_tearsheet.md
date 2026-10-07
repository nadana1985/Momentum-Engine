# Kronos V12: Institutional Symbol Tear Sheet — `TWT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.589`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-15.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.86x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.55%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-34.4%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`45.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.4% / -6.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$1.1637` | `$1.1956` | **+2.74%** | **+2.70%** | +6.2% | -3.5% | `time_expiry` |
| 2 | Book 3 | `2024-02-28 17:00` | `2024-02-29 04:00` | 11.0h | `$1.3033` | `$1.4166` | **+8.70%** | **+8.34%** | +10.1% | -3.9% | `target_reclaim` |
| 3 | Book 3 | `2024-03-14 13:00` | `2024-03-15 03:00` | 14.0h | `$1.5377` | `$1.4111` | **-8.23%** | **-8.59%** | +3.3% | -8.7% | `stop_loss` |
| 4 | Book 3 | `2024-06-07 18:00` | `2024-06-10 03:00` | 57.0h | `$1.2570` | `$1.1535` | **-8.23%** | **-8.59%** | +2.1% | -11.9% | `stop_loss` |
| 5 | Book 3 | `2024-09-16 21:00` | `2024-09-16 22:00` | 1.0h | `$0.9019` | `$0.8277` | **-8.23%** | **-8.59%** | +4.8% | -20.4% | `stop_loss` |
| 6 | Book 3 | `2024-11-12 10:00` | `2024-11-15 00:00` | 62.0h | `$1.0187` | `$0.9349` | **-8.23%** | **-8.59%** | +4.8% | -8.4% | `stop_loss` |
| 7 | Book 3 | `2025-04-28 02:00` | `2025-05-01 02:00` | 72.0h | `$0.7837` | `$0.7945` | **+1.37%** | **+1.36%** | +5.9% | -0.9% | `time_expiry` |
| 8 | Book 3 | `2025-10-09 11:00` | `2025-10-10 04:00` | 17.0h | `$1.4626` | `$1.5898` | **+8.70%** | **+8.34%** | +11.6% | -2.5% | `target_reclaim` |
| 9 | Book 3 | `2026-09-06 14:00` | `2026-09-09 14:00` | 72.0h | `$0.5917` | `$0.5720` | **-3.33%** | **-3.38%** | +1.9% | -7.1% | `time_expiry` |
| 10 | Book 3 | `2026-10-02 18:00` | `2026-10-05 18:00` | 72.0h | `$0.5613` | `$0.5697` | **+1.49%** | **+1.48%** | +3.6% | -1.3% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `time_expiry` | `4` | `75.0%` | **`+2.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `TWT`

* **Total Candidate Breakouts Filtered (Vetoed):** `166`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `86` (51.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `7`
* **Saved Capital Losses Avoided:** `+770.0%`
* **Missed Upside Forgone:** `-266.0%`
* **Net Veto Alpha:** `+504.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `86` | `51.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `35` | `21.1%` |
| `Core 1: Macro Bear Veto` | `34` | `20.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `11` | `6.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*