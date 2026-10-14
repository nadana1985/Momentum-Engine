# Kronos V12: Institutional Symbol Tear Sheet — `TXN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.646`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.31%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`54.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.8% / -2.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-07 08:00` | `2026-09-08 20:00` | 36.0h | `$262.5748` | `$258.3026` | **-1.71%** | **-1.73%** | +0.6% | -2.2% | `stall_bailout` |
| 2 | Book 3 | `2026-09-14 08:00` | `2026-09-17 08:00` | 72.0h | `$260.0736` | `$262.9909` | **+1.12%** | **+1.12%** | +3.1% | -1.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `1` | `0.0%` | **`-1.7%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `TXN`

* **Total Candidate Breakouts Filtered (Vetoed):** `9`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `6` (66.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+30.4%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+30.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `66.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `3` | `33.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*