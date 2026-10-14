# Kronos V12: Institutional Symbol Tear Sheet — `GRT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`57.1%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`5.254`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+95.4%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`2.60x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+13.62%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-2.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`161.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+19.6% / -5.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-08-13 00:00` | `2021-09-07 14:00` | 614.0h | `$0.9306` | `$0.7910` | **-18.12%** | **-19.64%** | +17.6% | -19.8% | `structural_stop` |
| 2 | Book 2 | `2022-11-03 04:00` | `2022-11-07 07:00` | 99.0h | `$0.0888` | `$0.0873` | **-2.15%** | **-2.17%** | +17.6% | -3.9% | `breakeven_ratchet` |
| 3 | Book 4 | `2023-02-04 23:00` | `2023-02-06 01:00` | 26.0h | `$0.1138` | `$0.1365` | **+37.53%** | **+32.66%** | +21.1% | -3.3% | `target_reclaim` |
| 4 | Book 2 | `2023-10-23 22:00` | `2023-10-30 22:00` | 168.0h | `$0.0908` | `$0.1092` | **+21.84%** | **+19.88%** | +22.3% | -2.8% | `time_cap` |
| 5 | Book 4 | `2024-11-15 22:00` | `2024-11-18 16:00` | 66.0h | `$0.1849` | `$0.2219` | **+41.05%** | **+35.30%** | +20.8% | -0.8% | `target_reclaim` |
| 6 | Book 2 | `2026-05-06 01:00` | `2026-05-08 01:00` | 48.0h | `$0.0261` | `$0.0259` | **-0.60%** | **-0.60%** | +2.3% | -2.2% | `fast_decay_cut` |
| 7 | Book 2 | `2026-09-18 20:00` | `2026-09-23 12:00` | 112.0h | `$0.0205` | `$0.0270` | **+34.47%** | **+29.94%** | +35.6% | -2.9% | `climax_top_harvest` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+68.0%`** |
| `breakeven_ratchet` | `1` | `0.0%` | **`-2.2%`** |
| `climax_top_harvest` | `1` | `100.0%` | **`+29.9%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.6%`** |
| `structural_stop` | `1` | `0.0%` | **`-19.6%`** |
| `time_cap` | `1` | `100.0%` | **`+19.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `GRT`

* **Total Candidate Breakouts Filtered (Vetoed):** `618`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `298` (48.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `114`
* **Saved Capital Losses Avoided:** `+3,504.8%`
* **Missed Upside Forgone:** `-3,423.5%`
* **Net Veto Alpha:** `+81.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `413` | `66.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `134` | `21.7%` |
| `Core 1: Macro Bear Veto` | `66` | `10.7%` |
| `Core 4: Funding Rate Cap` | `4` | `0.6%` |
| `Core 4: Whale Firewall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*