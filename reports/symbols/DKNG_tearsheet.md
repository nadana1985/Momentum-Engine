# Kronos V12: Institutional Symbol Tear Sheet — `DKNG`
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
| **Cumulative Net Log Return** | **`-6.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.33%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-6.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.8% / -4.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-11 14:00` | `2026-09-13 14:00` | 48.0h | `$24.2104` | `$24.0697` | **-0.58%** | **-0.58%** | +2.8% | -2.1% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-22 13:00` | `2026-09-23 13:00` | 24.0h | `$22.8370` | `$21.4921` | **-5.89%** | **-6.07%** | +2.7% | -6.6% | `initial_stop` |
| 3 | Book 2 | `2026-10-06 14:00` | `_Open Live_` | 14.9h | `$20.3507` | `$19.7500` | **-2.95%** | **-3.00%** | +-0.0% | -3.6% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.6%`** |
| `initial_stop` | `1` | `0.0%` | **`-6.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `DKNG`

* **Total Candidate Breakouts Filtered (Vetoed):** `8`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `2` (25.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+9.4%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+9.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `8` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*