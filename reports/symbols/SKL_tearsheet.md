# Kronos V12: Institutional Symbol Tear Sheet — `SKL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-8.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.20%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`40.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.2% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-07-13 16:00` | `2023-07-15 16:00` | 48.0h | `$0.0293` | `$0.0292` | **-0.29%** | **-0.29%** | +3.2% | -6.1% | `fast_decay_cut` |
| 2 | Book 2 | `2023-10-16 05:00` | `2023-10-17 13:00` | 32.0h | `$0.0223` | `$0.0206` | **-7.79%** | **-8.11%** | +1.2% | -8.2% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.3%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `SKL`

* **Total Candidate Breakouts Filtered (Vetoed):** `264`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `155` (58.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `73`
* **Saved Capital Losses Avoided:** `+2,247.5%`
* **Missed Upside Forgone:** `-4,201.0%`
* **Net Veto Alpha:** `+-1,953.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `60` | `22.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `53` | `20.1%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `52` | `19.7%` |
| `Core 1: Macro Bear Veto` | `51` | `19.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `48` | `18.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*