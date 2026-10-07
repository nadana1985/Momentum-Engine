# Kronos V12: Institutional Symbol Tear Sheet — `LUMIA`
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
| **Cumulative Net Log Return** | **`+16.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.34%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`24.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.4% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-13 13:00` | `2025-05-13 18:00` | 5.0h | `$0.4043` | `$0.4395` | **+8.70%** | **+8.34%** | +10.9% | -3.6% | `target_reclaim` |
| 2 | Book 3 | `2025-08-05 15:00` | `2025-08-07 10:00` | 43.0h | `$0.2789` | `$0.3031` | **+8.70%** | **+8.34%** | +9.9% | -2.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `LUMIA`

* **Total Candidate Breakouts Filtered (Vetoed):** `58`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `41` (70.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+608.6%`
* **Missed Upside Forgone:** `-883.0%`
* **Net Veto Alpha:** `+-274.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `41` | `70.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `14` | `24.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `5.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*