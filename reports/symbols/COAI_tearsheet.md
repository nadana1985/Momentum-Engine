# Kronos V12: Institutional Symbol Tear Sheet — `COAI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-3.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.76%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.7% / -5.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-18 20:00` | `2026-09-20 20:00` | 48.0h | `$0.3286` | `$0.3165` | **-3.69%** | **-3.76%** | +5.7% | -5.9% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-3.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `COAI`

* **Total Candidate Breakouts Filtered (Vetoed):** `35`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `29` (82.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+838.4%`
* **Missed Upside Forgone:** `-4,197.0%`
* **Net Veto Alpha:** `+-3,358.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `34` | `97.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `2.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*