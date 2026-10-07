# Kronos V12: Institutional Symbol Tear Sheet — `INTW`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.032`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+8.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.09x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.43%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`85.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.0% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-28 13:00` | `2026-08-28 16:00` | 3.0h | `$19.9698` | `$18.3263` | **-8.23%** | **-8.59%** | +0.9% | -8.4% | `initial_stop` |
| 2 | Book 2 | `2026-09-04 13:00` | `2026-09-11 13:00` | 168.0h | `$20.5913` | `$24.5186` | **+19.07%** | **+17.46%** | +25.1% | -6.0% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `time_cap` | `1` | `100.0%` | **`+17.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `INTW`

* **Total Candidate Breakouts Filtered (Vetoed):** `16`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `8` (50.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `1`
* **Saved Capital Losses Avoided:** `+75.8%`
* **Missed Upside Forgone:** `-20.1%`
* **Net Veto Alpha:** `+55.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `16` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*