# Kronos V12: Institutional Symbol Tear Sheet — `FOLKS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.971`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.13%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`5.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.2% / -9.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-11 07:00` | `2026-09-11 16:00` | 9.0h | `$2.0737` | `$1.9030` | **-8.23%** | **-8.59%** | +9.2% | -11.1% | `stop_loss` |
| 2 | Book 3 | `2026-09-23 14:00` | `2026-09-23 15:00` | 1.0h | `$2.1298` | `$2.3150` | **+8.70%** | **+8.34%** | +13.2% | -8.2% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `FOLKS`

* **Total Candidate Breakouts Filtered (Vetoed):** `39`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `35` (89.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+1,014.6%`
* **Missed Upside Forgone:** `-1,116.3%`
* **Net Veto Alpha:** `+-101.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `34` | `87.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `7.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `5.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*