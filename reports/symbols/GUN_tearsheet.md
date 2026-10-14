# Kronos V12: Institutional Symbol Tear Sheet — `GUN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.472`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+12.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.13x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.16%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`27.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.8% / -12.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-05-15 14:00` | `2025-05-15 21:00` | 7.0h | `$0.0596` | `$0.0547` | **-8.23%** | **-8.59%** | +6.4% | -8.8% | `stop_loss` |
| 2 | Book 3 | `2025-07-04 04:00` | `2025-07-04 06:00` | 2.0h | `$0.0306` | `$0.0332` | **+8.70%** | **+8.34%** | +10.1% | -0.6% | `target_reclaim` |
| 3 | Book 5 (Shelf Absorption Squeeze) | `2025-12-13 12:00` | `2025-12-17 12:00` | Live | `$0.0147` | `$0.0160` | **+8.50%** | **+8.16%** | +40.3% | -31.8% | `shelf_target_reclaim` |
| 4 | Book 3 | `2026-09-20 10:00` | `2026-09-23 10:00` | 72.0h | `$0.0030` | `$0.0032` | **+4.85%** | **+4.73%** | +14.3% | -7.0% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `100.0%` | **`+4.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `GUN`

* **Total Candidate Breakouts Filtered (Vetoed):** `78`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `60` (76.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `24`
* **Saved Capital Losses Avoided:** `+1,269.6%`
* **Missed Upside Forgone:** `-1,017.7%`
* **Net Veto Alpha:** `+251.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `64` | `82.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `13` | `16.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `1.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*