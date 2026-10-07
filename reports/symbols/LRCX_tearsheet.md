# Kronos V12: Institutional Symbol Tear Sheet — `LRCX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`17.063`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+7.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.72%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`117.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.6% / -1.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-21 15:00` | `2026-09-24 09:00` | 66.0h | `$299.4768` | `$298.0929` | **-0.46%** | **-0.46%** | +4.2% | -1.1% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-29 08:00` | `2026-10-06 08:00` | 168.0h | `$318.9353` | `$345.1649` | **+8.22%** | **+7.90%** | +11.1% | -1.0% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.5%`** |
| `time_cap` | `1` | `100.0%` | **`+7.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `LRCX`

* **Total Candidate Breakouts Filtered (Vetoed):** `10`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `8` (80.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+80.0%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+80.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `10` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*