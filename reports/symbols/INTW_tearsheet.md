# Kronos V12: Institutional Symbol Tear Sheet — `INTW`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.312`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+23.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.26x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.85%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-10.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`71.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.8% / -15.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-07-15 01:00` | `2026-07-19 01:00` | Live | `$27.7564` | `$30.1157` | **+8.50%** | **+8.16%** | +3.6% | -47.2% | `shelf_target_reclaim` |
| 2 | Book 2 | `2026-08-28 13:00` | `2026-08-28 16:00` | 3.0h | `$19.9698` | `$18.3263` | **-9.69%** | **-10.11%** | +0.9% | -8.4% | `initial_stop` |
| 3 | Book 2 | `2026-09-04 13:00` | `2026-09-11 13:00` | 168.0h | `$20.5913` | `$24.5186` | **+22.05%** | **+20.18%** | +25.1% | -6.0% | `time_cap` |
| 4 | Book 3 | `2026-09-25 15:00` | `2026-09-27 10:00` | 43.0h | `$33.1903` | `$34.9500` | **+5.30%** | **+5.17%** | +5.5% | -2.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-10.1%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+5.2%`** |
| `time_cap` | `1` | `100.0%` | **`+20.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `INTW`

* **Total Candidate Breakouts Filtered (Vetoed):** `61`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `7` (11.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+59.5%`
* **Missed Upside Forgone:** `-275.1%`
* **Net Veto Alpha:** `+-215.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `61` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*