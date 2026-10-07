# Kronos V12: Institutional Symbol Tear Sheet — `TIA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.120`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+27.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.32x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.96%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-0.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`106.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.3% / -5.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-02-03 07:00` | `2024-02-04 08:00` | 25.0h | `$18.3283` | `$16.8199` | **-8.23%** | **-8.59%** | +0.9% | -8.6% | `initial_stop` |
| 2 | Book 2 | `2024-09-13 21:00` | `2024-09-20 21:00` | 168.0h | `$4.5162` | `$5.9881` | **+32.59%** | **+28.21%** | +43.3% | -4.5% | `time_cap` |
| 3 | Book 2 | `2024-10-11 12:00` | `2024-10-18 12:00` | 168.0h | `$5.4141` | `$5.8968` | **+8.92%** | **+8.54%** | +20.2% | -2.8% | `time_cap` |
| 4 | Book 2 | `2026-09-01 13:00` | `2026-09-04 05:00` | 64.0h | `$0.3578` | `$0.3566` | **-0.33%** | **-0.33%** | +4.9% | -5.6% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `100.0%` | **`+36.8%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.3%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `TIA`

* **Total Candidate Breakouts Filtered (Vetoed):** `129`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `79` (61.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+818.2%`
* **Missed Upside Forgone:** `-759.3%`
* **Net Veto Alpha:** `+58.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `86` | `66.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `31` | `24.0%` |
| `Core 4: Defensible Whale Dump` | `12` | `9.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*