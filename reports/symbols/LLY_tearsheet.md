# Kronos V12: Institutional Symbol Tear Sheet — `LLY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.85%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.9% / -2.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-21 13:00` | `2026-09-23 13:00` | 48.0h | `$1167.2709` | `$1157.3893` | **-0.85%** | **-0.85%** | +1.9% | -2.7% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `LLY`

* **Total Candidate Breakouts Filtered (Vetoed):** `12`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `5` (41.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+31.1%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+31.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `11` | `91.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `8.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*