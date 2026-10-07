# Kronos V12: Institutional Symbol Tear Sheet — `BICO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`28.6%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.595`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-17.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.84x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.48%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-42.9%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`27.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.2% / -7.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-03-03 07:00` | `2024-03-03 08:00` | 1.0h | `$0.4514` | `$0.5130` | **+13.64%** | **+12.78%** | +16.4% | -0.3% | `target_reclaim` |
| 2 | Book 3 | `2024-03-14 18:00` | `2024-03-15 09:00` | 15.0h | `$0.6467` | `$0.5935` | **-8.23%** | **-8.59%** | +10.5% | -8.9% | `stop_loss` |
| 3 | Book 3 | `2024-04-05 03:00` | `2024-04-05 16:00` | 13.0h | `$0.6843` | `$0.6280` | **-8.23%** | **-8.59%** | +2.6% | -8.8% | `stop_loss` |
| 4 | Book 3 | `2024-04-09 05:00` | `2024-04-11 16:00` | 59.0h | `$0.7795` | `$0.7154` | **-8.23%** | **-8.59%** | +5.9% | -10.6% | `stop_loss` |
| 5 | Book 3 | `2024-06-10 13:00` | `2024-06-12 01:00` | 36.0h | `$0.5658` | `$0.5193` | **-8.23%** | **-8.59%** | +4.2% | -9.8% | `stop_loss` |
| 6 | Book 3 | `2024-08-27 08:00` | `2024-08-27 22:00` | 14.0h | `$0.2464` | `$0.2261` | **-8.23%** | **-8.59%** | +1.8% | -9.3% | `stop_loss` |
| 7 | Book 3 | `2024-11-12 10:00` | `2024-11-14 18:00` | 56.0h | `$0.2451` | `$0.2785` | **+13.64%** | **+12.78%** | +16.0% | -3.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `5` | `0.0%` | **`-42.9%`** |
| `target_reclaim` | `2` | `100.0%` | **`+25.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `BICO`

* **Total Candidate Breakouts Filtered (Vetoed):** `138`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `102` (73.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `24`
* **Saved Capital Losses Avoided:** `+1,490.3%`
* **Missed Upside Forgone:** `-2,396.3%`
* **Net Veto Alpha:** `+-906.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `80` | `58.0%` |
| `Core 1: Macro Bear Veto` | `58` | `42.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*