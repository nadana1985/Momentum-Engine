# Kronos V12: Institutional Symbol Tear Sheet — `ANIME`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.778`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+30.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.36x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.82%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.6% / -5.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-12 18:00` | `2025-05-13 09:00` | 15.0h | `$0.0199` | `$0.0217` | **+8.70%** | **+8.34%** | +10.3% | -1.4% | `target_reclaim` |
| 2 | Book 3 | `2025-05-15 06:00` | `2025-05-17 10:00` | 52.0h | `$0.0205` | `$0.0223` | **+8.70%** | **+8.34%** | +9.7% | -2.5% | `target_reclaim` |
| 3 | Book 3 | `2025-05-21 01:00` | `2025-05-22 02:00` | 25.0h | `$0.0231` | `$0.0251` | **+8.70%** | **+8.34%** | +11.5% | -2.2% | `target_reclaim` |
| 4 | Book 3 | `2025-05-24 02:00` | `2025-05-25 07:00` | 29.0h | `$0.0254` | `$0.0276` | **+8.70%** | **+8.34%** | +8.8% | -0.4% | `target_reclaim` |
| 5 | Book 3 | `2025-06-06 17:00` | `2025-06-06 18:00` | 1.0h | `$0.0291` | `$0.0316` | **+8.70%** | **+8.34%** | +22.0% | -0.2% | `target_reclaim` |
| 6 | Book 3 | `2025-06-10 16:00` | `2025-06-10 21:00` | 5.0h | `$0.0378` | `$0.0347` | **-8.23%** | **-8.59%** | +2.4% | -19.0% | `stop_loss` |
| 7 | Book 3 | `2025-07-23 17:00` | `2025-07-24 06:00` | 13.0h | `$0.0199` | `$0.0183` | **-8.23%** | **-8.59%** | +4.9% | -9.4% | `stop_loss` |
| 8 | Book 3 | `2026-09-10 12:00` | `2026-09-13 12:00` | 72.0h | `$0.0030` | `$0.0032` | **+6.22%** | **+6.03%** | +7.6% | -6.7% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+41.7%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+6.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `ANIME`

* **Total Candidate Breakouts Filtered (Vetoed):** `53`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `44` (83.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+663.4%`
* **Missed Upside Forgone:** `-127.9%`
* **Net Veto Alpha:** `+535.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `21` | `39.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `21` | `39.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `10` | `18.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*