# Kronos V12: Institutional Symbol Tear Sheet — `ALCH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.574`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-12.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.88x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.48%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-20.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`19.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.8% / -9.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-15 14:00` | `2025-04-15 15:00` | 1.0h | `$0.1404` | `$0.1527` | **+8.70%** | **+8.34%** | +20.3% | -0.5% | `target_reclaim` |
| 2 | Book 3 | `2025-04-25 18:00` | `2025-04-27 06:00` | 36.0h | `$0.1653` | `$0.1517` | **-8.23%** | **-8.59%** | +2.8% | -10.3% | `stop_loss` |
| 3 | Book 3 | `2025-10-04 10:00` | `2025-10-04 11:00` | 1.0h | `$0.1004` | `$0.0892` | **-11.20%** | **-11.87%** | +29.3% | -24.3% | `stop_loss` |
| 4 | Book 3 | `2026-08-26 09:00` | `2026-08-28 13:00` | 52.0h | `$0.0293` | `$0.0319` | **+8.70%** | **+8.34%** | +11.0% | -2.5% | `target_reclaim` |
| 5 | Book 3 | `2026-09-21 21:00` | `2026-09-22 03:00` | 6.0h | `$0.0546` | `$0.0501` | **-8.23%** | **-8.59%** | +10.8% | -8.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-29.1%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALCH`

* **Total Candidate Breakouts Filtered (Vetoed):** `64`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `50` (78.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+1,070.2%`
* **Missed Upside Forgone:** `-823.6%`
* **Net Veto Alpha:** `+246.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `40` | `62.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `11` | `17.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `9` | `14.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `6.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*