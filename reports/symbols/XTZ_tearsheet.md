# Kronos V12: Institutional Symbol Tear Sheet — `XTZ`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`6.725`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+14.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.15x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.57%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-2.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`105.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.7% / -6.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$1.0637` | `$1.2549` | **+17.98%** | **+16.53%** | +19.0% | -3.9% | `time_cap` |
| 2 | Book 2 | `2023-07-13 17:00` | `2023-07-15 17:00` | 48.0h | `$0.8892` | `$0.8768` | **-1.45%** | **-1.47%** | +3.8% | -4.6% | `fast_decay_cut` |
| 3 | Book 1 | `2023-11-06 23:00` | `2023-11-09 16:00` | 65.0h | `$0.8351` | `$0.8259` | **-1.02%** | **-1.03%** | +7.9% | -8.8% | `fast_decay_cut` |
| 4 | Book 1 | `2026-09-09 10:00` | `2026-09-15 05:00` | 139.0h | `$0.2637` | `$0.2643` | **+0.23%** | **+0.23%** | +16.1% | -7.3% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-2.5%`** |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `time_cap` | `1` | `100.0%` | **`+16.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `XTZ`

* **Total Candidate Breakouts Filtered (Vetoed):** `278`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `177` (63.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `43`
* **Saved Capital Losses Avoided:** `+2,179.2%`
* **Missed Upside Forgone:** `-1,713.1%`
* **Net Veto Alpha:** `+466.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `108` | `38.8%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `92` | `33.1%` |
| `Core 1: Macro Bear Veto` | `67` | `24.1%` |
| `Core 4: Funding Rate Cap` | `11` | `4.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*