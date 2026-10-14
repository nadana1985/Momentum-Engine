# Kronos V12: Institutional Symbol Tear Sheet — `DYM`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`55.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.858`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.95x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.54%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-13.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`58.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.3% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-03-12 08:00` | `2024-03-14 05:00` | 45.0h | `$7.2032` | `$6.6104` | **-8.23%** | **-8.59%** | +4.9% | -8.2% | `stop_loss` |
| 2 | Book 3 | `2024-05-30 06:00` | `2024-06-02 06:00` | 72.0h | `$2.9562` | `$3.1451` | **+6.39%** | **+6.19%** | +8.2% | -3.3% | `time_expiry` |
| 3 | Book 3 | `2024-06-03 13:00` | `2024-06-06 13:00` | 72.0h | `$3.2275` | `$3.2548` | **+0.85%** | **+0.84%** | +2.8% | -3.4% | `time_expiry` |
| 4 | Book 3 | `2024-11-12 09:00` | `2024-11-12 10:00` | 1.0h | `$1.7700` | `$1.6244` | **-8.23%** | **-8.59%** | +6.6% | -8.5% | `stop_loss` |
| 5 | Book 4 | `2024-11-24 13:00` | `2024-12-06 08:00` | 283.0h | `$2.2468` | `$2.6512` | **+9.90%** | **+9.11%** | +20.1% | -7.3% | `climax_whale_euphoria_harvest` |
| 6 | Book 3 | `2024-12-09 08:00` | `2024-12-09 20:00` | 12.0h | `$2.4084` | `$2.2102` | **-8.23%** | **-8.59%** | +2.1% | -12.8% | `stop_loss` |
| 7 | Book 3 | `2025-04-29 13:00` | `2025-04-29 18:00` | 5.0h | `$0.3374` | `$0.3515` | **+4.17%** | **+4.08%** | +5.3% | -0.8% | `target_reclaim` |
| 8 | Book 3 | `2025-05-15 01:00` | `2025-05-15 14:00` | 13.0h | `$0.4210` | `$0.3863` | **-8.23%** | **-8.59%** | +3.8% | -8.0% | `stop_loss` |
| 9 | Book 3 | `2025-09-17 10:00` | `2025-09-18 07:00` | 21.0h | `$0.2252` | `$0.2471` | **+9.71%** | **+9.26%** | +12.3% | -1.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `target_reclaim` | `2` | `100.0%` | **`+13.3%`** |
| `time_expiry` | `2` | `100.0%` | **`+7.0%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+9.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `DYM`

* **Total Candidate Breakouts Filtered (Vetoed):** `448`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `253` (56.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `36`
* **Saved Capital Losses Avoided:** `+4,606.8%`
* **Missed Upside Forgone:** `-940.4%`
* **Net Veto Alpha:** `+3,666.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `414` | `92.4%` |
| `Core 1: Macro Bear Veto` | `26` | `5.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `4` | `0.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `0.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*