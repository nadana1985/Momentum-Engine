# Kronos V12: Institutional Symbol Tear Sheet — `STG`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.445`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+19.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.21x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.33%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-4.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`82.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.6% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-01-09 00:00` | `2023-01-16 00:00` | 168.0h | `$0.3734` | `$0.4701` | **+25.89%** | **+23.03%** | +29.3% | -1.1% | `time_cap` |
| 2 | Book 2 | `2024-08-10 16:00` | `2024-08-12 00:00` | 32.0h | `$0.3374` | `$0.3383` | **+0.25%** | **+0.25%** | +18.0% | -1.8% | `breakeven_ratchet` |
| 3 | Book 2 | `2024-09-15 04:00` | `2024-09-17 04:00` | 48.0h | `$0.3032` | `$0.2905` | **-4.18%** | **-4.27%** | +5.4% | -5.9% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-4.3%`** |
| `time_cap` | `1` | `100.0%` | **`+23.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `STG`

* **Total Candidate Breakouts Filtered (Vetoed):** `215`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `126` (58.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `25`
* **Saved Capital Losses Avoided:** `+1,675.3%`
* **Missed Upside Forgone:** `-817.5%`
* **Net Veto Alpha:** `+857.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `87` | `40.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `66` | `30.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `33` | `15.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `29` | `13.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*