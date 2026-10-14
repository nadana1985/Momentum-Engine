# Kronos V12: Institutional Symbol Tear Sheet — `PENDLE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`55.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.979`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.09%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`72.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.5% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-09-28 18:00` | `2023-10-02 18:00` | Live | `$0.6448` | `$0.6996` | **+8.50%** | **+8.16%** | +11.0% | -15.8% | `shelf_target_reclaim` |
| 2 | Book 3 | `2024-03-03 07:00` | `2024-03-05 02:00` | 43.0h | `$3.1833` | `$2.9213` | **-8.23%** | **-8.59%** | +6.3% | -8.0% | `stop_loss` |
| 3 | Book 3 | `2024-09-22 12:00` | `2024-09-25 12:00` | 72.0h | `$4.1042` | `$4.1607` | **+1.38%** | **+1.37%** | +4.5% | -6.1% | `time_expiry` |
| 4 | Book 3 | `2024-12-03 14:00` | `2024-12-03 20:00` | 6.0h | `$5.4068` | `$6.1287` | **+13.35%** | **+12.53%** | +13.7% | -0.3% | `target_reclaim` |
| 5 | Book 3 | `2024-12-08 09:00` | `2024-12-09 20:00` | 35.0h | `$6.5475` | `$6.0087` | **-8.23%** | **-8.59%** | +3.5% | -12.6% | `stop_loss` |
| 6 | Book 3 | `2025-04-13 13:00` | `2025-04-15 19:00` | 54.0h | `$3.2934` | `$3.0223` | **-8.23%** | **-8.59%** | +3.1% | -8.0% | `stop_loss` |
| 7 | Book 2 | `2025-04-21 00:00` | `2025-04-28 00:00` | 168.0h | `$3.2389` | `$3.2576` | **+0.62%** | **+0.61%** | +16.3% | -4.0% | `time_cap` |
| 8 | Book 2 | `2025-07-09 13:00` | `2025-07-16 13:00` | 168.0h | `$3.5849` | `$4.1610` | **+16.38%** | **+15.19%** | +17.9% | -1.3% | `time_cap` |
| 9 | Book 1 | `2025-09-19 00:00` | `2025-09-20 12:00` | 36.0h | `$5.3997` | `$5.0592` | **-12.30%** | **-12.92%** | +0.4% | -9.0% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_cap` | `2` | `100.0%` | **`+15.8%`** |
| `stall_bailout` | `1` | `0.0%` | **`-12.9%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.5%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `PENDLE`

* **Total Candidate Breakouts Filtered (Vetoed):** `205`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `113` (55.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+1,056.9%`
* **Missed Upside Forgone:** `-315.7%`
* **Net Veto Alpha:** `+741.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `153` | `74.6%` |
| `Core 4: Funding Rate Cap` | `24` | `11.7%` |
| `Core 4: Whale Firewall` | `18` | `8.8%` |
| `Core 4: Defensible Whale Dump` | `8` | `3.9%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `1.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*