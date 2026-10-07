# Kronos V12: Institutional Symbol Tear Sheet — `DOT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `12` (`12` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `12` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`41.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.541`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+18.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.20x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.53%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-19.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`157.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.1% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-03-27 20:00` | `2022-04-03 20:00` | 168.0h | `$21.6961` | `$23.0313` | **+6.15%** | **+5.97%** | +9.9% | -5.2% | `time_cap` |
| 2 | Book 2 | `2022-10-25 15:00` | `2022-11-01 15:00` | 168.0h | `$6.1644` | `$6.4937` | **+5.34%** | **+5.20%** | +10.8% | -1.1% | `time_cap` |
| 3 | Book 1 | `2023-01-11 23:00` | `2023-02-01 23:00` | 504.0h | `$5.1418` | `$6.4468` | **+31.13%** | **+27.10%** | +32.5% | -2.6% | `time_cap` |
| 4 | Book 2 | `2023-03-14 12:00` | `2023-03-15 16:00` | 28.0h | `$6.3639` | `$5.8401` | **-8.23%** | **-8.59%** | +2.7% | -9.3% | `initial_stop` |
| 5 | Book 1 | `2023-03-18 00:00` | `2023-03-19 12:00` | 36.0h | `$6.6827` | `$6.4159` | **-3.40%** | **-3.46%** | +0.3% | -6.0% | `stall_bailout` |
| 6 | Book 2 | `2023-06-21 01:00` | `2023-06-28 01:00` | 168.0h | `$4.7087` | `$5.0434` | **+7.11%** | **+6.87%** | +11.3% | -1.4% | `time_cap` |
| 7 | Book 2 | `2023-10-01 10:00` | `2023-10-04 00:00` | 62.0h | `$4.1945` | `$4.0019` | **-4.59%** | **-4.70%** | +2.4% | -5.9% | `initial_stop` |
| 8 | Book 2 | `2023-10-16 05:00` | `2023-10-17 13:00` | 32.0h | `$3.8065` | `$3.6457` | **-4.22%** | **-4.32%** | +2.5% | -4.9% | `initial_stop` |
| 9 | Book 2 | `2023-10-21 14:00` | `2023-10-28 14:00` | 168.0h | `$3.8696` | `$4.1566` | **+7.41%** | **+7.15%** | +15.0% | -1.8% | `time_cap` |
| 10 | Book 1 | `2023-11-06 22:00` | `2023-11-08 10:00` | 36.0h | `$5.0015` | `$4.9476` | **-0.86%** | **-0.86%** | +0.2% | -5.6% | `stall_bailout` |
| 11 | Book 2 | `2025-06-09 21:00` | `2025-06-13 00:00` | 75.0h | `$4.1463` | `$3.8457` | **-7.25%** | **-7.53%** | +4.7% | -10.7% | `initial_stop` |
| 12 | Book 1 | `2025-07-11 05:00` | `2025-07-29 16:00` | 443.0h | `$3.9879` | `$3.8504` | **-4.38%** | **-4.48%** | +17.3% | -4.9% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `5` | `0.0%` | **`-29.6%`** |
| `time_cap` | `5` | `100.0%` | **`+52.3%`** |
| `stall_bailout` | `2` | `0.0%` | **`-4.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `DOT`

* **Total Candidate Breakouts Filtered (Vetoed):** `226`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `134` (59.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+1,833.3%`
* **Missed Upside Forgone:** `-984.8%`
* **Net Veto Alpha:** `+848.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `125` | `55.3%` |
| `Core 1: Macro Bear Veto` | `75` | `33.2%` |
| `Core 4: Funding Rate Cap` | `26` | `11.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*