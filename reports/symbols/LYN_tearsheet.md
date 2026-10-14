# Kronos V12: Institutional Symbol Tear Sheet — `LYN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.896`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+24.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.28x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.29%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`27.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+44.0% / -10.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-12-23 11:00` | `2025-12-27 11:00` | Live | `$0.0950` | `$0.1030` | **+8.50%** | **+8.16%** | +95.7% | -18.5% | `shelf_target_reclaim` |
| 2 | Book 4 | `2026-02-12 09:00` | `2026-02-14 14:00` | 53.0h | `$0.1848` | `$0.2217` | **+28.17%** | **+25.31%** | +20.4% | -2.7% | `target_reclaim` |
| 3 | Book 3 | `2026-09-25 17:00` | `2026-09-25 18:00` | 1.0h | `$0.0646` | `$0.0593` | **-8.23%** | **-8.59%** | +15.8% | -11.2% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+25.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `LYN`

* **Total Candidate Breakouts Filtered (Vetoed):** `414`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `78` (18.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `98`
* **Saved Capital Losses Avoided:** `+1,777.7%`
* **Missed Upside Forgone:** `-2,537.8%`
* **Net Veto Alpha:** `+-760.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `412` | `99.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `0.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*