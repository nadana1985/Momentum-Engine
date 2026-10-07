# Kronos V12: Institutional Symbol Tear Sheet — `BABY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.031`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-8.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.16%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`54.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.0% / -8.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-13 02:00` | `2025-05-14 15:00` | 37.0h | `$0.1052` | `$0.0965` | **-8.23%** | **-8.59%** | +3.2% | -8.2% | `stop_loss` |
| 2 | Book 3 | `2025-08-10 08:00` | `2025-08-13 08:00` | 72.0h | `$0.0634` | `$0.0635` | **+0.27%** | **+0.27%** | +6.9% | -7.9% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+0.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `BABY`

* **Total Candidate Breakouts Filtered (Vetoed):** `37`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `30` (81.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+437.2%`
* **Missed Upside Forgone:** `-648.0%`
* **Net Veto Alpha:** `+-210.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `18` | `48.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `18.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `6` | `16.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `16.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*