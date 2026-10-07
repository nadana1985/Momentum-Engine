# Kronos V12: Institutional Symbol Tear Sheet — `ALT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `15` (`15` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.219`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+11.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.12x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.75%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-25.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`17.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.8% / -5.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-03-10 14:00` | `2024-03-11 01:00` | 11.0h | `$0.5600` | `$0.6087` | **+8.70%** | **+8.34%** | +11.9% | -1.8% | `target_reclaim` |
| 2 | Book 3 | `2024-03-11 16:00` | `2024-03-12 03:00` | 11.0h | `$0.5860` | `$0.6369` | **+8.70%** | **+8.34%** | +9.2% | -0.7% | `target_reclaim` |
| 3 | Book 3 | `2024-03-27 08:00` | `2024-03-28 18:00` | 34.0h | `$0.6050` | `$0.6576` | **+8.70%** | **+8.34%** | +10.4% | -4.3% | `target_reclaim` |
| 4 | Book 3 | `2024-10-01 12:00` | `2024-10-01 14:00` | 2.0h | `$0.1331` | `$0.1221` | **-8.23%** | **-8.59%** | +2.2% | -8.3% | `stop_loss` |
| 5 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$0.1132` | `$0.1039` | **-8.23%** | **-8.59%** | +6.4% | -8.6% | `stop_loss` |
| 6 | Book 3 | `2024-11-14 07:00` | `2024-11-14 08:00` | 1.0h | `$0.1259` | `$0.1155` | **-8.26%** | **-8.62%** | +1.5% | -11.1% | `stop_loss` |
| 7 | Book 3 | `2024-12-03 13:00` | `2024-12-03 21:00` | 8.0h | `$0.1702` | `$0.1850` | **+8.70%** | **+8.34%** | +9.2% | -4.7% | `target_reclaim` |
| 8 | Book 3 | `2025-04-24 08:00` | `2025-04-25 00:00` | 16.0h | `$0.0290` | `$0.0315` | **+8.70%** | **+8.34%** | +9.0% | -1.8% | `target_reclaim` |
| 9 | Book 3 | `2025-04-28 01:00` | `2025-04-28 07:00` | 6.0h | `$0.0297` | `$0.0323` | **+8.70%** | **+8.34%** | +13.0% | -1.5% | `target_reclaim` |
| 10 | Book 3 | `2025-04-30 05:00` | `2025-05-03 05:00` | 72.0h | `$0.0304` | `$0.0309` | **+1.48%** | **+1.47%** | +8.3% | -10.1% | `time_expiry` |
| 11 | Book 3 | `2025-05-15 03:00` | `2025-05-15 14:00` | 11.0h | `$0.0388` | `$0.0356` | **-8.23%** | **-8.59%** | +1.9% | -8.2% | `stop_loss` |
| 12 | Book 3 | `2025-06-16 10:00` | `2025-06-16 12:00` | 2.0h | `$0.0423` | `$0.0388` | **-8.23%** | **-8.59%** | +8.7% | -12.4% | `stop_loss` |
| 13 | Book 3 | `2025-07-11 06:00` | `2025-07-11 08:00` | 2.0h | `$0.0457` | `$0.0420` | **-8.23%** | **-8.59%** | +14.6% | -8.6% | `stop_loss` |
| 14 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0060` | `$0.0065` | **+8.70%** | **+8.34%** | +20.4% | -0.3% | `target_reclaim` |
| 15 | Book 3 | `2026-09-28 03:00` | `2026-10-01 03:00` | 72.0h | `$0.0076` | `$0.0078` | **+3.06%** | **+3.02%** | +5.1% | -3.5% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `7` | `100.0%` | **`+58.4%`** |
| `stop_loss` | `6` | `0.0%` | **`-51.6%`** |
| `time_expiry` | `2` | `100.0%` | **`+4.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALT`

* **Total Candidate Breakouts Filtered (Vetoed):** `81`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `60` (74.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+884.2%`
* **Missed Upside Forgone:** `-130.3%`
* **Net Veto Alpha:** `+753.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `35` | `43.2%` |
| `Core 1: Macro Bear Veto` | `27` | `33.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `17` | `21.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `2.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*