# Kronos V12: Institutional Symbol Tear Sheet — `PENGU`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`6.281`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+98.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.68x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+19.69%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`110.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.7% / -8.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-05-21 16:00` | `2025-05-25 08:00` | 88.0h | `$0.0137` | `$0.0126` | **-9.03%** | **-9.43%** | +9.8% | -11.3% | `initial_stop` |
| 2 | Book 4 | `2025-06-29 18:00` | `2025-07-10 04:00` | 250.0h | `$0.0145` | `$0.0174` | **+108.25%** | **+77.15%** | +20.9% | -9.0% | `target_reclaim` |
| 3 | Book 2 | `2025-10-26 11:00` | `2025-10-28 21:00` | 58.0h | `$0.0220` | `$0.0202` | **-8.83%** | **-9.22%** | +5.8% | -8.6% | `initial_stop` |
| 4 | Book 4 | `2026-08-22 05:00` | `2026-08-25 04:00` | 71.0h | `$0.0087` | `$0.0105` | **+11.53%** | **+11.01%** | +20.4% | -7.8% | `target_reclaim` |
| 5 | Book 2 | `2026-09-19 17:00` | `2026-09-23 08:00` | 87.0h | `$0.0081` | `$0.0108` | **+33.50%** | **+28.92%** | +36.5% | -7.1% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-18.6%`** |
| `target_reclaim` | `2` | `100.0%` | **`+88.2%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+28.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `PENGU`

* **Total Candidate Breakouts Filtered (Vetoed):** `39`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (61.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+297.4%`
* **Missed Upside Forgone:** `-54.8%`
* **Net Veto Alpha:** `+242.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `36` | `92.3%` |
| `Core 4: Whale Firewall` | `2` | `5.1%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `2.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*