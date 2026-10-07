# Kronos V12: Institutional Symbol Tear Sheet — `LUNA2`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `15` (`15` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.506`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+22.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.25x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.50%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-42.7%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`23.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.0% / -6.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-07-17 13:00` | `2023-07-20 13:00` | 72.0h | `$0.6620` | `$0.6523` | **-1.48%** | **-1.49%** | +4.5% | -7.7% | `time_expiry` |
| 2 | Book 3 | `2023-11-09 16:00` | `2023-11-10 01:00` | 9.0h | `$0.4686` | `$0.5093` | **+8.70%** | **+8.34%** | +10.4% | -12.1% | `target_reclaim` |
| 3 | Book 3 | `2023-11-10 12:00` | `2023-11-10 13:00` | 1.0h | `$0.5449` | `$0.5923` | **+8.70%** | **+8.34%** | +9.2% | -0.9% | `target_reclaim` |
| 4 | Book 3 | `2023-12-04 11:00` | `2023-12-04 12:00` | 1.0h | `$0.9387` | `$1.0203` | **+8.70%** | **+8.34%** | +20.9% | -4.1% | `target_reclaim` |
| 5 | Book 3 | `2023-12-05 07:00` | `2023-12-05 10:00` | 3.0h | `$1.1211` | `$1.2186` | **+8.70%** | **+8.34%** | +10.5% | -4.9% | `target_reclaim` |
| 6 | Book 3 | `2024-02-29 21:00` | `2024-03-02 00:00` | 27.0h | `$0.7152` | `$0.7774` | **+8.70%** | **+8.34%** | +11.2% | -5.2% | `target_reclaim` |
| 7 | Book 3 | `2024-03-03 07:00` | `2024-03-03 08:00` | 1.0h | `$0.7395` | `$0.8038` | **+8.70%** | **+8.34%** | +14.0% | -4.2% | `target_reclaim` |
| 8 | Book 3 | `2024-03-05 19:00` | `2024-03-05 20:00` | 1.0h | `$0.8964` | `$0.9744` | **+8.70%** | **+8.34%** | +39.5% | -3.5% | `target_reclaim` |
| 9 | Book 3 | `2024-05-30 16:00` | `2024-05-31 01:00` | 9.0h | `$0.7176` | `$0.6585` | **-8.23%** | **-8.59%** | +10.2% | -8.5% | `stop_loss` |
| 10 | Book 3 | `2024-09-30 00:00` | `2024-09-30 23:00` | 23.0h | `$0.4433` | `$0.4068` | **-8.23%** | **-8.59%** | +3.4% | -9.6% | `stop_loss` |
| 11 | Book 3 | `2024-11-12 10:00` | `2024-11-13 04:00` | 18.0h | `$0.3890` | `$0.3570` | **-8.23%** | **-8.59%** | +4.5% | -10.2% | `stop_loss` |
| 12 | Book 3 | `2025-07-23 12:00` | `2025-07-23 21:00` | 9.0h | `$0.1786` | `$0.1639` | **-8.23%** | **-8.59%** | +3.0% | -8.6% | `stop_loss` |
| 13 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0490` | `$0.0491` | **+0.21%** | **+0.21%** | +9.7% | -7.0% | `time_expiry` |
| 14 | Book 3 | `2026-09-07 13:00` | `2026-09-09 22:00` | 57.0h | `$0.0507` | `$0.0465` | **-8.23%** | **-8.59%** | +4.6% | -12.1% | `stop_loss` |
| 15 | Book 3 | `2026-09-21 00:00` | `2026-09-22 21:00` | 45.0h | `$0.0527` | `$0.0573` | **+8.70%** | **+8.34%** | +9.4% | -3.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+66.7%`** |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `time_expiry` | `2` | `50.0%` | **`-1.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `LUNA2`

* **Total Candidate Breakouts Filtered (Vetoed):** `93`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `68` (73.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+1,033.8%`
* **Missed Upside Forgone:** `-879.7%`
* **Net Veto Alpha:** `+154.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `35` | `37.6%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `31` | `33.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `16` | `17.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `10` | `10.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `1.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*