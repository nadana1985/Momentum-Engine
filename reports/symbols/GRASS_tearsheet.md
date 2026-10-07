# Kronos V12: Institutional Symbol Tear Sheet — `GRASS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.744`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.46%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`16.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.6% / -6.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-12-16 19:00` | `2024-12-17 11:00` | 16.0h | `$3.4127` | `$3.1319` | **-8.23%** | **-8.59%** | +2.7% | -8.9% | `stop_loss` |
| 2 | Book 3 | `2025-06-05 21:00` | `2025-06-06 04:00` | 7.0h | `$1.6992` | `$1.9309` | **+13.64%** | **+12.78%** | +13.8% | -0.1% | `target_reclaim` |
| 3 | Book 3 | `2025-09-29 06:00` | `2025-09-30 08:00` | 26.0h | `$0.8893` | `$0.8161` | **-8.23%** | **-8.59%** | +3.3% | -10.7% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `GRASS`

* **Total Candidate Breakouts Filtered (Vetoed):** `84`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `70` (83.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+1,178.7%`
* **Missed Upside Forgone:** `-689.3%`
* **Net Veto Alpha:** `+489.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `71` | `84.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `13` | `15.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*