# Kronos V12: Institutional Symbol Tear Sheet — `DOOD`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`20.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.119`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-30.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.74x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-6.05%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-34.4%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`12.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.6% / -11.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-12 19:00` | `2025-07-13 05:00` | 10.0h | `$0.0028` | `$0.0029` | **+4.17%** | **+4.08%** | +4.4% | -4.3% | `target_reclaim` |
| 2 | Book 3 | `2025-07-21 16:00` | `2025-07-21 17:00` | 1.0h | `$0.0043` | `$0.0040` | **-8.23%** | **-8.59%** | +5.8% | -8.4% | `stop_loss` |
| 3 | Book 3 | `2025-07-23 16:00` | `2025-07-24 19:00` | 27.0h | `$0.0045` | `$0.0041` | **-8.23%** | **-8.59%** | +35.4% | -8.4% | `stop_loss` |
| 4 | Book 3 | `2025-10-07 07:00` | `2025-10-07 08:00` | 1.0h | `$0.0129` | `$0.0118` | **-8.23%** | **-8.59%** | +19.5% | -16.2% | `stop_loss` |
| 5 | Book 3 | `2026-08-22 05:00` | `2026-08-23 03:00` | 22.0h | `$0.0014` | `$0.0013` | **-8.23%** | **-8.59%** | +8.1% | -19.8% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `4` | `0.0%` | **`-34.4%`** |
| `target_reclaim` | `1` | `100.0%` | **`+4.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `DOOD`

* **Total Candidate Breakouts Filtered (Vetoed):** `46`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (73.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `16`
* **Saved Capital Losses Avoided:** `+613.6%`
* **Missed Upside Forgone:** `-497.0%`
* **Net Veto Alpha:** `+116.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `21` | `45.7%` |
| `Core 1: Macro Bear Veto` | `17` | `37.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `8.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `4` | `8.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*