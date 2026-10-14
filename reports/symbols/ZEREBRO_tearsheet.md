# Kronos V12: Institutional Symbol Tear Sheet — `ZEREBRO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+21.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.24x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+10.62%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`9.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+20.7% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-10 21:00` | `2025-07-11 03:00` | 6.0h | `$0.0293` | `$0.0344` | **+17.39%** | **+16.03%** | +20.6% | -7.9% | `target_reclaim` |
| 2 | Book 4 | `2026-04-29 11:00` | `2026-04-29 23:00` | 12.0h | `$0.0236` | `$0.0283` | **+5.33%** | **+5.20%** | +20.8% | -2.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+21.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZEREBRO`

* **Total Candidate Breakouts Filtered (Vetoed):** `433`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `308` (71.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `243`
* **Saved Capital Losses Avoided:** `+7,646.9%`
* **Missed Upside Forgone:** `-11,735.9%`
* **Net Veto Alpha:** `+-4,089.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `317` | `73.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `109` | `25.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `7` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*