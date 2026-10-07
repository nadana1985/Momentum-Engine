# Kronos V12: Institutional Symbol Tear Sheet — `GOAT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+14.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.15x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+14.40%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+30.5% / -3.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-18 22:00` | `2026-09-25 22:00` | 168.0h | `$0.0169` | `$0.0195` | **+15.48%** | **+14.40%** | +30.5% | -3.5% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+14.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `GOAT`

* **Total Candidate Breakouts Filtered (Vetoed):** `58`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `44` (75.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+722.5%`
* **Missed Upside Forgone:** `-1,046.0%`
* **Net Veto Alpha:** `+-323.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `27` | `46.6%` |
| `Core 1: Macro Bear Veto` | `25` | `43.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `6` | `10.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*