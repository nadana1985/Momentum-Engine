# Kronos V12: Institutional Symbol Tear Sheet — `SAGA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.744`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.46%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`41.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.8% / -5.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-09-25 22:00` | `2024-09-28 21:00` | 71.0h | `$2.4625` | `$2.2598` | **-8.23%** | **-8.59%** | +3.7% | -8.9% | `stop_loss` |
| 2 | Book 3 | `2024-10-09 02:00` | `2024-10-10 10:00` | 32.0h | `$2.6052` | `$2.3907` | **-8.23%** | **-8.59%** | +13.0% | -8.4% | `stop_loss` |
| 3 | Book 3 | `2024-12-02 08:00` | `2024-12-03 05:00` | 21.0h | `$2.1952` | `$2.4945` | **+13.64%** | **+12.78%** | +15.6% | -0.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `SAGA`

* **Total Candidate Breakouts Filtered (Vetoed):** `74`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `47` (63.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `30`
* **Saved Capital Losses Avoided:** `+879.5%`
* **Missed Upside Forgone:** `-1,876.1%`
* **Net Veto Alpha:** `+-996.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `37` | `50.0%` |
| `Core 1: Macro Bear Veto` | `37` | `50.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*