# Kronos V12: Institutional Symbol Tear Sheet — `HEI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.269`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+2.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.90%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`49.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.3% / -4.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-02 05:00` | `2025-05-05 05:00` | 72.0h | `$0.3525` | `$0.3473` | **-1.47%** | **-1.49%** | +9.2% | -5.8% | `time_expiry` |
| 2 | Book 3 | `2025-07-20 22:00` | `2025-07-22 09:00` | 35.0h | `$0.3401` | `$0.3865` | **+13.64%** | **+12.78%** | +20.3% | -0.2% | `target_reclaim` |
| 3 | Book 3 | `2025-08-04 02:00` | `2025-08-05 19:00` | 41.0h | `$0.4185` | `$0.3841` | **-8.23%** | **-8.59%** | +13.5% | -8.8% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |
| `time_expiry` | `1` | `0.0%` | **`-1.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `HEI`

* **Total Candidate Breakouts Filtered (Vetoed):** `38`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `35` (92.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+861.7%`
* **Missed Upside Forgone:** `-1,746.8%`
* **Net Veto Alpha:** `+-885.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `28` | `73.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `10` | `26.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*