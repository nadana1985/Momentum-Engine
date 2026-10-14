# Kronos V12: Institutional Symbol Tear Sheet — `TZA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.161`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-3.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.64%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`108.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.4% / -3.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-20 13:00` | `2026-08-22 13:00` | 48.0h | `$38.6865` | `$37.2267` | **-3.85%** | **-3.92%** | +1.6% | -4.4% | `fast_decay_cut` |
| 2 | Book 2 | `2026-08-28 15:00` | `2026-09-04 15:00` | 168.0h | `$39.6589` | `$39.9100` | **+0.63%** | **+0.63%** | +7.2% | -2.1% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-3.9%`** |
| `time_cap` | `1` | `100.0%` | **`+0.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `TZA`

* **Total Candidate Breakouts Filtered (Vetoed):** `21`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `13` (61.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+61.6%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+61.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `15` | `71.4%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `5` | `23.8%` |
| `Core 1: Macro Bear Veto` | `1` | `4.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*