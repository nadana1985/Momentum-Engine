# Kronos V12: Institutional Symbol Tear Sheet — `WIF`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `11` (`11` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `11` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`72.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.692`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+44.9%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.57x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+4.08%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-9.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`47.2h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+13.3% / -6.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-03-01 15:00` | `2024-03-01 17:00` | 2.0h | `$0.9601` | `$1.0436` | **+8.70%** | **+8.34%** | +14.0% | -1.8% | `target_reclaim` |
| 2 | Book 3 | `2024-03-05 15:00` | `2024-03-05 16:00` | 1.0h | `$1.2547` | `$1.3810` | **+10.07%** | **+9.59%** | +16.2% | -5.2% | `target_reclaim` |
| 3 | Book 3 | `2024-03-08 15:00` | `2024-03-08 17:00` | 2.0h | `$2.0991` | `$2.3213` | **+10.58%** | **+10.06%** | +12.8% | -4.7% | `target_reclaim` |
| 4 | Book 3 | `2024-03-10 22:00` | `2024-03-12 04:00` | 30.0h | `$2.1274` | `$1.9523` | **-8.23%** | **-8.59%** | +7.5% | -8.6% | `stop_loss` |
| 5 | Book 3 | `2024-03-16 05:00` | `2024-03-16 11:00` | 6.0h | `$2.5229` | `$2.7423` | **+8.70%** | **+8.34%** | +9.0% | -4.4% | `target_reclaim` |
| 6 | Book 3 | `2024-10-09 20:00` | `2024-10-11 15:00` | 43.0h | `$2.3146` | `$2.6804` | **+15.80%** | **+14.67%** | +17.2% | -4.3% | `target_reclaim` |
| 7 | Book 3 | `2024-10-15 15:00` | `2024-10-18 15:00` | 72.0h | `$2.5816` | `$2.6433` | **+2.39%** | **+2.36%** | +6.4% | -5.4% | `time_expiry` |
| 8 | Book 3 | `2024-11-13 19:00` | `2024-11-14 15:00` | 20.0h | `$4.1497` | `$3.8081` | **-8.23%** | **-8.59%** | +16.9% | -8.9% | `stop_loss` |
| 9 | Book 4 | `2025-07-14 03:00` | `2025-07-20 15:00` | 156.0h | `$1.0473` | `$1.2567` | **+11.58%** | **+11.05%** | +22.2% | -8.2% | `target_reclaim` |
| 10 | Book 2 | `2026-05-06 01:00` | `2026-05-13 01:00` | 168.0h | `$0.2110` | `$0.2235` | **+7.23%** | **+7.03%** | +20.8% | -4.7% | `time_cap` |
| 11 | Book 4 | `2026-08-25 02:00` | `2026-08-25 21:00` | 19.0h | `$0.2254` | `$0.1916` | **-8.64%** | **-9.36%** | +2.9% | -15.8% | `structural_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `6` | `100.0%` | **`+62.1%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-9.4%`** |
| `time_cap` | `1` | `100.0%` | **`+7.0%`** |
| `time_expiry` | `1` | `100.0%` | **`+2.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `WIF`

* **Total Candidate Breakouts Filtered (Vetoed):** `53`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `39` (73.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `19`
* **Saved Capital Losses Avoided:** `+789.1%`
* **Missed Upside Forgone:** `-1,056.8%`
* **Net Veto Alpha:** `+-267.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `26` | `49.1%` |
| `Core 4: Funding Rate Cap` | `15` | `28.3%` |
| `Core 4: Defensible Whale Dump` | `8` | `15.1%` |
| `Core 4: Whale Firewall` | `3` | `5.7%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `1.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*