# Kronos V12: Institutional Symbol Tear Sheet — `SOMI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.265`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-12.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.88x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.21%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`37.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.8% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-01 10:00` | `2026-09-02 00:00` | 14.0h | `$0.1148` | `$0.1054` | **-8.23%** | **-8.59%** | +1.8% | -8.7% | `stop_loss` |
| 2 | Book 3 | `2026-09-21 17:00` | `2026-09-24 17:00` | 72.0h | `$0.1854` | `$0.1940` | **+4.66%** | **+4.55%** | +6.8% | -1.3% | `time_expiry` |
| 3 | Book 3 | `2026-09-30 14:00` | `2026-10-01 15:00` | 25.0h | `$0.2264` | `$0.2078` | **-8.23%** | **-8.59%** | +2.9% | -8.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+4.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `SOMI`

* **Total Candidate Breakouts Filtered (Vetoed):** `57`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `30` (52.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+447.1%`
* **Missed Upside Forgone:** `-332.8%`
* **Net Veto Alpha:** `+114.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `25` | `43.9%` |
| `Core 1: Macro Bear Veto` | `18` | `31.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `14` | `24.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*