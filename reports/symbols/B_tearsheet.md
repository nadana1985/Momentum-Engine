# Kronos V12: Institutional Symbol Tear Sheet — `B`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.196`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+27.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.32x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.86%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`53.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.2% / -6.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-10-28 20:00` | `2025-10-29 19:00` | 23.0h | `$0.1853` | `$0.2029` | **+9.50%** | **+9.07%** | +10.3% | -2.5% | `target_reclaim` |
| 2 | Book 3 | `2026-09-06 05:00` | `2026-09-07 23:00` | 42.0h | `$0.1671` | `$0.1959` | **+17.25%** | **+15.91%** | +18.7% | -4.5% | `target_reclaim` |
| 3 | Book 4 | `2026-09-09 17:00` | `2026-09-14 18:00` | 121.0h | `$0.2036` | `$0.2443` | **+11.58%** | **+11.05%** | +21.4% | -10.0% | `target_reclaim` |
| 4 | Book 3 | `2026-09-15 10:00` | `2026-09-16 13:00` | 27.0h | `$0.2074` | `$0.1904` | **-8.23%** | **-8.59%** | +2.5% | -10.3% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+36.0%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `B`

* **Total Candidate Breakouts Filtered (Vetoed):** `137`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `117` (85.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `26`
* **Saved Capital Losses Avoided:** `+1,986.2%`
* **Missed Upside Forgone:** `-1,229.1%`
* **Net Veto Alpha:** `+757.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `82` | `59.9%` |
| `Core 1: Macro Bear Veto` | `33` | `24.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `22` | `16.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*