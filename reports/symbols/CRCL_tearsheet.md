# Kronos V12: Institutional Symbol Tear Sheet — `CRCL`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.578`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-9.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.91x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.28%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-11.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`73.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.3% / -7.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-05-05 01:00` | `2026-05-08 01:00` | 72.0h | `$125.5230` | `$113.5853` | **-9.51%** | **-9.99%** | +3.7% | -12.6% | `stagnation_cut` |
| 2 | Book 2 | `2026-08-20 08:00` | `2026-08-27 08:00` | 168.0h | `$83.1774` | `$91.6104` | **+13.35%** | **+12.53%** | +12.4% | -4.2% | `time_cap` |
| 3 | Book 2 | `2026-09-14 19:00` | `2026-09-15 13:00` | 18.0h | `$97.7738` | `$89.7270` | **-8.23%** | **-8.59%** | +0.4% | -9.3% | `initial_stop` |
| 4 | Book 2 | `2026-09-18 14:00` | `2026-09-20 02:00` | 36.0h | `$92.4305` | `$89.6254` | **-3.03%** | **-3.08%** | +0.8% | -2.9% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-10.0%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.1%`** |
| `time_cap` | `1` | `100.0%` | **`+12.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `CRCL`

* **Total Candidate Breakouts Filtered (Vetoed):** `56`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `28` (50.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `4`
* **Saved Capital Losses Avoided:** `+216.0%`
* **Missed Upside Forgone:** `-100.0%`
* **Net Veto Alpha:** `+116.0%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `53` | `94.6%` |
| `Core 4: Funding Rate Cap` | `3` | `5.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*