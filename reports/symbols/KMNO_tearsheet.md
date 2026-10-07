# Kronos V12: Institutional Symbol Tear Sheet — `KMNO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`42.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.585`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-14.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.87x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.04%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`30.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.5% / -6.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-07 11:00` | `2025-05-07 19:00` | 8.0h | `$0.0716` | `$0.0657` | **-8.23%** | **-8.59%** | +5.1% | -11.3% | `stop_loss` |
| 2 | Book 3 | `2025-07-23 12:00` | `2025-07-23 21:00` | 9.0h | `$0.0635` | `$0.0583` | **-8.23%** | **-8.59%** | +2.0% | -8.9% | `stop_loss` |
| 3 | Book 3 | `2025-08-14 21:00` | `2025-08-17 21:00` | 72.0h | `$0.0593` | `$0.0614` | **+3.48%** | **+3.42%** | +8.6% | -2.6% | `time_expiry` |
| 4 | Book 3 | `2025-09-30 02:00` | `2025-10-01 05:00` | 27.0h | `$0.0677` | `$0.0736` | **+8.70%** | **+8.34%** | +8.7% | -2.2% | `target_reclaim` |
| 5 | Book 3 | `2025-10-30 13:00` | `2025-10-31 04:00` | 15.0h | `$0.0627` | `$0.0681` | **+8.70%** | **+8.34%** | +10.6% | -6.1% | `target_reclaim` |
| 6 | Book 3 | `2026-08-25 19:00` | `2026-08-26 03:00` | 8.0h | `$0.0261` | `$0.0240` | **-8.23%** | **-8.59%** | +1.0% | -8.3% | `stop_loss` |
| 7 | Book 3 | `2026-08-28 00:00` | `2026-08-30 23:00` | 71.0h | `$0.0269` | `$0.0247` | **-8.23%** | **-8.59%** | +9.1% | -9.0% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `time_expiry` | `1` | `100.0%` | **`+3.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `KMNO`

* **Total Candidate Breakouts Filtered (Vetoed):** `83`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `51` (61.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `15`
* **Saved Capital Losses Avoided:** `+643.4%`
* **Missed Upside Forgone:** `-484.4%`
* **Net Veto Alpha:** `+159.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `33` | `39.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `27` | `32.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `18` | `21.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5` | `6.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*