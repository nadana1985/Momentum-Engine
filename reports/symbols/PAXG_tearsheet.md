# Kronos V12: Institutional Symbol Tear Sheet — `PAXG`
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
| **Cumulative Net Log Return** | **`-2.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.31%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-2.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`70.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.3% / -1.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-06-12 10:00` | `2025-06-16 18:00` | 104.0h | `$3406.4248` | `$3397.7244` | **-0.26%** | **-0.26%** | +2.6% | -0.8% | `stagnation_cut` |
| 2 | Book 2 | `2025-10-08 14:00` | `2025-10-10 02:00` | 36.0h | `$4072.8768` | `$3977.5811` | **-2.34%** | **-2.37%** | +0.1% | -2.8% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stagnation_cut` | `1` | `0.0%` | **`-0.3%`** |
| `stall_bailout` | `1` | `0.0%` | **`-2.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `PAXG`

* **Total Candidate Breakouts Filtered (Vetoed):** `195`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `89` (45.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+312.1%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+312.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `195` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*