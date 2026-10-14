# Kronos V12: Institutional Symbol Tear Sheet — `SUSHI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`62.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.316`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+58.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.80x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+7.36%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-12.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`102.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.9% / -8.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-09 15:00` | `2021-08-11 14:00` | 47.0h | `$10.1172` | `$12.1406` | **+22.13%** | **+20.22%** | +20.3% | -5.3% | `target_reclaim` |
| 2 | Book 1 | `2023-01-09 00:00` | `2023-01-10 12:00` | 36.0h | `$1.1118` | `$1.0783` | **-5.05%** | **-5.17%** | +2.3% | -4.5% | `fast_decay_cut` |
| 3 | Book 4 | `2023-10-31 14:00` | `2023-11-01 15:00` | 25.0h | `$0.7549` | `$0.9059` | **+25.17%** | **+22.85%** | +22.8% | -3.7% | `target_reclaim` |
| 4 | Book 4 | `2024-05-24 00:00` | `2024-06-07 18:00` | 354.0h | `$1.2165` | `$1.1021` | **-11.40%** | **-11.98%** | +8.2% | -21.4% | `structural_stop` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2024-09-28 10:00` | `2024-10-02 10:00` | Live | `$0.8040` | `$0.8723` | **+8.50%** | **+8.16%** | +0.7% | -23.0% | `shelf_target_reclaim` |
| 6 | Book 2 | `2025-04-22 15:00` | `2025-04-29 15:00` | 168.0h | `$0.6258` | `$0.6766` | **+9.60%** | **+9.23%** | +14.4% | -1.8% | `time_cap` |
| 7 | Book 4 | `2025-07-16 20:00` | `2025-07-18 05:00` | 33.0h | `$0.7674` | `$0.9209` | **+17.27%** | **+16.13%** | +36.3% | -5.6% | `target_reclaim` |
| 8 | Book 2 | `2026-05-02 02:00` | `2026-05-04 10:00` | 56.0h | `$0.2193` | `$0.2183` | **-0.59%** | **-0.60%** | +6.4% | -1.6% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+59.2%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-5.8%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-12.0%`** |
| `time_cap` | `1` | `100.0%` | **`+9.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `SUSHI`

* **Total Candidate Breakouts Filtered (Vetoed):** `1279`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `832` (65.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `126`
* **Saved Capital Losses Avoided:** `+10,917.9%`
* **Missed Upside Forgone:** `-3,772.5%`
* **Net Veto Alpha:** `+7,145.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `599` | `46.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `588` | `46.0%` |
| `Core 1: Macro Bear Veto` | `89` | `7.0%` |
| `Core 4: Funding Rate Cap` | `2` | `0.2%` |
| `Core 4: Whale Firewall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*