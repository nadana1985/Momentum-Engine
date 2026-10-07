# Kronos V12: Institutional Symbol Tear Sheet — `AAVE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`20.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.761`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-11.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.89x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.16%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-44.1%`** | `< -30%` | ⚠️ High Drawdown |
| **Average Trade Duration** | **`110.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+8.7% / -7.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2022-11-04 07:00` | `2022-11-06 07:00` | 48.0h | `$95.5683` | `$91.9496` | **-4.15%** | **-4.24%** | +2.8% | -7.2% | `fast_decay_cut` |
| 2 | Book 1 | `2023-01-11 23:00` | `2023-02-01 23:00` | 504.0h | `$64.3204` | `$88.1990` | **+44.41%** | **+36.75%** | +42.0% | -2.7% | `time_cap` |
| 3 | Book 2 | `2023-05-05 16:00` | `2023-05-07 04:00` | 36.0h | `$73.6938` | `$69.3662` | **-5.87%** | **-6.05%** | +0.8% | -7.2% | `stall_bailout` |
| 4 | Book 2 | `2023-09-20 20:00` | `2023-09-22 08:00` | 36.0h | `$65.8141` | `$63.5807` | **-3.39%** | **-3.45%** | +0.4% | -6.3% | `stall_bailout` |
| 5 | Book 2 | `2023-10-01 10:00` | `2023-10-04 00:00` | 62.0h | `$69.8743` | `$64.1236` | **-8.23%** | **-8.59%** | +3.6% | -9.9% | `initial_stop` |
| 6 | Book 2 | `2023-11-06 23:00` | `2023-11-09 16:00` | 65.0h | `$100.5808` | `$92.3030` | **-8.23%** | **-8.59%** | +9.4% | -8.5% | `initial_stop` |
| 7 | Book 1 | `2023-11-13 00:00` | `2023-11-14 00:00` | 24.0h | `$103.5382` | `$91.5406` | **-6.90%** | **-7.15%** | +1.2% | -12.3% | `initial_stop` |
| 8 | Book 2 | `2024-09-22 02:00` | `2024-09-28 21:00` | 163.0h | `$160.9413` | `$161.3417` | **+0.25%** | **+0.25%** | +15.1% | -4.3% | `breakeven_ratchet` |
| 9 | Book 2 | `2024-10-14 03:00` | `2024-10-17 03:00` | 72.0h | `$159.5779` | `$156.5177` | **-1.92%** | **-1.94%** | +4.0% | -4.3% | `stagnation_cut` |
| 10 | Book 2 | `2025-08-12 16:00` | `2025-08-16 12:00` | 92.0h | `$315.5669` | `$289.5958` | **-8.23%** | **-8.59%** | +7.9% | -8.1% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `4` | `0.0%` | **`-32.9%`** |
| `stall_bailout` | `2` | `0.0%` | **`-9.5%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-4.2%`** |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `stagnation_cut` | `1` | `0.0%` | **`-1.9%`** |
| `time_cap` | `1` | `100.0%` | **`+36.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `AAVE`

* **Total Candidate Breakouts Filtered (Vetoed):** `244`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `155` (63.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `33`
* **Saved Capital Losses Avoided:** `+2,107.6%`
* **Missed Upside Forgone:** `-1,105.2%`
* **Net Veto Alpha:** `+1,002.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `95` | `38.9%` |
| `Core 1: Macro Bear Veto` | `94` | `38.5%` |
| `Core 4: Defensible Whale Dump` | `22` | `9.0%` |
| `Core 4: Funding Rate Cap` | `21` | `8.6%` |
| `Core 4: Whale Firewall` | `12` | `4.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*