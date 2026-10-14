# Kronos V12: Institutional Symbol Tear Sheet — `1000000MOG`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.723`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.19%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`9.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.0% / -6.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-21 16:00` | `2025-04-22 02:00` | 10.0h | `$0.4740` | `$0.4938` | **+4.17%** | **+4.08%** | +4.3% | -6.8% | `target_reclaim` |
| 2 | Book 3 | `2025-05-11 07:00` | `2025-05-11 12:00` | 5.0h | `$1.1217` | `$1.2192` | **+8.70%** | **+8.34%** | +10.3% | -1.5% | `target_reclaim` |
| 3 | Book 3 | `2025-07-04 02:00` | `2025-07-04 16:00` | 14.0h | `$1.0295` | `$0.9448` | **-8.23%** | **-8.59%** | +2.2% | -9.8% | `stop_loss` |
| 4 | Book 3 | `2025-07-14 15:00` | `2025-07-15 01:00` | 10.0h | `$1.7221` | `$1.5803` | **-8.23%** | **-8.59%** | +3.3% | -9.3% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+12.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000000MOG`

* **Total Candidate Breakouts Filtered (Vetoed):** `236`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `164` (69.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `52`
* **Saved Capital Losses Avoided:** `+2,365.5%`
* **Missed Upside Forgone:** `-1,747.7%`
* **Net Veto Alpha:** `+617.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `183` | `77.5%` |
| `Core 1: Macro Bear Veto` | `32` | `13.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `19` | `8.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*