# Kronos V12: Institutional Symbol Tear Sheet — `CRWD`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+13.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.14x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.52%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.3% / -3.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-14 13:00` | `2026-09-21 13:00` | 168.0h | `$227.6978` | `$245.8439` | **+7.97%** | **+7.67%** | +9.9% | -4.8% | `time_cap` |
| 2 | Book 2 | `2026-09-29 19:00` | `2026-10-06 19:00` | 168.0h | `$263.4871` | `$278.0531` | **+5.53%** | **+5.38%** | +8.8% | -1.6% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `100.0%` | **`+13.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `CRWD`

* **Total Candidate Breakouts Filtered (Vetoed):** `18`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `13` (72.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+568.4%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+568.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `14` | `77.8%` |
| `Core 4: Defensible Whale Dump` | `3` | `16.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `5.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*