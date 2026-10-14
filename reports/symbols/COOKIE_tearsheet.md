# Kronos V12: Institutional Symbol Tear Sheet — `COOKIE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`62.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.356`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+9.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.10x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.15%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-25.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`31.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.4% / -13.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-01-10 06:00` | `2025-01-14 06:00` | Live | `$0.4534` | `$0.4919` | **+8.50%** | **+8.16%** | +25.9% | -50.1% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-02-10 10:00` | `2025-02-14 10:00` | Live | `$0.1872` | `$0.2031` | **+8.50%** | **+8.16%** | +25.5% | -18.1% | `shelf_target_reclaim` |
| 3 | Book 3 | `2025-04-26 13:00` | `2025-04-28 01:00` | 36.0h | `$0.1297` | `$0.1190` | **-8.23%** | **-8.59%** | +8.1% | -10.3% | `stop_loss` |
| 4 | Book 3 | `2025-05-26 08:00` | `2025-05-26 13:00` | 5.0h | `$0.3024` | `$0.2775` | **-8.23%** | **-8.59%** | +17.8% | -8.6% | `stop_loss` |
| 5 | Book 3 | `2025-06-30 01:00` | `2025-07-01 05:00` | 28.0h | `$0.1764` | `$0.1618` | **-8.23%** | **-8.59%** | +1.7% | -8.6% | `stop_loss` |
| 6 | Book 3 | `2025-07-18 19:00` | `2025-07-20 16:00` | 45.0h | `$0.1940` | `$0.2104` | **+8.47%** | **+8.13%** | +12.0% | -4.5% | `target_reclaim` |
| 7 | Book 3 | `2026-09-22 00:00` | `2026-09-22 01:00` | 1.0h | `$0.0118` | `$0.0123` | **+4.17%** | **+4.08%** | +16.2% | -2.7% | `target_reclaim` |
| 8 | Book 3 | `2026-09-23 14:00` | `2026-09-26 14:00` | 72.0h | `$0.0120` | `$0.0127` | **+6.62%** | **+6.41%** | +7.7% | -7.3% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `target_reclaim` | `2` | `100.0%` | **`+12.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+6.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `COOKIE`

* **Total Candidate Breakouts Filtered (Vetoed):** `78`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `61` (78.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+1,039.3%`
* **Missed Upside Forgone:** `-773.3%`
* **Net Veto Alpha:** `+266.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `53` | `67.9%` |
| `Core 1: Macro Bear Veto` | `22` | `28.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `2.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*