# Kronos V12: Institutional Symbol Tear Sheet — `FHE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.584`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+6.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.05%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-10.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`8.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.1% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-18 12:00` | `2025-05-18 15:00` | 3.0h | `$0.0904` | `$0.0983` | **+8.70%** | **+8.34%** | +10.1% | -0.9% | `target_reclaim` |
| 2 | Book 3 | `2025-05-23 20:00` | `2025-05-24 18:00` | 22.0h | `$0.0989` | `$0.1075` | **+8.70%** | **+8.34%** | +9.2% | -2.9% | `target_reclaim` |
| 3 | Book 3 | `2025-08-04 19:00` | `2025-08-04 20:00` | 1.0h | `$0.0814` | `$0.0733` | **-9.99%** | **-10.52%** | +8.1% | -14.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `stop_loss` | `1` | `0.0%` | **`-10.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `FHE`

* **Total Candidate Breakouts Filtered (Vetoed):** `69`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `51` (73.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `41`
* **Saved Capital Losses Avoided:** `+1,419.6%`
* **Missed Upside Forgone:** `-3,495.1%`
* **Net Veto Alpha:** `+-2,075.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `58` | `84.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `8.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `5` | `7.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*