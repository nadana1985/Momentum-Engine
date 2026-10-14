# Kronos V12: Institutional Symbol Tear Sheet — `ALPINE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-31.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.73x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-7.86%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-22.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`19.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.8% / -10.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-07 10:00` | `2025-07-07 12:00` | 2.0h | `$0.9459` | `$0.8680` | **-8.23%** | **-8.59%** | +5.0% | -12.8% | `stop_loss` |
| 2 | Book 3 | `2025-07-29 14:00` | `2025-08-01 14:00` | 72.0h | `$0.9122` | `$0.8780` | **-3.74%** | **-3.82%** | +3.0% | -6.2% | `time_expiry` |
| 3 | Book 3 | `2025-09-29 05:00` | `2025-09-29 06:00` | 1.0h | `$6.0552` | `$5.4549` | **-9.91%** | **-10.44%** | +1.4% | -11.9% | `stop_loss` |
| 4 | Book 3 | `2025-09-30 18:00` | `2025-09-30 22:00` | 4.0h | `$7.3613` | `$6.7555` | **-8.23%** | **-8.59%** | +21.7% | -9.9% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-27.6%`** |
| `time_expiry` | `1` | `0.0%` | **`-3.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALPINE`

* **Total Candidate Breakouts Filtered (Vetoed):** `64`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `50` (78.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `14`
* **Saved Capital Losses Avoided:** `+768.1%`
* **Missed Upside Forgone:** `-1,155.9%`
* **Net Veto Alpha:** `+-387.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `35` | `54.7%` |
| `Core 1: Macro Bear Veto` | `28` | `43.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*