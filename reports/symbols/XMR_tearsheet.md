# Kronos V12: Institutional Symbol Tear Sheet — `XMR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`71.4%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`15.553`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+54.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.72x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+7.78%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-3.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`222.1h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+11.7% / -3.4%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2021-07-28 23:00` | `2021-08-16 09:00` | 442.0h | `$235.7130` | `$282.8556` | **+32.02%** | **+28.38%** | +21.2% | -5.4% | `target_reclaim` |
| 2 | Book 4 | `2022-03-26 12:00` | `2022-04-12 08:00` | 404.0h | `$207.0000` | `$244.2600` | **+9.41%** | **+8.65%** | +21.6% | -1.3% | `climax_whale_euphoria_harvest` |
| 3 | Book 3 | `2023-12-29 12:00` | `2023-12-31 00:00` | 36.0h | `$171.4540` | `$165.9840` | **-3.19%** | **-3.24%** | +0.7% | -5.4% | `stall_bailout` |
| 4 | Book 4 | `2024-05-23 19:00` | `2024-05-30 19:00` | 168.0h | `$141.0212` | `$145.3616` | **+4.64%** | **+4.56%** | +3.8% | -2.6% | `stagnation_cut` |
| 5 | Book 1 | `2024-06-10 18:00` | `2024-06-13 18:00` | 72.0h | `$177.6029` | `$176.9066` | **-0.50%** | **-0.50%** | +3.0% | -5.7% | `stagnation_bailout` |
| 6 | Book 3 | `2025-01-19 22:00` | `2025-01-22 22:00` | 72.0h | `$201.0189` | `$221.7343` | **+10.31%** | **+9.81%** | +11.4% | -2.8% | `time_expiry` |
| 7 | Book 4 | `2026-04-21 09:00` | `2026-05-06 10:00` | 361.0h | `$364.7563` | `$437.7076` | **+7.01%** | **+6.81%** | +20.3% | -0.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+35.2%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+8.7%`** |
| `stagnation_bailout` | `1` | `0.0%` | **`-0.5%`** |
| `stagnation_cut` | `1` | `100.0%` | **`+4.6%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.2%`** |
| `time_expiry` | `1` | `100.0%` | **`+9.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `XMR`

* **Total Candidate Breakouts Filtered (Vetoed):** `869`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `461` (53.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `28`
* **Saved Capital Losses Avoided:** `+3,756.2%`
* **Missed Upside Forgone:** `-922.3%`
* **Net Veto Alpha:** `+2,833.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `567` | `65.2%` |
| `Core 0: Zero-Tolerance Data Firewall` | `229` | `26.4%` |
| `Core 4: Defensible Whale Dump` | `40` | `4.6%` |
| `Core 4: Funding Rate Cap` | `22` | `2.5%` |
| `Core 4: Whale Firewall` | `7` | `0.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `4` | `0.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*