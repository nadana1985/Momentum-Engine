# Kronos V12: Institutional Symbol Tear Sheet — `JELLYJELLY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-48.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.61x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-6.96%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-40.2%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`28.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.3% / -14.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-01 12:00` | `2025-05-01 16:00` | 4.0h | `$0.0377` | `$0.0346` | **-8.23%** | **-8.59%** | +4.3% | -9.0% | `stop_loss` |
| 2 | Book 3 | `2025-05-09 09:00` | `2025-05-09 10:00` | 1.0h | `$0.0397` | `$0.0355` | **-10.47%** | **-11.06%** | +9.7% | -34.3% | `stop_loss` |
| 3 | Book 3 | `2025-05-14 13:00` | `2025-05-14 14:00` | 1.0h | `$0.0481` | `$0.0441` | **-8.23%** | **-8.59%** | +16.9% | -26.3% | `stop_loss` |
| 4 | Book 3 | `2025-06-12 11:00` | `2025-06-12 20:00` | 9.0h | `$0.0241` | `$0.0221` | **-8.23%** | **-8.59%** | +2.5% | -8.4% | `stop_loss` |
| 5 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0566` | `$0.0553` | **-2.26%** | **-2.29%** | +9.5% | -7.8% | `time_expiry` |
| 6 | Book 3 | `2026-09-18 04:00` | `2026-09-21 04:00` | 72.0h | `$0.0562` | `$0.0556` | **-1.04%** | **-1.04%** | +12.0% | -4.6% | `time_expiry` |
| 7 | Book 3 | `2026-09-26 14:00` | `2026-09-28 05:00` | 39.0h | `$0.0611` | `$0.0561` | **-8.23%** | **-8.59%** | +10.0% | -8.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `5` | `0.0%` | **`-45.4%`** |
| `time_expiry` | `2` | `0.0%` | **`-3.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `JELLYJELLY`

* **Total Candidate Breakouts Filtered (Vetoed):** `93`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `81` (87.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `51`
* **Saved Capital Losses Avoided:** `+2,383.5%`
* **Missed Upside Forgone:** `-2,905.6%`
* **Net Veto Alpha:** `+-522.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `68` | `73.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `18` | `19.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5` | `5.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `2.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*