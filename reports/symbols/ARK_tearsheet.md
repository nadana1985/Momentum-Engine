# Kronos V12: Institutional Symbol Tear Sheet — `ARK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.128`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+3.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.60%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-23.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`180.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.3% / -13.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2023-10-05 09:00` | `2023-10-09 09:00` | Live | `$0.4375` | `$0.4746` | **+8.50%** | **+8.16%** | +20.2% | -11.2% | `shelf_target_reclaim` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2025-02-17 06:00` | `2025-02-21 06:00` | Live | `$0.4198` | `$0.4555` | **+8.50%** | **+8.16%** | +17.2% | -30.4% | `shelf_target_reclaim` |
| 3 | Book 4 | `2025-04-15 13:00` | `2025-05-06 09:00` | 500.0h | `$0.4672` | `$0.3971` | **-18.12%** | **-19.64%** | +19.6% | -15.8% | `structural_stop` |
| 4 | Book 1 | `2026-09-04 07:00` | `2026-09-05 20:00` | 37.0h | `$0.1200` | `$0.1172` | **-3.52%** | **-3.58%** | +2.5% | -4.7% | `fast_decay_cut` |
| 5 | Book 4 | `2026-09-13 02:00` | `2026-09-13 07:00` | 5.0h | `$0.1506` | `$0.1808` | **+10.36%** | **+9.89%** | +27.2% | -4.3% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `2` | `100.0%` | **`+16.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-3.6%`** |
| `structural_stop` | `1` | `0.0%` | **`-19.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+9.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `ARK`

* **Total Candidate Breakouts Filtered (Vetoed):** `120`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `96` (80.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `21`
* **Saved Capital Losses Avoided:** `+1,262.1%`
* **Missed Upside Forgone:** `-1,045.4%`
* **Net Veto Alpha:** `+216.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `64` | `53.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `42` | `35.0%` |
| `Core 4: Defensible Whale Dump` | `10` | `8.3%` |
| `Core 4: Whale Firewall` | `4` | `3.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*