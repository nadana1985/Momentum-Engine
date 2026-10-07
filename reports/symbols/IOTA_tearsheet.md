# Kronos V12: Institutional Symbol Tear Sheet — `IOTA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.539`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+4.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.05x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.11%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`92.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.8% / -3.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2022-03-28 05:00` | `2022-03-29 17:00` | 36.0h | `$0.9078` | `$0.8569` | **-7.02%** | **-7.27%** | +-0.2% | -7.6% | `fast_decay_cut` |
| 2 | Book 2 | `2022-10-25 17:00` | `2022-10-27 17:00` | 48.0h | `$0.2556` | `$0.2545` | **-0.46%** | **-0.46%** | +3.4% | -1.7% | `fast_decay_cut` |
| 3 | Book 2 | `2023-07-13 15:00` | `2023-07-18 11:00` | 116.0h | `$0.1869` | `$0.1859` | **-0.50%** | **-0.50%** | +5.3% | -4.1% | `fast_decay_cut` |
| 4 | Book 2 | `2025-04-22 19:00` | `2025-04-29 19:00` | 168.0h | `$0.1845` | `$0.2094` | **+13.51%** | **+12.67%** | +30.7% | -1.4% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `3` | `0.0%` | **`-8.2%`** |
| `time_cap` | `1` | `100.0%` | **`+12.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `IOTA`

* **Total Candidate Breakouts Filtered (Vetoed):** `296`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `167` (56.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `77`
* **Saved Capital Losses Avoided:** `+2,443.2%`
* **Missed Upside Forgone:** `-3,454.5%`
* **Net Veto Alpha:** `+-1,011.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `124` | `41.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `94` | `31.8%` |
| `Core 1: Macro Bear Veto` | `65` | `22.0%` |
| `Core 4: Funding Rate Cap` | `9` | `3.0%` |
| `Core 4: Defensible Whale Dump` | `3` | `1.0%` |
| `Core 4: Whale Firewall` | `1` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*