# Kronos V12: Institutional Symbol Tear Sheet — `BIGTIME`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`77.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.075`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+35.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.43x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.96%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`16.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.0% / -5.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-11-13 14:00` | `2023-11-13 17:00` | 3.0h | `$0.1845` | `$0.1694` | **-8.23%** | **-8.59%** | +14.2% | -13.6% | `stop_loss` |
| 2 | Book 3 | `2023-12-04 14:00` | `2023-12-04 15:00` | 1.0h | `$0.5100` | `$0.5543` | **+8.70%** | **+8.34%** | +13.0% | -2.0% | `target_reclaim` |
| 3 | Book 3 | `2023-12-06 11:00` | `2023-12-06 15:00` | 4.0h | `$0.6128` | `$0.6661` | **+8.70%** | **+8.34%** | +12.4% | -4.8% | `target_reclaim` |
| 4 | Book 3 | `2024-03-03 07:00` | `2024-03-03 08:00` | 1.0h | `$0.4371` | `$0.4835` | **+10.62%** | **+10.09%** | +16.9% | -8.3% | `target_reclaim` |
| 5 | Book 3 | `2024-03-10 14:00` | `2024-03-10 15:00` | 1.0h | `$0.5498` | `$0.5769` | **+4.92%** | **+4.80%** | +7.2% | -2.3% | `target_reclaim` |
| 6 | Book 3 | `2024-09-16 13:00` | `2024-09-16 23:00` | 10.0h | `$0.1128` | `$0.1207` | **+6.99%** | **+6.75%** | +7.4% | -0.5% | `target_reclaim` |
| 7 | Book 3 | `2024-10-21 08:00` | `2024-10-22 15:00` | 31.0h | `$0.1459` | `$0.1675` | **+14.83%** | **+13.83%** | +15.1% | -4.0% | `target_reclaim` |
| 8 | Book 3 | `2024-10-23 05:00` | `2024-10-26 05:00` | 72.0h | `$0.1686` | `$0.1698` | **+0.67%** | **+0.67%** | +11.8% | -7.1% | `time_expiry` |
| 9 | Book 3 | `2024-12-08 05:00` | `2024-12-09 07:00` | 26.0h | `$0.2224` | `$0.2041` | **-8.23%** | **-8.59%** | +1.0% | -8.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+52.2%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+0.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `BIGTIME`

* **Total Candidate Breakouts Filtered (Vetoed):** `401`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `290` (72.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `34`
* **Saved Capital Losses Avoided:** `+3,767.9%`
* **Missed Upside Forgone:** `-2,185.7%`
* **Net Veto Alpha:** `+1,582.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `330` | `82.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `29` | `7.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `23` | `5.7%` |
| `Core 1: Macro Bear Veto` | `19` | `4.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*