# Kronos V12: Institutional Symbol Tear Sheet — `PYTH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`71.4%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.508`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+25.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.30x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.70%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`43.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.6% / -5.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-28 17:00` | `2024-03-02 17:00` | 72.0h | `$0.6465` | `$0.6677` | **+3.28%** | **+3.22%** | +8.2% | -8.7% | `time_expiry` |
| 2 | Book 3 | `2024-03-14 13:00` | `2024-03-15 23:00` | 34.0h | `$0.8354` | `$0.9493` | **+13.64%** | **+12.78%** | +16.1% | -5.4% | `target_reclaim` |
| 3 | Book 3 | `2024-10-01 14:00` | `2024-10-01 17:00` | 3.0h | `$0.3324` | `$0.3050` | **-8.23%** | **-8.59%** | +2.6% | -9.2% | `stop_loss` |
| 4 | Book 3 | `2024-10-25 23:00` | `2024-10-28 23:00` | 72.0h | `$0.3308` | `$0.3633` | **+9.82%** | **+9.37%** | +12.5% | -5.6% | `time_expiry` |
| 5 | Book 3 | `2024-11-12 13:00` | `2024-11-15 13:00` | 72.0h | `$0.3934` | `$0.4133` | **+5.04%** | **+4.91%** | +9.2% | -2.7% | `time_expiry` |
| 6 | Book 3 | `2024-11-26 12:00` | `2024-11-27 22:00` | 34.0h | `$0.4059` | `$0.4612` | **+13.64%** | **+12.78%** | +14.2% | -0.1% | `target_reclaim` |
| 7 | Book 3 | `2025-07-23 13:00` | `2025-07-24 06:00` | 17.0h | `$0.1320` | `$0.1211` | **-8.23%** | **-8.59%** | +4.3% | -8.9% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `3` | `100.0%` | **`+17.5%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+25.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `PYTH`

* **Total Candidate Breakouts Filtered (Vetoed):** `133`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `82` (61.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `10`
* **Saved Capital Losses Avoided:** `+912.6%`
* **Missed Upside Forgone:** `-301.0%`
* **Net Veto Alpha:** `+611.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `72` | `54.1%` |
| `Core 1: Macro Bear Veto` | `60` | `45.1%` |
| `Core 4: Funding Rate Cap` | `1` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*