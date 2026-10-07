# Kronos V12: Institutional Symbol Tear Sheet — `BANANAS31`
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
| **Cumulative Net Log Return** | **`+0.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.25%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`38.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.2% / -3.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-02 15:00` | `2026-05-04 05:00` | 38.0h | `$0.0103` | `$0.0103` | **+0.25%** | **+0.25%** | +19.2% | -3.9% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `BANANAS31`

* **Total Candidate Breakouts Filtered (Vetoed):** `77`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `54` (70.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `42`
* **Saved Capital Losses Avoided:** `+1,391.6%`
* **Missed Upside Forgone:** `-3,954.6%`
* **Net Veto Alpha:** `+-2,563.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `59` | `76.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `17` | `22.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*