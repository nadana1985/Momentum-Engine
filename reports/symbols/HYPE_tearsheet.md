# Kronos V12: Institutional Symbol Tear Sheet — `HYPE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-15.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.86x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-7.59%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-9.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`267.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.9% / -9.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2025-07-10 16:00` | `2025-07-25 00:00` | 344.0h | `$42.6383` | `$41.3593` | **-5.63%** | **-5.76%** | +17.1% | -2.8% | `breakeven_ratchet` |
| 2 | Book 4 | `2026-02-03 00:00` | `2026-02-10 23:00` | 191.0h | `$34.1331` | `$29.0132` | **-9.06%** | **-9.42%** | +12.7% | -15.8% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `0.0%` | **`-5.8%`** |
| `structural_stop` | `1` | `0.0%` | **`-9.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `HYPE`

* **Total Candidate Breakouts Filtered (Vetoed):** `89`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `42` (47.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+466.8%`
* **Missed Upside Forgone:** `-242.3%`
* **Net Veto Alpha:** `+224.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `89` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*