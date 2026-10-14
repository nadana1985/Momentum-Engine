# Kronos V12: Institutional Symbol Tear Sheet — `BTC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`62.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.700`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+18.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.20x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.25%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`241.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.1% / -6.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2020-11-26 03:00` | `2020-11-26 08:00` | 5.0h | `$18271.9488` | `$16768.1674` | **-8.23%** | **-8.59%** | +0.8% | -10.7% | `stop_loss` |
| 2 | Book 3 | `2021-01-04 09:00` | `2021-01-04 10:00` | 1.0h | `$31117.6936` | `$28556.7074` | **-8.23%** | **-8.59%** | +3.6% | -10.7% | `stop_loss` |
| 3 | Book 3 | `2021-02-22 12:00` | `2021-02-22 14:00` | 2.0h | `$52789.4160` | `$48444.8471` | **-8.23%** | **-8.59%** | +3.8% | -9.5% | `stop_loss` |
| 4 | Book 4 | `2021-07-27 22:00` | `2021-08-13 20:00` | 406.0h | `$39205.7505` | `$47046.9007` | **+23.98%** | **+21.86%** | +22.4% | -4.9% | `target_reclaim` |
| 5 | Book 4 | `2023-01-14 03:00` | `2023-02-13 02:00` | 719.0h | `$21027.7945` | `$21717.5747` | **+4.11%** | **+4.04%** | +15.5% | -3.7% | `time_expiry` |
| 6 | Book 3 | `2024-01-03 12:00` | `2024-01-06 12:00` | 72.0h | `$43372.6080` | `$43498.3815` | **+0.29%** | **+0.29%** | +3.4% | -7.0% | `time_expiry` |
| 7 | Book 3 | `2024-03-05 19:00` | `2024-03-06 05:00` | 10.0h | `$61471.0943` | `$65331.4000` | **+6.28%** | **+6.09%** | +8.2% | -3.8% | `target_reclaim` |
| 8 | Book 4 | `2026-08-20 08:00` | `2026-09-19 07:00` | 719.0h | `$71667.9409` | `$80955.3845` | **+12.27%** | **+11.53%** | +14.8% | -0.8% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_expiry` | `3` | `100.0%` | **`+15.9%`** |
| `target_reclaim` | `2` | `100.0%` | **`+27.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `BTC`

* **Total Candidate Breakouts Filtered (Vetoed):** `287`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `131` (45.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+886.6%`
* **Missed Upside Forgone:** `-113.3%`
* **Net Veto Alpha:** `+773.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: Defensible Whale Dump` | `134` | `46.7%` |
| `Core 1: Macro Bear Veto` | `61` | `21.3%` |
| `Core 4: Funding Rate Cap` | `58` | `20.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `19` | `6.6%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `10` | `3.5%` |
| `Core 4: Whale Firewall` | `5` | `1.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*