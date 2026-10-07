# Kronos V12: Institutional Symbol Tear Sheet — `CVX`
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
| **Cumulative Net Log Return** | **`+16.7%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.18x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+8.34%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`3.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.0% / -1.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$1.7084` | `$1.8570` | **+8.70%** | **+8.34%** | +21.9% | -1.9% | `target_reclaim` |
| 2 | Book 3 | `2026-10-01 21:00` | `2026-10-02 02:00` | 5.0h | `$2.1004` | `$2.2830` | **+8.70%** | **+8.34%** | +10.0% | -1.1% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `CVX`

* **Total Candidate Breakouts Filtered (Vetoed):** `53`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `38` (71.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `1`
* **Saved Capital Losses Avoided:** `+381.1%`
* **Missed Upside Forgone:** `-24.8%`
* **Net Veto Alpha:** `+356.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `36` | `67.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `13` | `24.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `3` | `5.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `1.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*