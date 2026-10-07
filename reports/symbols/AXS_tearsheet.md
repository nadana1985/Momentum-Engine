# Kronos V12: Institutional Symbol Tear Sheet — `AXS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `10` (`10` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `10` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.142`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+3.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.32%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-11.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`95.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.2% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-04-02 00:00` | `2022-04-02 18:00` | 18.0h | `$71.2276` | `$65.3656` | **-8.23%** | **-8.59%** | +5.9% | -10.5% | `initial_stop` |
| 2 | Book 1 | `2023-01-13 03:00` | `2023-01-18 15:00` | 132.0h | `$8.1583` | `$8.1786` | **+0.23%** | **+0.23%** | +25.6% | -4.5% | `breakeven_ratchet` |
| 3 | Book 2 | `2023-02-15 20:00` | `2023-02-17 21:00` | 49.0h | `$10.6185` | `$10.5555` | **-0.59%** | **-0.59%** | +5.1% | -5.3% | `fast_decay_cut` |
| 4 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$8.1573` | `$9.0094` | **+10.45%** | **+9.94%** | +20.3% | -6.9% | `time_cap` |
| 5 | Book 2 | `2023-04-07 04:00` | `2023-04-08 16:00` | 36.0h | `$8.8330` | `$8.5955` | **-2.69%** | **-2.73%** | +0.9% | -4.4% | `stall_bailout` |
| 6 | Book 2 | `2023-04-26 12:00` | `2023-04-26 19:00` | 7.0h | `$8.3007` | `$7.6176` | **-8.23%** | **-8.59%** | +-0.0% | -9.6% | `initial_stop` |
| 7 | Book 2 | `2023-07-13 15:00` | `2023-07-20 15:00` | 168.0h | `$6.3438` | `$6.3900` | **+0.73%** | **+0.73%** | +8.6% | -3.5% | `time_cap` |
| 8 | Book 2 | `2023-10-21 14:00` | `2023-10-28 14:00` | 168.0h | `$4.3899` | `$4.8050` | **+9.45%** | **+9.03%** | +13.3% | -1.4% | `time_cap` |
| 9 | Book 2 | `2024-09-13 16:00` | `2024-09-15 04:00` | 36.0h | `$4.8100` | `$4.7202` | **-1.87%** | **-1.89%** | +0.9% | -2.7% | `stall_bailout` |
| 10 | Book 2 | `2025-04-22 17:00` | `2025-04-29 17:00` | 168.0h | `$2.4210` | `$2.5616` | **+5.81%** | **+5.64%** | +11.4% | -1.2% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_cap` | `4` | `100.0%` | **`+25.3%`** |
| `stall_bailout` | `2` | `0.0%` | **`-4.6%`** |
| `initial_stop` | `2` | `0.0%` | **`-17.2%`** |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `AXS`

* **Total Candidate Breakouts Filtered (Vetoed):** `275`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `148` (53.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `103`
* **Saved Capital Losses Avoided:** `+2,116.6%`
* **Missed Upside Forgone:** `-3,955.6%`
* **Net Veto Alpha:** `+-1,838.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `110` | `40.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `87` | `31.6%` |
| `Core 1: Macro Bear Veto` | `76` | `27.6%` |
| `Core 4: Funding Rate Cap` | `2` | `0.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*