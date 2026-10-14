# Kronos V12: Institutional Symbol Tear Sheet — `KAT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.425`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+3.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.22%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`14.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.5% / -21.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-03-14 15:00` | `2026-03-18 15:00` | Live | `$0.0161` | `$0.0175` | **+8.50%** | **+8.16%** | +5.3% | -50.3% | `shelf_target_reclaim` |
| 2 | Book 3 | `2026-08-22 05:00` | `2026-08-22 13:00` | 8.0h | `$0.0047` | `$0.0049` | **+4.17%** | **+4.08%** | +7.4% | -4.6% | `target_reclaim` |
| 3 | Book 3 | `2026-09-10 04:00` | `2026-09-11 00:00` | 20.0h | `$0.0051` | `$0.0047` | **-8.23%** | **-8.59%** | +6.7% | -8.7% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+4.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `KAT`

* **Total Candidate Breakouts Filtered (Vetoed):** `32`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `27` (84.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `17`
* **Saved Capital Losses Avoided:** `+1,156.3%`
* **Missed Upside Forgone:** `-1,648.6%`
* **Net Veto Alpha:** `+-492.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `28` | `87.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `6.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `6.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*