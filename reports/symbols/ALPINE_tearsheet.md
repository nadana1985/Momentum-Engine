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
| **Cumulative Net Log Return** | **`-32.5%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.72x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-8.13%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-23.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`19.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.4% / -10.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-07 10:00` | `2025-07-07 12:00` | 2.0h | `$0.9065` | `$0.8319` | **-8.23%** | **-8.59%** | +9.5% | -9.0% | `stop_loss` |
| 2 | Book 3 | `2025-07-28 20:00` | `2025-07-31 20:00` | 72.0h | `$0.9579` | `$0.8955` | **-6.52%** | **-6.74%** | +2.0% | -7.8% | `time_expiry` |
| 3 | Book 3 | `2025-09-29 04:00` | `2025-09-29 05:00` | 1.0h | `$6.4017` | `$5.8749` | **-8.23%** | **-8.59%** | +12.5% | -15.9% | `stop_loss` |
| 4 | Book 3 | `2025-09-30 18:00` | `2025-09-30 22:00` | 4.0h | `$7.3613` | `$6.7555` | **-8.23%** | **-8.59%** | +21.7% | -9.9% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_expiry` | `1` | `0.0%` | **`-6.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALPINE`

* **Total Candidate Breakouts Filtered (Vetoed):** `38`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `24` (63.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `14`
* **Saved Capital Losses Avoided:** `+460.1%`
* **Missed Upside Forgone:** `-1,155.9%`
* **Net Veto Alpha:** `+-695.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `28` | `73.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `9` | `23.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `2.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*