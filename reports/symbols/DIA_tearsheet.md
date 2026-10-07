# Kronos V12: Institutional Symbol Tear Sheet — `DIA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`5` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`80.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.622`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+22.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.25x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.50%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`28.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.0% / -2.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-15 01:00` | `2025-07-18 01:00` | 72.0h | `$0.4236` | `$0.4502` | **+6.28%** | **+6.09%** | +8.4% | -2.8% | `time_expiry` |
| 2 | Book 3 | `2025-10-28 06:00` | `2025-10-28 07:00` | 1.0h | `$0.5776` | `$0.6278` | **+8.70%** | **+8.34%** | +13.9% | -0.2% | `target_reclaim` |
| 3 | Book 3 | `2026-09-07 23:00` | `2026-09-10 12:00` | 61.0h | `$0.1388` | `$0.1274` | **-8.23%** | **-8.59%** | +1.8% | -8.2% | `stop_loss` |
| 4 | Book 3 | `2026-10-02 18:00` | `2026-10-02 23:00` | 5.0h | `$0.1535` | `$0.1668` | **+8.70%** | **+8.34%** | +11.2% | -0.1% | `target_reclaim` |
| 5 | Book 3 | `2026-10-06 02:00` | `2026-10-06 07:00` | 5.0h | `$0.1665` | `$0.1810` | **+8.70%** | **+8.34%** | +9.8% | -0.8% | `target_reclaim` |
| 6 | Book 3 | `2026-10-06 13:00` | `_Open Live_` | 13.7h | `$0.1759` | `$0.1717` | **-2.39%** | **-2.42%** | +3.6% | -3.6% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+25.0%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+6.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `DIA`

* **Total Candidate Breakouts Filtered (Vetoed):** `73`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `41` (56.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+709.0%`
* **Missed Upside Forgone:** `-877.4%`
* **Net Veto Alpha:** `+-168.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `32` | `43.8%` |
| `Core 1: Macro Bear Veto` | `23` | `31.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `10` | `13.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `8` | `11.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*