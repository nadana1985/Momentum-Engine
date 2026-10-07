# Kronos V12: Institutional Symbol Tear Sheet — `DYM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.421`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-22.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.80x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.87%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-31.0%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`36.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.7% / -6.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-03-12 08:00` | `2024-03-14 13:00` | 53.0h | `$7.0481` | `$6.4681` | **-8.23%** | **-8.59%** | +7.2% | -9.9% | `stop_loss` |
| 2 | Book 3 | `2024-05-29 16:00` | `2024-06-01 16:00` | 72.0h | `$3.0176` | `$3.0035` | **-0.47%** | **-0.47%** | +1.3% | -5.2% | `time_expiry` |
| 3 | Book 3 | `2024-09-25 06:00` | `2024-09-28 06:00` | 72.0h | `$1.9312` | `$1.8408` | **-4.68%** | **-4.79%** | +5.3% | -7.0% | `time_expiry` |
| 4 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$1.7138` | `$1.5727` | **-8.23%** | **-8.59%** | +4.3% | -10.8% | `stop_loss` |
| 5 | Book 3 | `2024-12-08 05:00` | `2024-12-09 09:00` | 28.0h | `$2.5496` | `$2.3398` | **-8.23%** | **-8.59%** | +2.0% | -8.9% | `stop_loss` |
| 6 | Book 3 | `2025-05-15 01:00` | `2025-05-15 14:00` | 13.0h | `$0.4209` | `$0.3863` | **-8.23%** | **-8.59%** | +3.8% | -8.0% | `stop_loss` |
| 7 | Book 3 | `2025-09-17 10:00` | `2025-09-18 07:00` | 21.0h | `$0.2273` | `$0.2471` | **+8.70%** | **+8.34%** | +11.2% | -2.7% | `target_reclaim` |
| 8 | Book 3 | `2026-09-20 09:00` | `2026-09-21 00:00` | 15.0h | `$0.0163` | `$0.0177` | **+8.70%** | **+8.34%** | +10.5% | -1.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `time_expiry` | `2` | `0.0%` | **`-5.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `DYM`

* **Total Candidate Breakouts Filtered (Vetoed):** `82`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `49` (59.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+719.4%`
* **Missed Upside Forgone:** `-587.3%`
* **Net Veto Alpha:** `+132.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `48` | `58.5%` |
| `Core 1: Macro Bear Veto` | `26` | `31.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `4` | `4.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `4.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*