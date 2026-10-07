# Kronos V12: Institutional Symbol Tear Sheet — `ORDER`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.217`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+5.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.87%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-2.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`38.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.7% / -3.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-09 22:00` | `2026-09-10 03:00` | 5.0h | `$0.0341` | `$0.0371` | **+8.70%** | **+8.34%** | +10.7% | -1.2% | `target_reclaim` |
| 2 | Book 3 | `2026-09-11 00:00` | `2026-09-14 00:00` | 72.0h | `$0.0350` | `$0.0341` | **-2.56%** | **-2.59%** | +4.6% | -5.1% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `0.0%` | **`-2.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `ORDER`

* **Total Candidate Breakouts Filtered (Vetoed):** `27`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `25` (92.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+274.8%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+274.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `21` | `77.8%` |
| `Core 1: Macro Bear Veto` | `6` | `22.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*