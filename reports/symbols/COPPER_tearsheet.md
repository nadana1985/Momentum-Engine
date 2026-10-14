# Kronos V12: Institutional Symbol Tear Sheet — `COPPER`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-1.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.53%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`47.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.4% / -0.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-21 07:00` | `2026-09-23 18:00` | 59.0h | `$6.7639` | `$6.7451` | **-0.28%** | **-0.28%** | +2.5% | -0.5% | `fast_decay_cut` |
| 2 | Book 2 | `2026-10-05 14:00` | `2026-10-07 02:00` | 36.0h | `$6.6666` | `$6.6144` | **-0.78%** | **-0.79%** | +0.3% | -0.7% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.3%`** |
| `stall_bailout` | `1` | `0.0%` | **`-0.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `COPPER`

* **Total Candidate Breakouts Filtered (Vetoed):** `39`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `17` (43.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+49.3%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+49.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `39` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*