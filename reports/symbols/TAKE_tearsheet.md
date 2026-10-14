# Kronos V12: Institutional Symbol Tear Sheet — `TAKE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.396`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+12.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.13x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.00%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`4.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+28.4% / -17.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-02-12 02:00` | `2026-02-16 02:00` | Live | `$0.0341` | `$0.0370` | **+8.50%** | **+8.16%** | +70.7% | -56.8% | `shelf_target_reclaim` |
| 2 | Book 3 | `2026-09-03 16:00` | `2026-09-03 17:00` | 1.0h | `$0.0615` | `$0.0641` | **+4.17%** | **+4.08%** | +8.2% | -0.4% | `target_reclaim` |
| 3 | Book 3 | `2026-09-04 06:00` | `2026-09-04 16:00` | 10.0h | `$0.0625` | `$0.0574` | **-8.23%** | **-8.59%** | +2.9% | -10.0% | `stop_loss` |
| 4 | Book 3 | `2026-09-23 15:00` | `2026-09-23 16:00` | 1.0h | `$0.0938` | `$0.1020` | **+8.70%** | **+8.34%** | +31.8% | -1.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+12.4%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `TAKE`

* **Total Candidate Breakouts Filtered (Vetoed):** `46`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `38` (82.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `27`
* **Saved Capital Losses Avoided:** `+1,240.5%`
* **Missed Upside Forgone:** `-1,326.7%`
* **Net Veto Alpha:** `+-86.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `37` | `80.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `3` | `6.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `6.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `6.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*