# Kronos V12: Institutional Symbol Tear Sheet — `IO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.537`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-11.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.90x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.75%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-23.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`41.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.2% / -7.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-11-26 10:00` | `2024-11-27 21:00` | 35.0h | `$2.5133` | `$2.8560` | **+13.64%** | **+12.78%** | +14.2% | -4.7% | `target_reclaim` |
| 2 | Book 3 | `2025-04-27 13:00` | `2025-04-30 13:00` | 72.0h | `$0.7982` | `$0.7471` | **-6.40%** | **-6.62%** | +7.7% | -6.5% | `time_expiry` |
| 3 | Book 3 | `2025-05-15 07:00` | `2025-05-17 01:00` | 42.0h | `$1.0079` | `$0.9249` | **-8.23%** | **-8.59%** | +6.3% | -8.6% | `stop_loss` |
| 4 | Book 3 | `2025-05-24 22:00` | `2025-05-25 15:00` | 17.0h | `$0.9729` | `$0.8929` | **-8.23%** | **-8.59%** | +0.7% | -8.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |
| `time_expiry` | `1` | `0.0%` | **`-6.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `IO`

* **Total Candidate Breakouts Filtered (Vetoed):** `69`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `49` (71.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `10`
* **Saved Capital Losses Avoided:** `+628.9%`
* **Missed Upside Forgone:** `-273.0%`
* **Net Veto Alpha:** `+356.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `44` | `63.8%` |
| `Core 1: Macro Bear Veto` | `25` | `36.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*