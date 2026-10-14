# Kronos V12: Institutional Symbol Tear Sheet — `ZEN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.507`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+32.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.38x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.99%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-15.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`115.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.5% / -7.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-12-26 09:00` | `2022-12-28 09:00` | 48.0h | `$9.3704` | `$8.9336` | **-5.74%** | **-5.88%** | +2.2% | -6.3% | `fast_decay_cut` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2023-06-30 08:00` | `2023-07-04 08:00` | Live | `$7.6443` | `$8.2940` | **+8.50%** | **+8.16%** | +12.6% | -8.2% | `shelf_target_reclaim` |
| 3 | Book 4 | `2023-10-23 22:00` | `2023-11-06 02:00` | 316.0h | `$8.8372` | `$10.6047` | **+11.07%** | **+10.13%** | +22.0% | -4.0% | `target_reclaim` |
| 4 | Book 4 | `2024-02-17 12:00` | `2024-02-17 13:00` | 1.0h | `$9.2919` | `$11.1503` | **+4.82%** | **+4.61%** | +21.4% | -0.5% | `target_reclaim` |
| 5 | Book 4 | `2024-07-09 00:00` | `2024-07-10 04:00` | 28.0h | `$9.3981` | `$11.2777` | **+5.79%** | **+5.65%** | +23.7% | -1.0% | `target_reclaim` |
| 6 | Book 4 | `2025-06-02 22:00` | `2025-06-05 20:00` | 70.0h | `$11.7466` | `$9.9846` | **-14.14%** | **-15.33%** | +5.1% | -15.5% | `structural_stop` |
| 7 | Book 4 | `2026-01-13 11:00` | `2026-01-14 16:00` | 29.0h | `$10.3745` | `$12.4494` | **+5.79%** | **+5.65%** | +24.8% | -6.2% | `target_reclaim` |
| 8 | Book 4 | `2026-08-22 17:00` | `2026-09-04 20:00` | 315.0h | `$5.6194` | `$6.7433` | **+20.53%** | **+18.96%** | +20.4% | -14.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+45.0%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-5.9%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-15.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZEN`

* **Total Candidate Breakouts Filtered (Vetoed):** `1088`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `716` (65.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `207`
* **Saved Capital Losses Avoided:** `+12,266.8%`
* **Missed Upside Forgone:** `-8,935.1%`
* **Net Veto Alpha:** `+3,331.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `521` | `47.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `472` | `43.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `85` | `7.8%` |
| `Core 4: Funding Rate Cap` | `8` | `0.7%` |
| `Core 4: Whale Firewall` | `1` | `0.1%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*