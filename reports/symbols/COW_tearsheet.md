# Kronos V12: Institutional Symbol Tear Sheet — `COW`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.466`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+12.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.13x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.24%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-12.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.3% / -8.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-12-17 06:00` | `2024-12-17 07:00` | 1.0h | `$0.8025` | `$0.8723` | **+8.70%** | **+8.34%** | +10.4% | -1.0% | `target_reclaim` |
| 2 | Book 3 | `2024-12-27 16:00` | `2024-12-29 03:00` | 35.0h | `$1.0003` | `$1.0673` | **+6.70%** | **+6.48%** | +7.7% | -6.2% | `target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2025-02-25 08:00` | `2025-03-01 08:00` | Live | `$0.3688` | `$0.3386` | **-8.20%** | **-8.56%** | +-2.9% | -41.0% | `shelf_stop_loss` |
| 4 | Book 3 | `2025-04-24 03:00` | `2025-04-26 00:00` | 45.0h | `$0.2980` | `$0.3165` | **+6.20%** | **+6.01%** | +9.2% | -2.8% | `target_reclaim` |
| 5 | Book 3 | `2025-04-26 11:00` | `2025-04-29 11:00` | 72.0h | `$0.3051` | `$0.3026` | **-0.80%** | **-0.80%** | +3.1% | -7.3% | `time_expiry` |
| 6 | Book 3 | `2025-05-14 22:00` | `2025-05-16 22:00` | 48.0h | `$0.3947` | `$0.3622` | **-8.23%** | **-8.59%** | +2.4% | -8.2% | `stop_loss` |
| 7 | Book 3 | `2025-07-12 12:00` | `2025-07-13 10:00` | 22.0h | `$0.3597` | `$0.3747` | **+4.17%** | **+4.08%** | +4.4% | -3.0% | `target_reclaim` |
| 8 | Book 3 | `2025-07-16 03:00` | `2025-07-16 04:00` | 1.0h | `$0.3930` | `$0.4110` | **+4.59%** | **+4.49%** | +15.0% | -0.8% | `target_reclaim` |
| 9 | Book 3 | `2025-08-10 02:00` | `2025-08-11 11:00` | 33.0h | `$0.4444` | `$0.4078` | **-8.23%** | **-8.59%** | +1.2% | -9.5% | `stop_loss` |
| 10 | Book 3 | `2026-09-28 03:00` | `2026-10-01 03:00` | 72.0h | `$0.1517` | `$0.1668` | **+9.96%** | **+9.49%** | +12.4% | -2.3% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+29.4%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `2` | `50.0%` | **`+8.7%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `COW`

* **Total Candidate Breakouts Filtered (Vetoed):** `388`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `221` (57.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `26`
* **Saved Capital Losses Avoided:** `+2,535.9%`
* **Missed Upside Forgone:** `-714.5%`
* **Net Veto Alpha:** `+1,821.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `340` | `87.6%` |
| `Core 1: Macro Bear Veto` | `35` | `9.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `11` | `2.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*