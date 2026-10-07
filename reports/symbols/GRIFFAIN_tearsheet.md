# Kronos V12: Institutional Symbol Tear Sheet — `GRIFFAIN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`28.6%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.374`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-28.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.76x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.99%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`14.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.7% / -9.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-27 01:00` | `2025-04-27 02:00` | 1.0h | `$0.0674` | `$0.0608` | **-9.77%** | **-10.28%** | +9.5% | -11.5% | `stop_loss` |
| 2 | Book 3 | `2025-05-01 18:00` | `2025-05-03 17:00` | 47.0h | `$0.0691` | `$0.0634` | **-8.23%** | **-8.59%** | +6.9% | -8.6% | `stop_loss` |
| 3 | Book 3 | `2025-05-15 23:00` | `2025-05-16 20:00` | 21.0h | `$0.1067` | `$0.0979` | **-8.23%** | **-8.59%** | +7.6% | -8.1% | `stop_loss` |
| 4 | Book 3 | `2025-07-12 12:00` | `2025-07-13 11:00` | 23.0h | `$0.0486` | `$0.0528` | **+8.70%** | **+8.34%** | +11.2% | -0.7% | `target_reclaim` |
| 5 | Book 3 | `2026-08-22 05:00` | `2026-08-22 07:00` | 2.0h | `$0.0127` | `$0.0138` | **+8.70%** | **+8.34%** | +10.4% | -16.3% | `target_reclaim` |
| 6 | Book 3 | `2026-09-12 09:00` | `2026-09-12 13:00` | 4.0h | `$0.0136` | `$0.0125` | **-8.23%** | **-8.59%** | +8.7% | -8.7% | `stop_loss` |
| 7 | Book 3 | `2026-09-13 01:00` | `2026-09-13 02:00` | 1.0h | `$0.0148` | `$0.0135` | **-8.23%** | **-8.59%** | +6.8% | -11.2% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `5` | `0.0%` | **`-44.6%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `GRIFFAIN`

* **Total Candidate Breakouts Filtered (Vetoed):** `82`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `58` (70.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+950.9%`
* **Missed Upside Forgone:** `-741.4%`
* **Net Veto Alpha:** `+209.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `52` | `63.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `20` | `24.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `7` | `8.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `3.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*