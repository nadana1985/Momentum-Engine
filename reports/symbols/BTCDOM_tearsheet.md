# Kronos V12: Institutional Symbol Tear Sheet — `BTCDOM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.405`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+6.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.24%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-13.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`180.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.2% / -4.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-09-19 11:00` | `2021-10-11 19:00` | 536.0h | `$1007.5090` | `$1209.0108` | **+20.68%** | **+19.08%** | +20.3% | -1.4% | `target_reclaim` |
| 2 | Book 3 | `2024-01-11 00:00` | `2024-01-14 00:00` | 72.0h | `$2121.9400` | `$1984.6260` | **-6.47%** | **-6.69%** | +2.2% | -7.3% | `time_expiry` |
| 3 | Book 3 | `2025-01-19 14:00` | `2025-01-22 14:00` | 72.0h | `$3114.2400` | `$3170.3543` | **+1.80%** | **+1.79%** | +4.1% | -1.1% | `time_expiry` |
| 4 | Book 3 | `2025-05-08 12:00` | `2025-05-10 17:00` | 53.0h | `$5272.0320` | `$4838.1438` | **-8.23%** | **-8.59%** | +2.3% | -8.5% | `stop_loss` |
| 5 | Book 4 | `2025-10-16 20:00` | `2025-10-23 20:00` | 168.0h | `$4281.9133` | `$4331.6927` | **+0.61%** | **+0.61%** | +2.4% | -2.8% | `stagnation_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `2` | `50.0%` | **`-4.9%`** |
| `stagnation_cut` | `1` | `100.0%` | **`+0.6%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+19.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `BTCDOM`

* **Total Candidate Breakouts Filtered (Vetoed):** `939`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `531` (56.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `7`
* **Saved Capital Losses Avoided:** `+2,033.1%`
* **Missed Upside Forgone:** `-214.9%`
* **Net Veto Alpha:** `+1,818.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `392` | `41.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `371` | `39.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `67` | `7.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `63` | `6.7%` |
| `Core 4: Defensible Whale Dump` | `25` | `2.7%` |
| `Core 3: Min Turnover Velocity` | `15` | `1.6%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `6` | `0.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*