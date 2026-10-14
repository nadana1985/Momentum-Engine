# Kronos V12: Institutional Symbol Tear Sheet — `TAC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+20.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.23x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.82%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`9.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+97.5% / -45.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-11-14 08:00` | `2025-11-18 08:00` | Live | `$0.0055` | `$0.0059` | **+8.50%** | **+8.16%** | +184.6% | -38.9% | `shelf_target_reclaim` |
| 2 | Book 4 | `2026-04-22 02:00` | `2026-04-22 11:00` | 9.0h | `$0.0062` | `$0.0073` | **+4.50%** | **+4.14%** | +22.1% | -3.1% | `climax_whale_euphoria_harvest` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2026-06-29 07:00` | `2026-07-03 07:00` | Live | `$0.0312` | `$0.0339` | **+8.50%** | **+8.16%** | +85.7% | -93.0% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+4.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `TAC`

* **Total Candidate Breakouts Filtered (Vetoed):** `214`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `55` (25.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `156`
* **Saved Capital Losses Avoided:** `+976.6%`
* **Missed Upside Forgone:** `-11,616.6%`
* **Net Veto Alpha:** `+-10,640.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `211` | `98.6%` |
| `Core 4: Defensible Whale Dump` | `3` | `1.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*