# Kronos V12: Institutional Symbol Tear Sheet — `WAXP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.545`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-16.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.85x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.81%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-27.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`46.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.9% / -8.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2023-12-11 02:00` | `2023-12-14 02:00` | 72.0h | `$0.0671` | `$0.0691` | **+2.93%** | **+2.88%** | +8.5% | -17.5% | `time_expiry` |
| 2 | Book 3 | `2023-12-26 17:00` | `2023-12-29 17:00` | 72.0h | `$0.0710` | `$0.0702` | **-1.25%** | **-1.26%** | +7.4% | -11.6% | `time_expiry` |
| 3 | Book 3 | `2024-03-01 07:00` | `2024-03-03 07:00` | 48.0h | `$0.0863` | `$0.0792` | **-8.23%** | **-8.59%** | +3.9% | -16.8% | `stop_loss` |
| 4 | Book 3 | `2024-03-28 01:00` | `2024-03-31 01:00` | 72.0h | `$0.0967` | `$0.0965` | **-0.25%** | **-0.25%** | +6.1% | -1.0% | `time_expiry` |
| 5 | Book 3 | `2024-08-26 17:00` | `2024-08-27 22:00` | 29.0h | `$0.0337` | `$0.0309` | **-8.23%** | **-8.59%** | +1.6% | -10.2% | `stop_loss` |
| 6 | Book 3 | `2024-09-30 09:00` | `2024-10-01 15:00` | 30.0h | `$0.0357` | `$0.0327` | **-8.23%** | **-8.59%** | +2.0% | -8.6% | `stop_loss` |
| 7 | Book 3 | `2024-11-26 14:00` | `2024-11-27 20:00` | 30.0h | `$0.0508` | `$0.0553` | **+8.70%** | **+8.34%** | +10.7% | -1.2% | `target_reclaim` |
| 8 | Book 3 | `2025-05-30 00:00` | `2025-05-30 23:00` | 23.0h | `$0.0227` | `$0.0208` | **-8.23%** | **-8.59%** | +4.0% | -8.1% | `stop_loss` |
| 9 | Book 3 | `2026-09-11 09:00` | `2026-09-12 23:00` | 38.0h | `$0.0044` | `$0.0048` | **+8.70%** | **+8.34%** | +8.9% | -1.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `time_expiry` | `3` | `33.3%` | **`+1.4%`** |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `WAXP`

* **Total Candidate Breakouts Filtered (Vetoed):** `144`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `78` (54.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `25`
* **Saved Capital Losses Avoided:** `+813.4%`
* **Missed Upside Forgone:** `-837.8%`
* **Net Veto Alpha:** `+-24.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `73` | `50.7%` |
| `Core 1: Macro Bear Veto` | `42` | `29.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `27` | `18.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `1.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*