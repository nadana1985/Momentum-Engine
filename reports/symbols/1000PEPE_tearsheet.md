# Kronos V12: Institutional Symbol Tear Sheet — `1000PEPE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `17` (`17` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `17` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`47.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.523`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+40.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.50x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+2.39%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-42.9%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`54.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.1% / -10.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-05-07 19:00` | `2023-05-11 19:00` | Live | `$0.0026` | `$0.0024` | **-8.20%** | **-8.56%** | +-31.5% | -54.2% | `shelf_stop_loss` |
| 2 | Book 3 | `2023-06-22 14:00` | `2023-06-22 16:00` | 2.0h | `$0.0016` | `$0.0016` | **+4.17%** | **+4.08%** | +7.2% | -7.1% | `target_reclaim` |
| 3 | Book 3 | `2023-06-23 17:00` | `2023-06-24 12:00` | 19.0h | `$0.0016` | `$0.0017` | **+4.62%** | **+4.52%** | +7.2% | -4.5% | `target_reclaim` |
| 4 | Book 3 | `2023-07-05 10:00` | `2023-07-07 07:00` | 45.0h | `$0.0016` | `$0.0015` | **-8.23%** | **-8.59%** | +8.9% | -8.2% | `stop_loss` |
| 5 | Book 3 | `2023-11-09 16:00` | `2023-11-12 13:00` | 69.0h | `$0.0013` | `$0.0012` | **-8.23%** | **-8.59%** | +7.4% | -22.3% | `stop_loss` |
| 6 | Book 3 | `2023-12-04 11:00` | `2023-12-05 00:00` | 13.0h | `$0.0012` | `$0.0014` | **+16.74%** | **+15.48%** | +19.7% | -8.3% | `target_reclaim` |
| 7 | Book 3 | `2024-02-23 15:00` | `2024-02-25 18:00` | 51.0h | `$0.0012` | `$0.0014` | **+12.38%** | **+11.67%** | +13.7% | -6.0% | `target_reclaim` |
| 8 | Book 3 | `2024-03-02 06:00` | `2024-03-02 07:00` | 1.0h | `$0.0042` | `$0.0044` | **+5.19%** | **+5.06%** | +17.0% | -1.5% | `target_reclaim` |
| 9 | Book 3 | `2024-03-02 11:00` | `2024-03-03 07:00` | 20.0h | `$0.0042` | `$0.0039` | **-8.23%** | **-8.59%** | +8.4% | -14.6% | `stop_loss` |
| 10 | Book 3 | `2024-03-15 03:00` | `2024-03-15 09:00` | 6.0h | `$0.0092` | `$0.0084` | **-8.23%** | **-8.59%** | +6.5% | -10.1% | `stop_loss` |
| 11 | Book 3 | `2024-05-29 08:00` | `2024-05-30 06:00` | 22.0h | `$0.0150` | `$0.0138` | **-8.23%** | **-8.59%** | +4.6% | -9.3% | `stop_loss` |
| 12 | Book 3 | `2024-11-13 19:00` | `2024-11-13 21:00` | 2.0h | `$0.0193` | `$0.0177` | **-8.23%** | **-8.59%** | +9.3% | -8.2% | `stop_loss` |
| 13 | Book 3 | `2024-11-14 03:00` | `2024-11-14 11:00` | 8.0h | `$0.0227` | `$0.0209` | **-8.23%** | **-8.59%** | +8.7% | -10.3% | `stop_loss` |
| 14 | Book 2 | `2025-05-08 03:00` | `2025-05-12 18:00` | 111.0h | `$0.0087` | `$0.0131` | **+54.38%** | **+44.19%** | +76.3% | -4.2% | `trail_stop` |
| 15 | Book 2 | `2025-06-29 22:00` | `2025-07-01 05:00` | 31.0h | `$0.0104` | `$0.0095` | **-8.52%** | **-8.89%** | +1.3% | -8.6% | `initial_stop` |
| 16 | Book 1 | `2025-07-09 21:00` | `2025-07-29 13:00` | 472.0h | `$0.0112` | `$0.0132` | **+27.00%** | **+24.83%** | +32.3% | -2.4% | `climax_whale_euphoria_harvest` |
| 17 | Book 3 | `2026-09-21 23:00` | `2026-09-22 01:00` | 2.0h | `$0.0047` | `$0.0051` | **+8.70%** | **+8.34%** | +8.8% | -0.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `target_reclaim` | `6` | `100.0%` | **`+49.1%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.9%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+24.8%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `trail_stop` | `1` | `100.0%` | **`+44.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000PEPE`

* **Total Candidate Breakouts Filtered (Vetoed):** `100`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `65` (65.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `34`
* **Saved Capital Losses Avoided:** `+996.1%`
* **Missed Upside Forgone:** `-1,975.9%`
* **Net Veto Alpha:** `+-979.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `46` | `46.0%` |
| `Core 4: Funding Rate Cap` | `42` | `42.0%` |
| `Core 4: Whale Firewall` | `5` | `5.0%` |
| `Core 4: Defensible Whale Dump` | `4` | `4.0%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `3` | `3.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*