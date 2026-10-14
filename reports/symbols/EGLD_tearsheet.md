# Kronos V12: Institutional Symbol Tear Sheet — `EGLD`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`7.449`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+53.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.70x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+13.27%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`80.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.8% / -6.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-02-08 01:00` | `2023-02-09 13:00` | 36.0h | `$48.0899` | `$45.3862` | **-6.35%** | **-6.58%** | +0.4% | -8.5% | `fast_decay_cut` |
| 2 | Book 4 | `2023-11-01 20:00` | `2023-11-05 00:00` | 76.0h | `$32.0680` | `$38.4816` | **+31.71%** | **+28.14%** | +35.6% | -1.5% | `target_reclaim` |
| 3 | Book 4 | `2024-11-16 23:00` | `2024-11-24 03:00` | 172.0h | `$31.9108` | `$38.2930` | **+38.23%** | **+33.19%** | +22.9% | -12.6% | `target_reclaim` |
| 4 | Book 1 | `2026-08-23 15:00` | `2026-08-25 03:00` | 36.0h | `$3.5599` | `$3.5112` | **-1.64%** | **-1.66%** | +4.4% | -4.2% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-8.2%`** |
| `target_reclaim` | `2` | `100.0%` | **`+61.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `EGLD`

* **Total Candidate Breakouts Filtered (Vetoed):** `801`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `272` (34.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `265`
* **Saved Capital Losses Avoided:** `+3,353.5%`
* **Missed Upside Forgone:** `-9,312.3%`
* **Net Veto Alpha:** `+-5,958.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `533` | `66.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `192` | `24.0%` |
| `Core 1: Macro Bear Veto` | `68` | `8.5%` |
| `Core 4: Funding Rate Cap` | `8` | `1.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*