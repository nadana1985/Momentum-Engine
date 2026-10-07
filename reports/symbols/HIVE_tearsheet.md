# Kronos V12: Institutional Symbol Tear Sheet — `HIVE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.676`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-5.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.11%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.2% / -4.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-28 01:00` | `2025-05-01 01:00` | 72.0h | `$0.2448` | `$0.2522` | **+3.01%** | **+2.97%** | +8.2% | -1.2% | `time_expiry` |
| 2 | Book 3 | `2025-05-04 00:00` | `2025-05-06 11:00` | 59.0h | `$0.2517` | `$0.2310` | **-8.23%** | **-8.59%** | +3.2% | -8.0% | `stop_loss` |
| 3 | Book 3 | `2025-07-24 05:00` | `2025-07-27 05:00` | 72.0h | `$0.2378` | `$0.2385` | **+0.31%** | **+0.31%** | +3.3% | -3.2% | `time_expiry` |
| 4 | Book 3 | `2026-09-13 15:00` | `2026-09-15 00:00` | 33.0h | `$0.0504` | `$0.0548` | **+8.70%** | **+8.34%** | +23.2% | -4.1% | `target_reclaim` |
| 5 | Book 3 | `2026-09-15 03:00` | `2026-09-15 08:00` | 5.0h | `$0.0544` | `$0.0499` | **-8.23%** | **-8.59%** | +8.1% | -8.0% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `2` | `100.0%` | **`+3.3%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `HIVE`

* **Total Candidate Breakouts Filtered (Vetoed):** `43`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `36` (83.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `3`
* **Saved Capital Losses Avoided:** `+384.2%`
* **Missed Upside Forgone:** `-110.7%`
* **Net Veto Alpha:** `+273.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `21` | `48.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `12` | `27.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `16.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `7.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*