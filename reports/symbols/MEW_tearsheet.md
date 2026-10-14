# Kronos V12: Institutional Symbol Tear Sheet — `MEW`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`46.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.927`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.34%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-26.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`30.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.9% / -10.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-07-20 05:00` | `2024-07-24 05:00` | Live | `$0.0043` | `$0.0047` | **+8.50%** | **+8.16%** | +88.8% | -27.0% | `shelf_target_reclaim` |
| 2 | Book 3 | `2024-07-24 12:00` | `2024-07-24 15:00` | 3.0h | `$0.0083` | `$0.0076` | **-8.23%** | **-8.59%** | +2.0% | -9.8% | `stop_loss` |
| 3 | Book 3 | `2024-10-08 08:00` | `2024-10-09 12:00` | 28.0h | `$0.0067` | `$0.0061` | **-8.23%** | **-8.59%** | +3.6% | -10.6% | `stop_loss` |
| 4 | Book 3 | `2024-10-22 09:00` | `2024-10-24 02:00` | 41.0h | `$0.0087` | `$0.0099` | **+13.56%** | **+12.71%** | +16.5% | -0.3% | `target_reclaim` |
| 5 | Book 3 | `2024-11-14 15:00` | `2024-11-16 01:00` | 34.0h | `$0.0105` | `$0.0122` | **+16.88%** | **+15.60%** | +18.3% | -7.6% | `target_reclaim` |
| 6 | Book 3 | `2024-11-18 19:00` | `2024-11-20 03:00` | 32.0h | `$0.0113` | `$0.0103` | **-8.23%** | **-8.59%** | +3.1% | -8.5% | `stop_loss` |
| 7 | Book 5 (Shelf Absorption Squeeze) | `2025-03-26 06:00` | `2025-03-30 06:00` | Live | `$0.0024` | `$0.0026` | **+8.50%** | **+8.16%** | +16.3% | -29.1% | `shelf_target_reclaim` |
| 8 | Book 3 | `2025-04-26 11:00` | `2025-04-29 11:00` | 72.0h | `$0.0029` | `$0.0029` | **+2.80%** | **+2.76%** | +4.7% | -7.9% | `time_expiry` |
| 9 | Book 3 | `2025-05-04 04:00` | `2025-05-06 11:00` | 55.0h | `$0.0028` | `$0.0025` | **-8.23%** | **-8.59%** | +1.7% | -8.9% | `stop_loss` |
| 10 | Book 3 | `2025-05-13 02:00` | `2025-05-13 16:00` | 14.0h | `$0.0037` | `$0.0040` | **+8.70%** | **+8.34%** | +10.9% | -2.1% | `target_reclaim` |
| 11 | Book 3 | `2025-05-23 11:00` | `2025-05-23 22:00` | 11.0h | `$0.0043` | `$0.0040` | **-8.23%** | **-8.59%** | +9.1% | -8.3% | `stop_loss` |
| 12 | Book 3 | `2026-08-25 09:00` | `2026-08-26 14:00` | 29.0h | `$0.0004` | `$0.0004` | **-8.23%** | **-8.59%** | +2.5% | -8.7% | `stop_loss` |
| 13 | Book 3 | `2026-09-30 07:00` | `2026-09-30 21:00` | 14.0h | `$0.0005` | `$0.0005` | **-8.23%** | **-8.59%** | +3.8% | -8.5% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `target_reclaim` | `3` | `100.0%` | **`+36.7%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+2.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `MEW`

* **Total Candidate Breakouts Filtered (Vetoed):** `299`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `177` (59.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+2,733.4%`
* **Missed Upside Forgone:** `-962.5%`
* **Net Veto Alpha:** `+1,770.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `232` | `77.6%` |
| `Core 1: Macro Bear Veto` | `38` | `12.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `25` | `8.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `1.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*