# Kronos V12: Institutional Symbol Tear Sheet — `MERL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.441`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-5.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.86%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-10.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`54.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.0% / -14.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-07 00:00` | `2025-07-10 00:00` | 72.0h | `$0.1049` | `$0.1096` | **+4.50%** | **+4.41%** | +6.0% | -2.5% | `time_expiry` |
| 2 | Book 3 | `2025-10-27 23:00` | `2025-10-28 18:00` | 19.0h | `$0.3637` | `$0.3338` | **-8.23%** | **-8.59%** | +4.0% | -24.4% | `stop_loss` |
| 3 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0198` | `$0.0196` | **-1.40%** | **-1.41%** | +17.0% | -15.3% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `2` | `50.0%` | **`+3.0%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `MERL`

* **Total Candidate Breakouts Filtered (Vetoed):** `105`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `97` (92.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `52`
* **Saved Capital Losses Avoided:** `+1,664.1%`
* **Missed Upside Forgone:** `-1,580.2%`
* **Net Veto Alpha:** `+83.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `58` | `55.2%` |
| `Core 1: Macro Bear Veto` | `36` | `34.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `7.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `2.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*