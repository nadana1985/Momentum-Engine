# Kronos V12: Institutional Symbol Tear Sheet — `TNSR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `15` (`15` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `15` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.364`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-45.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.63x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.04%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-50.4%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`33.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.5% / -10.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-10-25 16:00` | `2024-10-25 23:00` | 7.0h | `$0.4209` | `$0.3863` | **-8.23%** | **-8.59%** | +2.9% | -8.6% | `stop_loss` |
| 2 | Book 3 | `2024-10-28 02:00` | `2024-10-29 18:00` | 40.0h | `$0.4291` | `$0.4838` | **+12.74%** | **+11.99%** | +24.3% | -6.7% | `target_reclaim` |
| 3 | Book 3 | `2024-11-01 03:00` | `2024-11-02 18:00` | 39.0h | `$0.4358` | `$0.4000` | **-8.23%** | **-8.59%** | +3.9% | -9.2% | `stop_loss` |
| 4 | Book 3 | `2024-11-12 03:00` | `2024-11-12 10:00` | 7.0h | `$0.5026` | `$0.4612` | **-8.23%** | **-8.59%** | +2.8% | -12.7% | `stop_loss` |
| 5 | Book 3 | `2024-11-14 22:00` | `2024-11-15 01:00` | 3.0h | `$0.5895` | `$0.5410` | **-8.23%** | **-8.59%** | +4.5% | -8.9% | `stop_loss` |
| 6 | Book 3 | `2024-11-16 15:00` | `2024-11-18 19:00` | 52.0h | `$0.6116` | `$0.5613` | **-8.23%** | **-8.59%** | +5.1% | -9.9% | `stop_loss` |
| 7 | Book 3 | `2025-02-01 14:00` | `2025-02-02 16:00` | 26.0h | `$0.3988` | `$0.3660` | **-8.23%** | **-8.59%** | +3.6% | -11.7% | `stop_loss` |
| 8 | Book 3 | `2025-07-04 18:00` | `2025-07-07 18:00` | 72.0h | `$0.1138` | `$0.1134` | **-0.30%** | **-0.30%** | +3.8% | -6.8% | `time_expiry` |
| 9 | Book 3 | `2025-07-14 14:00` | `2025-07-15 18:00` | 28.0h | `$0.1400` | `$0.1458` | **+4.17%** | **+4.08%** | +4.5% | -5.5% | `target_reclaim` |
| 10 | Book 3 | `2025-07-18 20:00` | `2025-07-20 03:00` | 31.0h | `$0.1420` | `$0.1488` | **+4.82%** | **+4.71%** | +4.8% | -1.4% | `target_reclaim` |
| 11 | Book 3 | `2025-07-23 20:00` | `2025-07-26 20:00` | 72.0h | `$0.1420` | `$0.1436` | **+1.18%** | **+1.18%** | +3.1% | -7.8% | `time_expiry` |
| 12 | Book 3 | `2025-10-27 20:00` | `2025-10-28 20:00` | 24.0h | `$0.0647` | `$0.0594` | **-8.23%** | **-8.59%** | +0.5% | -9.1% | `stop_loss` |
| 13 | Book 5 (Shelf Absorption Squeeze) | `2026-06-21 06:00` | `2026-06-25 06:00` | Live | `$0.0425` | `$0.0390` | **-8.20%** | **-8.56%** | +-3.6% | -30.5% | `shelf_stop_loss` |
| 14 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0326` | `$0.0339` | **+4.17%** | **+4.08%** | +18.4% | -14.5% | `target_reclaim` |
| 15 | Book 3 | `2026-08-31 13:00` | `2026-09-03 13:00` | 72.0h | `$0.0356` | `$0.0346` | **-2.59%** | **-2.62%** | +4.8% | -6.5% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `7` | `0.0%` | **`-60.1%`** |
| `target_reclaim` | `4` | `100.0%` | **`+24.9%`** |
| `time_expiry` | `3` | `33.3%` | **`-1.7%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `TNSR`

* **Total Candidate Breakouts Filtered (Vetoed):** `112`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `92` (82.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+1,710.8%`
* **Missed Upside Forgone:** `-1,419.6%`
* **Net Veto Alpha:** `+291.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `69` | `61.6%` |
| `Core 1: Macro Bear Veto` | `30` | `26.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `13` | `11.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*