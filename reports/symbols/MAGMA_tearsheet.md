# Kronos V12: Institutional Symbol Tear Sheet — `MAGMA`
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
| **Cumulative Net Log Return** | **`-20.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.82x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-10.08%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`11.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.3% / -16.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-21 20:00` | `2026-08-22 02:00` | 6.0h | `$0.3241` | `$0.2975` | **-10.82%** | **-11.45%** | +5.8% | -9.5% | `initial_stop` |
| 2 | Book 2 | `2026-10-02 14:00` | `2026-10-03 07:00` | 17.0h | `$0.3293` | `$0.3022` | **-8.34%** | **-8.71%** | +14.8% | -22.8% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-20.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `MAGMA`

* **Total Candidate Breakouts Filtered (Vetoed):** `51`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `33` (64.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+829.7%`
* **Missed Upside Forgone:** `-1,418.6%`
* **Net Veto Alpha:** `+-588.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `31` | `60.8%` |
| `Core 4: Whale Firewall` | `18` | `35.3%` |
| `Core 4: Defensible Whale Dump` | `2` | `3.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*