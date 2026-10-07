# Kronos V12: Institutional Symbol Tear Sheet — `ALICE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`15.835`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+8.3%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.09x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.17%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`112.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.7% / -3.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 17:00` | `2022-10-28 02:00` | 57.0h | `$1.6000` | `$1.5910` | **-0.56%** | **-0.56%** | +4.5% | -2.9% | `fast_decay_cut` |
| 2 | Book 2 | `2023-03-13 00:00` | `2023-03-20 00:00` | 168.0h | `$1.5037` | `$1.6439` | **+9.32%** | **+8.91%** | +17.0% | -4.8% | `time_cap` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.6%`** |
| `time_cap` | `1` | `100.0%` | **`+8.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `ALICE`

* **Total Candidate Breakouts Filtered (Vetoed):** `213`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `120` (56.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `43`
* **Saved Capital Losses Avoided:** `+2,107.4%`
* **Missed Upside Forgone:** `-1,603.3%`
* **Net Veto Alpha:** `+504.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `71` | `33.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `44` | `20.7%` |
| `Core 0: Zero-Tolerance Data Firewall` | `38` | `17.8%` |
| `Core 1: Macro Bear Veto` | `36` | `16.9%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `24` | `11.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*