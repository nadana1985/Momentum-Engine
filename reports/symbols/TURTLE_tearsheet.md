# Kronos V12: Institutional Symbol Tear Sheet — `TURTLE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`2` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+4.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.05x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.22%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`72.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.9% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0443` | `$0.0445` | **+0.59%** | **+0.58%** | +9.0% | -5.2% | `time_expiry` |
| 2 | Book 3 | `2026-09-29 01:00` | `2026-10-02 01:00` | 72.0h | `$0.0418` | `$0.0434` | **+3.94%** | **+3.86%** | +4.8% | -0.5% | `time_expiry` |
| 3 | Book 3 | `2026-10-05 19:00` | `_Open Live_` | 31.7h | `$0.0437` | `$0.0423` | **-3.35%** | **-3.41%** | +19.1% | -5.0% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `2` | `100.0%` | **`+4.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `TURTLE`

* **Total Candidate Breakouts Filtered (Vetoed):** `29`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `28` (96.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+312.8%`
* **Missed Upside Forgone:** `-48.7%`
* **Net Veto Alpha:** `+264.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `20` | `69.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `9` | `31.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*