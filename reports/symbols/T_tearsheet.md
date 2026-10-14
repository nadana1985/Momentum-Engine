# Kronos V12: Institutional Symbol Tear Sheet — `T`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+90.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.47x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+10.06%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`141.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.5% / -15.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-03-02 06:00` | `2023-03-06 06:00` | Live | `$0.0400` | `$0.0434` | **+8.50%** | **+8.16%** | +12.4% | -30.5% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2023-03-14 06:00` | `2023-03-18 06:00` | Live | `$0.0391` | `$0.0424` | **+8.50%** | **+8.16%** | +6.6% | -16.2% | `shelf_target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2023-06-23 10:00` | `2023-06-27 10:00` | Live | `$0.0213` | `$0.0232` | **+8.50%** | **+8.16%** | +12.6% | -12.6% | `shelf_target_reclaim` |
| 4 | Book 2 | `2023-10-23 22:00` | `2023-10-30 22:00` | 168.0h | `$0.0211` | `$0.0234` | **+11.44%** | **+10.88%** | +11.5% | -3.8% | `time_cap` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2024-01-06 00:00` | `2024-01-10 00:00` | Live | `$0.0316` | `$0.0343` | **+8.50%** | **+8.16%** | +26.4% | -27.5% | `shelf_target_reclaim` |
| 6 | Book 4 | `2024-11-16 01:00` | `2024-11-19 17:00` | 88.0h | `$0.0251` | `$0.0301` | **+28.08%** | **+25.23%** | +34.0% | -2.9% | `target_reclaim` |
| 7 | Book 2 | `2026-05-04 02:00` | `2026-05-11 02:00` | 168.0h | `$0.0060` | `$0.0063` | **+5.64%** | **+5.51%** | +7.5% | -2.7% | `time_cap` |
| 8 | Book 5 (Shelf Absorption Squeeze) | `2026-07-11 12:00` | `2026-07-15 12:00` | Live | `$0.0040` | `$0.0043` | **+8.50%** | **+8.16%** | +24.7% | -19.3% | `shelf_target_reclaim` |
| 9 | Book 5 (Shelf Absorption Squeeze) | `2026-09-02 11:00` | `2026-09-06 11:00` | Live | `$0.0050` | `$0.0055` | **+8.50%** | **+8.16%** | +4.0% | -25.0% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `6` | `100.0%` | **`+48.9%`** |
| `time_cap` | `2` | `100.0%` | **`+16.4%`** |
| `target_reclaim` | `1` | `100.0%` | **`+25.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `T`

* **Total Candidate Breakouts Filtered (Vetoed):** `504`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `220` (43.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `139`
* **Saved Capital Losses Avoided:** `+2,644.7%`
* **Missed Upside Forgone:** `-4,142.7%`
* **Net Veto Alpha:** `+-1,498.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `462` | `91.7%` |
| `Core 1: Macro Bear Veto` | `37` | `7.3%` |
| `Core 4: Whale Firewall` | `3` | `0.6%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*