# Kronos V12: Institutional Symbol Tear Sheet — `MOCA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.549`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+26.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.30x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+5.32%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-13.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`55.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.4% / -11.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-01-25 22:00` | `2025-01-29 22:00` | Live | `$0.1703` | `$0.1848` | **+8.50%** | **+8.16%** | +14.5% | -33.3% | `shelf_target_reclaim` |
| 2 | Book 2 | `2025-04-22 14:00` | `2025-04-28 23:00` | 153.0h | `$0.0806` | `$0.1041` | **+35.95%** | **+31.54%** | +38.3% | -2.5% | `climax_top_harvest` |
| 3 | Book 3 | `2025-07-13 01:00` | `2025-07-13 03:00` | 2.0h | `$0.1039` | `$0.0953` | **-8.23%** | **-8.59%** | +8.1% | -10.0% | `stop_loss` |
| 4 | Book 3 | `2025-09-30 07:00` | `2025-09-30 19:00` | 12.0h | `$0.0721` | `$0.0751` | **+4.17%** | **+4.08%** | +8.2% | -2.1% | `target_reclaim` |
| 5 | Book 3 | `2025-10-28 05:00` | `2025-10-30 12:00` | 55.0h | `$0.0547` | `$0.0502` | **-8.23%** | **-8.59%** | +2.9% | -8.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+31.5%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+4.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `MOCA`

* **Total Candidate Breakouts Filtered (Vetoed):** `43`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (79.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+383.7%`
* **Missed Upside Forgone:** `-67.6%`
* **Net Veto Alpha:** `+316.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `22` | `51.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `16` | `37.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `5` | `11.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*