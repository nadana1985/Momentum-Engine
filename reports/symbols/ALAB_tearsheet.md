# Kronos V12: Institutional Symbol Tear Sheet — `ALAB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.787`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+20.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.23x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.14%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-5.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`90.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.9% / -7.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-06-29 16:00` | `2026-07-03 16:00` | Live | `$412.7028` | `$447.7825` | **+8.50%** | **+8.16%** | +4.4% | -21.8% | `shelf_target_reclaim` |
| 2 | Book 2 | `2026-08-26 20:00` | `2026-08-28 20:00` | 48.0h | `$294.4543` | `$289.9533` | **-1.75%** | **-1.76%** | +5.3% | -2.7% | `fast_decay_cut` |
| 3 | Book 2 | `2026-09-17 13:00` | `2026-09-24 13:00` | 168.0h | `$290.9556` | `$347.2298` | **+21.82%** | **+19.94%** | +26.9% | -4.0% | `time_cap` |
| 4 | Book 3 | `2026-09-28 01:00` | `2026-10-01 01:00` | 72.0h | `$357.8784` | `$356.4068` | **-0.41%** | **-0.41%** | +2.6% | -4.3% | `time_expiry` |
| 5 | Book 2 | `2026-10-05 15:00` | `2026-10-08 17:00` | 74.0h | `$363.6870` | `$345.1179` | **-5.11%** | **-5.24%** | +10.5% | -5.4% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.8%`** |
| `initial_stop` | `1` | `0.0%` | **`-5.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `time_cap` | `1` | `100.0%` | **`+19.9%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALAB`

* **Total Candidate Breakouts Filtered (Vetoed):** `9`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `8` (88.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+120.0%`
* **Missed Upside Forgone:** `-42.5%`
* **Net Veto Alpha:** `+77.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `8` | `88.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `11.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*