# Kronos V12: Institutional Symbol Tear Sheet — `ME`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`83.3%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`4.021`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+25.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.30x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.32%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`31.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.2% / -6.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-04-29 23:00` | `2025-04-30 00:00` | 1.0h | `$0.9632` | `$1.0470` | **+8.70%** | **+8.34%** | +9.1% | -0.2% | `target_reclaim` |
| 2 | Book 3 | `2025-05-02 05:00` | `2025-05-04 00:00` | 43.0h | `$1.0433` | `$0.9574` | **-8.23%** | **-8.59%** | +3.1% | -11.0% | `stop_loss` |
| 3 | Book 3 | `2025-05-12 15:00` | `2025-05-14 01:00` | 34.0h | `$1.0847` | `$1.1790` | **+8.70%** | **+8.34%** | +8.8% | -2.3% | `target_reclaim` |
| 4 | Book 3 | `2025-09-22 06:00` | `2025-09-22 07:00` | 1.0h | `$0.6837` | `$0.7432` | **+8.70%** | **+8.34%** | +24.3% | -7.0% | `target_reclaim` |
| 5 | Book 3 | `2026-08-22 05:00` | `2026-08-23 21:00` | 40.0h | `$0.0651` | `$0.0707` | **+8.70%** | **+8.34%** | +13.1% | -18.1% | `target_reclaim` |
| 6 | Book 3 | `2026-09-28 14:00` | `2026-10-01 14:00` | 72.0h | `$0.0732` | `$0.0741` | **+1.19%** | **+1.18%** | +8.5% | -1.4% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `4` | `100.0%` | **`+33.4%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `100.0%` | **`+1.2%`** |

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