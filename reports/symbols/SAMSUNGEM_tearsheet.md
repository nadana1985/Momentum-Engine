# Kronos V12: Institutional Symbol Tear Sheet — `SAMSUNGEM`
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
| **Cumulative Net Log Return** | **`-10.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.90x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-5.42%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-6.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`44.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.3% / -5.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-22 00:00` | `2026-09-24 00:00` | 48.0h | `$1113.9980` | `$1066.1280` | **-4.30%** | **-4.39%** | +1.9% | -4.8% | `fast_decay_cut` |
| 2 | Book 2 | `2026-10-06 00:00` | `2026-10-07 17:00` | 41.0h | `$1230.3682` | `$1153.5008` | **-6.25%** | **-6.45%** | +2.7% | -6.8% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-4.4%`** |
| `initial_stop` | `1` | `0.0%` | **`-6.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `SAMSUNGEM`

* **Total Candidate Breakouts Filtered (Vetoed):** `2`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `2` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+14.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+14.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `1` | `50.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `50.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*