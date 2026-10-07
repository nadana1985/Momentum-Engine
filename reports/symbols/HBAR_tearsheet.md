# Kronos V12: Institutional Symbol Tear Sheet — `HBAR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`42.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.261`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+43.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.54x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+6.16%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-19.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`115.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.3% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2023-01-09 14:00` | `2023-01-16 14:00` | 168.0h | `$0.0446` | `$0.0520` | **+16.53%** | **+15.30%** | +22.6% | -3.3% | `time_cap` |
| 2 | Book 2 | `2023-04-26 08:00` | `2023-04-26 20:00` | 12.0h | `$0.0622` | `$0.0582` | **-6.45%** | **-6.66%** | +1.9% | -6.7% | `initial_stop` |
| 3 | Book 2 | `2023-07-20 01:00` | `2023-07-22 01:00` | 48.0h | `$0.0593` | `$0.0544` | **-6.51%** | **-6.73%** | +4.1% | -8.0% | `initial_stop` |
| 4 | Book 1 | `2023-11-17 06:00` | `2023-11-19 06:00` | 48.0h | `$0.0662` | `$0.0614` | **-5.11%** | **-5.25%** | +3.3% | -10.0% | `fast_decay_cut` |
| 5 | Book 1 | `2024-09-26 18:00` | `2024-09-29 18:00` | 72.0h | `$0.0621` | `$0.0618` | **-0.45%** | **-0.45%** | +2.8% | -3.9% | `stagnation_bailout` |
| 6 | Book 1 | `2025-07-10 02:00` | `2025-07-25 12:00` | 370.0h | `$0.1749` | `$0.2496` | **+59.49%** | **+46.68%** | +70.8% | -1.5% | `climax_top_harvest` |
| 7 | Book 2 | `2026-09-20 14:00` | `2026-09-24 09:00` | 91.0h | `$0.0877` | `$0.0879` | **+0.25%** | **+0.25%** | +15.6% | -3.8% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-13.4%`** |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+46.7%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-5.2%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-0.5%`** |
| `time_cap` | `1` | `100.0%` | **`+15.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `HBAR`

* **Total Candidate Breakouts Filtered (Vetoed):** `109`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `84` (77.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `13`
* **Saved Capital Losses Avoided:** `+1,235.2%`
* **Missed Upside Forgone:** `-381.3%`
* **Net Veto Alpha:** `+854.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `55` | `50.5%` |
| `Core 0: Zero-Tolerance Data Firewall` | `39` | `35.8%` |
| `Core 4: Funding Rate Cap` | `14` | `12.8%` |
| `Core 4: Whale Firewall` | `1` | `0.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*