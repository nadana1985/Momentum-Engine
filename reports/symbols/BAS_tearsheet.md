# Kronos V12: Institutional Symbol Tear Sheet — `BAS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-5.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.67%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.1% / -4.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-20 14:00` | `2026-09-22 14:00` | 48.0h | `$0.0246` | `$0.0234` | **-4.60%** | **-4.71%** | +2.0% | -5.0% | `fast_decay_cut` |
| 2 | Book 2 | `2026-10-01 05:00` | `2026-10-03 05:00` | 48.0h | `$0.0237` | `$0.0236` | **-0.62%** | **-0.62%** | +6.2% | -3.3% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-5.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `BAS`

* **Total Candidate Breakouts Filtered (Vetoed):** `57`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `44` (77.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `30`
* **Saved Capital Losses Avoided:** `+1,288.4%`
* **Missed Upside Forgone:** `-2,153.2%`
* **Net Veto Alpha:** `+-864.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `56` | `98.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `1` | `1.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*