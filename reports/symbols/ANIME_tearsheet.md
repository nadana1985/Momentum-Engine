# Kronos V12: Institutional Symbol Tear Sheet — `ANIME`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.451`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+12.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.13x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.49%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`35.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.5% / -6.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-12 18:00` | `2025-05-13 09:00` | 15.0h | `$0.0198` | `$0.0217` | **+9.32%** | **+8.91%** | +10.9% | -0.9% | `target_reclaim` |
| 2 | Book 3 | `2025-05-19 00:00` | `2025-05-19 14:00` | 14.0h | `$0.0239` | `$0.0251` | **+4.73%** | **+4.62%** | +9.8% | -2.9% | `target_reclaim` |
| 3 | Book 3 | `2025-06-10 17:00` | `2025-06-10 21:00` | 4.0h | `$0.0364` | `$0.0334` | **-8.23%** | **-8.59%** | +2.8% | -16.0% | `stop_loss` |
| 4 | Book 3 | `2025-07-23 21:00` | `2025-07-26 21:00` | 72.0h | `$0.0192` | `$0.0195` | **+1.57%** | **+1.55%** | +5.0% | -6.2% | `time_expiry` |
| 5 | Book 3 | `2026-09-10 16:00` | `2026-09-13 16:00` | 72.0h | `$0.0030` | `$0.0031` | **+6.15%** | **+5.97%** | +8.9% | -5.9% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+13.5%`** |
| `time_expiry` | `2` | `100.0%` | **`+7.5%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `ANIME`

* **Total Candidate Breakouts Filtered (Vetoed):** `63`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `54` (85.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+1,091.8%`
* **Missed Upside Forgone:** `-127.9%`
* **Net Veto Alpha:** `+963.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `31` | `49.2%` |
| `Core 1: Macro Bear Veto` | `21` | `33.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `10` | `15.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*