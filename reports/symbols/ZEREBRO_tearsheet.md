# Kronos V12: Institutional Symbol Tear Sheet — `ZEREBRO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+8.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.09x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.34%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`15.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.6% / -3.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-10 02:00` | `2025-07-10 17:00` | 15.0h | `$0.0317` | `$0.0344` | **+8.70%** | **+8.34%** | +14.6% | -3.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZEREBRO`

* **Total Candidate Breakouts Filtered (Vetoed):** `63`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `45` (71.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `34`
* **Saved Capital Losses Avoided:** `+1,036.9%`
* **Missed Upside Forgone:** `-2,192.8%`
* **Net Veto Alpha:** `+-1,155.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `55` | `87.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `7` | `11.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*