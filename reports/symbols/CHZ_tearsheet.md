# Kronos V12: Institutional Symbol Tear Sheet — `CHZ`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`37.5%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.151`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+4.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.54%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-16.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`97.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.1% / -6.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2022-08-14 00:00` | `2022-08-15 15:00` | 39.0h | `$0.1680` | `$0.2016` | **+6.96%** | **+6.64%** | +20.6% | -1.2% | `target_reclaim` |
| 2 | Book 1 | `2023-01-12 17:00` | `2023-01-18 16:00` | 143.0h | `$0.1290` | `$0.1264` | **-1.66%** | **-1.67%** | +12.1% | -5.8% | `fast_decay_cut` |
| 3 | Book 2 | `2023-07-13 17:00` | `2023-07-15 17:00` | 48.0h | `$0.0823` | `$0.0814` | **-1.33%** | **-1.34%** | +3.6% | -5.7% | `fast_decay_cut` |
| 4 | Book 2 | `2023-10-21 03:00` | `2023-10-28 03:00` | 168.0h | `$0.0598` | `$0.0648` | **+9.57%** | **+9.20%** | +15.0% | -1.7% | `time_cap` |
| 5 | Book 1 | `2023-11-05 23:00` | `2023-11-07 11:00` | 36.0h | `$0.0803` | `$0.0770` | **-5.23%** | **-5.36%** | +2.0% | -5.0% | `fast_decay_cut` |
| 6 | Book 4 | `2023-11-10 23:00` | `2023-11-17 23:00` | 168.0h | `$0.0828` | `$0.0772` | **-3.99%** | **-4.16%** | +4.3% | -11.9% | `stagnation_cut` |
| 7 | Book 4 | `2024-11-18 06:00` | `2024-11-24 03:00` | 141.0h | `$0.0775` | `$0.0930` | **+19.32%** | **+17.05%** | +21.9% | -10.3% | `target_reclaim` |
| 8 | Book 1 | `2026-09-22 23:00` | `2026-09-24 11:00` | 36.0h | `$0.0172` | `$0.0156` | **-14.91%** | **-16.04%** | +1.1% | -11.2% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `4` | `0.0%` | **`-24.4%`** |
| `target_reclaim` | `2` | `100.0%` | **`+23.7%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-4.2%`** |
| `time_cap` | `1` | `100.0%` | **`+9.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `CHZ`

* **Total Candidate Breakouts Filtered (Vetoed):** `1011`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `507` (50.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `243`
* **Saved Capital Losses Avoided:** `+5,813.6%`
* **Missed Upside Forgone:** `-8,782.8%`
* **Net Veto Alpha:** `+-2,969.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `478` | `47.3%` |
| `Core 1: Macro Bear Veto` | `471` | `46.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `56` | `5.5%` |
| `Core 4: Funding Rate Cap` | `4` | `0.4%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `2` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*