# Kronos V12: Institutional Symbol Tear Sheet — `ARB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-33.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.72x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-6.67%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-23.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`55.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.2% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-10-01 09:00` | `2023-10-04 00:00` | 63.0h | `$0.9594` | `$0.8685` | **-9.66%** | **-10.16%** | +3.0% | -11.2% | `fast_decay_cut` |
| 2 | Book 2 | `2023-10-16 05:00` | `2023-10-17 13:00` | 32.0h | `$0.8263` | `$0.7918` | **-4.17%** | **-4.26%** | +2.6% | -6.1% | `initial_stop` |
| 3 | Book 1 | `2024-09-26 16:00` | `2024-09-30 18:00` | 98.0h | `$0.6396` | `$0.6134` | **-5.35%** | **-5.50%** | +6.4% | -4.8% | `fast_decay_cut` |
| 4 | Book 2 | `2025-02-12 22:00` | `2025-02-15 22:00` | 72.0h | `$0.4978` | `$0.4742` | **-4.75%** | **-4.86%** | +2.8% | -5.5% | `stagnation_cut` |
| 5 | Book 2 | `2025-08-17 15:00` | `2025-08-18 03:00` | 12.0h | `$0.5586` | `$0.5126` | **-8.23%** | **-8.59%** | +1.1% | -8.6% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-15.7%`** |
| `initial_stop` | `2` | `0.0%` | **`-12.8%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-4.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `ARB`

* **Total Candidate Breakouts Filtered (Vetoed):** `108`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `85` (78.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `7`
* **Saved Capital Losses Avoided:** `+982.8%`
* **Missed Upside Forgone:** `-162.1%`
* **Net Veto Alpha:** `+820.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `79` | `73.1%` |
| `Core 4: Funding Rate Cap` | `29` | `26.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*