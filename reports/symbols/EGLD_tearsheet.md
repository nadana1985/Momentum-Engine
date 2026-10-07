# Kronos V12: Institutional Symbol Tear Sheet — `EGLD`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-6.9%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.93x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-3.44%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.4% / -6.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-02-08 01:00` | `2023-02-09 13:00` | 36.0h | `$48.0899` | `$45.3863` | **-5.70%** | **-5.87%** | +0.4% | -8.5% | `fast_decay_cut` |
| 2 | Book 1 | `2026-08-23 15:00` | `2026-08-25 03:00` | 36.0h | `$3.5599` | `$3.5112` | **-0.99%** | **-1.00%** | +4.4% | -4.2% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-6.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `EGLD`

* **Total Candidate Breakouts Filtered (Vetoed):** `314`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `142` (45.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `81`
* **Saved Capital Losses Avoided:** `+1,867.1%`
* **Missed Upside Forgone:** `-3,331.1%`
* **Net Veto Alpha:** `+-1,464.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `176` | `56.1%` |
| `Core 1: Macro Bear Veto` | `68` | `21.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `62` | `19.7%` |
| `Core 4: Funding Rate Cap` | `8` | `2.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*