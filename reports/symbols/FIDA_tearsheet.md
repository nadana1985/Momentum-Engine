# Kronos V12: Institutional Symbol Tear Sheet — `FIDA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `5` (`5` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `5` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`60.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.340`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+5.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.17%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`12.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.9% / -4.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-12-05 01:00` | `2024-12-05 23:00` | 22.0h | `$0.3424` | `$0.3770` | **+10.12%** | **+9.64%** | +10.3% | -0.7% | `target_reclaim` |
| 2 | Book 3 | `2025-01-19 14:00` | `2025-01-19 22:00` | 8.0h | `$0.2585` | `$0.2373` | **-8.23%** | **-8.59%** | +5.6% | -8.4% | `stop_loss` |
| 3 | Book 3 | `2025-05-13 03:00` | `2025-05-13 09:00` | 6.0h | `$0.0956` | `$0.1031` | **+7.84%** | **+7.55%** | +9.7% | -0.7% | `target_reclaim` |
| 4 | Book 3 | `2025-07-04 07:00` | `2025-07-05 02:00` | 19.0h | `$0.0791` | `$0.0839` | **+6.01%** | **+5.83%** | +7.4% | -4.2% | `target_reclaim` |
| 5 | Book 3 | `2026-09-06 21:00` | `2026-09-07 05:00` | 8.0h | `$0.0220` | `$0.0202` | **-8.23%** | **-8.59%** | +6.5% | -8.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `3` | `100.0%` | **`+23.0%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `FIDA`

* **Total Candidate Breakouts Filtered (Vetoed):** `452`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `288` (63.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `105`
* **Saved Capital Losses Avoided:** `+5,945.2%`
* **Missed Upside Forgone:** `-3,074.0%`
* **Net Veto Alpha:** `+2,871.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `296` | `65.5%` |
| `Core 1: Macro Bear Veto` | `155` | `34.3%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*