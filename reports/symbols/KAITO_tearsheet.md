# Kronos V12: Institutional Symbol Tear Sheet — `KAITO`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.896`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+55.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.75x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+11.16%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-10.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`46.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.2% / -8.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2025-04-20 04:00` | `2025-04-22 04:00` | 48.0h | `$0.7878` | `$0.7704` | **-2.63%** | **-2.66%** | +1.8% | -6.9% | `fast_decay_cut` |
| 2 | Book 4 | `2025-05-07 05:00` | `2025-05-07 17:00` | 12.0h | `$1.1414` | `$1.3697` | **+46.85%** | **+39.55%** | +21.5% | -3.0% | `target_reclaim` |
| 3 | Book 1 | `2026-05-05 01:00` | `2026-05-06 13:00` | 36.0h | `$0.5129` | `$0.4943` | **-6.00%** | **-6.16%** | +0.7% | -8.2% | `fast_decay_cut` |
| 4 | Book 4 | `2026-06-26 15:00` | `2026-07-02 02:00` | 131.0h | `$0.5351` | `$0.6421` | **+41.30%** | **+35.49%** | +20.9% | -5.3% | `target_reclaim` |
| 5 | Book 2 | `2026-08-21 22:00` | `2026-08-22 05:00` | 7.0h | `$0.3911` | `$0.3589` | **-10.00%** | **-10.44%** | +5.9% | -17.3% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-8.8%`** |
| `target_reclaim` | `2` | `100.0%` | **`+75.0%`** |
| `initial_stop` | `1` | `0.0%` | **`-10.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `KAITO`

* **Total Candidate Breakouts Filtered (Vetoed):** `844`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `339` (40.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `256`
* **Saved Capital Losses Avoided:** `+4,019.5%`
* **Missed Upside Forgone:** `-8,653.2%`
* **Net Veto Alpha:** `+-4,633.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `449` | `53.2%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `395` | `46.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*