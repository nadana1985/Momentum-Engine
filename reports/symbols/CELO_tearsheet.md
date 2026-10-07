# Kronos V12: Institutional Symbol Tear Sheet — `CELO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-20.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.82x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-6.66%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-14.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`40.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.3% / -7.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-31 11:00` | `2022-11-02 11:00` | 48.0h | `$0.7429` | `$0.7022` | **-5.47%** | **-5.62%** | +3.0% | -6.6% | `fast_decay_cut` |
| 2 | Book 2 | `2022-12-15 05:00` | `2022-12-16 23:00` | 42.0h | `$0.5764` | `$0.5290` | **-8.23%** | **-8.59%** | +5.0% | -8.6% | `initial_stop` |
| 3 | Book 2 | `2023-10-16 05:00` | `2023-10-17 13:00` | 32.0h | `$0.4311` | `$0.4070` | **-5.59%** | **-5.76%** | +1.8% | -6.3% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-14.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-5.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CELO`

* **Total Candidate Breakouts Filtered (Vetoed):** `238`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `129` (54.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `16`
* **Saved Capital Losses Avoided:** `+1,603.7%`
* **Missed Upside Forgone:** `-445.2%`
* **Net Veto Alpha:** `+1,158.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `97` | `40.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `69` | `29.0%` |
| `Core 1: Macro Bear Veto` | `43` | `18.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `20` | `8.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `9` | `3.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*