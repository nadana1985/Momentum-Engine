# Kronos V12: Institutional Symbol Tear Sheet — `WIF`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.029`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-16.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.85x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.11%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`73.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.0% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-10-11 15:00` | `2024-10-17 17:00` | 146.0h | `$2.6774` | `$2.4570` | **-8.23%** | **-8.59%** | +11.0% | -8.0% | `initial_stop` |
| 2 | Book 1 | `2024-10-18 18:00` | `2024-10-21 18:00` | 72.0h | `$2.6859` | `$2.5020` | **-7.99%** | **-8.33%** | +3.7% | -7.4% | `stagnation_bailout` |
| 3 | Book 2 | `2026-05-06 01:00` | `2026-05-07 04:00` | 27.0h | `$0.2110` | `$0.2116` | **+0.25%** | **+0.25%** | +20.8% | -4.7% | `breakeven_ratchet` |
| 4 | Book 2 | `2026-09-21 13:00` | `2026-09-23 14:00` | 49.0h | `$0.2326` | `$0.2332` | **+0.25%** | **+0.25%** | +20.5% | -3.8% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `2` | `100.0%` | **`+0.5%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `WIF`

* **Total Candidate Breakouts Filtered (Vetoed):** `51`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `38` (74.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+774.8%`
* **Missed Upside Forgone:** `-1,036.0%`
* **Net Veto Alpha:** `+-261.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `26` | `51.0%` |
| `Core 4: Funding Rate Cap` | `15` | `29.4%` |
| `Core 4: Defensible Whale Dump` | `7` | `13.7%` |
| `Core 4: Whale Firewall` | `3` | `5.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*