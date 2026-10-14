# Kronos V12: Institutional Symbol Tear Sheet — `SANTOS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `8` (`8` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `8` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.358`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-25.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.77x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.24%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-31.8%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`53.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.4% / -7.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-12-08 10:00` | `2024-12-09 03:00` | 17.0h | `$5.1394` | `$4.7164` | **-8.23%** | **-8.59%** | +6.9% | -9.1% | `stop_loss` |
| 2 | Book 3 | `2025-01-31 14:00` | `2025-02-01 10:00` | 20.0h | `$3.3004` | `$3.0288` | **-8.23%** | **-8.59%** | +5.7% | -8.3% | `stop_loss` |
| 3 | Book 3 | `2025-05-04 17:00` | `2025-05-07 17:00` | 72.0h | `$2.4912` | `$2.3152` | **-7.06%** | **-7.33%** | +1.6% | -7.9% | `time_expiry` |
| 4 | Book 3 | `2025-07-22 01:00` | `2025-07-24 05:00` | 52.0h | `$2.3395` | `$2.1470` | **-8.23%** | **-8.59%** | +2.5% | -8.4% | `stop_loss` |
| 5 | Book 3 | `2025-07-28 20:00` | `2025-07-31 20:00` | 72.0h | `$2.3713` | `$2.2484` | **-5.19%** | **-5.33%** | +3.4% | -6.3% | `time_expiry` |
| 6 | Book 3 | `2025-10-01 04:00` | `2025-10-04 04:00` | 72.0h | `$1.9899` | `$1.9511` | **-1.95%** | **-1.97%** | +3.2% | -4.3% | `time_expiry` |
| 7 | Book 4 | `2026-01-11 10:00` | `2026-01-16 14:00` | 124.0h | `$1.9669` | `$2.3603` | **+10.83%** | **+10.37%** | +22.5% | -3.4% | `target_reclaim` |
| 8 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.4849` | `$0.5051` | **+4.17%** | **+4.08%** | +13.1% | -15.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_expiry` | `3` | `0.0%` | **`-14.6%`** |
| `target_reclaim` | `2` | `100.0%` | **`+14.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `SANTOS`

* **Total Candidate Breakouts Filtered (Vetoed):** `487`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `282` (57.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+3,700.5%`
* **Missed Upside Forgone:** `-293.1%`
* **Net Veto Alpha:** `+3,407.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `469` | `96.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `15` | `3.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `2` | `0.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*