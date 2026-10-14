# Kronos V12: Institutional Symbol Tear Sheet — `DOLO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.743`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+12.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.14x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.13%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`32.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.0% / -10.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-05-24 01:00` | `2025-05-28 01:00` | Live | `$0.0390` | `$0.0423` | **+8.50%** | **+8.16%** | +9.0% | -29.9% | `shelf_target_reclaim` |
| 2 | Book 3 | `2025-07-01 15:00` | `2025-07-02 01:00` | 10.0h | `$0.0375` | `$0.0345` | **-8.23%** | **-8.59%** | +4.7% | -9.9% | `stop_loss` |
| 3 | Book 3 | `2025-07-03 16:00` | `2025-07-06 16:00` | 72.0h | `$0.0375` | `$0.0385` | **+2.42%** | **+2.39%** | +7.3% | -1.4% | `time_expiry` |
| 4 | Book 4 | `2025-07-10 21:00` | `2025-07-12 15:00` | 42.0h | `$0.0485` | `$0.0485` | **+11.58%** | **+11.05%** | +62.1% | -2.7% | `donchian_floor` |
| 5 | Book 3 | `2025-07-23 12:00` | `2025-07-24 11:00` | 23.0h | `$0.0775` | `$0.0843` | **+8.70%** | **+8.34%** | +13.9% | -7.2% | `target_reclaim` |
| 6 | Book 3 | `2025-07-29 10:00` | `2025-07-30 00:00` | 14.0h | `$0.1665` | `$0.1528` | **-8.23%** | **-8.59%** | +17.1% | -12.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `donchian_floor` | `1` | `100.0%` | **`+11.1%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+2.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `DOLO`

* **Total Candidate Breakouts Filtered (Vetoed):** `354`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `188` (53.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `186`
* **Saved Capital Losses Avoided:** `+2,388.9%`
* **Missed Upside Forgone:** `-11,754.5%`
* **Net Veto Alpha:** `+-9,365.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `332` | `93.8%` |
| `Core 1: Macro Bear Veto` | `19` | `5.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*