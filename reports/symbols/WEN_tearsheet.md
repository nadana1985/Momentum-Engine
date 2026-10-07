# Kronos V12: Institutional Symbol Tear Sheet — `WEN`
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
| **Cumulative Net Log Return** | **`-3.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.82%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`17.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.2% / -3.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-15 15:00` | `2026-09-16 08:00` | 17.0h | `$7.7162` | `$7.4267` | **-3.75%** | **-3.82%** | +0.2% | -3.5% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-3.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `WEN`

* **Total Candidate Breakouts Filtered (Vetoed):** `4`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `2` (50.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+5.3%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+5.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `4` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*