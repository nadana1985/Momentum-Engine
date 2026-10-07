# Kronos V12: Institutional Symbol Tear Sheet — `DEXE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.488`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+4.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.10%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`6.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.0% / -6.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-01-29 04:00` | `2025-01-29 08:00` | 4.0h | `$18.8426` | `$17.2918` | **-8.23%** | **-8.59%** | +3.3% | -12.3% | `stop_loss` |
| 2 | Book 3 | `2025-02-02 23:00` | `2025-02-03 07:00` | 8.0h | `$19.4867` | `$22.1440` | **+13.64%** | **+12.78%** | +22.7% | -0.5% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `DEXE`

* **Total Candidate Breakouts Filtered (Vetoed):** `102`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `58` (56.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+810.6%`
* **Missed Upside Forgone:** `-996.3%`
* **Net Veto Alpha:** `+-185.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `89` | `87.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `13` | `12.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*