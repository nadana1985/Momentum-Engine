# Kronos V12: Institutional Symbol Tear Sheet — `STRK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`100.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`999.000`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+84.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.32x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+42.13%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`185.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+21.3% / -9.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2025-11-14 14:00` | `2025-11-15 17:00` | 27.0h | `$0.1730` | `$0.2076` | **+4.47%** | **+4.37%** | +21.3% | -8.0% | `target_reclaim` |
| 2 | Book 4 | `2026-09-19 08:00` | `2026-10-03 16:00` | 344.0h | `$0.0425` | `$0.0510` | **+113.52%** | **+79.89%** | +21.3% | -10.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+84.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `STRK`

* **Total Candidate Breakouts Filtered (Vetoed):** `542`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `393` (72.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `106`
* **Saved Capital Losses Avoided:** `+9,225.9%`
* **Missed Upside Forgone:** `-3,873.1%`
* **Net Veto Alpha:** `+5,352.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `281` | `51.8%` |
| `Core 1: Macro Bear Veto` | `261` | `48.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*