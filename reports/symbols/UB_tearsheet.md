# Kronos V12: Institutional Symbol Tear Sheet — `UB`
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
| **Cumulative Net Log Return** | **`-15.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.86x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-7.80%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-7.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`19.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.2% / -11.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-20 01:00` | `2026-09-20 03:00` | 2.0h | `$0.1551` | `$0.1423` | **-8.23%** | **-8.59%** | +0.4% | -10.6% | `initial_stop` |
| 2 | Book 1 | `2026-09-23 16:00` | `2026-09-25 04:00` | 36.0h | `$0.1567` | `$0.1443` | **-6.77%** | **-7.01%** | +-0.1% | -11.7% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-7.0%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `UB`

* **Total Candidate Breakouts Filtered (Vetoed):** `75`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `54` (72.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+1,213.3%`
* **Missed Upside Forgone:** `-1,268.7%`
* **Net Veto Alpha:** `+-55.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `71` | `94.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `4` | `5.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*