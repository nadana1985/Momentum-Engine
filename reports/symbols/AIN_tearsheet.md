# Kronos V12: Institutional Symbol Tear Sheet — `AIN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.883`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+24.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.28x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.95%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`1.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.9% / -5.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-09-19 15:00` | `2025-09-19 16:00` | 1.0h | `$0.1456` | `$0.1583` | **+8.70%** | **+8.34%** | +14.8% | -0.5% | `target_reclaim` |
| 2 | Book 3 | `2026-09-14 12:00` | `2026-09-14 13:00` | 1.0h | `$0.0929` | `$0.1010` | **+8.70%** | **+8.34%** | +14.6% | -8.5% | `target_reclaim` |
| 3 | Book 3 | `2026-09-14 19:00` | `2026-09-14 21:00` | 2.0h | `$0.1174` | `$0.1277` | **+8.70%** | **+8.34%** | +13.5% | -1.4% | `target_reclaim` |
| 4 | Book 3 | `2026-09-15 02:00` | `2026-09-15 04:00` | 2.0h | `$0.1343` | `$0.1233` | **-8.23%** | **-8.59%** | +13.2% | -16.9% | `stop_loss` |
| 5 | Book 3 | `2026-09-15 20:00` | `2026-09-15 21:00` | 1.0h | `$0.1643` | `$0.1785` | **+8.70%** | **+8.34%** | +18.4% | -0.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `AIN`

* **Total Candidate Breakouts Filtered (Vetoed):** `27`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (88.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+969.9%`
* **Missed Upside Forgone:** `-491.9%`
* **Net Veto Alpha:** `+478.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `20` | `74.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `6` | `22.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `1` | `3.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*