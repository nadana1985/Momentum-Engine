# Kronos V12: Institutional Symbol Tear Sheet — `FIL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`84.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.720`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+69.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.01x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+5.37%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-32.0%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`102.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.7% / -7.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-11 09:00` | `2021-09-04 16:00` | 583.0h | `$71.8136` | `$86.1763` | **+8.37%** | **+7.99%** | +25.8% | -8.2% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2023-02-17 04:00` | `2023-02-21 04:00` | Live | `$5.9800` | `$6.4883` | **+8.50%** | **+8.16%** | +32.6% | -12.6% | `shelf_target_reclaim` |
| 3 | Book 4 | `2023-11-05 10:00` | `2023-11-12 20:00` | 178.0h | `$4.1362` | `$4.9634` | **+18.04%** | **+16.81%** | +24.9% | -3.3% | `target_reclaim` |
| 4 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$4.5820` | `$4.7082` | **+2.75%** | **+2.72%** | +13.1% | -5.0% | `time_expiry` |
| 5 | Book 3 | `2024-01-03 11:00` | `2024-01-03 12:00` | 1.0h | `$6.9055` | `$6.3372` | **-8.23%** | **-8.59%** | +8.1% | -18.9% | `stop_loss` |
| 6 | Book 3 | `2024-02-29 21:00` | `2024-03-02 04:00` | 31.0h | `$8.2642` | `$8.6860` | **+5.10%** | **+4.98%** | +7.6% | -4.5% | `target_reclaim` |
| 7 | Book 3 | `2024-03-05 19:00` | `2024-03-06 05:00` | 10.0h | `$8.2342` | `$9.1760` | **+11.44%** | **+10.83%** | +14.1% | -7.7% | `target_reclaim` |
| 8 | Book 3 | `2024-03-11 00:00` | `2024-03-11 08:00` | 8.0h | `$10.0860` | `$10.9630` | **+8.70%** | **+8.34%** | +8.9% | -1.5% | `target_reclaim` |
| 9 | Book 3 | `2024-11-13 04:00` | `2024-11-16 04:00` | 72.0h | `$3.9167` | `$4.1636` | **+6.30%** | **+6.11%** | +9.0% | -3.4% | `time_expiry` |
| 10 | Book 4 | `2024-11-16 11:00` | `2024-11-23 13:00` | 170.0h | `$4.4957` | `$5.3949` | **+33.82%** | **+29.35%** | +20.0% | -9.3% | `target_reclaim` |
| 11 | Book 3 | `2024-12-03 07:00` | `2024-12-04 00:00` | 17.0h | `$7.2394` | `$7.5410` | **+4.17%** | **+4.08%** | +4.5% | -7.7% | `target_reclaim` |
| 12 | Book 1 | `2026-09-13 14:00` | `2026-09-16 12:00` | 70.0h | `$0.9137` | `$0.7747` | **-28.20%** | **-32.00%** | +13.8% | -17.5% | `initial_stop` |
| 13 | Book 4 | `2026-09-18 20:00` | `2026-09-19 17:00` | 21.0h | `$0.9238` | `$1.1085` | **+11.58%** | **+11.05%** | +21.6% | -1.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+93.4%`** |
| `time_expiry` | `2` | `100.0%` | **`+8.8%`** |
| `initial_stop` | `1` | `0.0%` | **`-32.0%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `FIL`

* **Total Candidate Breakouts Filtered (Vetoed):** `680`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `490` (72.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `136`
* **Saved Capital Losses Avoided:** `+8,787.6%`
* **Missed Upside Forgone:** `-4,508.0%`
* **Net Veto Alpha:** `+4,279.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `495` | `72.8%` |
| `Core 1: Macro Bear Veto` | `137` | `20.1%` |
| `Core 4: Funding Rate Cap` | `43` | `6.3%` |
| `Core 4: Whale Firewall` | `3` | `0.4%` |
| `Core 4: Defensible Whale Dump` | `2` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*