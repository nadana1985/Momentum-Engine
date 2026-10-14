# Kronos V12: Institutional Symbol Tear Sheet — `CARV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`6.939`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+3.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.75%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`45.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.7% / -2.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-23 03:00` | `2026-08-26 03:00` | 72.0h | `$0.0320` | `$0.0318` | **-0.59%** | **-0.59%** | +4.2% | -4.1% | `time_expiry` |
| 2 | Book 3 | `2026-09-20 10:00` | `2026-09-21 04:00` | 18.0h | `$0.0372` | `$0.0388` | **+4.17%** | **+4.08%** | +5.2% | -0.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+4.1%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CARV`

* **Total Candidate Breakouts Filtered (Vetoed):** `22`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `13` (59.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `7`
* **Saved Capital Losses Avoided:** `+129.9%`
* **Missed Upside Forgone:** `-227.3%`
* **Net Veto Alpha:** `+-97.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `13` | `59.1%` |
| `Core 1: Macro Bear Veto` | `9` | `40.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*