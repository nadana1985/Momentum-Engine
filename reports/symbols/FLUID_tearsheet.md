# Kronos V12: Institutional Symbol Tear Sheet — `FLUID`
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
| **Cumulative Net Log Return** | **`-8.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-8.59%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`51.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.0% / -8.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-26 08:00` | `2026-08-28 11:00` | 51.0h | `$1.4536` | `$1.3340` | **-8.23%** | **-8.59%** | +5.0% | -8.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `FLUID`

* **Total Candidate Breakouts Filtered (Vetoed):** `46`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `29` (63.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+367.4%`
* **Missed Upside Forgone:** `-269.5%`
* **Net Veto Alpha:** `+97.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `18` | `39.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `15` | `32.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `13` | `28.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*