# Kronos V12: Institutional Symbol Tear Sheet — `HIMS`
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
| **Cumulative Net Log Return** | **`-7.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.93x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.68%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-6.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`70.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.3% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-20 13:00` | `2026-08-24 10:00` | 93.0h | `$33.0825` | `$32.6881` | **-1.19%** | **-1.20%** | +4.3% | -8.5% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-22 13:00` | `2026-09-24 13:00` | 48.0h | `$29.8945` | `$28.1096` | **-5.97%** | **-6.16%** | +6.3% | -6.0% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-7.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `HIMS`

* **Total Candidate Breakouts Filtered (Vetoed):** `21`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `8` (38.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+95.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+95.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `21` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*