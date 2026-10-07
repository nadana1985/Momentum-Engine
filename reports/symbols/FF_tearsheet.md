# Kronos V12: Institutional Symbol Tear Sheet — `FF`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.488`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+8.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.09x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.10%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`15.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.6% / -10.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-26 08:00` | `2026-08-26 09:00` | 1.0h | `$0.0900` | `$0.1023` | **+13.64%** | **+12.78%** | +14.0% | -9.1% | `target_reclaim` |
| 2 | Book 3 | `2026-09-03 06:00` | `2026-09-03 10:00` | 4.0h | `$0.0966` | `$0.1098` | **+13.64%** | **+12.78%** | +19.0% | -6.0% | `target_reclaim` |
| 3 | Book 3 | `2026-09-12 02:00` | `2026-09-14 11:00` | 57.0h | `$0.1500` | `$0.1376` | **-8.23%** | **-8.59%** | +10.0% | -8.9% | `stop_loss` |
| 4 | Book 3 | `2026-09-20 22:00` | `2026-09-20 23:00` | 1.0h | `$0.1600` | `$0.1468` | **-8.23%** | **-8.59%** | +15.5% | -18.3% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+25.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `FF`

* **Total Candidate Breakouts Filtered (Vetoed):** `26`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `17` (65.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `6`
* **Saved Capital Losses Avoided:** `+303.0%`
* **Missed Upside Forgone:** `-151.6%`
* **Net Veto Alpha:** `+151.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `18` | `69.2%` |
| `Core 4: Defensible Whale Dump` | `5` | `19.2%` |
| `Core 3: Min Turnover Velocity` | `3` | `11.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*