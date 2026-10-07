# Kronos V12: Institutional Symbol Tear Sheet — `TRB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`2.962`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+7.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.56%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-3.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`107.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.6% / -2.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2022-03-27 01:00` | `2022-04-06 00:00` | 239.0h | `$22.6164` | `$24.6203` | **+12.30%** | **+11.60%** | +33.1% | -3.6% | `trail_stop` |
| 2 | Book 1 | `2023-04-10 07:00` | `2023-04-11 19:00` | 36.0h | `$15.9899` | `$15.6209` | **-3.38%** | **-3.43%** | +3.8% | -3.2% | `fast_decay_cut` |
| 3 | Book 2 | `2024-09-13 17:00` | `2024-09-15 17:00` | 48.0h | `$64.4758` | `$64.1652` | **-0.48%** | **-0.48%** | +3.9% | -1.8% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-3.9%`** |
| `trail_stop` | `1` | `100.0%` | **`+11.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `TRB`

* **Total Candidate Breakouts Filtered (Vetoed):** `225`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `164` (72.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `70`
* **Saved Capital Losses Avoided:** `+2,794.4%`
* **Missed Upside Forgone:** `-2,607.1%`
* **Net Veto Alpha:** `+187.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `91` | `40.4%` |
| `Core 0: Zero-Tolerance Data Firewall` | `79` | `35.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `39` | `17.3%` |
| `Core 4: Defensible Whale Dump` | `12` | `5.3%` |
| `Core 4: Funding Rate Cap` | `4` | `1.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*