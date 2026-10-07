# Kronos V12: Institutional Symbol Tear Sheet — `IMX`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`85.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`76.476`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+91.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.51x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+13.13%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`121.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+22.9% / -2.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 19:00` | `2022-10-31 14:00` | 139.0h | `$0.5764` | `$0.5779` | **+0.25%** | **+0.25%** | +17.5% | -3.2% | `breakeven_ratchet` |
| 2 | Book 2 | `2023-07-13 16:00` | `2023-07-20 16:00` | 168.0h | `$0.7247` | `$0.7312` | **+0.89%** | **+0.89%** | +10.4% | -2.1% | `time_cap` |
| 3 | Book 2 | `2023-10-23 08:00` | `2023-10-30 08:00` | 168.0h | `$0.5957` | `$0.6748` | **+13.28%** | **+12.47%** | +15.8% | -1.9% | `time_cap` |
| 4 | Book 2 | `2023-11-03 05:00` | `2023-11-05 05:00` | 48.0h | `$0.7019` | `$0.9325` | **+32.86%** | **+28.41%** | +36.9% | -4.0% | `climax_top_harvest` |
| 5 | Book 2 | `2023-12-01 17:00` | `2023-12-04 18:00` | 73.0h | `$1.4017` | `$1.3847` | **-1.21%** | **-1.22%** | +6.8% | -3.9% | `fast_decay_cut` |
| 6 | Book 2 | `2023-12-07 22:00` | `2023-12-11 12:00` | 86.0h | `$1.5205` | `$1.9971` | **+31.35%** | **+27.27%** | +36.7% | -2.6% | `climax_top_harvest` |
| 7 | Book 2 | `2024-02-09 23:00` | `2024-02-16 23:00` | 168.0h | `$2.4734` | `$3.1394` | **+26.93%** | **+23.85%** | +36.6% | -1.1% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `3` | `100.0%` | **`+37.2%`** |
| `climax_top_harvest` | `2` | `100.0%` | **`+55.7%`** |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `IMX`

* **Total Candidate Breakouts Filtered (Vetoed):** `220`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `131` (59.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `22`
* **Saved Capital Losses Avoided:** `+1,461.0%`
* **Missed Upside Forgone:** `-576.7%`
* **Net Veto Alpha:** `+884.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `77` | `35.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `54` | `24.5%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `50` | `22.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `28` | `12.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `8` | `3.6%` |
| `Core 4: Defensible Whale Dump` | `3` | `1.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*