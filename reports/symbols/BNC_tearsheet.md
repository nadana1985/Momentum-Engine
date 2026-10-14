# Kronos V12: Institutional Symbol Tear Sheet — `BNC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`8.526`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+7.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.89%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`43.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.5% / -2.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-21 00:00` | `2026-08-21 14:00` | 14.0h | `$2.6362` | `$2.8790` | **+9.21%** | **+8.81%** | +16.6% | -0.1% | `target_reclaim` |
| 2 | Book 3 | `2026-09-22 02:00` | `2026-09-25 02:00` | 72.0h | `$6.2276` | `$6.1636` | **-1.03%** | **-1.03%** | +6.4% | -5.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+8.8%`** |
| `time_expiry` | `1` | `0.0%` | **`-1.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `BNC`

* **Total Candidate Breakouts Filtered (Vetoed):** `25`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `10` (40.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `10`
* **Saved Capital Losses Avoided:** `+85.5%`
* **Missed Upside Forgone:** `-631.1%`
* **Net Veto Alpha:** `+-545.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `12` | `48.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `10` | `40.0%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `8.0%` |
| `Core 1: Macro Bear Veto` | `1` | `4.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*