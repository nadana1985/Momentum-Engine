# Kronos V12: Institutional Symbol Tear Sheet — `HYPER`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.384`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+11.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.13x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.96%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`6.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+3.5% / -18.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-08-10 08:00` | `2025-08-10 14:00` | 6.0h | `$0.4056` | `$0.4225` | **+4.17%** | **+4.08%** | +4.6% | -1.1% | `target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-12-09 16:00` | `2025-12-13 16:00` | Live | `$0.1407` | `$0.1526` | **+8.50%** | **+8.16%** | +11.0% | -24.6% | `shelf_target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2026-01-11 01:00` | `2026-01-15 01:00` | Live | `$0.1421` | `$0.1305` | **-8.20%** | **-8.56%** | +-4.5% | -27.2% | `shelf_stop_loss` |
| 4 | Book 5 (Shelf Absorption Squeeze) | `2026-04-25 11:00` | `2026-04-29 11:00` | Live | `$0.1204` | `$0.1306` | **+8.50%** | **+8.16%** | +3.0% | -20.7% | `shelf_target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+4.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `HYPER`

* **Total Candidate Breakouts Filtered (Vetoed):** `42`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `34` (81.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `11`
* **Saved Capital Losses Avoided:** `+652.5%`
* **Missed Upside Forgone:** `-2,204.4%`
* **Net Veto Alpha:** `+-1,551.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `22` | `52.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `12` | `28.6%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `19.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*