# Kronos V12: Institutional Symbol Tear Sheet — `FRAX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.915`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+2.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.16%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-2.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`50.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.3% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-28 05:00` | `2026-09-29 09:00` | 28.0h | `$0.2978` | `$0.3126` | **+4.98%** | **+4.86%** | +9.6% | -2.5% | `target_reclaim` |
| 2 | Book 3 | `2026-10-07 00:00` | `2026-10-10 00:00` | 72.0h | `$0.3110` | `$0.3032` | **-2.51%** | **-2.54%** | +3.0% | -7.5% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+4.9%`** |
| `time_expiry` | `1` | `0.0%` | **`-2.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `FRAX`

* **Total Candidate Breakouts Filtered (Vetoed):** `14`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `11` (78.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+91.5%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+91.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `11` | `78.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `21.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*