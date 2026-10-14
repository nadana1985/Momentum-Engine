# Kronos V12: Institutional Symbol Tear Sheet — `EPIC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`13.368`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+95.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.59x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+15.89%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-7.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`28.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+22.3% / -6.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2025-07-18 03:00` | `2025-07-18 16:00` | 13.0h | `$1.2660` | `$1.5192` | **+47.05%** | **+39.70%** | +29.4% | -1.3% | `target_reclaim` |
| 2 | Book 2 | `2026-05-04 00:00` | `2026-05-06 00:00` | 48.0h | `$0.3601` | `$0.3523` | **-2.62%** | **-2.65%** | +3.7% | -6.7% | `fast_decay_cut` |
| 3 | Book 4 | `2026-06-03 10:00` | `2026-06-03 11:00` | 1.0h | `$0.5714` | `$0.4857` | **-4.86%** | **-5.05%** | +1.5% | -16.8% | `structural_stop` |
| 4 | Book 2 | `2026-09-04 16:00` | `2026-09-06 10:00` | 42.0h | `$0.3601` | `$0.4743` | **+37.09%** | **+32.22%** | +36.0% | -5.1% | `climax_top_harvest` |
| 5 | Book 2 | `2026-09-18 18:00` | `2026-09-20 00:00` | 30.0h | `$0.3799` | `$0.4590` | **+23.53%** | **+21.38%** | +42.5% | -4.4% | `trail_stop` |
| 6 | Book 4 | `2026-09-20 13:00` | `2026-09-22 00:00` | 35.0h | `$0.5307` | `$0.6368` | **+10.20%** | **+9.74%** | +20.8% | -5.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+49.4%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+32.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-2.7%`** |
| `structural_stop` | `1` | `0.0%` | **`-5.1%`** |
| `trail_stop` | `1` | `100.0%` | **`+21.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `EPIC`

* **Total Candidate Breakouts Filtered (Vetoed):** `434`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `301` (69.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `120`
* **Saved Capital Losses Avoided:** `+4,447.6%`
* **Missed Upside Forgone:** `-6,746.4%`
* **Net Veto Alpha:** `+-2,298.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `391` | `90.1%` |
| `Core 1: Macro Bear Veto` | `42` | `9.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*