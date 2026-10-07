# Kronos V12: Institutional Symbol Tear Sheet — `C`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.260`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-12.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.88x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.24%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+14.0% / -9.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0642` | `$0.0672` | **+4.57%** | **+4.47%** | +16.8% | -4.1% | `time_expiry` |
| 2 | Book 3 | `2026-09-18 17:00` | `2026-09-18 22:00` | 5.0h | `$0.0715` | `$0.0657` | **-8.23%** | **-8.59%** | +13.1% | -8.1% | `stop_loss` |
| 3 | Book 3 | `2026-09-20 07:00` | `2026-09-20 08:00` | 1.0h | `$0.0844` | `$0.0775` | **-8.23%** | **-8.59%** | +12.2% | -14.8% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+4.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `C`

* **Total Candidate Breakouts Filtered (Vetoed):** `29`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (82.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+409.1%`
* **Missed Upside Forgone:** `-153.0%`
* **Net Veto Alpha:** `+256.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `14` | `48.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `11` | `37.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `13.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*