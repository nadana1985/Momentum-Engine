# Kronos V12: Institutional Symbol Tear Sheet — `DOLO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.320`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+4.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.01%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`32.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.5% / -7.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-01 17:00` | `2025-07-02 17:00` | 24.0h | `$0.0362` | `$0.0393` | **+8.70%** | **+8.34%** | +9.0% | -6.5% | `target_reclaim` |
| 2 | Book 3 | `2025-07-03 10:00` | `2025-07-06 10:00` | 72.0h | `$0.0393` | `$0.0377` | **-3.96%** | **-4.04%** | +2.6% | -5.7% | `time_expiry` |
| 3 | Book 3 | `2025-07-23 12:00` | `2025-07-24 11:00` | 23.0h | `$0.0775` | `$0.0843` | **+8.70%** | **+8.34%** | +13.9% | -7.2% | `target_reclaim` |
| 4 | Book 3 | `2025-07-29 10:00` | `2025-07-29 20:00` | 10.0h | `$0.1797` | `$0.1649` | **-8.23%** | **-8.59%** | +8.5% | -8.7% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_expiry` | `1` | `0.0%` | **`-4.0%`** |

---

## 4. Counterfactual Risk Gate Audit for `DOLO`

* **Total Candidate Breakouts Filtered (Vetoed):** `44`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `26` (59.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+464.6%`
* **Missed Upside Forgone:** `-1,082.6%`
* **Net Veto Alpha:** `+-618.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `26` | `59.1%` |
| `Core 1: Macro Bear Veto` | `15` | `34.1%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `6.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*