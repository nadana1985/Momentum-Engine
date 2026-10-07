# Kronos V12: Institutional Symbol Tear Sheet — `CRDO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`2` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.959`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+10.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.12x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.46%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`108.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.4% / -3.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-27 08:00` | `2026-08-29 08:00` | 48.0h | `$242.0937` | `$233.3252` | **-3.62%** | **-3.69%** | +1.2% | -5.5% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-16 23:00` | `2026-09-23 23:00` | 168.0h | `$166.6656` | `$192.8766` | **+15.73%** | **+14.61%** | +17.6% | -1.8% | `time_cap` |
| 3 | Book 2 | `2026-10-01 15:00` | `_Open Live_` | 133.9h | `$205.7631` | `$219.8100` | **+6.83%** | **+6.60%** | +12.3% | -2.2% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-3.7%`** |
| `time_cap` | `1` | `100.0%` | **`+14.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CRDO`

* **Total Candidate Breakouts Filtered (Vetoed):** `15`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `13` (86.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+123.6%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+123.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `15` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*