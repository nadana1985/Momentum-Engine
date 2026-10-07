# Kronos V12: Institutional Symbol Tear Sheet — `SWARMS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.485`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-17.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.84x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.95%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`8.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.3% / -10.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-23 06:00` | `2025-04-23 09:00` | 3.0h | `$0.0352` | `$0.0323` | **-8.23%** | **-8.59%** | +7.9% | -11.3% | `stop_loss` |
| 2 | Book 3 | `2025-05-12 15:00` | `2025-05-13 02:00` | 11.0h | `$0.0405` | `$0.0372` | **-8.23%** | **-8.59%** | +3.4% | -11.5% | `stop_loss` |
| 3 | Book 3 | `2025-07-04 16:00` | `2025-07-04 22:00` | 6.0h | `$0.0240` | `$0.0261` | **+8.70%** | **+8.34%** | +9.7% | -1.0% | `target_reclaim` |
| 4 | Book 3 | `2025-08-10 22:00` | `2025-08-11 00:00` | 2.0h | `$0.0294` | `$0.0269` | **-8.23%** | **-8.59%** | +8.5% | -11.2% | `stop_loss` |
| 5 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0089` | `$0.0082` | **-8.23%** | **-8.59%** | +11.0% | -28.0% | `stop_loss` |
| 6 | Book 3 | `2026-09-23 14:00` | `2026-09-24 17:00` | 27.0h | `$0.0078` | `$0.0084` | **+8.70%** | **+8.34%** | +9.3% | -2.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `SWARMS`

* **Total Candidate Breakouts Filtered (Vetoed):** `52`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `41` (78.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `9`
* **Saved Capital Losses Avoided:** `+808.2%`
* **Missed Upside Forgone:** `-249.9%`
* **Net Veto Alpha:** `+558.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `37` | `71.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `6` | `11.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `5` | `9.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `7.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*