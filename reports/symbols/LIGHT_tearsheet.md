# Kronos V12: Institutional Symbol Tear Sheet — `LIGHT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-17.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.84x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-8.59%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`49.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.1% / -9.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-30 14:00` | `2026-08-31 16:00` | 26.0h | `$0.1861` | `$0.1708` | **-8.23%** | **-8.59%** | +6.0% | -11.1% | `stop_loss` |
| 2 | Book 3 | `2026-09-23 14:00` | `2026-09-26 14:00` | 72.0h | `$0.1860` | `$0.1707` | **-8.23%** | **-8.59%** | +4.3% | -8.1% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `LIGHT`

* **Total Candidate Breakouts Filtered (Vetoed):** `56`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `49` (87.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `31`
* **Saved Capital Losses Avoided:** `+2,035.8%`
* **Missed Upside Forgone:** `-1,874.9%`
* **Net Veto Alpha:** `+160.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `52` | `92.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `7.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*