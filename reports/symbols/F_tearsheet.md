# Kronos V12: Institutional Symbol Tear Sheet — `F`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.223`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+1.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.64%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`29.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.7% / -7.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-24 05:00` | `2025-07-24 16:00` | 11.0h | `$0.0094` | `$0.0086` | **-8.23%** | **-8.59%** | +5.8% | -12.3% | `stop_loss` |
| 2 | Book 3 | `2026-09-09 22:00` | `2026-09-12 22:00` | 72.0h | `$0.0033` | `$0.0033` | **+2.19%** | **+2.16%** | +5.0% | -5.2% | `time_expiry` |
| 3 | Book 3 | `2026-09-18 17:00` | `2026-09-18 22:00` | 5.0h | `$0.0046` | `$0.0050` | **+8.70%** | **+8.34%** | +21.2% | -6.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+2.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `F`

* **Total Candidate Breakouts Filtered (Vetoed):** `342`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `264` (77.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `128`
* **Saved Capital Losses Avoided:** `+5,076.1%`
* **Missed Upside Forgone:** `-12,246.5%`
* **Net Veto Alpha:** `+-7,170.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `246` | `71.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `89` | `26.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `1.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*