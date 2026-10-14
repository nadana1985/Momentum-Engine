# Kronos V12: Institutional Symbol Tear Sheet — `LPT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`11.849`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+61.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.85x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+10.25%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-4.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`75.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.2% / -10.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2023-08-11 05:00` | `2023-08-12 18:00` | 37.0h | `$5.7506` | `$6.9007` | **+6.93%** | **+6.61%** | +20.2% | -1.5% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2024-06-06 11:00` | `2024-06-10 11:00` | Live | `$22.0726` | `$23.9488` | **+8.50%** | **+8.16%** | +3.5% | -38.0% | `shelf_target_reclaim` |
| 3 | Book 2 | `2024-09-13 16:00` | `2024-09-15 16:00` | 48.0h | `$12.8641` | `$12.3311` | **-4.36%** | **-4.45%** | +1.2% | -4.5% | `fast_decay_cut` |
| 4 | Book 4 | `2024-11-24 22:00` | `2024-11-30 03:00` | 125.0h | `$13.0255` | `$15.6306` | **+27.05%** | **+24.39%** | +24.2% | -9.3% | `target_reclaim` |
| 5 | Book 2 | `2025-04-22 14:00` | `2025-04-22 16:00` | 2.0h | `$4.3408` | `$5.4503` | **+31.47%** | **+28.02%** | +37.3% | -1.7% | `climax_top_harvest` |
| 6 | Book 1 | `2026-09-21 09:00` | `2026-09-28 08:00` | 167.0h | `$1.7103` | `$1.6878` | **-1.21%** | **-1.22%** | +10.7% | -7.1% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-5.7%`** |
| `target_reclaim` | `2` | `100.0%` | **`+31.0%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+28.0%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `LPT`

* **Total Candidate Breakouts Filtered (Vetoed):** `877`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `465` (53.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `217`
* **Saved Capital Losses Avoided:** `+7,554.4%`
* **Missed Upside Forgone:** `-7,798.6%`
* **Net Veto Alpha:** `+-244.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `455` | `51.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `420` | `47.9%` |
| `Core 4: Whale Firewall` | `1` | `0.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*