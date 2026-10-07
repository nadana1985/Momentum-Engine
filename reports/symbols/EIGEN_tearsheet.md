# Kronos V12: Institutional Symbol Tear Sheet — `EIGEN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`22.2%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.299`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-38.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.68x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.29%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-51.4%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`34.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.5% / -8.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-12-05 22:00` | `2024-12-06 02:00` | 4.0h | `$3.6522` | `$4.1502` | **+13.64%** | **+12.78%** | +15.0% | -2.8% | `target_reclaim` |
| 2 | Book 3 | `2024-12-18 20:00` | `2024-12-19 17:00` | 21.0h | `$4.7459` | `$4.3553` | **-8.23%** | **-8.59%** | +10.6% | -10.4% | `stop_loss` |
| 3 | Book 3 | `2025-04-28 00:00` | `2025-05-01 00:00` | 72.0h | `$0.9035` | `$0.9372` | **+3.73%** | **+3.66%** | +9.2% | -2.1% | `time_expiry` |
| 4 | Book 3 | `2025-05-15 05:00` | `2025-05-16 22:00` | 41.0h | `$1.3738` | `$1.2607` | **-8.23%** | **-8.59%** | +12.7% | -8.3% | `stop_loss` |
| 5 | Book 3 | `2025-05-23 12:00` | `2025-05-25 08:00` | 44.0h | `$1.4514` | `$1.3319` | **-8.23%** | **-8.59%** | +4.8% | -8.4% | `stop_loss` |
| 6 | Book 3 | `2025-05-29 23:00` | `2025-05-30 16:00` | 17.0h | `$1.5782` | `$1.4483` | **-8.23%** | **-8.59%** | +2.6% | -11.9% | `stop_loss` |
| 7 | Book 3 | `2025-08-15 15:00` | `2025-08-18 15:00` | 72.0h | `$1.3650` | `$1.3367` | **-2.07%** | **-2.10%** | +6.7% | -5.0% | `time_expiry` |
| 8 | Book 1 | `2026-08-22 02:00` | `2026-08-22 05:00` | 3.0h | `$0.2305` | `$0.2023` | **-16.03%** | **-17.47%** | +2.7% | -19.4% | `initial_stop` |
| 9 | Book 1 | `2026-09-18 17:00` | `2026-09-20 05:00` | 36.0h | `$0.2337` | `$0.2313` | **-1.12%** | **-1.12%** | +3.7% | -4.1% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `time_expiry` | `2` | `50.0%` | **`+1.6%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.1%`** |
| `initial_stop` | `1` | `0.0%` | **`-17.5%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `EIGEN`

* **Total Candidate Breakouts Filtered (Vetoed):** `80`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `58` (72.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `6`
* **Saved Capital Losses Avoided:** `+835.3%`
* **Missed Upside Forgone:** `-202.3%`
* **Net Veto Alpha:** `+633.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `47` | `58.8%` |
| `Core 1: Macro Bear Veto` | `33` | `41.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*