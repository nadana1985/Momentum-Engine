# Kronos V12: Institutional Symbol Tear Sheet — `ATH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.912`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.38%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-13.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`49.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.5% / -7.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-15 18:00` | `2025-05-15 21:00` | 3.0h | `$0.0504` | `$0.0463` | **-8.23%** | **-8.59%** | +8.9% | -10.7% | `stop_loss` |
| 2 | Book 3 | `2025-07-12 05:00` | `2025-07-12 08:00` | 3.0h | `$0.0288` | `$0.0300` | **+4.17%** | **+4.08%** | +4.5% | -0.5% | `target_reclaim` |
| 3 | Book 3 | `2025-07-30 08:00` | `2025-08-01 11:00` | 51.0h | `$0.0341` | `$0.0313` | **-8.23%** | **-8.59%** | +3.8% | -8.2% | `stop_loss` |
| 4 | Book 3 | `2025-08-12 10:00` | `2025-08-15 10:00` | 72.0h | `$0.0332` | `$0.0343` | **+3.45%** | **+3.39%** | +6.1% | -5.1% | `time_expiry` |
| 5 | Book 3 | `2025-09-29 13:00` | `2025-09-29 14:00` | 1.0h | `$0.0612` | `$0.0561` | **-8.23%** | **-8.59%** | +9.4% | -13.9% | `stop_loss` |
| 6 | Book 2 | `2026-05-05 04:00` | `2026-05-12 04:00` | 168.0h | `$0.0063` | `$0.0072` | **+17.11%** | **+16.02%** | +18.4% | -3.6% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `target_reclaim` | `1` | `100.0%` | **`+4.1%`** |
| `time_cap` | `1` | `100.0%` | **`+16.0%`** |
| `time_expiry` | `1` | `100.0%` | **`+3.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `ATH`

* **Total Candidate Breakouts Filtered (Vetoed):** `290`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `219` (75.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `24`
* **Saved Capital Losses Avoided:** `+2,886.0%`
* **Missed Upside Forgone:** `-742.8%`
* **Net Veto Alpha:** `+2,143.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `157` | `54.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `93` | `32.1%` |
| `Core 1: Macro Bear Veto` | `20` | `6.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `19` | `6.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*