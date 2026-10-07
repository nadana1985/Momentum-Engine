# Kronos V12: Institutional Symbol Tear Sheet — `1000CHEEMS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.012`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+0.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.04%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-12.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`39.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.3% / -5.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-02-09 15:00` | `2025-02-09 21:00` | 6.0h | `$0.0009` | `$0.0008` | **-8.23%** | **-8.59%** | +8.4% | -12.3% | `stop_loss` |
| 2 | Book 3 | `2025-05-09 14:00` | `2025-05-10 00:00` | 10.0h | `$0.0016` | `$0.0017` | **+8.70%** | **+8.34%** | +12.6% | -3.0% | `target_reclaim` |
| 3 | Book 3 | `2025-05-13 13:00` | `2025-05-14 04:00` | 15.0h | `$0.0017` | `$0.0018` | **+8.70%** | **+8.34%** | +9.2% | -1.5% | `target_reclaim` |
| 4 | Book 3 | `2025-08-18 01:00` | `2025-08-20 14:00` | 61.0h | `$0.0013` | `$0.0012` | **-8.23%** | **-8.59%** | +1.6% | -8.5% | `stop_loss` |
| 5 | Book 3 | `2025-09-19 15:00` | `2025-09-22 15:00` | 72.0h | `$0.0012` | `$0.0012` | **-3.94%** | **-4.02%** | +6.6% | -5.5% | `time_expiry` |
| 6 | Book 3 | `2026-09-23 15:00` | `2026-09-26 15:00` | 72.0h | `$0.0005` | `$0.0006` | **+4.90%** | **+4.78%** | +5.6% | -1.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `time_expiry` | `2` | `50.0%` | **`+0.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000CHEEMS`

* **Total Candidate Breakouts Filtered (Vetoed):** `64`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `45` (70.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `10`
* **Saved Capital Losses Avoided:** `+647.0%`
* **Missed Upside Forgone:** `-367.3%`
* **Net Veto Alpha:** `+279.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `37` | `57.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `14` | `21.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `13` | `20.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*