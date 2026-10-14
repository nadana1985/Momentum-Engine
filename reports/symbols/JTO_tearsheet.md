# Kronos V12: Institutional Symbol Tear Sheet — `JTO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.131`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+4.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.69%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-31.0%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`60.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.4% / -15.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2024-07-19 12:00` | `2024-07-23 12:00` | Live | `$2.4071` | `$2.6117` | **+8.50%** | **+8.16%** | +25.7% | -27.7% | `shelf_target_reclaim` |
| 2 | Book 2 | `2025-04-22 16:00` | `2025-04-24 16:00` | 48.0h | `$1.8182` | `$1.8101` | **-0.52%** | **-0.52%** | +4.7% | -7.0% | `fast_decay_cut` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2025-06-10 23:00` | `2025-06-14 23:00` | Live | `$2.0447` | `$2.2185` | **+8.50%** | **+8.16%** | +12.0% | -15.0% | `shelf_target_reclaim` |
| 4 | Book 4 | `2025-06-16 01:00` | `2025-06-22 14:00` | 157.0h | `$2.3003` | `$1.9553` | **-14.51%** | **-15.73%** | +5.0% | -15.5% | `structural_stop` |
| 5 | Book 1 | `2026-08-21 22:00` | `2026-08-22 05:00` | 7.0h | `$0.6463` | `$0.5673` | **-14.17%** | **-15.30%** | +4.8% | -23.4% | `initial_stop` |
| 6 | Book 1 | `2026-09-25 09:00` | `2026-09-26 16:00` | 31.0h | `$0.5341` | `$0.6143` | **+21.14%** | **+19.38%** | +15.9% | -3.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.5%`** |
| `initial_stop` | `1` | `0.0%` | **`-15.3%`** |
| `structural_stop` | `1` | `0.0%` | **`-15.7%`** |
| `target_reclaim` | `1` | `100.0%` | **`+19.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `JTO`

* **Total Candidate Breakouts Filtered (Vetoed):** `356`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `279` (78.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+4,443.7%`
* **Missed Upside Forgone:** `-413.6%`
* **Net Veto Alpha:** `+4,030.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `272` | `76.4%` |
| `Core 1: Macro Bear Veto` | `81` | `22.8%` |
| `Core 4: Funding Rate Cap` | `3` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*