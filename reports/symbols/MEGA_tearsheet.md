# Kronos V12: Institutional Symbol Tear Sheet — `MEGA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-19.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.83x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-9.56%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-10.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`39.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+-7.7% / -31.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-04-30 04:00` | `2026-05-04 04:00` | Live | `$0.1832` | `$0.1682` | **-8.20%** | **-8.56%** | +-17.8% | -51.5% | `shelf_stop_loss` |
| 2 | Book 2 | `2026-09-08 07:00` | `2026-09-09 22:00` | 39.0h | `$0.0436` | `$0.0400` | **-10.13%** | **-10.57%** | +2.3% | -11.1% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-10.6%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `MEGA`

* **Total Candidate Breakouts Filtered (Vetoed):** `16`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `8` (50.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+94.5%`
* **Missed Upside Forgone:** `-447.2%`
* **Net Veto Alpha:** `+-352.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `16` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*