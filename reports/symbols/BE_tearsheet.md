# Kronos V12: Institutional Symbol Tear Sheet — `BE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`4` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`3.241`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+8.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.09x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.11%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-2.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`108.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.0% / -4.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-24 15:00` | `2026-08-31 15:00` | 168.0h | `$206.6052` | `$203.6596` | **-1.43%** | **-1.44%** | +12.8% | -4.7% | `time_cap` |
| 2 | Book 2 | `2026-09-03 15:00` | `2026-09-10 15:00` | 168.0h | `$235.5574` | `$266.0931` | **+12.96%** | **+12.19%** | +20.5% | -5.5% | `time_cap` |
| 3 | Book 2 | `2026-09-16 13:00` | `2026-09-18 13:00` | 48.0h | `$274.7151` | `$273.2053` | **-0.55%** | **-0.55%** | +5.2% | -4.5% | `fast_decay_cut` |
| 4 | Book 2 | `2026-09-21 15:00` | `2026-09-23 15:00` | 48.0h | `$279.6975` | `$274.7813` | **-1.76%** | **-1.77%** | +1.7% | -4.3% | `fast_decay_cut` |
| 5 | Book 2 | `2026-10-06 13:00` | `_Open Live_` | 15.9h | `$295.8578` | `$294.2600` | **-0.54%** | **-0.54%** | +1.7% | -3.3% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-2.3%`** |
| `time_cap` | `2` | `50.0%` | **`+10.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `BE`

* **Total Candidate Breakouts Filtered (Vetoed):** `9`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `4` (44.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+39.2%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+39.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `9` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*