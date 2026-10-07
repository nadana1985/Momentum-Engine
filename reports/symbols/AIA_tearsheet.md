# Kronos V12: Institutional Symbol Tear Sheet — `AIA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.924`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.23%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-9.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`27.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.2% / -9.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0709` | `$0.0771` | **+8.70%** | **+8.34%** | +17.1% | -14.3% | `target_reclaim` |
| 2 | Book 3 | `2026-08-28 05:00` | `2026-08-31 05:00` | 72.0h | `$0.0773` | `$0.0769` | **-0.43%** | **-0.43%** | +6.3% | -3.9% | `time_expiry` |
| 3 | Book 3 | `2026-09-09 13:00` | `2026-09-09 22:00` | 9.0h | `$0.0845` | `$0.0776` | **-8.23%** | **-8.59%** | +4.2% | -11.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `AIA`

* **Total Candidate Breakouts Filtered (Vetoed):** `26`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (92.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `7`
* **Saved Capital Losses Avoided:** `+541.2%`
* **Missed Upside Forgone:** `-201.8%`
* **Net Veto Alpha:** `+339.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `19` | `73.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `15.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `11.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*