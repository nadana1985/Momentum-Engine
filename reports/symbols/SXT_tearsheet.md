# Kronos V12: Institutional Symbol Tear Sheet — `SXT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`77.8%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.201`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+20.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.23x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.29%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`31.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.3% / -8.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-12 04:00` | `2025-07-12 18:00` | 14.0h | `$0.0775` | `$0.0808` | **+4.17%** | **+4.08%** | +4.6% | -3.1% | `target_reclaim` |
| 2 | Book 3 | `2025-07-17 01:00` | `2025-07-18 05:00` | 28.0h | `$0.0912` | `$0.0950` | **+4.17%** | **+4.08%** | +4.6% | -3.7% | `target_reclaim` |
| 3 | Book 3 | `2025-07-23 18:00` | `2025-07-23 19:00` | 1.0h | `$0.1165` | `$0.1214` | **+4.17%** | **+4.08%** | +6.9% | -8.0% | `target_reclaim` |
| 4 | Book 3 | `2025-08-05 21:00` | `2025-08-07 22:00` | 49.0h | `$0.0800` | `$0.0884` | **+10.47%** | **+9.96%** | +10.9% | -1.2% | `target_reclaim` |
| 5 | Book 5 (Shelf Absorption Squeeze) | `2026-07-11 17:00` | `2026-07-15 17:00` | Live | `$0.0085` | `$0.0078` | **-8.20%** | **-8.56%** | +-0.5% | -29.9% | `shelf_stop_loss` |
| 6 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0071` | `$0.0079` | **+10.63%** | **+10.10%** | +19.9% | -11.2% | `time_expiry` |
| 7 | Book 3 | `2026-08-30 23:00` | `2026-08-31 06:00` | 7.0h | `$0.0085` | `$0.0089` | **+4.47%** | **+4.37%** | +5.3% | -4.4% | `target_reclaim` |
| 8 | Book 3 | `2026-09-23 14:00` | `2026-09-26 14:00` | 72.0h | `$0.0094` | `$0.0095` | **+1.06%** | **+1.05%** | +4.8% | -5.1% | `time_expiry` |
| 9 | Book 3 | `2026-10-12 13:00` | `2026-10-12 23:00` | 10.0h | `$0.0099` | `$0.0091` | **-8.23%** | **-8.59%** | +9.5% | -8.8% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `5` | `100.0%` | **`+26.6%`** |
| `time_expiry` | `2` | `100.0%` | **`+11.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `SXT`

* **Total Candidate Breakouts Filtered (Vetoed):** `30`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `27` (90.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+368.7%`
* **Missed Upside Forgone:** `-169.4%`
* **Net Veto Alpha:** `+199.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `17` | `56.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `7` | `23.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `6` | `20.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*