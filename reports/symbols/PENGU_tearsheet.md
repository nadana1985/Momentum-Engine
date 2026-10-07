# Kronos V12: Institutional Symbol Tear Sheet — `PENGU`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.114`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+2.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.74%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`83.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.1% / -8.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-05-21 16:00` | `2025-05-25 08:00` | 88.0h | `$0.0137` | `$0.0126` | **-8.23%** | **-8.59%** | +9.8% | -11.3% | `initial_stop` |
| 2 | Book 2 | `2025-08-08 00:00` | `2025-08-12 05:00` | 101.0h | `$0.0386` | `$0.0355` | **-8.23%** | **-8.59%** | +8.3% | -8.4% | `initial_stop` |
| 3 | Book 2 | `2025-10-26 11:00` | `2025-10-28 21:00` | 58.0h | `$0.0220` | `$0.0202` | **-8.23%** | **-8.59%** | +5.8% | -8.6% | `initial_stop` |
| 4 | Book 2 | `2026-09-19 17:00` | `2026-09-23 08:00` | 87.0h | `$0.0081` | `$0.0108` | **+33.26%** | **+28.71%** | +36.5% | -7.1% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `3` | `0.0%` | **`-25.8%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+28.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `PENGU`

* **Total Candidate Breakouts Filtered (Vetoed):** `38`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (63.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+297.4%`
* **Missed Upside Forgone:** `-54.8%`
* **Net Veto Alpha:** `+242.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `36` | `94.7%` |
| `Core 4: Whale Firewall` | `2` | `5.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*