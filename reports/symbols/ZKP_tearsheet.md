# Kronos V12: Institutional Symbol Tear Sheet — `ZKP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`3` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`11.901`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+15.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.17x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.09%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`28.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.9% / -2.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-29 16:00` | `2026-08-30 00:00` | 8.0h | `$0.0478` | `$0.0519` | **+8.70%** | **+8.34%** | +19.3% | -3.6% | `target_reclaim` |
| 2 | Book 3 | `2026-08-30 04:00` | `2026-08-30 08:00` | 4.0h | `$0.0522` | `$0.0568` | **+8.70%** | **+8.34%** | +9.3% | -0.9% | `target_reclaim` |
| 3 | Book 3 | `2026-09-28 14:00` | `2026-10-01 14:00` | 72.0h | `$0.0483` | `$0.0476` | **-1.39%** | **-1.40%** | +4.1% | -2.5% | `time_expiry` |
| 4 | Book 3 | `2026-10-06 03:00` | `_Open Live_` | 23.7h | `$0.0498` | `$0.0473` | **-5.12%** | **-5.25%** | +1.4% | -5.2% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `time_expiry` | `1` | `0.0%` | **`-1.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZKP`

* **Total Candidate Breakouts Filtered (Vetoed):** `21`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `19` (90.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `3`
* **Saved Capital Losses Avoided:** `+282.0%`
* **Missed Upside Forgone:** `-63.5%`
* **Net Veto Alpha:** `+218.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `12` | `57.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `38.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `4.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*