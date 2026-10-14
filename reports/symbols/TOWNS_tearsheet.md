# Kronos V12: Institutional Symbol Tear Sheet — `TOWNS`
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
| **Cumulative Net Log Return** | **`+23.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.27x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+11.76%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`56.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+20.1% / -10.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-22 05:00` | `2026-08-25 05:00` | 72.0h | `$0.0023` | `$0.0027` | **+18.00%** | **+16.55%** | +22.2% | -14.5% | `climax_whale_euphoria_harvest` |
| 2 | Book 3 | `2026-10-02 17:00` | `2026-10-04 09:00` | 40.0h | `$0.0022` | `$0.0023` | **+7.22%** | **+6.97%** | +18.1% | -6.0% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+7.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `TOWNS`

* **Total Candidate Breakouts Filtered (Vetoed):** `14`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `14` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+289.2%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+289.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `10` | `71.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `28.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*