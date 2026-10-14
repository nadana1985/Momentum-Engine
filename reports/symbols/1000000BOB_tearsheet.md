# Kronos V12: Institutional Symbol Tear Sheet — `1000000BOB`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.189`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-55.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.57x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-13.95%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-68.9%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`2.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+21.7% / -17.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-09 11:00` | `2025-07-09 17:00` | 6.0h | `$0.0700` | `$0.0750` | **+7.17%** | **+6.92%** | +11.3% | -7.6% | `target_reclaim` |
| 2 | Book 3 | `2025-08-04 19:00` | `2025-08-04 20:00` | 1.0h | `$0.0700` | `$0.0744` | **+6.31%** | **+6.12%** | +9.4% | -0.7% | `target_reclaim` |
| 3 | Book 3 | `2026-09-06 12:00` | `2026-09-06 13:00` | 1.0h | `$0.0211` | `$0.0193` | **-8.23%** | **-8.59%** | +16.1% | -10.6% | `stop_loss` |
| 4 | Book 3 | `2026-10-05 08:00` | `2026-10-05 09:00` | 1.0h | `$0.0175` | `$0.0096` | **-45.27%** | **-60.27%** | +49.7% | -51.3% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-68.9%`** |
| `target_reclaim` | `2` | `100.0%` | **`+13.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `1000000BOB`

* **Total Candidate Breakouts Filtered (Vetoed):** `242`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `184` (76.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `8`
* **Saved Capital Losses Avoided:** `+2,147.0%`
* **Missed Upside Forgone:** `-248.8%`
* **Net Veto Alpha:** `+1,898.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `194` | `80.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `43` | `17.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `4` | `1.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*