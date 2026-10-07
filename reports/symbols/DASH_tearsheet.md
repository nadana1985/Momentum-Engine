# Kronos V12: Institutional Symbol Tear Sheet — `DASH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.007`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-38.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.68x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-9.49%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-26.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`65.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.9% / -9.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-11-12 20:00` | `2023-11-14 20:00` | 48.0h | `$33.8945` | `$30.5335` | **-10.85%** | **-11.48%** | +1.3% | -12.1% | `fast_decay_cut` |
| 2 | Book 1 | `2023-12-27 12:00` | `2023-12-30 12:00` | 72.0h | `$37.4935` | `$32.8178` | **-16.59%** | **-18.14%** | +3.7% | -14.4% | `stagnation_bailout` |
| 3 | Book 2 | `2025-10-26 08:00` | `2025-10-28 15:00` | 55.0h | `$46.4157` | `$46.5312` | **+0.25%** | **+0.25%** | +16.8% | -3.4% | `breakeven_ratchet` |
| 4 | Book 2 | `2026-09-17 01:00` | `2026-09-20 14:00` | 85.0h | `$59.2477` | `$54.3717` | **-8.23%** | **-8.59%** | +9.8% | -8.1% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-11.5%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-18.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `DASH`

* **Total Candidate Breakouts Filtered (Vetoed):** `217`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `108` (49.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `56`
* **Saved Capital Losses Avoided:** `+1,429.7%`
* **Missed Upside Forgone:** `-2,628.9%`
* **Net Veto Alpha:** `+-1,199.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `115` | `53.0%` |
| `Core 1: Macro Bear Veto` | `80` | `36.9%` |
| `Core 4: Funding Rate Cap` | `22` | `10.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*