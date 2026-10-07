# Kronos V12: Institutional Symbol Tear Sheet — `GAS`
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
| **Cumulative Net Log Return** | **`-0.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.32%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`50.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.0% / -1.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-05 01:00` | `2026-05-07 03:00` | 50.0h | `$1.6401` | `$1.6349` | **-0.32%** | **-0.32%** | +3.0% | -1.0% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `GAS`

* **Total Candidate Breakouts Filtered (Vetoed):** `82`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `59` (72.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `27`
* **Saved Capital Losses Avoided:** `+1,258.5%`
* **Missed Upside Forgone:** `-1,080.9%`
* **Net Veto Alpha:** `+177.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `36` | `43.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `31` | `37.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `14` | `17.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*