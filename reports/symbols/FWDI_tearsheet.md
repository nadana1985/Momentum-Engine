# Kronos V12: Institutional Symbol Tear Sheet — `FWDI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.921`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+7.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.64%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`15.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.4% / -8.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-07-14 14:00` | `2026-07-18 14:00` | Live | `$4.1584` | `$4.5119` | **+8.50%** | **+8.16%** | +17.2% | -16.6% | `shelf_target_reclaim` |
| 2 | Book 3 | `2026-08-28 15:00` | `2026-08-28 19:00` | 4.0h | `$6.3949` | `$5.8686` | **-8.23%** | **-8.59%** | +1.7% | -8.1% | `stop_loss` |
| 3 | Book 3 | `2026-09-24 09:00` | `2026-09-25 11:00` | 26.0h | `$7.9433` | `$8.6340` | **+8.70%** | **+8.34%** | +9.1% | -0.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `FWDI`

* **Total Candidate Breakouts Filtered (Vetoed):** `18`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `8` (44.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `1`
* **Saved Capital Losses Avoided:** `+107.2%`
* **Missed Upside Forgone:** `-28.6%`
* **Net Veto Alpha:** `+78.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `8` | `44.4%` |
| `Core 1: Macro Bear Veto` | `5` | `27.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `16.7%` |
| `Core 4: Defensible Whale Dump` | `2` | `11.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*