# Kronos V12: Institutional Symbol Tear Sheet — `ZORA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.843`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.67%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-25.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`8.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.2% / -13.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-10-08 03:00` | `2025-10-08 17:00` | 14.0h | `$0.0545` | `$0.0568` | **+4.17%** | **+4.08%** | +4.8% | -4.5% | `target_reclaim` |
| 2 | Book 3 | `2025-10-09 19:00` | `2025-10-09 20:00` | 1.0h | `$0.0792` | `$0.0825` | **+4.17%** | **+4.08%** | +12.4% | -4.1% | `target_reclaim` |
| 3 | Book 3 | `2025-10-10 01:00` | `2025-10-10 09:00` | 8.0h | `$0.0795` | `$0.0911` | **+14.53%** | **+13.56%** | +17.1% | -1.7% | `target_reclaim` |
| 4 | Book 3 | `2025-10-10 20:00` | `2025-10-10 21:00` | 1.0h | `$0.0952` | `$0.0874` | **-8.23%** | **-8.59%** | +16.5% | -46.8% | `stop_loss` |
| 5 | Book 3 | `2026-08-22 05:00` | `2026-08-23 04:00` | 23.0h | `$0.0065` | `$0.0059` | **-8.23%** | **-8.59%** | +8.3% | -14.1% | `stop_loss` |
| 6 | Book 3 | `2026-08-23 21:00` | `2026-08-24 01:00` | 4.0h | `$0.0072` | `$0.0067` | **-8.23%** | **-8.59%** | +2.2% | -8.6% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `target_reclaim` | `3` | `100.0%` | **`+21.7%`** |

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