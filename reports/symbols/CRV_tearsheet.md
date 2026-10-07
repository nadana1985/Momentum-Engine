# Kronos V12: Institutional Symbol Tear Sheet — `CRV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `13` (`13` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `13` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`23.1%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.134`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+7.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.60%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-33.7%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`124.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.9% / -5.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2022-03-27 21:00` | `2022-04-01 01:00` | 100.0h | `$2.6265` | `$2.6015` | **-1.36%** | **-1.37%** | +12.0% | -4.2% | `fast_decay_cut` |
| 2 | Book 1 | `2022-10-28 16:00` | `2022-10-30 16:00` | 48.0h | `$0.9634` | `$0.8918` | **-8.52%** | **-8.91%** | +1.6% | -7.7% | `fast_decay_cut` |
| 3 | Book 2 | `2023-04-14 00:00` | `2023-04-17 00:00` | 72.0h | `$1.0967` | `$1.0683` | **-2.59%** | **-2.62%** | +1.5% | -3.0% | `stagnation_cut` |
| 4 | Book 2 | `2023-06-20 17:00` | `2023-06-27 17:00` | 168.0h | `$0.6546` | `$0.6963` | **+6.36%** | **+6.16%** | +13.5% | -2.5% | `time_cap` |
| 5 | Book 2 | `2023-07-13 16:00` | `2023-07-18 16:00` | 120.0h | `$0.8411` | `$0.7719` | **-8.23%** | **-8.59%** | +4.5% | -8.1% | `initial_stop` |
| 6 | Book 2 | `2023-10-01 22:00` | `2023-10-02 14:00` | 16.0h | `$0.5434` | `$0.5084` | **-6.42%** | **-6.64%** | +0.5% | -6.9% | `initial_stop` |
| 7 | Book 1 | `2023-11-05 03:00` | `2023-11-07 15:00` | 60.0h | `$0.5674` | `$0.5436` | **-2.30%** | **-2.32%** | +4.5% | -4.8% | `fast_decay_cut` |
| 8 | Book 2 | `2025-04-22 14:00` | `2025-04-28 16:00` | 146.0h | `$0.6777` | `$0.6219` | **-8.23%** | **-8.59%** | +4.6% | -8.2% | `initial_stop` |
| 9 | Book 1 | `2025-04-30 17:00` | `2025-05-04 18:00` | 97.0h | `$0.6937` | `$0.6813` | **-2.18%** | **-2.20%** | +8.4% | -3.6% | `fast_decay_cut` |
| 10 | Book 1 | `2025-07-10 21:00` | `2025-07-31 21:00` | 504.0h | `$0.6015` | `$0.9576` | **+78.60%** | **+58.00%** | +93.5% | -3.7% | `time_cap` |
| 11 | Book 2 | `2025-10-26 22:00` | `2025-10-28 20:00` | 46.0h | `$0.5804` | `$0.5327` | **-8.23%** | **-8.59%** | +2.7% | -8.5% | `initial_stop` |
| 12 | Book 2 | `2026-09-20 16:00` | `2026-09-23 16:00` | 72.0h | `$0.3523` | `$0.3233` | **-8.23%** | **-8.59%** | +5.9% | -8.9% | `initial_stop` |
| 13 | Book 2 | `2026-09-28 18:00` | `2026-10-05 18:00` | 168.0h | `$0.3650` | `$0.3727` | **+2.10%** | **+2.08%** | +13.9% | -4.3% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `5` | `0.0%` | **`-41.0%`** |
| `fast_decay_cut` | `4` | `0.0%` | **`-14.8%`** |
| `time_cap` | `3` | `100.0%` | **`+66.2%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-2.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CRV`

* **Total Candidate Breakouts Filtered (Vetoed):** `212`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `150` (70.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `44`
* **Saved Capital Losses Avoided:** `+2,357.9%`
* **Missed Upside Forgone:** `-1,643.8%`
* **Net Veto Alpha:** `+714.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `101` | `47.6%` |
| `Core 1: Macro Bear Veto` | `86` | `40.6%` |
| `Core 4: Funding Rate Cap` | `21` | `9.9%` |
| `Core 4: Defensible Whale Dump` | `4` | `1.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*