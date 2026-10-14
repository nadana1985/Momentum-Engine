# Kronos V12: Institutional Symbol Tear Sheet — `1000RATS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `12` (`12` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `12` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`58.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.550`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+25.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.29x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.13%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-38.0%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`11.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.9% / -12.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-28 17:00` | `2024-02-29 01:00` | 8.0h | `$0.2710` | `$0.3135` | **+15.69%** | **+14.57%** | +22.0% | -7.6% | `target_reclaim` |
| 2 | Book 3 | `2024-03-03 07:00` | `2024-03-03 14:00` | 7.0h | `$0.3254` | `$0.3692` | **+13.45%** | **+12.62%** | +23.2% | -10.4% | `target_reclaim` |
| 3 | Book 3 | `2024-03-05 19:00` | `2024-03-06 05:00` | 10.0h | `$0.3581` | `$0.4184` | **+16.84%** | **+15.56%** | +23.4% | -7.2% | `target_reclaim` |
| 4 | Book 3 | `2024-06-06 19:00` | `2024-06-07 04:00` | 9.0h | `$0.1704` | `$0.1804` | **+5.87%** | **+5.70%** | +12.1% | -2.4% | `target_reclaim` |
| 5 | Book 3 | `2024-06-07 06:00` | `2024-06-07 18:00` | 12.0h | `$0.1757` | `$0.1612` | **-8.23%** | **-8.59%** | +4.4% | -19.5% | `stop_loss` |
| 6 | Book 3 | `2024-09-25 23:00` | `2024-09-26 16:00` | 17.0h | `$0.1393` | `$0.1549` | **+11.17%** | **+10.59%** | +15.2% | -5.4% | `target_reclaim` |
| 7 | Book 3 | `2024-09-28 08:00` | `2024-09-29 07:00` | 23.0h | `$0.1578` | `$0.1448` | **-8.23%** | **-8.59%** | +2.7% | -8.7% | `stop_loss` |
| 8 | Book 3 | `2024-11-11 05:00` | `2024-11-12 10:00` | 29.0h | `$0.1219` | `$0.1119` | **-8.23%** | **-8.59%** | +10.6% | -14.1% | `stop_loss` |
| 9 | Book 3 | `2024-12-09 20:00` | `2024-12-09 21:00` | 1.0h | `$0.1128` | `$0.1035` | **-8.23%** | **-8.59%** | +2.2% | -23.1% | `stop_loss` |
| 10 | Book 3 | `2025-05-14 03:00` | `2025-05-14 04:00` | 1.0h | `$0.0364` | `$0.0322` | **-11.49%** | **-12.20%** | +12.0% | -21.6% | `stop_loss` |
| 11 | Book 3 | `2025-07-17 16:00` | `2025-07-17 23:00` | 7.0h | `$0.0217` | `$0.0228` | **+5.07%** | **+4.95%** | +5.5% | -0.4% | `target_reclaim` |
| 12 | Book 5 (Shelf Absorption Squeeze) | `2025-11-23 13:00` | `2025-11-27 13:00` | Live | `$0.0362` | `$0.0393` | **+8.50%** | **+8.16%** | +22.2% | -30.1% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+64.0%`** |
| `stop_loss` | `5` | `0.0%` | **`-46.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000RATS`

* **Total Candidate Breakouts Filtered (Vetoed):** `421`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `364` (86.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `86`
* **Saved Capital Losses Avoided:** `+7,094.1%`
* **Missed Upside Forgone:** `-3,720.5%`
* **Net Veto Alpha:** `+3,373.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `359` | `85.3%` |
| `Core 1: Macro Bear Veto` | `58` | `13.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `0.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*