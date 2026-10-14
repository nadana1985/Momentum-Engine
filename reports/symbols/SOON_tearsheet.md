# Kronos V12: Institutional Symbol Tear Sheet — `SOON`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.161`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+7.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.62%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-3.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`64.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+5.4% / -4.8%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-08-05 19:00` | `2025-08-06 05:00` | 10.0h | `$0.1562` | `$0.1682` | **+7.70%** | **+7.42%** | +10.1% | -1.4% | `target_reclaim` |
| 2 | Book 4 | `2026-07-31 16:00` | `2026-08-07 16:00` | 168.0h | `$0.2321` | `$0.2120` | **-3.56%** | **-3.64%** | +1.4% | -12.0% | `stagnation_cut` |
| 3 | Book 3 | `2026-09-23 14:00` | `2026-09-24 05:00` | 15.0h | `$0.1916` | `$0.1996` | **+4.17%** | **+4.08%** | +4.7% | -0.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+11.5%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-3.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `SOON`

* **Total Candidate Breakouts Filtered (Vetoed):** `254`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `214` (84.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `85`
* **Saved Capital Losses Avoided:** `+4,356.0%`
* **Missed Upside Forgone:** `-4,167.2%`
* **Net Veto Alpha:** `+188.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `135` | `53.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `106` | `41.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `9` | `3.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `1.2%` |
| `Core 3: Min Turnover Velocity` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*