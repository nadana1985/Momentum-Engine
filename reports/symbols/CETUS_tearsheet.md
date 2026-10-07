# Kronos V12: Institutional Symbol Tear Sheet — `CETUS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.353`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-26.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.77x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-5.23%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-34.5%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`34.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.4% / -11.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-12-15 22:00` | `2024-12-16 00:00` | 2.0h | `$0.4364` | `$0.4743` | **+8.70%** | **+8.34%** | +10.8% | -0.7% | `target_reclaim` |
| 2 | Book 3 | `2025-05-22 10:00` | `2025-05-22 11:00` | 1.0h | `$0.2267` | `$0.1798` | **-20.70%** | **-23.19%** | +13.4% | -36.0% | `stop_loss` |
| 3 | Book 3 | `2025-07-18 14:00` | `2025-07-21 14:00` | 72.0h | `$0.1189` | `$0.1261` | **+6.07%** | **+5.90%** | +7.1% | -5.6% | `time_expiry` |
| 4 | Book 3 | `2025-07-28 23:00` | `2025-07-30 12:00` | 37.0h | `$0.1247` | `$0.1145` | **-8.23%** | **-8.59%** | +7.7% | -8.5% | `stop_loss` |
| 5 | Book 3 | `2025-10-28 02:00` | `2025-10-30 12:00` | 58.0h | `$0.0505` | `$0.0463` | **-8.23%** | **-8.59%** | +3.1% | -8.2% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-40.4%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+5.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `CETUS`

* **Total Candidate Breakouts Filtered (Vetoed):** `91`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `57` (62.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+811.5%`
* **Missed Upside Forgone:** `-910.2%`
* **Net Veto Alpha:** `+-98.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `42` | `46.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `30` | `33.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `10` | `11.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `9` | `9.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*