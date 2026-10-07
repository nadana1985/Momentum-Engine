# Kronos V12: Institutional Symbol Tear Sheet — `COTI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`16.7%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.544`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.4%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.73%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-5.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`73.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.3% / -4.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 11:00` | `2022-10-28 02:00` | 63.0h | `$0.1029` | `$0.1015` | **-1.33%** | **-1.34%** | +4.6% | -1.6% | `fast_decay_cut` |
| 2 | Book 2 | `2022-12-26 10:00` | `2022-12-28 05:00` | 43.0h | `$0.0589` | `$0.0568` | **-3.49%** | **-3.55%** | +1.7% | -4.0% | `initial_stop` |
| 3 | Book 1 | `2023-01-13 19:00` | `2023-01-18 16:00` | 117.0h | `$0.0697` | `$0.0685` | **-1.68%** | **-1.69%** | +11.1% | -7.1% | `fast_decay_cut` |
| 4 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$0.0723` | `$0.0762` | **+5.38%** | **+5.24%** | +14.8% | -4.9% | `time_cap` |
| 5 | Book 1 | `2023-11-04 05:00` | `2023-11-05 21:00` | 40.0h | `$0.0505` | `$0.0499` | **-1.10%** | **-1.11%** | +1.9% | -2.7% | `fast_decay_cut` |
| 6 | Book 2 | `2026-08-21 12:00` | `2026-08-21 19:00` | 7.0h | `$0.0108` | `$0.0106` | **-1.93%** | **-1.94%** | +15.9% | -4.9% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `3` | `0.0%` | **`-4.1%`** |
| `breakeven_ratchet` | `1` | `0.0%` | **`-1.9%`** |
| `initial_stop` | `1` | `0.0%` | **`-3.5%`** |
| `time_cap` | `1` | `100.0%` | **`+5.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `COTI`

* **Total Candidate Breakouts Filtered (Vetoed):** `189`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `122` (64.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `29`
* **Saved Capital Losses Avoided:** `+1,741.1%`
* **Missed Upside Forgone:** `-1,253.6%`
* **Net Veto Alpha:** `+487.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `68` | `36.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `57` | `30.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `53` | `28.0%` |
| `Core 4: Funding Rate Cap` | `9` | `4.8%` |
| `Core 4: Defensible Whale Dump` | `2` | `1.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*