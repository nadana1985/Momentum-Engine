# Kronos V12: Institutional Symbol Tear Sheet — `CROSS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.942`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+8.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.70%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`15.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.1% / -5.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-09-22 15:00` | `2025-09-24 09:00` | 42.0h | `$0.2437` | `$0.2649` | **+8.70%** | **+8.34%** | +9.5% | -6.0% | `target_reclaim` |
| 2 | Book 3 | `2026-09-16 03:00` | `2026-09-16 05:00` | 2.0h | `$0.1181` | `$0.1284` | **+8.70%** | **+8.34%** | +17.3% | -2.9% | `target_reclaim` |
| 3 | Book 3 | `2026-09-18 13:00` | `2026-09-18 15:00` | 2.0h | `$0.1467` | `$0.1346` | **-8.23%** | **-8.59%** | +6.4% | -8.5% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CROSS`

* **Total Candidate Breakouts Filtered (Vetoed):** `33`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `32` (97.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `10`
* **Saved Capital Losses Avoided:** `+764.7%`
* **Missed Upside Forgone:** `-391.9%`
* **Net Veto Alpha:** `+372.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `26` | `78.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `18.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `1` | `3.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*