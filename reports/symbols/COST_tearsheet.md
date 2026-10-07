# Kronos V12: Institutional Symbol Tear Sheet — `COST`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`4` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-3.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.94%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-2.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`42.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.7% / -1.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-24 14:00` | `2026-08-26 14:00` | 48.0h | `$965.3173` | `$953.6000` | **-1.21%** | **-1.22%** | +1.2% | -1.0% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-14 01:00` | `2026-09-16 01:00` | 48.0h | `$910.6910` | `$901.0417` | **-1.06%** | **-1.07%** | +1.2% | -1.0% | `fast_decay_cut` |
| 3 | Book 2 | `2026-09-22 05:00` | `2026-09-23 17:00` | 36.0h | `$904.9868` | `$900.0941` | **-0.54%** | **-0.54%** | +0.3% | -1.1% | `stall_bailout` |
| 4 | Book 2 | `2026-09-28 13:00` | `2026-09-30 01:00` | 36.0h | `$930.0293` | `$921.3409` | **-0.93%** | **-0.94%** | +0.1% | -1.8% | `stall_bailout` |
| 5 | Book 2 | `2026-10-06 15:00` | `_Open Live_` | 13.9h | `$932.0142` | `$934.0800` | **+0.22%** | **+0.22%** | +0.5% | -0.5% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-2.3%`** |
| `stall_bailout` | `2` | `0.0%` | **`-1.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `COST`

* **Total Candidate Breakouts Filtered (Vetoed):** `6`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `6` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+15.9%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+15.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `5` | `83.3%` |
| `Core 3: Min Turnover Velocity` | `1` | `16.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*