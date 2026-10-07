# Kronos V12: Institutional Symbol Tear Sheet — `PIEVERSE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.007`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+0.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.05%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-12.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`33.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.3% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-22 05:00` | `2026-08-24 13:00` | 56.0h | `$0.9456` | `$1.0745` | **+13.64%** | **+12.78%** | +19.4% | -6.2% | `target_reclaim` |
| 2 | Book 2 | `2026-09-07 13:00` | `2026-09-08 00:00` | 11.0h | `$1.3013` | `$1.1942` | **-11.92%** | **-12.69%** | +1.3% | -8.2% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-12.7%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `PIEVERSE`

* **Total Candidate Breakouts Filtered (Vetoed):** `42`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `36` (85.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `14`
* **Saved Capital Losses Avoided:** `+839.4%`
* **Missed Upside Forgone:** `-1,064.6%`
* **Net Veto Alpha:** `+-225.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `37` | `88.1%` |
| `Core 4: Defensible Whale Dump` | `5` | `11.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*