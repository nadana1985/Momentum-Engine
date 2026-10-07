# Kronos V12: Institutional Symbol Tear Sheet — `MTL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.473`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+4.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.05x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.54%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`87.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.1% / -4.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 17:00` | `2022-10-27 20:00` | 51.0h | `$1.0152` | `$1.0033` | **-1.18%** | **-1.18%** | +3.4% | -2.4% | `fast_decay_cut` |
| 2 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$1.0646` | `$1.2293` | **+15.48%** | **+14.39%** | +21.5% | -3.6% | `time_cap` |
| 3 | Book 2 | `2024-08-10 11:00` | `2024-08-12 06:00` | 43.0h | `$1.0153` | `$0.9318` | **-8.23%** | **-8.59%** | +2.2% | -8.6% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `time_cap` | `1` | `100.0%` | **`+14.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `MTL`

* **Total Candidate Breakouts Filtered (Vetoed):** `233`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `144` (61.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `37`
* **Saved Capital Losses Avoided:** `+1,821.2%`
* **Missed Upside Forgone:** `-1,772.2%`
* **Net Veto Alpha:** `+49.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `82` | `35.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `79` | `33.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `48` | `20.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `13` | `5.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `11` | `4.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*