# Kronos V12: Institutional Symbol Tear Sheet — `CATI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.150`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-23.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.79x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-7.71%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-18.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`2.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.2% / -9.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-11-15 12:00` | `2024-11-15 13:00` | 1.0h | `$0.4593` | `$0.4215` | **-8.23%** | **-8.59%** | +7.5% | -10.2% | `stop_loss` |
| 2 | Book 3 | `2025-07-17 04:00` | `2025-07-17 09:00` | 5.0h | `$0.0968` | `$0.1008` | **+4.17%** | **+4.08%** | +4.2% | -0.3% | `target_reclaim` |
| 3 | Book 4 | `2026-08-22 03:00` | `2026-08-22 05:00` | 2.0h | `$0.0540` | `$0.0459` | **-17.19%** | **-18.64%** | +0.9% | -18.5% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `structural_stop` | `1` | `0.0%` | **`-18.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+4.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `CATI`

* **Total Candidate Breakouts Filtered (Vetoed):** `253`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `148` (58.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+1,926.9%`
* **Missed Upside Forgone:** `-755.8%`
* **Net Veto Alpha:** `+1,171.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `191` | `75.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `35` | `13.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `20` | `7.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `2.4%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*