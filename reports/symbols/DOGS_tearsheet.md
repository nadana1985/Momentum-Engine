# Kronos V12: Institutional Symbol Tear Sheet — `DOGS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.294`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+7.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.08%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`12.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.9% / -5.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-11-10 06:00` | `2024-11-10 21:00` | 15.0h | `$0.0007` | `$0.0007` | **-8.23%** | **-8.59%** | +4.0% | -9.1% | `stop_loss` |
| 2 | Book 3 | `2024-12-02 03:00` | `2024-12-02 04:00` | 1.0h | `$0.0007` | `$0.0007` | **-8.23%** | **-8.59%** | +4.2% | -8.8% | `stop_loss` |
| 3 | Book 3 | `2024-12-09 03:00` | `2024-12-09 12:00` | 9.0h | `$0.0008` | `$0.0009` | **+8.70%** | **+8.34%** | +9.3% | -0.2% | `target_reclaim` |
| 4 | Book 3 | `2025-05-02 11:00` | `2025-05-03 14:00` | 27.0h | `$0.0002` | `$0.0002` | **-8.23%** | **-8.59%** | +1.3% | -8.5% | `stop_loss` |
| 5 | Book 3 | `2025-07-17 03:00` | `2025-07-17 10:00` | 7.0h | `$0.0002` | `$0.0002` | **+8.70%** | **+8.34%** | +8.8% | -0.8% | `target_reclaim` |
| 6 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0000` | `$0.0000` | **+8.70%** | **+8.34%** | +23.4% | -6.0% | `target_reclaim` |
| 7 | Book 3 | `2026-09-09 22:00` | `2026-09-11 03:00` | 29.0h | `$0.0000` | `$0.0000` | **+8.70%** | **+8.34%** | +11.5% | -4.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `DOGS`

* **Total Candidate Breakouts Filtered (Vetoed):** `51`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `42` (82.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+713.3%`
* **Missed Upside Forgone:** `-595.5%`
* **Net Veto Alpha:** `+117.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `23` | `45.1%` |
| `Core 1: Macro Bear Veto` | `12` | `23.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `9` | `17.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `13.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*