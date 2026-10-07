# Kronos V12: Institutional Symbol Tear Sheet — `QNT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `6` (`6` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `6` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.968`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.10%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-13.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`72.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.9% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-12-14 17:00` | `2022-12-16 05:00` | 36.0h | `$127.1972` | `$119.9793` | **-5.67%** | **-5.84%** | +0.1% | -6.6% | `stall_bailout` |
| 2 | Book 2 | `2023-01-16 20:00` | `2023-01-18 16:00` | 44.0h | `$143.1670` | `$131.3844` | **-8.23%** | **-8.59%** | +3.2% | -9.4% | `initial_stop` |
| 3 | Book 1 | `2023-01-20 18:00` | `2023-01-22 20:00` | 50.0h | `$144.0994` | `$137.7049` | **-4.44%** | **-4.54%** | +3.1% | -4.9% | `fast_decay_cut` |
| 4 | Book 2 | `2023-10-21 14:00` | `2023-10-28 14:00` | 168.0h | `$87.8491` | `$105.9046` | **+20.55%** | **+18.69%** | +25.3% | -1.0% | `time_cap` |
| 5 | Book 1 | `2023-12-24 20:00` | `2023-12-29 00:00` | 100.0h | `$133.8337` | `$134.1667` | **+0.15%** | **+0.15%** | +15.2% | -6.8% | `breakeven_ratchet` |
| 6 | Book 2 | `2025-04-20 20:00` | `2025-04-22 08:00` | 36.0h | `$67.4382` | `$67.1118` | **-0.48%** | **-0.49%** | +0.7% | -3.2% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stall_bailout` | `2` | `0.0%` | **`-6.3%`** |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.1%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-4.5%`** |
| `initial_stop` | `1` | `0.0%` | **`-8.6%`** |
| `time_cap` | `1` | `100.0%` | **`+18.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `QNT`

* **Total Candidate Breakouts Filtered (Vetoed):** `169`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `109` (64.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+1,099.6%`
* **Missed Upside Forgone:** `-714.2%`
* **Net Veto Alpha:** `+385.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `84` | `49.7%` |
| `Core 1: Macro Bear Veto` | `74` | `43.8%` |
| `Core 4: Whale Firewall` | `5` | `3.0%` |
| `Core 0: Zero-Tolerance Data Firewall` | `3` | `1.8%` |
| `Core 4: Funding Rate Cap` | `3` | `1.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*