# Kronos V12: Institutional Symbol Tear Sheet — `LDO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.355`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+6.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.24%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`146.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+18.2% / -6.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-07-03 02:00` | `2023-07-05 13:00` | 59.0h | `$2.1943` | `$2.0573` | **-6.11%** | **-6.31%** | +2.4% | -7.1% | `fast_decay_cut` |
| 2 | Book 2 | `2023-07-13 16:00` | `2023-07-17 10:00` | 90.0h | `$2.1027` | `$2.1080` | **+0.25%** | **+0.25%** | +20.3% | -6.4% | `breakeven_ratchet` |
| 3 | Book 2 | `2025-05-27 08:00` | `2025-05-30 00:00` | 64.0h | `$0.9315` | `$0.8549` | **-8.23%** | **-8.59%** | +8.7% | -9.3% | `initial_stop` |
| 4 | Book 1 | `2025-07-10 17:00` | `2025-07-30 19:00` | 482.0h | `$0.8139` | `$0.9662` | **+26.46%** | **+23.47%** | +58.7% | -2.6% | `trail_stop` |
| 5 | Book 2 | `2026-05-06 09:00` | `2026-05-07 21:00` | 36.0h | `$0.3920` | `$0.3818` | **-2.59%** | **-2.62%** | +0.9% | -4.9% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-6.3%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `stall_bailout` | `1` | `0.0%` | **`-2.6%`** |
| `trail_stop` | `1` | `100.0%` | **`+23.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `LDO`

* **Total Candidate Breakouts Filtered (Vetoed):** `68`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `47` (69.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `5`
* **Saved Capital Losses Avoided:** `+548.2%`
* **Missed Upside Forgone:** `-168.7%`
* **Net Veto Alpha:** `+379.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `49` | `72.1%` |
| `Core 4: Funding Rate Cap` | `12` | `17.6%` |
| `Core 0: Zero-Tolerance Data Firewall` | `3` | `4.4%` |
| `Core 4: Whale Firewall` | `3` | `4.4%` |
| `Core 4: Defensible Whale Dump` | `1` | `1.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*