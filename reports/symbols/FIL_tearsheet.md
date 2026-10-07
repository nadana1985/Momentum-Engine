# Kronos V12: Institutional Symbol Tear Sheet — `FIL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-25.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.77x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-25.66%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`70.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.8% / -17.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2026-09-13 14:00` | `2026-09-16 12:00` | 70.0h | `$0.9137` | `$0.7747` | **-22.63%** | **-25.66%** | +13.8% | -17.5% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-25.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `FIL`

* **Total Candidate Breakouts Filtered (Vetoed):** `175`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `104` (59.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `65`
* **Saved Capital Losses Avoided:** `+1,657.5%`
* **Missed Upside Forgone:** `-2,686.6%`
* **Net Veto Alpha:** `+-1,029.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `70` | `40.0%` |
| `Core 1: Macro Bear Veto` | `54` | `30.9%` |
| `Core 4: Funding Rate Cap` | `44` | `25.1%` |
| `Core 4: Whale Firewall` | `5` | `2.9%` |
| `Core 4: Defensible Whale Dump` | `2` | `1.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*