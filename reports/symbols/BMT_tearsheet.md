# Kronos V12: Institutional Symbol Tear Sheet — `BMT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.824`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-1.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.75%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`88.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.1% / -6.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-13 13:00` | `2026-09-13 22:00` | 9.0h | `$0.0193` | `$0.0177` | **-8.23%** | **-8.59%** | +2.4% | -8.8% | `initial_stop` |
| 2 | Book 2 | `2026-09-17 14:00` | `2026-09-24 14:00` | 168.0h | `$0.0191` | `$0.0205` | **+7.34%** | **+7.08%** | +11.7% | -4.5% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `time_cap` | `1` | `100.0%` | **`+7.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `BMT`

* **Total Candidate Breakouts Filtered (Vetoed):** `27`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (88.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+466.6%`
* **Missed Upside Forgone:** `-683.6%`
* **Net Veto Alpha:** `+-217.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `14` | `51.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `13` | `48.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*