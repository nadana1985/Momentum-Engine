# Kronos V12: Institutional Symbol Tear Sheet — `TST`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.125`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+15.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.17x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.82%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`20.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+23.2% / -6.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-11 11:00` | `2025-07-11 12:00` | 1.0h | `$0.0451` | `$0.0512` | **+13.64%** | **+12.78%** | +29.2% | -3.4% | `target_reclaim` |
| 2 | Book 3 | `2025-09-17 11:00` | `2025-09-17 12:00` | 1.0h | `$0.0455` | `$0.0418` | **-8.23%** | **-8.59%** | +9.8% | -8.5% | `stop_loss` |
| 3 | Book 2 | `2026-05-04 04:00` | `2026-05-04 10:00` | 6.0h | `$0.0192` | `$0.0226` | **+17.48%** | **+16.11%** | +48.3% | -8.9% | `trail_stop` |
| 4 | Book 3 | `2026-09-06 14:00` | `2026-09-09 14:00` | 72.0h | `$0.0178` | `$0.0169` | **-4.89%** | **-5.01%** | +5.4% | -6.3% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |
| `time_expiry` | `1` | `0.0%` | **`-5.0%`** |
| `trail_stop` | `1` | `100.0%` | **`+16.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `TST`

* **Total Candidate Breakouts Filtered (Vetoed):** `28`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `26` (92.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+570.4%`
* **Missed Upside Forgone:** `-397.0%`
* **Net Veto Alpha:** `+173.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `22` | `78.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `5` | `17.9%` |
| `Core 4: Funding Rate Cap` | `1` | `3.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*