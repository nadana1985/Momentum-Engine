# Kronos V12: Institutional Symbol Tear Sheet — `LUMIA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`71.4%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.009`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+15.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.17x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.28%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-15.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.0% / -12.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-02-08 09:00` | `2025-02-12 09:00` | Live | `$0.5630` | `$0.6109` | **+8.50%** | **+8.16%** | +6.7% | -38.6% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-05-06 20:00` | `2025-05-10 20:00` | Live | `$0.2943` | `$0.3193` | **+8.50%** | **+8.16%** | +44.4% | -10.2% | `shelf_target_reclaim` |
| 3 | Book 3 | `2025-05-13 01:00` | `2025-05-13 02:00` | 1.0h | `$0.4199` | `$0.4395` | **+4.66%** | **+4.55%** | +10.0% | -1.8% | `target_reclaim` |
| 4 | Book 3 | `2025-08-05 07:00` | `2025-08-07 10:00` | 51.0h | `$0.2910` | `$0.3031` | **+4.17%** | **+4.08%** | +5.3% | -6.2% | `target_reclaim` |
| 5 | Book 4 | `2026-04-25 13:00` | `2026-04-27 14:00` | 49.0h | `$0.1426` | `$0.1711` | **+6.97%** | **+6.76%** | +32.1% | -7.1% | `target_reclaim` |
| 6 | Book 4 | `2026-06-22 13:00` | `2026-06-28 10:00` | 141.0h | `$0.1327` | `$0.1128` | **-6.92%** | **-7.19%** | +12.9% | -16.3% | `structural_stop` |
| 7 | Book 3 | `2026-10-10 08:00` | `2026-10-10 10:00` | 2.0h | `$0.1146` | `$0.1051` | **-8.23%** | **-8.59%** | +21.8% | -9.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+15.4%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `structural_stop` | `1` | `0.0%` | **`-7.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `LUMIA`

* **Total Candidate Breakouts Filtered (Vetoed):** `377`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `293` (77.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `103`
* **Saved Capital Losses Avoided:** `+5,115.2%`
* **Missed Upside Forgone:** `-3,619.7%`
* **Net Veto Alpha:** `+1,495.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `275` | `72.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `85` | `22.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `14` | `3.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*