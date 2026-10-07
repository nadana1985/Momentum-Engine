# Kronos V12: Institutional Symbol Tear Sheet — `CYBER`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.657`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.47%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`91.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.9% / -6.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2024-08-11 05:00` | `2024-08-11 19:00` | 14.0h | `$3.1709` | `$2.9099` | **-8.23%** | **-8.59%** | +1.8% | -8.9% | `initial_stop` |
| 2 | Book 2 | `2025-04-21 04:00` | `2025-04-28 04:00` | 168.0h | `$1.2351` | `$1.3067` | **+5.80%** | **+5.64%** | +16.0% | -5.0% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `time_cap` | `1` | `100.0%` | **`+5.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CYBER`

* **Total Candidate Breakouts Filtered (Vetoed):** `103`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `68` (66.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+1,116.2%`
* **Missed Upside Forgone:** `-757.9%`
* **Net Veto Alpha:** `+358.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `53` | `51.5%` |
| `Core 1: Macro Bear Veto` | `25` | `24.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `20` | `19.4%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `5` | `4.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*