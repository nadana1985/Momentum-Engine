# Kronos V12: Institutional Symbol Tear Sheet — `BARD`
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
| **Cumulative Net Log Return** | **`-1.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.65%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`72.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.9% / -6.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-28 07:00` | `2026-10-01 07:00` | 72.0h | `$0.1409` | `$0.1386` | **-1.63%** | **-1.65%** | +1.9% | -6.7% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `1` | `0.0%` | **`-1.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `BARD`

* **Total Candidate Breakouts Filtered (Vetoed):** `40`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `28` (70.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `7`
* **Saved Capital Losses Avoided:** `+423.1%`
* **Missed Upside Forgone:** `-221.3%`
* **Net Veto Alpha:** `+201.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `26` | `65.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `14` | `35.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*