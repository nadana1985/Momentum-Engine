# Kronos V12: Institutional Symbol Tear Sheet — `DYDX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `1` (`1` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `1` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+16.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+16.58%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`168.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+23.9% / -2.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-01-09 00:00` | `2023-01-16 00:00` | 168.0h | `$1.2862` | `$1.5182` | **+18.04%** | **+16.58%** | +23.9% | -2.7% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `1` | `100.0%` | **`+16.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `DYDX`

* **Total Candidate Breakouts Filtered (Vetoed):** `146`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `104` (71.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `22`
* **Saved Capital Losses Avoided:** `+1,410.8%`
* **Missed Upside Forgone:** `-694.0%`
* **Net Veto Alpha:** `+716.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `64` | `43.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `60` | `41.1%` |
| `Core 0: Zero-Tolerance Data Firewall` | `11` | `7.5%` |
| `Core 4: Funding Rate Cap` | `6` | `4.1%` |
| `Core 4: Defensible Whale Dump` | `3` | `2.1%` |
| `Core 4: Whale Firewall` | `2` | `1.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*