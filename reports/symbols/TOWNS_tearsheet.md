# Kronos V12: Institutional Symbol Tear Sheet — `TOWNS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.687`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+6.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.07x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.28%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`55.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.7% / -12.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0025` | `$0.0025` | **-1.76%** | **-1.78%** | +13.7% | -20.5% | `time_expiry` |
| 2 | Book 3 | `2026-10-02 18:00` | `2026-10-04 09:00` | 39.0h | `$0.0021` | `$0.0023` | **+8.70%** | **+8.34%** | +19.7% | -4.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `0.0%` | **`-1.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `TOWNS`

* **Total Candidate Breakouts Filtered (Vetoed):** `13`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `13` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+267.3%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+267.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `9` | `69.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `30.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*