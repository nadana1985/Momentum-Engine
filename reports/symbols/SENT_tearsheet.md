# Kronos V12: Institutional Symbol Tear Sheet — `SENT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.457`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+23.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.26x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+7.75%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`83.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.2% / -8.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2026-09-08 01:00` | `2026-09-10 13:00` | 60.0h | `$0.0147` | `$0.0134` | **-14.88%** | **-15.96%** | +5.0% | -11.0% | `fast_decay_cut` |
| 2 | Book 1 | `2026-09-14 16:00` | `2026-09-21 13:00` | 165.0h | `$0.0159` | `$0.0191` | **+29.43%** | **+25.80%** | +21.3% | -11.0% | `target_reclaim` |
| 3 | Book 4 | `2026-09-22 05:00` | `2026-09-23 06:00` | 25.0h | `$0.0195` | `$0.0235` | **+14.30%** | **+13.41%** | +22.2% | -4.6% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+39.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-16.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `SENT`

* **Total Candidate Breakouts Filtered (Vetoed):** `19`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `16` (84.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+196.1%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+196.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `19` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*