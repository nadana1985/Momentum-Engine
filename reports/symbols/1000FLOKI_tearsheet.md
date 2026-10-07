# Kronos V12: Institutional Symbol Tear Sheet — `1000FLOKI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`8.407`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+69.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.01x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+17.43%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`90.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+31.7% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-09-30 16:00` | `2023-10-04 00:00` | 80.0h | `$0.0190` | `$0.0175` | **-8.98%** | **-9.41%** | +10.0% | -10.1% | `initial_stop` |
| 2 | Book 2 | `2023-10-21 06:00` | `2023-10-25 14:00` | 104.0h | `$0.0216` | `$0.0254` | **+11.12%** | **+10.55%** | +43.7% | -5.5% | `trail_stop` |
| 3 | Book 1 | `2024-02-26 06:00` | `2024-02-27 12:00` | 30.0h | `$0.0374` | `$0.0479` | **+36.43%** | **+31.06%** | +36.2% | -5.4% | `climax_top_harvest` |
| 4 | Book 1 | `2025-04-22 14:00` | `2025-04-28 18:00` | 148.0h | `$0.0622` | `$0.0819` | **+45.54%** | **+37.53%** | +37.1% | -3.5% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_top_harvest` | `2` | `100.0%` | **`+68.6%`** |
| `initial_stop` | `1` | `0.0%` | **`-9.4%`** |
| `trail_stop` | `1` | `100.0%` | **`+10.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000FLOKI`

* **Total Candidate Breakouts Filtered (Vetoed):** `138`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `85` (61.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `31`
* **Saved Capital Losses Avoided:** `+1,099.4%`
* **Missed Upside Forgone:** `-1,381.7%`
* **Net Veto Alpha:** `+-282.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `83` | `60.1%` |
| `Core 1: Macro Bear Veto` | `50` | `36.2%` |
| `Core 4: Funding Rate Cap` | `5` | `3.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*