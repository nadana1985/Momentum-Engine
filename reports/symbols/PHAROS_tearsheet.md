# Kronos V12: Institutional Symbol Tear Sheet — `PHAROS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.650`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-6.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.50%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`29.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.8% / -4.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-26 12:00` | `2026-08-29 12:00` | 72.0h | `$0.4076` | `$0.4192` | **+2.87%** | **+2.83%** | +4.5% | -1.4% | `time_expiry` |
| 2 | Book 3 | `2026-09-09 05:00` | `2026-09-09 15:00` | 10.0h | `$0.4949` | `$0.4541` | **-8.23%** | **-8.59%** | +15.0% | -8.4% | `stop_loss` |
| 3 | Book 3 | `2026-09-20 12:00` | `2026-09-21 05:00` | 17.0h | `$0.4981` | `$0.5414` | **+8.70%** | **+8.34%** | +13.8% | -0.4% | `target_reclaim` |
| 4 | Book 3 | `2026-10-06 00:00` | `2026-10-06 17:00` | 17.0h | `$0.7308` | `$0.6707` | **-8.23%** | **-8.59%** | +2.1% | -8.6% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+2.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `PHAROS`

* **Total Candidate Breakouts Filtered (Vetoed):** `13`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `8` (61.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+106.3%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+106.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `5` | `38.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `5` | `38.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `23.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*