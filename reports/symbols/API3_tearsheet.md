# Kronos V12: Institutional Symbol Tear Sheet — `API3`
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
| **Cumulative Net Log Return** | **`-6.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.21%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`53.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.3% / -5.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-09-14 01:00` | `2024-09-16 01:00` | 48.0h | `$1.5180` | `$1.4486` | **-4.57%** | **-4.68%** | +4.7% | -5.3% | `fast_decay_cut` |
| 2 | Book 2 | `2025-04-21 16:00` | `2025-04-24 03:00` | 59.0h | `$0.7562` | `$0.7431` | **-1.73%** | **-1.74%** | +6.0% | -6.2% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-6.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `API3`

* **Total Candidate Breakouts Filtered (Vetoed):** `175`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `111` (63.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `26`
* **Saved Capital Losses Avoided:** `+1,443.0%`
* **Missed Upside Forgone:** `-936.8%`
* **Net Veto Alpha:** `+506.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `62` | `35.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `54` | `30.9%` |
| `Core 1: Macro Bear Veto` | `42` | `24.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `17` | `9.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*