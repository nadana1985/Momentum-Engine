# Kronos V12: Institutional Symbol Tear Sheet — `IO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.367`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+7.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.07x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.60%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-19.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`269.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.5% / -12.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2024-11-15 22:00` | `2024-11-25 09:00` | 227.0h | `$2.3866` | `$2.8639` | **+30.10%** | **+26.85%** | +21.8% | -9.0% | `target_reclaim` |
| 2 | Book 4 | `2026-09-25 18:00` | `2026-10-08 17:00` | 311.0h | `$0.1652` | `$0.1405` | **-18.12%** | **-19.64%** | +11.2% | -15.2% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `structural_stop` | `1` | `0.0%` | **`-19.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+26.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `IO`

* **Total Candidate Breakouts Filtered (Vetoed):** `295`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `176` (59.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `39`
* **Saved Capital Losses Avoided:** `+2,227.8%`
* **Missed Upside Forgone:** `-983.7%`
* **Net Veto Alpha:** `+1,244.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `270` | `91.5%` |
| `Core 1: Macro Bear Veto` | `25` | `8.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*