# Kronos V12: Institutional Symbol Tear Sheet — `VVV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.029`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-8.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.17%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`43.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.0% / -5.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-07-27 16:00` | `2025-07-29 16:00` | 48.0h | `$3.2311` | `$2.9651` | **-8.23%** | **-8.59%** | +12.7% | -9.1% | `initial_stop` |
| 2 | Book 2 | `2025-10-26 13:00` | `2025-10-28 03:00` | 38.0h | `$1.5799` | `$1.5839` | **+0.25%** | **+0.25%** | +17.4% | -1.9% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `VVV`

* **Total Candidate Breakouts Filtered (Vetoed):** `113`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `50` (44.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `33`
* **Saved Capital Losses Avoided:** `+788.2%`
* **Missed Upside Forgone:** `-1,166.5%`
* **Net Veto Alpha:** `+-378.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `92` | `81.4%` |
| `Core 4: Defensible Whale Dump` | `15` | `13.3%` |
| `Core 4: Whale Firewall` | `6` | `5.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*