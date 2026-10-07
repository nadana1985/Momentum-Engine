# Kronos V12: Institutional Symbol Tear Sheet — `CTSI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.497`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`1.00x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.13%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`56.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.6% / -4.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-03-12 23:00` | `2023-03-15 16:00` | 65.0h | `$0.1311` | `$0.1315` | **+0.25%** | **+0.25%** | +16.8% | -4.0% | `breakeven_ratchet` |
| 2 | Book 2 | `2024-08-09 08:00` | `2024-08-11 08:00` | 48.0h | `$0.1339` | `$0.1333` | **-0.50%** | **-0.50%** | +2.3% | -4.8% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `CTSI`

* **Total Candidate Breakouts Filtered (Vetoed):** `186`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `105` (56.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+1,362.2%`
* **Missed Upside Forgone:** `-1,491.0%`
* **Net Veto Alpha:** `+-128.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `64` | `34.4%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `52` | `28.0%` |
| `Core 1: Macro Bear Veto` | `41` | `22.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `19` | `10.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `7` | `3.8%` |
| `Core 4: Defensible Whale Dump` | `3` | `1.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*