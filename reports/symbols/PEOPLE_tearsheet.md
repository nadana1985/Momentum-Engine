# Kronos V12: Institutional Symbol Tear Sheet — `PEOPLE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.317`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-18.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.83x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-4.59%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-19.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`269.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.9% / -10.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-01-10 11:00` | `2023-01-12 05:00` | 42.0h | `$0.0246` | `$0.0236` | **-6.98%** | **-7.20%** | +3.8% | -7.9% | `fast_decay_cut` |
| 2 | Book 4 | `2023-01-21 05:00` | `2023-02-20 04:00` | 719.0h | `$0.0282` | `$0.0292` | **+3.81%** | **+3.75%** | +17.6% | -11.4% | `time_expiry` |
| 3 | Book 4 | `2023-11-11 09:00` | `2023-11-21 17:00` | 248.0h | `$0.0136` | `$0.0116` | **-18.12%** | **-19.64%** | +10.0% | -15.9% | `structural_stop` |
| 4 | Book 4 | `2026-08-06 20:00` | `2026-08-09 17:00` | 69.0h | `$0.0076` | `$0.0092` | **+4.86%** | **+4.75%** | +24.0% | -7.8% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-7.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-19.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+4.7%`** |
| `time_expiry` | `1` | `100.0%` | **`+3.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `PEOPLE`

* **Total Candidate Breakouts Filtered (Vetoed):** `363`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `246` (67.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `93`
* **Saved Capital Losses Avoided:** `+3,819.3%`
* **Missed Upside Forgone:** `-5,133.5%`
* **Net Veto Alpha:** `+-1,314.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `262` | `72.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `92` | `25.3%` |
| `Core 4: Funding Rate Cap` | `4` | `1.1%` |
| `Core 4: Whale Firewall` | `3` | `0.8%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.3%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*