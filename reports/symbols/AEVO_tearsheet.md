# Kronos V12: Institutional Symbol Tear Sheet — `AEVO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`62.5%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.863`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+15.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.17x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.96%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-13.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`30.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.1% / -5.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-09-18 09:00` | `2024-09-18 23:00` | 14.0h | `$0.3556` | `$0.3749` | **+5.43%** | **+5.29%** | +5.9% | -1.1% | `target_reclaim` |
| 2 | Book 3 | `2024-11-13 04:00` | `2024-11-16 04:00` | 72.0h | `$0.3434` | `$0.3462` | **+0.84%** | **+0.83%** | +8.1% | -7.0% | `time_expiry` |
| 3 | Book 3 | `2024-12-02 08:00` | `2024-12-02 12:00` | 4.0h | `$0.4741` | `$0.5056` | **+6.64%** | **+6.43%** | +7.8% | -0.8% | `target_reclaim` |
| 4 | Book 3 | `2025-05-13 03:00` | `2025-05-13 18:00` | 15.0h | `$0.1326` | `$0.1557` | **+17.42%** | **+16.06%** | +18.4% | -0.5% | `target_reclaim` |
| 5 | Book 3 | `2025-05-14 02:00` | `2025-05-15 01:00` | 23.0h | `$0.1531` | `$0.1405` | **-8.23%** | **-8.59%** | +2.7% | -8.4% | `stop_loss` |
| 6 | Book 3 | `2025-07-16 08:00` | `2025-07-18 05:00` | 45.0h | `$0.1177` | `$0.1239` | **+5.29%** | **+5.16%** | +6.5% | -4.2% | `target_reclaim` |
| 7 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0237` | `$0.0235` | **-0.94%** | **-0.94%** | +10.8% | -14.1% | `time_expiry` |
| 8 | Book 3 | `2026-10-08 13:00` | `2026-10-08 14:00` | 1.0h | `$0.0280` | `$0.0257` | **-8.23%** | **-8.59%** | +12.9% | -9.0% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+32.9%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `2` | `50.0%` | **`-0.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `AEVO`

* **Total Candidate Breakouts Filtered (Vetoed):** `103`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `61` (59.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+787.9%`
* **Missed Upside Forgone:** `-537.4%`
* **Net Veto Alpha:** `+250.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `67` | `65.0%` |
| `Core 1: Macro Bear Veto` | `24` | `23.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `11` | `10.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*