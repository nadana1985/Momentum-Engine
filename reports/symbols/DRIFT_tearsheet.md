# Kronos V12: Institutional Symbol Tear Sheet — `DRIFT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.320`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+5.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.10%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`35.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.6% / -9.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-04-30 00:00` | `2025-05-04 00:00` | Live | `$0.6408` | `$0.6952` | **+8.50%** | **+8.16%** | +5.1% | -21.5% | `shelf_target_reclaim` |
| 2 | Book 3 | `2025-05-30 06:00` | `2025-05-30 09:00` | 3.0h | `$0.7023` | `$0.6445` | **-8.23%** | **-8.59%** | +4.9% | -8.1% | `stop_loss` |
| 3 | Book 3 | `2025-09-18 02:00` | `2025-09-18 08:00` | 6.0h | `$0.7930` | `$0.8620` | **+8.70%** | **+8.34%** | +8.8% | -0.5% | `target_reclaim` |
| 4 | Book 3 | `2025-09-19 15:00` | `2025-09-22 03:00` | 60.0h | `$0.8538` | `$0.7835` | **-8.23%** | **-8.59%** | +5.2% | -10.2% | `stop_loss` |
| 5 | Book 3 | `2026-09-23 14:00` | `2026-09-26 14:00` | 72.0h | `$0.0185` | `$0.0197` | **+6.37%** | **+6.18%** | +14.2% | -5.6% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+6.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `DRIFT`

* **Total Candidate Breakouts Filtered (Vetoed):** `130`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `116` (89.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+1,678.5%`
* **Missed Upside Forgone:** `-376.6%`
* **Net Veto Alpha:** `+1,302.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `71` | `54.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `52` | `40.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `5` | `3.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*