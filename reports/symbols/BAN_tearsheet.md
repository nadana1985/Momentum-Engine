# Kronos V12: Institutional Symbol Tear Sheet — `BAN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.810`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+24.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.27x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+6.03%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`64.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+47.0% / -15.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-01-25 13:00` | `2025-01-25 14:00` | 1.0h | `$0.0703` | `$0.0645` | **-8.23%** | **-8.59%** | +14.1% | -21.0% | `stop_loss` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-02-17 11:00` | `2025-02-21 11:00` | Live | `$0.0734` | `$0.0797` | **+8.50%** | **+8.16%** | +141.7% | -34.5% | `shelf_target_reclaim` |
| 3 | Book 3 | `2025-04-29 09:00` | `2025-04-29 10:00` | 1.0h | `$0.0524` | `$0.0545` | **+4.17%** | **+4.08%** | +10.6% | -2.2% | `target_reclaim` |
| 4 | Book 4 | `2025-08-20 16:00` | `2025-08-28 16:00` | 192.0h | `$0.0792` | `$0.0951` | **+22.33%** | **+20.48%** | +21.8% | -2.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+24.6%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `BAN`

* **Total Candidate Breakouts Filtered (Vetoed):** `635`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `277` (43.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `67`
* **Saved Capital Losses Avoided:** `+5,351.5%`
* **Missed Upside Forgone:** `-1,676.0%`
* **Net Veto Alpha:** `+3,675.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `625` | `98.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `10` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*