# Kronos V12: Institutional Symbol Tear Sheet — `ZIL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`40.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.070`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-6.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.94x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.25%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-6.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`44.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.6% / -4.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 17:00` | `2022-10-27 17:00` | 48.0h | `$0.0302` | `$0.0301` | **-0.27%** | **-0.27%** | +3.7% | -2.2% | `fast_decay_cut` |
| 2 | Book 1 | `2024-02-25 21:00` | `2024-02-28 17:00` | 68.0h | `$0.0251` | `$0.0251` | **+0.22%** | **+0.22%** | +17.0% | -5.3% | `breakeven_ratchet` |
| 3 | Book 2 | `2026-05-06 00:00` | `2026-05-08 00:00` | 48.0h | `$0.0044` | `$0.0042` | **-4.13%** | **-4.21%** | +6.6% | -4.3% | `fast_decay_cut` |
| 4 | Book 2 | `2026-08-21 07:00` | `2026-08-22 05:00` | 22.0h | `$0.0026` | `$0.0026` | **+0.25%** | **+0.25%** | +15.2% | -5.5% | `breakeven_ratchet` |
| 5 | Book 2 | `2026-09-06 15:00` | `2026-09-08 03:00` | 36.0h | `$0.0030` | `$0.0029` | **-2.22%** | **-2.24%** | +0.4% | -3.6% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `2` | `100.0%` | **`+0.5%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-4.5%`** |
| `stall_bailout` | `1` | `0.0%` | **`-2.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `ZIL`

* **Total Candidate Breakouts Filtered (Vetoed):** `273`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `142` (52.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `64`
* **Saved Capital Losses Avoided:** `+1,963.3%`
* **Missed Upside Forgone:** `-2,570.3%`
* **Net Veto Alpha:** `+-607.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `113` | `41.4%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `93` | `34.1%` |
| `Core 1: Macro Bear Veto` | `54` | `19.8%` |
| `Core 4: Funding Rate Cap` | `13` | `4.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*