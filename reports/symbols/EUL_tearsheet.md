# Kronos V12: Institutional Symbol Tear Sheet — `EUL`
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
| **Cumulative Net Log Return** | **`-9.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.91x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.52%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.4% / -13.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-21 14:00` | `2026-08-22 05:00` | 15.0h | `$1.3594` | `$1.2475` | **-8.23%** | **-8.59%** | +2.7% | -22.8% | `initial_stop` |
| 2 | Book 1 | `2026-08-26 06:00` | `2026-08-28 18:00` | 60.0h | `$1.3684` | `$1.3573` | **-0.45%** | **-0.45%** | +10.0% | -3.7% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.5%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `EUL`

* **Total Candidate Breakouts Filtered (Vetoed):** `61`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `29` (47.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+372.3%`
* **Missed Upside Forgone:** `-944.6%`
* **Net Veto Alpha:** `+-572.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: Defensible Whale Dump` | `43` | `70.5%` |
| `Core 1: Macro Bear Veto` | `18` | `29.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*