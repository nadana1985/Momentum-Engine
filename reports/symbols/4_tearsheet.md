# Kronos V12: Institutional Symbol Tear Sheet — `4`
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
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`10.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.4% / -8.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-29 14:00` | `2026-08-29 22:00` | 8.0h | `$0.0162` | `$0.0184` | **+13.64%** | **+12.78%** | +23.6% | -4.9% | `target_reclaim` |
| 2 | Book 3 | `2026-08-30 05:00` | `2026-08-30 18:00` | 13.0h | `$0.0189` | `$0.0173` | **-8.23%** | **-8.59%** | +15.1% | -12.2% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+12.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `4`

* **Total Candidate Breakouts Filtered (Vetoed):** `42`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `40` (95.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+1,052.3%`
* **Missed Upside Forgone:** `-439.4%`
* **Net Veto Alpha:** `+612.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `32` | `76.2%` |
| `Core 4: Funding Rate Cap` | `10` | `23.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*