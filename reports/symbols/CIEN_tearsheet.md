# Kronos V12: Institutional Symbol Tear Sheet — `CIEN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`2` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-6.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.30%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.8% / -4.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 17:00` | `2026-08-28 17:00` | 48.0h | `$402.1228` | `$382.2719` | **-4.94%** | **-5.06%** | +4.4% | -5.4% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-21 12:00` | `2026-09-23 12:00` | 48.0h | `$372.4488` | `$366.7808` | **-1.52%** | **-1.53%** | +1.2% | -4.1% | `fast_decay_cut` |
| 3 | Book 2 | `2026-09-30 12:00` | `_Open Live_` | 160.9h | `$360.9200` | `$441.4800` | **+22.32%** | **+20.15%** | +24.2% | -5.5% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-6.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CIEN`

* **Total Candidate Breakouts Filtered (Vetoed):** `8`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `7` (87.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+56.1%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+56.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `8` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*