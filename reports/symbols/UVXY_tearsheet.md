# Kronos V12: Institutional Symbol Tear Sheet — `UVXY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.714`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-1.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.83%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-5.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`102.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.5% / -4.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-08 08:00` | `2026-09-15 08:00` | 168.0h | `$17.9047` | `$18.6632` | **+4.24%** | **+4.15%** | +8.3% | -2.4% | `time_cap` |
| 2 | Book 2 | `2026-10-01 14:00` | `2026-10-03 02:00` | 36.0h | `$17.8345` | `$16.8278` | **-5.64%** | **-5.81%** | +0.7% | -5.5% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `1` | `0.0%` | **`-5.8%`** |
| `time_cap` | `1` | `100.0%` | **`+4.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `UVXY`

* **Total Candidate Breakouts Filtered (Vetoed):** `3`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `3` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+31.6%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+31.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `3` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*