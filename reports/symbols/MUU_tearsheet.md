# Kronos V12: Institutional Symbol Tear Sheet — `MUU`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-7.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.93x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.64%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`55.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.1% / -4.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-08 19:00` | `2026-09-11 19:00` | 72.0h | `$33.5616` | `$31.3614` | **-6.56%** | **-6.78%** | +7.4% | -7.7% | `time_expiry` |
| 2 | Book 3 | `2026-10-03 01:00` | `2026-10-04 15:00` | 38.0h | `$36.6620` | `$36.4786` | **-0.50%** | **-0.50%** | +0.8% | -0.6% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `1` | `0.0%` | **`-0.5%`** |
| `time_expiry` | `1` | `0.0%` | **`-6.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `MUU`

* **Total Candidate Breakouts Filtered (Vetoed):** `9`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `8` (88.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+111.3%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+111.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5` | `55.6%` |
| `Core 1: Macro Bear Veto` | `3` | `33.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `11.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*