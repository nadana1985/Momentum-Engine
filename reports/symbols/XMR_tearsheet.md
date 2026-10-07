# Kronos V12: Institutional Symbol Tear Sheet — `XMR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`16.7%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.013`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-18.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.83x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.05%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-13.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`93.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.0% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-01-11 23:00` | `2023-01-18 23:00` | 168.0h | `$169.1618` | `$162.2334` | **-5.12%** | **-5.26%** | +11.1% | -6.1% | `time_cap` |
| 2 | Book 2 | `2023-10-07 20:00` | `2023-10-10 20:00` | 72.0h | `$154.9965` | `$152.4479` | **-1.64%** | **-1.66%** | +1.0% | -2.2% | `stagnation_cut` |
| 3 | Book 2 | `2024-06-07 09:00` | `2024-06-07 17:00` | 8.0h | `$174.6355` | `$160.2630` | **-8.23%** | **-8.59%** | +0.1% | -8.8% | `initial_stop` |
| 4 | Book 1 | `2024-06-10 18:00` | `2024-06-13 18:00` | 72.0h | `$177.6029` | `$176.9066` | **-0.27%** | **-0.27%** | +3.0% | -5.7% | `stagnation_bailout` |
| 5 | Book 2 | `2024-07-26 02:00` | `2024-07-29 02:00` | 72.0h | `$168.5202` | `$163.8693` | **-2.76%** | **-2.80%** | +3.8% | -5.2% | `stagnation_cut` |
| 6 | Book 2 | `2025-05-21 02:00` | `2025-05-28 00:00` | 166.0h | `$359.4263` | `$360.3204` | **+0.25%** | **+0.25%** | +17.1% | -2.1% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stagnation_cut` | `2` | `0.0%` | **`-4.5%`** |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-0.3%`** |
| `time_cap` | `1` | `0.0%` | **`-5.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `XMR`

* **Total Candidate Breakouts Filtered (Vetoed):** `358`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `191` (53.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+1,794.4%`
* **Missed Upside Forgone:** `-922.3%`
* **Net Veto Alpha:** `+872.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `151` | `42.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `141` | `39.4%` |
| `Core 4: Defensible Whale Dump` | `36` | `10.1%` |
| `Core 4: Funding Rate Cap` | `23` | `6.4%` |
| `Core 4: Whale Firewall` | `7` | `2.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*