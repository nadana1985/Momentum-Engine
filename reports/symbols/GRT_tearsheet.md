# Kronos V12: Institutional Symbol Tear Sheet — `GRT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`92.590`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+45.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.58x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+11.45%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-0.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`106.8h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.4% / -3.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-11-03 04:00` | `2022-11-07 07:00` | 99.0h | `$0.0888` | `$0.0891` | **+0.25%** | **+0.25%** | +17.6% | -3.9% | `breakeven_ratchet` |
| 2 | Book 2 | `2023-10-23 22:00` | `2023-10-30 22:00` | 168.0h | `$0.0908` | `$0.1092` | **+20.32%** | **+18.50%** | +22.3% | -2.8% | `time_cap` |
| 3 | Book 2 | `2026-05-06 01:00` | `2026-05-08 01:00` | 48.0h | `$0.0261` | `$0.0259` | **-0.50%** | **-0.50%** | +2.3% | -2.2% | `fast_decay_cut` |
| 4 | Book 2 | `2026-09-18 20:00` | `2026-09-23 12:00` | 112.0h | `$0.0205` | `$0.0270` | **+31.71%** | **+27.54%** | +35.6% | -2.9% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+27.5%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.5%`** |
| `time_cap` | `1` | `100.0%` | **`+18.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `GRT`

* **Total Candidate Breakouts Filtered (Vetoed):** `230`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `135` (58.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `27`
* **Saved Capital Losses Avoided:** `+1,660.2%`
* **Missed Upside Forgone:** `-1,401.4%`
* **Net Veto Alpha:** `+258.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `104` | `45.2%` |
| `Core 1: Macro Bear Veto` | `66` | `28.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `55` | `23.9%` |
| `Core 4: Funding Rate Cap` | `4` | `1.7%` |
| `Core 4: Whale Firewall` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*