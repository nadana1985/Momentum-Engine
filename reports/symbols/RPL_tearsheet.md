# Kronos V12: Institutional Symbol Tear Sheet — `RPL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`46.2%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.953`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-1.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.15%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-15.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`67.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.1% / -8.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-10-21 13:00` | `2024-10-23 16:00` | 51.0h | `$11.7740` | `$10.8050` | **-8.23%** | **-8.59%** | +2.4% | -9.1% | `stop_loss` |
| 2 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$11.2007` | `$10.2789` | **-8.23%** | **-8.59%** | +4.0% | -9.2% | `stop_loss` |
| 3 | Book 3 | `2024-12-01 20:00` | `2024-12-02 01:00` | 5.0h | `$14.2320` | `$14.8250` | **+4.17%** | **+4.08%** | +4.4% | -2.0% | `target_reclaim` |
| 4 | Book 3 | `2024-12-03 13:00` | `2024-12-03 18:00` | 5.0h | `$14.4155` | `$15.4520` | **+7.19%** | **+6.94%** | +7.9% | -2.9% | `target_reclaim` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2025-02-09 03:00` | `2025-02-13 03:00` | Live | `$7.1383` | `$7.7450` | **+8.50%** | **+8.16%** | +50.4% | -23.5% | `shelf_target_reclaim` |
| 6 | Book 3 | `2025-02-11 16:00` | `2025-02-11 17:00` | 1.0h | `$10.1537` | `$9.3181` | **-8.23%** | **-8.59%** | +14.9% | -9.8% | `stop_loss` |
| 7 | Book 3 | `2025-04-24 03:00` | `2025-04-25 05:00` | 26.0h | `$4.2716` | `$4.6430` | **+8.70%** | **+8.34%** | +11.4% | -0.9% | `target_reclaim` |
| 8 | Book 3 | `2025-04-27 01:00` | `2025-04-30 01:00` | 72.0h | `$4.3240` | `$4.2883` | **-0.83%** | **-0.83%** | +5.3% | -2.8% | `time_expiry` |
| 9 | Book 3 | `2025-06-12 11:00` | `2025-06-13 01:00` | 14.0h | `$6.3575` | `$5.8343` | **-8.23%** | **-8.59%** | +6.7% | -8.8% | `stop_loss` |
| 10 | Book 3 | `2025-07-11 22:00` | `2025-07-14 22:00` | 72.0h | `$6.0854` | `$5.7546` | **-5.44%** | **-5.59%** | +1.9% | -7.9% | `time_expiry` |
| 11 | Book 3 | `2025-07-17 03:00` | `2025-07-17 06:00` | 3.0h | `$6.2438` | `$6.5040` | **+4.17%** | **+4.08%** | +5.0% | -1.1% | `target_reclaim` |
| 12 | Book 5 (Shelf Absorption Squeeze) | `2026-02-16 18:00` | `2026-02-20 18:00` | Live | `$2.1905` | `$2.3767` | **+8.50%** | **+8.16%** | +13.1% | -27.0% | `shelf_target_reclaim` |
| 13 | Book 4 | `2026-09-21 05:00` | `2026-10-11 00:00` | 475.0h | `$1.8658` | `$1.8962` | **-0.93%** | **-0.93%** | +17.0% | -9.6% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `target_reclaim` | `4` | `100.0%` | **`+23.4%`** |
| `time_expiry` | `3` | `0.0%` | **`-7.4%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `RPL`

* **Total Candidate Breakouts Filtered (Vetoed):** `500`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `326` (65.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `55`
* **Saved Capital Losses Avoided:** `+4,555.8%`
* **Missed Upside Forgone:** `-1,639.8%`
* **Net Veto Alpha:** `+2,916.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `453` | `90.6%` |
| `Core 1: Macro Bear Veto` | `39` | `7.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `1.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*