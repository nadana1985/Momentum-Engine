# Kronos V12: Institutional Symbol Tear Sheet — `ME`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`85.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.509`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+30.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.35x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.31%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`31.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.8% / -8.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2025-02-08 15:00` | `2025-02-12 15:00` | Live | `$1.3772` | `$1.4943` | **+8.50%** | **+8.16%** | +44.4% | -17.9% | `shelf_target_reclaim` |
| 2 | Book 3 | `2025-04-29 23:00` | `2025-04-30 00:00` | 1.0h | `$0.9632` | `$1.0470` | **+8.70%** | **+8.34%** | +9.1% | -0.2% | `target_reclaim` |
| 3 | Book 3 | `2025-05-02 05:00` | `2025-05-04 00:00` | 43.0h | `$1.0433` | `$0.9574` | **-8.23%** | **-8.59%** | +3.1% | -11.0% | `stop_loss` |
| 4 | Book 3 | `2025-05-12 15:00` | `2025-05-14 01:00` | 34.0h | `$1.0826` | `$1.1790` | **+8.90%** | **+8.53%** | +9.0% | -2.1% | `target_reclaim` |
| 5 | Book 3 | `2025-07-23 21:00` | `2025-07-26 21:00` | 72.0h | `$0.8655` | `$0.8796` | **+1.63%** | **+1.61%** | +4.8% | -6.2% | `time_expiry` |
| 6 | Book 3 | `2025-09-21 14:00` | `2025-09-21 15:00` | 1.0h | `$0.7135` | `$0.7432` | **+4.17%** | **+4.08%** | +6.4% | -0.4% | `target_reclaim` |
| 7 | Book 3 | `2026-08-22 05:00` | `2026-08-23 21:00` | 40.0h | `$0.0653` | `$0.0707` | **+8.34%** | **+8.01%** | +12.7% | -18.4% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+29.0%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `ME`

* **Total Candidate Breakouts Filtered (Vetoed):** `51`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `35` (68.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+473.0%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+473.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `19` | `37.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `18` | `35.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `14` | `27.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*