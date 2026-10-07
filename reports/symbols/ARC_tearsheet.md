# Kronos V12: Institutional Symbol Tear Sheet — `ARC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`55.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.424`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+12.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.13x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.38%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-25.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`21.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.6% / -7.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-23 16:00` | `2025-04-23 18:00` | 2.0h | `$0.0497` | `$0.0540` | **+8.70%** | **+8.34%** | +14.1% | -8.4% | `target_reclaim` |
| 2 | Book 3 | `2025-04-25 09:00` | `2025-04-25 11:00` | 2.0h | `$0.0578` | `$0.0628` | **+8.70%** | **+8.34%** | +12.6% | -1.2% | `target_reclaim` |
| 3 | Book 3 | `2025-04-25 13:00` | `2025-04-26 01:00` | 12.0h | `$0.0592` | `$0.0644` | **+8.70%** | **+8.34%** | +11.0% | -6.6% | `target_reclaim` |
| 4 | Book 3 | `2025-04-27 01:00` | `2025-04-27 03:00` | 2.0h | `$0.0622` | `$0.0571` | **-8.23%** | **-8.59%** | +11.3% | -10.6% | `stop_loss` |
| 5 | Book 3 | `2025-04-28 12:00` | `2025-04-30 03:00` | 39.0h | `$0.0664` | `$0.0609` | **-8.23%** | **-8.59%** | +5.7% | -10.5% | `stop_loss` |
| 6 | Book 3 | `2025-05-12 17:00` | `2025-05-13 03:00` | 10.0h | `$0.0911` | `$0.0836` | **-8.23%** | **-8.59%** | +5.7% | -10.3% | `stop_loss` |
| 7 | Book 3 | `2025-07-11 21:00` | `2025-07-14 04:00` | 55.0h | `$0.0313` | `$0.0341` | **+8.70%** | **+8.34%** | +9.6% | -7.5% | `target_reclaim` |
| 8 | Book 3 | `2025-10-04 02:00` | `2025-10-07 02:00` | 72.0h | `$0.0224` | `$0.0216` | **-3.46%** | **-3.52%** | +7.3% | -7.5% | `time_expiry` |
| 9 | Book 3 | `2026-09-15 18:00` | `2026-09-15 21:00` | 3.0h | `$0.0747` | `$0.0812` | **+8.70%** | **+8.34%** | +9.2% | -1.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+41.7%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_expiry` | `1` | `0.0%` | **`-3.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `ARC`

* **Total Candidate Breakouts Filtered (Vetoed):** `73`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `61` (83.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+1,636.1%`
* **Missed Upside Forgone:** `-563.7%`
* **Net Veto Alpha:** `+1,072.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `58` | `79.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `13` | `17.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `2.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*