# Kronos V12: Institutional Symbol Tear Sheet — `USELESS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.198`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+3.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.85%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-10.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`8.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.4% / -4.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-05 05:00` | `2026-09-05 08:00` | 3.0h | `$0.2128` | `$0.2445` | **+14.85%** | **+13.85%** | +15.5% | -0.9% | `target_reclaim` |
| 2 | Book 3 | `2026-09-05 20:00` | `2026-09-06 05:00` | 9.0h | `$0.2588` | `$0.2375` | **-8.23%** | **-8.59%** | +11.9% | -9.0% | `stop_loss` |
| 3 | Book 3 | `2026-09-09 09:00` | `2026-09-09 10:00` | 1.0h | `$0.3022` | `$0.3232` | **+6.96%** | **+6.73%** | +8.0% | -0.3% | `target_reclaim` |
| 4 | Book 3 | `2026-09-23 15:00` | `2026-09-24 12:00` | 21.0h | `$0.2963` | `$0.2719` | **-8.23%** | **-8.59%** | +10.2% | -8.8% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+20.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `USELESS`

* **Total Candidate Breakouts Filtered (Vetoed):** `52`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `40` (76.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `10`
* **Saved Capital Losses Avoided:** `+883.6%`
* **Missed Upside Forgone:** `-316.7%`
* **Net Veto Alpha:** `+566.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `42` | `80.8%` |
| `Core 4: Defensible Whale Dump` | `4` | `7.7%` |
| `Core 4: Whale Firewall` | `3` | `5.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `3.8%` |
| `Core 4: Funding Rate Cap` | `1` | `1.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*