# Kronos V12: Institutional Symbol Tear Sheet — `QNT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`42.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`3.266`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+27.6%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.32x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+3.94%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-4.8%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`76.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.2% / -4.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-12-14 17:00` | `2022-12-16 05:00` | 36.0h | `$127.1972` | `$119.9793` | **-6.28%** | **-6.47%** | +0.1% | -6.6% | `stall_bailout` |
| 2 | Book 1 | `2023-01-20 18:00` | `2023-01-22 20:00` | 50.0h | `$144.0994` | `$137.7049` | **-4.70%** | **-4.82%** | +3.1% | -4.9% | `fast_decay_cut` |
| 3 | Book 2 | `2023-10-21 14:00` | `2023-10-28 14:00` | 168.0h | `$87.8491` | `$105.9046` | **+22.47%** | **+20.43%** | +25.3% | -1.0% | `time_cap` |
| 4 | Book 1 | `2023-12-24 20:00` | `2023-12-29 02:00` | 102.0h | `$133.8337` | `$133.4356` | **-0.34%** | **-0.34%** | +15.2% | -6.8% | `fast_decay_cut` |
| 5 | Book 4 | `2024-11-16 16:00` | `2024-11-16 17:00` | 1.0h | `$77.9267` | `$93.5121` | **+4.82%** | **+4.61%** | +20.6% | -3.4% | `target_reclaim` |
| 6 | Book 2 | `2025-04-20 20:00` | `2025-04-22 08:00` | 36.0h | `$67.4382` | `$67.1118` | **-0.55%** | **-0.55%** | +0.7% | -3.2% | `stall_bailout` |
| 7 | Book 4 | `2025-05-06 14:00` | `2025-05-12 13:00` | 143.0h | `$86.4695` | `$103.7634` | **+15.72%** | **+14.74%** | +20.3% | -3.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-5.2%`** |
| `stall_bailout` | `2` | `0.0%` | **`-7.0%`** |
| `target_reclaim` | `2` | `100.0%` | **`+19.4%`** |
| `time_cap` | `1` | `100.0%` | **`+20.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `QNT`

* **Total Candidate Breakouts Filtered (Vetoed):** `1007`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `451` (44.8% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `164`
* **Saved Capital Losses Avoided:** `+3,809.8%`
* **Missed Upside Forgone:** `-6,198.6%`
* **Net Veto Alpha:** `+-2,388.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `790` | `78.5%` |
| `Core 1: Macro Bear Veto` | `206` | `20.5%` |
| `Core 4: Whale Firewall` | `5` | `0.5%` |
| `Core 0: Zero-Tolerance Data Firewall` | `3` | `0.3%` |
| `Core 4: Funding Rate Cap` | `3` | `0.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*