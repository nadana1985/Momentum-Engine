# Kronos V12: Institutional Symbol Tear Sheet — `BE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`7.937`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+11.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.12x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.70%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.7% / -5.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-24 15:00` | `2026-08-31 15:00` | 168.0h | `$206.6052` | `$203.6596` | **-1.63%** | **-1.64%** | +12.8% | -4.7% | `time_cap` |
| 2 | Book 2 | `2026-09-03 15:00` | `2026-09-10 15:00` | 168.0h | `$235.5574` | `$266.0931` | **+13.86%** | **+13.03%** | +20.5% | -5.5% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `50.0%` | **`+11.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `BE`

* **Total Candidate Breakouts Filtered (Vetoed):** `12`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `7` (58.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+62.5%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+62.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `9` | `75.0%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `3` | `25.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*