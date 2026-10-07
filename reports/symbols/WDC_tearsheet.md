# Kronos V12: Institutional Symbol Tear Sheet — `WDC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-17.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.84x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.35%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.8% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-04 13:00` | `2026-09-06 13:00` | 48.0h | `$467.3254` | `$466.1517` | **-0.25%** | **-0.25%** | +0.6% | -5.3% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-09 14:00` | `2026-09-10 13:00` | 23.0h | `$494.6636` | `$462.2600` | **-6.55%** | **-6.78%** | +0.3% | -7.6% | `initial_stop` |
| 3 | Book 2 | `2026-09-18 17:00` | `2026-09-20 17:00` | 48.0h | `$443.0047` | `$435.2093` | **-1.76%** | **-1.78%** | +1.3% | -3.9% | `fast_decay_cut` |
| 4 | Book 2 | `2026-10-05 13:00` | `2026-10-06 18:00` | 29.0h | `$443.1351` | `$406.6651` | **-8.23%** | **-8.59%** | +1.1% | -8.0% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-2.0%`** |
| `initial_stop` | `2` | `0.0%` | **`-15.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `WDC`

* **Total Candidate Breakouts Filtered (Vetoed):** `20`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `6` (30.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `3`
* **Saved Capital Losses Avoided:** `+72.6%`
* **Missed Upside Forgone:** `-73.8%`
* **Net Veto Alpha:** `+-1.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `20` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*