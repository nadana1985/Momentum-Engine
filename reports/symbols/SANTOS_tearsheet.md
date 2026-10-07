# Kronos V12: Institutional Symbol Tear Sheet — `SANTOS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.097`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+2.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.02x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.28%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-14.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`38.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.8% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-12-08 11:00` | `2024-12-09 08:00` | 21.0h | `$5.0324` | `$4.6182` | **-8.23%** | **-8.59%** | +3.6% | -9.6% | `stop_loss` |
| 2 | Book 3 | `2025-01-31 20:00` | `2025-02-01 13:00` | 17.0h | `$3.2467` | `$2.9795` | **-8.23%** | **-8.59%** | +1.2% | -8.6% | `stop_loss` |
| 3 | Book 3 | `2025-05-05 01:00` | `2025-05-08 01:00` | 72.0h | `$2.3874` | `$2.3611` | **-1.10%** | **-1.11%** | +5.1% | -3.9% | `time_expiry` |
| 4 | Book 3 | `2025-07-23 17:00` | `2025-07-26 17:00` | 72.0h | `$2.2420` | `$2.2534` | **+0.50%** | **+0.50%** | +5.0% | -6.9% | `time_expiry` |
| 5 | Book 3 | `2025-07-29 14:00` | `2025-08-01 14:00` | 72.0h | `$2.3074` | `$2.1955` | **-4.85%** | **-4.97%** | +3.5% | -6.9% | `time_expiry` |
| 6 | Book 3 | `2025-08-10 18:00` | `2025-08-10 20:00` | 2.0h | `$2.9596` | `$3.2170` | **+8.70%** | **+8.34%** | +9.0% | -1.2% | `target_reclaim` |
| 7 | Book 3 | `2025-10-02 14:00` | `2025-10-04 16:00` | 50.0h | `$1.9219` | `$2.0890` | **+8.70%** | **+8.34%** | +8.9% | -0.9% | `target_reclaim` |
| 8 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.4647` | `$0.5051` | **+8.70%** | **+8.34%** | +18.0% | -11.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+25.0%`** |
| `time_expiry` | `3` | `33.3%` | **`-5.6%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `SANTOS`

* **Total Candidate Breakouts Filtered (Vetoed):** `44`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `26` (59.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+423.5%`
* **Missed Upside Forgone:** `-86.3%`
* **Net Veto Alpha:** `+337.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `28` | `63.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `13` | `29.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `4.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `2.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*