# Kronos V12: Institutional Symbol Tear Sheet — `APP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.26%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-3.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.6% / -3.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-14 15:00` | `2026-09-16 15:00` | 48.0h | `$332.0380` | `$328.7062` | **-1.00%** | **-1.01%** | +1.8% | -2.7% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-28 11:00` | `2026-09-28 16:00` | 5.0h | `$319.1860` | `$308.1435` | **-3.46%** | **-3.52%** | +1.5% | -3.3% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.0%`** |
| `initial_stop` | `1` | `0.0%` | **`-3.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `APP`

* **Total Candidate Breakouts Filtered (Vetoed):** `0`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `0` (0.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+0.0%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+0.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*