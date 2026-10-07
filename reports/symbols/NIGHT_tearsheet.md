# Kronos V12: Institutional Symbol Tear Sheet — `NIGHT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.15%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`72.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.6% / -8.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2026-09-19 01:00` | `2026-09-22 01:00` | 72.0h | `$0.0249` | `$0.0241` | **-4.07%** | **-4.15%** | +2.6% | -8.6% | `stagnation_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stagnation_bailout` | `1` | `0.0%` | **`-4.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `NIGHT`

* **Total Candidate Breakouts Filtered (Vetoed):** `14`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `12` (85.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+182.9%`
* **Missed Upside Forgone:** `-62.3%`
* **Net Veto Alpha:** `+120.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `14` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*