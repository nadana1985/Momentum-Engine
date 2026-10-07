# Kronos V12: Institutional Symbol Tear Sheet — `XPL`
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
| **Cumulative Net Log Return** | **`-29.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.75x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-14.55%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-20.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`10.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.5% / -19.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-09-25 16:00` | `2025-09-25 17:00` | 1.0h | `$1.0530` | `$0.9664` | **-8.23%** | **-8.59%** | +2.9% | -17.4% | `initial_stop` |
| 2 | Book 1 | `2026-08-21 09:00` | `2026-08-22 05:00` | 20.0h | `$0.1011` | `$0.0857` | **-18.55%** | **-20.52%** | +8.1% | -20.9% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-29.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `XPL`

* **Total Candidate Breakouts Filtered (Vetoed):** `82`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `63` (76.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `31`
* **Saved Capital Losses Avoided:** `+1,649.1%`
* **Missed Upside Forgone:** `-1,075.7%`
* **Net Veto Alpha:** `+573.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `82` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*