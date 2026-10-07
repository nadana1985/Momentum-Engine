# Kronos V12: Institutional Symbol Tear Sheet — `V`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`2` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-3.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.76%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-3.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`47.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.1% / -2.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-24 13:00` | `2026-08-27 08:00` | 67.0h | `$380.6292` | `$379.4390` | **-0.31%** | **-0.31%** | +1.3% | -2.1% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-21 11:00` | `2026-09-22 15:00` | 28.0h | `$372.0478` | `$360.3316` | **-3.15%** | **-3.20%** | +0.8% | -3.2% | `initial_stop` |
| 3 | Book 2 | `2026-10-05 17:00` | `_Open Live_` | 35.9h | `$369.5917` | `$370.9600` | **+0.37%** | **+0.37%** | +0.7% | -0.7% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.3%`** |
| `initial_stop` | `1` | `0.0%` | **`-3.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `V`

* **Total Candidate Breakouts Filtered (Vetoed):** `22`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `13` (59.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+32.6%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+32.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `22` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*