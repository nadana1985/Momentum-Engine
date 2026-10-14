# Kronos V12: Institutional Symbol Tear Sheet — `CFX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`42.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.167`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+38.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.46x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.45%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-23.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`191.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+26.8% / -14.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-03-01 17:00` | `2023-03-05 17:00` | Live | `$0.2295` | `$0.2491` | **+8.50%** | **+8.16%** | +95.9% | -47.0% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2023-06-20 23:00` | `2023-06-24 23:00` | Live | `$0.2003` | `$0.2173` | **+8.50%** | **+8.16%** | +28.6% | -17.7% | `shelf_target_reclaim` |
| 3 | Book 1 | `2023-10-02 00:00` | `2023-10-03 12:00` | 36.0h | `$0.1388` | `$0.1342` | **-5.72%** | **-5.87%** | +0.8% | -8.2% | `fast_decay_cut` |
| 4 | Book 4 | `2024-10-02 03:00` | `2024-10-17 18:00` | 375.0h | `$0.1818` | `$0.1545` | **-16.58%** | **-17.97%** | +17.9% | -15.8% | `structural_stop` |
| 5 | Book 4 | `2025-07-13 06:00` | `2025-07-20 05:00` | 167.0h | `$0.1015` | `$0.1217` | **+69.00%** | **+54.51%** | +30.8% | -4.9% | `target_reclaim` |
| 6 | Book 2 | `2026-09-20 16:00` | `2026-09-23 14:00` | 70.0h | `$0.0527` | `$0.0522` | **-0.89%** | **-0.89%** | +6.2% | -3.0% | `fast_decay_cut` |
| 7 | Book 4 | `2026-09-24 14:00` | `2026-10-07 13:00` | 311.0h | `$0.0540` | `$0.0506` | **-7.69%** | **-7.95%** | +7.2% | -6.7% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-6.8%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `structural_stop` | `2` | `0.0%` | **`-25.9%`** |
| `target_reclaim` | `1` | `100.0%` | **`+54.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `CFX`

* **Total Candidate Breakouts Filtered (Vetoed):** `517`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `251` (48.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `122`
* **Saved Capital Losses Avoided:** `+3,758.0%`
* **Missed Upside Forgone:** `-10,975.3%`
* **Net Veto Alpha:** `+-7,217.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `446` | `86.3%` |
| `Core 1: Macro Bear Veto` | `64` | `12.4%` |
| `Core 4: Funding Rate Cap` | `6` | `1.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*