# Kronos V12: Institutional Symbol Tear Sheet — `CC`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.546`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+8.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.09x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.20%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-2.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`62.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+20.9% / -3.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2025-12-28 05:00` | `2025-12-28 22:00` | 17.0h | `$0.1165` | `$0.1398` | **+11.25%** | **+10.76%** | +23.6% | -2.5% | `target_reclaim` |
| 2 | Book 1 | `2026-09-25 11:00` | `2026-09-29 23:00` | 108.0h | `$0.1242` | `$0.1220` | **-2.34%** | **-2.37%** | +18.2% | -4.0% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `0.0%` | **`-2.4%`** |
| `target_reclaim` | `1` | `100.0%` | **`+10.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `CC`

* **Total Candidate Breakouts Filtered (Vetoed):** `400`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `235` (58.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `88`
* **Saved Capital Losses Avoided:** `+2,501.3%`
* **Missed Upside Forgone:** `-2,460.7%`
* **Net Veto Alpha:** `+40.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `400` | `100.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*