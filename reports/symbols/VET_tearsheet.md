# Kronos V12: Institutional Symbol Tear Sheet — `VET`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+37.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.46x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+18.83%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`336.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+26.6% / -3.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-01-12 01:00` | `2023-01-26 01:00` | 336.0h | `$0.0188` | `$0.0231` | **+27.35%** | **+24.18%** | +24.8% | -4.2% | `time_cap` |
| 2 | Book 1 | `2026-08-26 22:00` | `2026-09-09 22:00` | 336.0h | `$0.0064` | `$0.0074` | **+14.44%** | **+13.49%** | +28.4% | -3.6% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `2` | `100.0%` | **`+37.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `VET`

* **Total Candidate Breakouts Filtered (Vetoed):** `339`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `183` (54.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `58`
* **Saved Capital Losses Avoided:** `+2,506.6%`
* **Missed Upside Forgone:** `-2,162.2%`
* **Net Veto Alpha:** `+344.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `155` | `45.7%` |
| `Core 1: Macro Bear Veto` | `88` | `26.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `84` | `24.8%` |
| `Core 4: Funding Rate Cap` | `12` | `3.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*