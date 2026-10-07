# Kronos V12: Institutional Symbol Tear Sheet — `ARIA`
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
| **Cumulative Net Log Return** | **`+16.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.34%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`23.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+29.0% / -5.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-27 02:00` | `2026-08-27 03:00` | 1.0h | `$0.0365` | `$0.0397` | **+8.70%** | **+8.34%** | +48.2% | -8.6% | `target_reclaim` |
| 2 | Book 3 | `2026-09-23 20:00` | `2026-09-25 18:00` | 46.0h | `$0.0351` | `$0.0381` | **+8.70%** | **+8.34%** | +9.9% | -3.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `ARIA`

* **Total Candidate Breakouts Filtered (Vetoed):** `55`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `38` (69.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+938.3%`
* **Missed Upside Forgone:** `-689.4%`
* **Net Veto Alpha:** `+248.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `51` | `92.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `5.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*