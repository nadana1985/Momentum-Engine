# Kronos V12: Institutional Symbol Tear Sheet — `1000RATS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `14` (`14` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `14` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`35.7%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.504`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-41.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.66x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.93%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-49.3%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`12.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.3% / -11.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-02-28 04:00` | `2024-02-28 10:00` | 6.0h | `$0.2885` | `$0.3135` | **+8.70%** | **+8.34%** | +23.4% | -3.3% | `target_reclaim` |
| 2 | Book 3 | `2024-02-28 11:00` | `2024-02-28 17:00` | 6.0h | `$0.3205` | `$0.2941` | **-8.23%** | **-8.59%** | +11.1% | -21.9% | `stop_loss` |
| 3 | Book 3 | `2024-03-02 14:00` | `2024-03-03 07:00` | 17.0h | `$0.3397` | `$0.3117` | **-8.23%** | **-8.59%** | +6.1% | -14.1% | `stop_loss` |
| 4 | Book 3 | `2024-03-04 10:00` | `2024-03-04 12:00` | 2.0h | `$0.3849` | `$0.4184` | **+8.70%** | **+8.34%** | +14.1% | -2.0% | `target_reclaim` |
| 5 | Book 3 | `2024-03-05 14:00` | `2024-03-05 19:00` | 5.0h | `$0.4554` | `$0.4179` | **-8.23%** | **-8.59%** | +8.9% | -27.0% | `stop_loss` |
| 6 | Book 3 | `2024-05-28 03:00` | `2024-05-29 05:00` | 26.0h | `$0.1435` | `$0.1560` | **+8.70%** | **+8.34%** | +10.6% | -2.4% | `target_reclaim` |
| 7 | Book 3 | `2024-06-07 18:00` | `2024-06-07 19:00` | 1.0h | `$0.1660` | `$0.1497` | **-9.82%** | **-10.34%** | +2.4% | -14.8% | `stop_loss` |
| 8 | Book 3 | `2024-09-25 17:00` | `2024-09-26 16:00` | 23.0h | `$0.1425` | `$0.1549` | **+8.70%** | **+8.34%** | +12.6% | -7.5% | `target_reclaim` |
| 9 | Book 3 | `2024-09-28 08:00` | `2024-09-29 07:00` | 23.0h | `$0.1578` | `$0.1448` | **-8.23%** | **-8.59%** | +2.7% | -8.7% | `stop_loss` |
| 10 | Book 3 | `2024-11-11 05:00` | `2024-11-11 06:00` | 1.0h | `$0.1309` | `$0.1201` | **-8.23%** | **-8.59%** | +3.0% | -8.6% | `stop_loss` |
| 11 | Book 3 | `2024-12-09 03:00` | `2024-12-09 20:00` | 17.0h | `$0.1217` | `$0.1117` | **-8.23%** | **-8.59%** | +4.1% | -16.2% | `stop_loss` |
| 12 | Book 3 | `2025-05-14 03:00` | `2025-05-14 04:00` | 1.0h | `$0.0364` | `$0.0322` | **-11.49%** | **-12.20%** | +12.0% | -21.6% | `stop_loss` |
| 13 | Book 3 | `2025-09-17 19:00` | `2025-09-18 16:00` | 21.0h | `$0.0220` | `$0.0239` | **+8.70%** | **+8.34%** | +15.6% | -3.8% | `target_reclaim` |
| 14 | Book 3 | `2025-09-19 00:00` | `2025-09-20 01:00` | 25.0h | `$0.0226` | `$0.0207` | **-8.23%** | **-8.59%** | +3.2% | -8.2% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `9` | `0.0%` | **`-82.7%`** |
| `target_reclaim` | `5` | `100.0%` | **`+41.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000RATS`

* **Total Candidate Breakouts Filtered (Vetoed):** `87`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `74` (85.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+1,630.3%`
* **Missed Upside Forgone:** `-408.6%`
* **Net Veto Alpha:** `+1,221.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `46` | `52.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `37` | `42.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `3.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*