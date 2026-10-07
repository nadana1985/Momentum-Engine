# Kronos V12: Institutional Symbol Tear Sheet — `ARX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.488`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+4.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.10%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`12.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.0% / -6.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-26 13:00` | `2026-09-27 10:00` | 21.0h | `$0.2293` | `$0.2606` | **+13.64%** | **+12.78%** | +17.3% | -4.6% | `target_reclaim` |
| 2 | Book 3 | `2026-09-27 22:00` | `2026-09-28 02:00` | 4.0h | `$0.2512` | `$0.2306` | **-8.23%** | **-8.59%** | +2.7% | -8.7% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `ARX`

* **Total Candidate Breakouts Filtered (Vetoed):** `8`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `8` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+119.6%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+119.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: Funding Rate Cap` | `8` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*