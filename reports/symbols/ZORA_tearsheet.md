# Kronos V12: Institutional Symbol Tear Sheet — `ZORA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.456`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+7.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.57%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`12.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.3% / -9.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-10-08 16:00` | `2025-10-08 17:00` | 1.0h | `$0.0523` | `$0.0568` | **+8.70%** | **+8.34%** | +9.3% | -0.4% | `target_reclaim` |
| 2 | Book 3 | `2025-10-10 21:00` | `2025-10-10 22:00` | 1.0h | `$0.0759` | `$0.0696` | **-8.23%** | **-8.59%** | +30.6% | -33.3% | `stop_loss` |
| 3 | Book 3 | `2026-08-21 15:00` | `2026-08-21 17:00` | 2.0h | `$0.0066` | `$0.0071` | **+8.70%** | **+8.34%** | +9.2% | -0.2% | `target_reclaim` |
| 4 | Book 3 | `2026-08-24 00:00` | `2026-08-25 12:00` | 36.0h | `$0.0069` | `$0.0064` | **-8.23%** | **-8.59%** | +3.0% | -8.5% | `stop_loss` |
| 5 | Book 3 | `2026-09-02 07:00` | `2026-09-03 07:00` | 24.0h | `$0.0073` | `$0.0079` | **+8.70%** | **+8.34%** | +9.5% | -3.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+25.0%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZORA`

* **Total Candidate Breakouts Filtered (Vetoed):** `22`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `19` (86.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `10`
* **Saved Capital Losses Avoided:** `+556.2%`
* **Missed Upside Forgone:** `-367.9%`
* **Net Veto Alpha:** `+188.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `11` | `50.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `6` | `27.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `4` | `18.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `4.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*