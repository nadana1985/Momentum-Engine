# Kronos V12: Institutional Symbol Tear Sheet — `AVA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.761`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.03%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`27.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.5% / -5.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-27 13:00` | `2025-04-29 04:00` | 39.0h | `$0.5957` | `$0.6205` | **+4.17%** | **+4.08%** | +4.3% | -3.1% | `target_reclaim` |
| 2 | Book 3 | `2025-05-04 12:00` | `2025-05-05 10:00` | 22.0h | `$0.6227` | `$0.5714` | **-8.23%** | **-8.59%** | +1.7% | -9.4% | `stop_loss` |
| 3 | Book 3 | `2025-05-15 05:00` | `2025-05-17 01:00` | 44.0h | `$0.6773` | `$0.6216` | **-8.23%** | **-8.59%** | +1.2% | -9.0% | `stop_loss` |
| 4 | Book 3 | `2025-09-21 09:00` | `2025-09-21 15:00` | 6.0h | `$0.5649` | `$0.6180` | **+9.40%** | **+8.98%** | +10.9% | -1.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+13.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `AVA`

* **Total Candidate Breakouts Filtered (Vetoed):** `76`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `48` (63.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+496.8%`
* **Missed Upside Forgone:** `-54.2%`
* **Net Veto Alpha:** `+442.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `47` | `61.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `20` | `26.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `7.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `3.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*