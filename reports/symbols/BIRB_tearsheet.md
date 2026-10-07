# Kronos V12: Institutional Symbol Tear Sheet — `BIRB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.624`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+6.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.07x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.27%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`38.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.8% / -4.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-22 21:00` | `2026-08-25 21:00` | 72.0h | `$0.0553` | `$0.0543` | **-1.79%** | **-1.80%** | +7.3% | -4.4% | `time_expiry` |
| 2 | Book 3 | `2026-09-09 21:00` | `2026-09-10 01:00` | 4.0h | `$0.0610` | `$0.0663` | **+8.70%** | **+8.34%** | +12.3% | -4.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `0.0%` | **`-1.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `BIRB`

* **Total Candidate Breakouts Filtered (Vetoed):** `14`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `14` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+218.4%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+218.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `8` | `57.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5` | `35.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `7.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*