# Kronos V12: Institutional Symbol Tear Sheet — `LSK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-14.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.87x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-7.00%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-5.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`26.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.1% / -9.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-05 02:00` | `2025-05-06 21:00` | 43.0h | `$0.4924` | `$0.4519` | **-8.23%** | **-8.59%** | +2.9% | -8.5% | `stop_loss` |
| 2 | Book 2 | `2026-09-11 06:00` | `2026-09-11 15:00` | 9.0h | `$0.1324` | `$0.1215` | **-5.26%** | **-5.40%** | +7.3% | -10.0% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-5.4%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `LSK`

* **Total Candidate Breakouts Filtered (Vetoed):** `106`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `61` (57.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+655.9%`
* **Missed Upside Forgone:** `-947.2%`
* **Net Veto Alpha:** `+-291.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `75` | `70.8%` |
| `Core 1: Macro Bear Veto` | `31` | `29.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*