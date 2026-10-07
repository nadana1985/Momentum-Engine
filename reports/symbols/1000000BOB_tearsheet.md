# Kronos V12: Institutional Symbol Tear Sheet — `1000000BOB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.273`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-55.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.58x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-11.03%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-75.9%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`24.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.1% / -16.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-09 11:00` | `2025-07-09 17:00` | 6.0h | `$0.0690` | `$0.0750` | **+8.70%** | **+8.34%** | +12.9% | -6.3% | `target_reclaim` |
| 2 | Book 3 | `2025-07-29 14:00` | `2025-07-31 06:00` | 40.0h | `$0.0552` | `$0.0600` | **+8.70%** | **+8.34%** | +8.7% | -2.7% | `target_reclaim` |
| 3 | Book 3 | `2025-08-05 06:00` | `2025-08-08 06:00` | 72.0h | `$0.0685` | `$0.0713` | **+4.11%** | **+4.03%** | +8.1% | -7.2% | `time_expiry` |
| 4 | Book 3 | `2026-09-06 12:00` | `2026-09-06 13:00` | 1.0h | `$0.0211` | `$0.0193` | **-8.23%** | **-8.59%** | +16.1% | -10.6% | `stop_loss` |
| 5 | Book 3 | `2026-10-05 08:00` | `2026-10-05 09:00` | 1.0h | `$0.0188` | `$0.0096` | **-48.98%** | **-67.29%** | +39.6% | -54.6% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-75.9%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `time_expiry` | `1` | `100.0%` | **`+4.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000000BOB`

* **Total Candidate Breakouts Filtered (Vetoed):** `37`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `32` (86.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+588.6%`
* **Missed Upside Forgone:** `-248.8%`
* **Net Veto Alpha:** `+339.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `22` | `59.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `10` | `27.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `4` | `10.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `2.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*