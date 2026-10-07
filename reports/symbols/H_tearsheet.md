# Kronos V12: Institutional Symbol Tear Sheet — `H`
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
| **Cumulative Net Log Return** | **`-8.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-8.59%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`27.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.6% / -8.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-08-14 12:00` | `2025-08-15 15:00` | 27.0h | `$0.0367` | `$0.0337` | **-8.23%** | **-8.59%** | +8.6% | -8.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `H`

* **Total Candidate Breakouts Filtered (Vetoed):** `106`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `75` (70.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `54`
* **Saved Capital Losses Avoided:** `+1,585.4%`
* **Missed Upside Forgone:** `-3,370.3%`
* **Net Veto Alpha:** `+-1,784.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `102` | `96.2%` |
| `Core 3: Min Turnover Velocity` | `2` | `1.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `1` | `0.9%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*