# Kronos V12: Institutional Symbol Tear Sheet — `XPT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-5.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.66%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-4.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`76.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.1% / -2.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-20 15:00` | `2026-08-26 16:00` | 145.0h | `$1838.2742` | `$1833.2853` | **-0.27%** | **-0.27%** | +4.8% | -1.2% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-09 07:00` | `2026-09-10 18:00` | 35.0h | `$1865.6826` | `$1789.3894` | **-4.09%** | **-4.18%** | +3.4% | -4.2% | `initial_stop` |
| 3 | Book 2 | `2026-09-17 07:00` | `2026-09-19 07:00` | 48.0h | `$1807.3571` | `$1797.6047` | **-0.54%** | **-0.54%** | +1.0% | -1.9% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-0.8%`** |
| `initial_stop` | `1` | `0.0%` | **`-4.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `XPT`

* **Total Candidate Breakouts Filtered (Vetoed):** `32`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `19` (59.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+82.3%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+82.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `32` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*