# Kronos V12: Institutional Symbol Tear Sheet — `MAVIA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.883`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+24.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.28x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.95%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`20.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.4% / -6.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-13 19:00` | `2025-07-14 08:00` | 13.0h | `$0.1854` | `$0.2015` | **+8.70%** | **+8.34%** | +10.0% | -0.7% | `target_reclaim` |
| 2 | Book 3 | `2025-08-11 22:00` | `2025-08-12 17:00` | 19.0h | `$0.1821` | `$0.1979` | **+8.70%** | **+8.34%** | +16.2% | -7.3% | `target_reclaim` |
| 3 | Book 3 | `2025-10-26 19:00` | `2025-10-26 21:00` | 2.0h | `$0.1480` | `$0.1609` | **+8.70%** | **+8.34%** | +19.5% | -4.5% | `target_reclaim` |
| 4 | Book 3 | `2025-10-28 09:00` | `2025-10-28 10:00` | 1.0h | `$0.2154` | `$0.1976` | **-8.23%** | **-8.59%** | +7.3% | -16.7% | `stop_loss` |
| 5 | Book 3 | `2026-09-24 00:00` | `2026-09-26 18:00` | 66.0h | `$0.0331` | `$0.0359` | **+8.70%** | **+8.34%** | +9.1% | -2.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `MAVIA`

* **Total Candidate Breakouts Filtered (Vetoed):** `27`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `21` (77.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `7`
* **Saved Capital Losses Avoided:** `+380.9%`
* **Missed Upside Forgone:** `-258.7%`
* **Net Veto Alpha:** `+122.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `14` | `51.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `9` | `33.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `11.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `3.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*