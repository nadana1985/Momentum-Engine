# Kronos V12: Institutional Symbol Tear Sheet — `PNUT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.465`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+29.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.35x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+7.44%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`24.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.8% / -4.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-24 08:00` | `2025-04-25 06:00` | 22.0h | `$0.1513` | `$0.1719` | **+13.64%** | **+12.78%** | +15.4% | -0.5% | `target_reclaim` |
| 2 | Book 3 | `2025-04-28 01:00` | `2025-04-28 08:00` | 7.0h | `$0.1648` | `$0.1873` | **+13.64%** | **+12.78%** | +13.7% | -2.9% | `target_reclaim` |
| 3 | Book 3 | `2025-07-14 14:00` | `2025-07-16 20:00` | 54.0h | `$0.2761` | `$0.3137` | **+13.64%** | **+12.78%** | +13.8% | -7.3% | `target_reclaim` |
| 4 | Book 3 | `2025-07-23 16:00` | `2025-07-24 05:00` | 13.0h | `$0.2914` | `$0.2674` | **-8.23%** | **-8.59%** | +4.4% | -8.9% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+38.4%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `PNUT`

* **Total Candidate Breakouts Filtered (Vetoed):** `38`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (63.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+427.4%`
* **Missed Upside Forgone:** `-1,071.0%`
* **Net Veto Alpha:** `+-643.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `20` | `52.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `18` | `47.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*