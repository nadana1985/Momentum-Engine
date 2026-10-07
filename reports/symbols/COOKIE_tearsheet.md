# Kronos V12: Institutional Symbol Tear Sheet — `COOKIE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`42.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.728`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-9.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.91x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.33%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`25.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.6% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-26 13:00` | `2025-04-28 01:00` | 36.0h | `$0.1297` | `$0.1190` | **-8.23%** | **-8.59%** | +8.1% | -10.3% | `stop_loss` |
| 2 | Book 3 | `2025-05-21 17:00` | `2025-05-21 22:00` | 5.0h | `$0.2061` | `$0.2240` | **+8.70%** | **+8.34%** | +9.1% | -1.0% | `target_reclaim` |
| 3 | Book 3 | `2025-05-26 08:00` | `2025-05-26 09:00` | 1.0h | `$0.3190` | `$0.2927` | **-8.23%** | **-8.59%** | +11.7% | -8.7% | `stop_loss` |
| 4 | Book 3 | `2025-06-30 12:00` | `2025-07-01 22:00` | 34.0h | `$0.1690` | `$0.1551` | **-8.23%** | **-8.59%** | +5.7% | -8.4% | `stop_loss` |
| 5 | Book 3 | `2025-07-18 19:00` | `2025-07-20 16:00` | 45.0h | `$0.1936` | `$0.2104` | **+8.70%** | **+8.34%** | +12.3% | -4.3% | `target_reclaim` |
| 6 | Book 3 | `2025-07-23 13:00` | `2025-07-23 20:00` | 7.0h | `$0.1996` | `$0.1832` | **-8.23%** | **-8.59%** | +4.5% | -8.6% | `stop_loss` |
| 7 | Book 3 | `2026-09-23 14:00` | `2026-09-25 18:00` | 52.0h | `$0.0114` | `$0.0123` | **+8.70%** | **+8.34%** | +8.8% | -2.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `target_reclaim` | `3` | `100.0%` | **`+25.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `COOKIE`

* **Total Candidate Breakouts Filtered (Vetoed):** `51`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (66.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `15`
* **Saved Capital Losses Avoided:** `+493.1%`
* **Missed Upside Forgone:** `-463.4%`
* **Net Veto Alpha:** `+29.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `26` | `51.0%` |
| `Core 1: Macro Bear Veto` | `22` | `43.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `3.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `2.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*