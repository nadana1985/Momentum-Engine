# Kronos V12: Institutional Symbol Tear Sheet — `RUNE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`14.642`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+43.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.55x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+8.77%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`194.4h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+17.8% / -4.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-04-14 05:00` | `2023-04-15 17:00` | 36.0h | `$1.6922` | `$1.6748` | **-1.50%** | **-1.51%** | +0.3% | -4.3% | `stall_bailout` |
| 2 | Book 1 | `2023-07-01 23:00` | `2023-07-04 23:00` | 72.0h | `$1.0677` | `$1.0534` | **-1.69%** | **-1.70%** | +3.7% | -2.3% | `stagnation_bailout` |
| 3 | Book 1 | `2025-04-21 08:00` | `2025-05-03 07:00` | 287.0h | `$1.2501` | `$1.2808` | **+3.60%** | **+3.54%** | +18.5% | -3.7% | `trail_stop` |
| 4 | Book 1 | `2026-05-05 08:00` | `2026-05-15 09:00` | 241.0h | `$0.5512` | `$0.5570` | **+1.36%** | **+1.35%** | +15.6% | -9.7% | `breakeven_ratchet` |
| 5 | Book 1 | `2026-09-20 15:00` | `2026-10-04 15:00` | 336.0h | `$0.5604` | `$0.8031` | **+52.47%** | **+42.18%** | +51.0% | -2.8% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+1.4%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-1.7%`** |
| `stall_bailout` | `1` | `0.0%` | **`-1.5%`** |
| `time_cap` | `1` | `100.0%` | **`+42.2%`** |
| `trail_stop` | `1` | `100.0%` | **`+3.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `RUNE`

* **Total Candidate Breakouts Filtered (Vetoed):** `400`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `203` (50.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `60`
* **Saved Capital Losses Avoided:** `+2,567.9%`
* **Missed Upside Forgone:** `-1,755.3%`
* **Net Veto Alpha:** `+812.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `142` | `35.5%` |
| `Core 1: Macro Bear Veto` | `126` | `31.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `97` | `24.2%` |
| `Core 4: Defensible Whale Dump` | `21` | `5.2%` |
| `Core 4: Whale Firewall` | `8` | `2.0%` |
| `Core 4: Funding Rate Cap` | `6` | `1.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*