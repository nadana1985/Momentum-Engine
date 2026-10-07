# Kronos V12: Institutional Symbol Tear Sheet — `NEAR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`10.843`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+35.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.42x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.82%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-3.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`268.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+26.9% / -6.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-11-01 09:00` | `2023-11-09 16:00` | 199.0h | `$1.3654` | `$1.3688` | **+0.24%** | **+0.24%** | +23.0% | -7.6% | `breakeven_ratchet` |
| 2 | Book 1 | `2025-04-25 09:00` | `2025-04-28 09:00` | 72.0h | `$2.6456` | `$2.5546` | **-3.52%** | **-3.58%** | +3.1% | -8.6% | `stagnation_bailout` |
| 3 | Book 1 | `2025-07-10 16:00` | `2025-07-30 19:00` | 483.0h | `$2.4010` | `$2.5706` | **+8.66%** | **+8.31%** | +29.2% | -2.3% | `trail_stop` |
| 4 | Book 1 | `2026-09-04 19:00` | `2026-09-18 01:00` | 318.0h | `$2.1714` | `$3.2169` | **+35.42%** | **+30.32%** | +52.6% | -7.3% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+30.3%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-3.6%`** |
| `trail_stop` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `NEAR`

* **Total Candidate Breakouts Filtered (Vetoed):** `274`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `161` (58.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `72`
* **Saved Capital Losses Avoided:** `+2,389.3%`
* **Missed Upside Forgone:** `-2,190.2%`
* **Net Veto Alpha:** `+199.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `125` | `45.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `101` | `36.9%` |
| `Core 4: Funding Rate Cap` | `47` | `17.2%` |
| `Core 4: Whale Firewall` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*