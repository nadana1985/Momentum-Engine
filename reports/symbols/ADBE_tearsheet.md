# Kronos V12: Institutional Symbol Tear Sheet — `ADBE`
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
| **Cumulative Net Log Return** | **`-5.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.97%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-5.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`57.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+1.9% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-27 13:00` | `2026-09-01 12:00` | 119.0h | `$287.9982` | `$286.1329` | **-0.65%** | **-0.65%** | +2.2% | -3.7% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-14 07:00` | `2026-09-16 07:00` | 48.0h | `$258.7853` | `$255.8887` | **-1.12%** | **-1.13%** | +2.9% | -0.9% | `fast_decay_cut` |
| 3 | Book 2 | `2026-09-22 08:00` | `2026-09-22 14:00` | 6.0h | `$253.3919` | `$243.1397` | **-4.05%** | **-4.13%** | +0.6% | -4.1% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-1.8%`** |
| `initial_stop` | `1` | `0.0%` | **`-4.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `ADBE`

* **Total Candidate Breakouts Filtered (Vetoed):** `32`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `18` (56.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+97.0%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+97.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `29` | `90.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `9.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*