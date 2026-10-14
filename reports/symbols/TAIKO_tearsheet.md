# Kronos V12: Institutional Symbol Tear Sheet — `TAIKO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.432`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-14.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.86x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.47%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-10.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`22.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.2% / -14.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-01-26 00:00` | `2026-01-30 00:00` | Live | `$0.2159` | `$0.1982` | **-8.20%** | **-8.56%** | +-19.8% | -56.0% | `shelf_stop_loss` |
| 2 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0738` | `$0.0769` | **+4.17%** | **+4.08%** | +12.5% | -3.0% | `target_reclaim` |
| 3 | Book 3 | `2026-09-09 15:00` | `2026-09-09 22:00` | 7.0h | `$0.0809` | `$0.0742` | **-8.23%** | **-8.59%** | +2.0% | -9.4% | `stop_loss` |
| 4 | Book 2 | `2026-09-19 21:00` | `2026-09-21 21:00` | 48.0h | `$0.0899` | `$0.0896` | **-0.32%** | **-0.32%** | +3.6% | -7.1% | `fast_decay_cut` |
| 5 | Book 3 | `2026-09-23 16:00` | `2026-09-25 23:00` | 55.0h | `$0.0868` | `$0.0933` | **+7.44%** | **+7.17%** | +7.5% | -0.6% | `target_reclaim` |
| 6 | Book 3 | `2026-09-29 01:00` | `2026-09-29 02:00` | 1.0h | `$0.0902` | `$0.0828` | **-8.23%** | **-8.59%** | +1.2% | -8.7% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+11.3%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `TAIKO`

* **Total Candidate Breakouts Filtered (Vetoed):** `119`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `94` (79.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+1,260.2%`
* **Missed Upside Forgone:** `-1,061.9%`
* **Net Veto Alpha:** `+198.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `83` | `69.7%` |
| `Core 1: Macro Bear Veto` | `23` | `19.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `11` | `9.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*