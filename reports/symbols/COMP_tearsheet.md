# Kronos V12: Institutional Symbol Tear Sheet — `COMP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `9` (`9` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `9` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.923`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+44.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.57x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.99%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-20.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`160.9h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+12.2% / -9.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-12-27 09:00` | `2022-12-28 21:00` | 36.0h | `$33.2930` | `$31.9001` | **-5.15%** | **-5.26%** | +0.5% | -4.6% | `stall_bailout` |
| 2 | Book 1 | `2023-01-09 14:00` | `2023-01-11 02:00` | 36.0h | `$37.0023` | `$35.7404` | **-5.38%** | **-5.52%** | +0.1% | -6.3% | `fast_decay_cut` |
| 3 | Book 4 | `2023-01-27 16:00` | `2023-02-09 22:00` | 318.0h | `$57.2357` | `$48.6504` | **-13.89%** | **-15.06%** | +8.0% | -16.8% | `structural_stop` |
| 4 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$43.1877` | `$45.6955` | **+6.49%** | **+6.31%** | +12.5% | -5.6% | `time_cap` |
| 5 | Book 4 | `2023-06-27 13:00` | `2023-06-29 13:00` | 48.0h | `$42.5437` | `$51.0525` | **+26.12%** | **+23.63%** | +24.3% | -9.3% | `target_reclaim` |
| 6 | Book 1 | `2023-12-25 05:00` | `2023-12-26 17:00` | 36.0h | `$59.5084` | `$58.6829` | **-2.66%** | **-2.69%** | +3.5% | -6.2% | `fast_decay_cut` |
| 7 | Book 4 | `2024-05-24 00:00` | `2024-06-07 18:00` | 354.0h | `$60.3103` | `$54.6379` | **-11.41%** | **-11.99%** | +9.3% | -16.6% | `structural_stop` |
| 8 | Book 4 | `2024-11-16 02:00` | `2024-11-22 23:00` | 165.0h | `$48.9734` | `$58.7680` | **+84.05%** | **+63.70%** | +34.1% | -0.5% | `target_reclaim` |
| 9 | Book 4 | `2025-06-09 22:00` | `2025-06-21 21:00` | 287.0h | `$53.2998` | `$45.3049` | **-7.55%** | **-8.18%** | +17.9% | -15.5% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `structural_stop` | `3` | `0.0%` | **`-35.2%`** |
| `fast_decay_cut` | `2` | `0.0%` | **`-8.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+87.3%`** |
| `stall_bailout` | `1` | `0.0%` | **`-5.3%`** |
| `time_cap` | `1` | `100.0%` | **`+6.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `COMP`

* **Total Candidate Breakouts Filtered (Vetoed):** `1584`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `1128` (71.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `144`
* **Saved Capital Losses Avoided:** `+12,898.8%`
* **Missed Upside Forgone:** `-4,530.6%`
* **Net Veto Alpha:** `+8,368.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `742` | `46.8%` |
| `Core 0: Zero-Tolerance Data Firewall` | `655` | `41.4%` |
| `Core 1: Macro Bear Veto` | `167` | `10.5%` |
| `Core 4: Defensible Whale Dump` | `14` | `0.9%` |
| `Core 4: Funding Rate Cap` | `4` | `0.3%` |
| `Core 4: Whale Firewall` | `2` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*