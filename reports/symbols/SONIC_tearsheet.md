# Kronos V12: Institutional Symbol Tear Sheet — `SONIC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`37.979`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+16.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.41%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-0.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.6% / -2.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-24 07:00` | `2025-04-26 00:00` | 41.0h | `$0.2383` | `$0.2590` | **+8.70%** | **+8.34%** | +8.8% | -0.1% | `target_reclaim` |
| 2 | Book 3 | `2025-06-17 15:00` | `2025-06-20 15:00` | 72.0h | `$0.2015` | `$0.2006` | **-0.44%** | **-0.44%** | +4.8% | -2.0% | `time_expiry` |
| 3 | Book 3 | `2025-07-24 05:00` | `2025-07-25 12:00` | 31.0h | `$0.2384` | `$0.2591` | **+8.70%** | **+8.34%** | +9.1% | -6.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `SONIC`

* **Total Candidate Breakouts Filtered (Vetoed):** `52`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `36` (69.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+355.6%`
* **Missed Upside Forgone:** `-47.6%`
* **Net Veto Alpha:** `+308.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `19` | `36.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `18` | `34.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `15` | `28.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*