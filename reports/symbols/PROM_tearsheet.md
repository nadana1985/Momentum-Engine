# Kronos V12: Institutional Symbol Tear Sheet — `PROM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.227`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+1.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.75%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`3.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+43.7% / -21.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-05-30 18:00` | `2025-05-30 21:00` | 3.0h | `$5.5819` | `$5.2536` | **-6.45%** | **-6.65%** | +1.8% | -9.4% | `initial_stop` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2026-08-11 01:00` | `2026-08-15 01:00` | Live | `$2.4720` | `$2.6822` | **+8.50%** | **+8.16%** | +85.7% | -33.1% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-6.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `PROM`

* **Total Candidate Breakouts Filtered (Vetoed):** `72`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `43` (59.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+617.1%`
* **Missed Upside Forgone:** `-1,008.7%`
* **Net Veto Alpha:** `+-391.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `54` | `75.0%` |
| `Core 4: Defensible Whale Dump` | `10` | `13.9%` |
| `Core 4: Whale Firewall` | `5` | `6.9%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `3` | `4.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*