# Kronos V12: Institutional Symbol Tear Sheet — `BARD`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+9.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.10x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.61%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`40.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.9% / -1.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-23 04:00` | `2026-08-23 13:00` | 9.0h | `$0.1151` | `$0.1201` | **+4.39%** | **+4.29%** | +4.9% | -1.7% | `target_reclaim` |
| 2 | Book 3 | `2026-09-29 05:00` | `2026-10-02 05:00` | 72.0h | `$0.1319` | `$0.1386` | **+5.06%** | **+4.93%** | +8.8% | -0.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+4.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+4.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `BARD`

* **Total Candidate Breakouts Filtered (Vetoed):** `50`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `38` (76.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+595.6%`
* **Missed Upside Forgone:** `-253.4%`
* **Net Veto Alpha:** `+342.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `36` | `72.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `14` | `28.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*