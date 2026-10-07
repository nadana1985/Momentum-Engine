# Kronos V12: Institutional Symbol Tear Sheet — `TRUTH`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`2` Closed, `1` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.907`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+5.5%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.06x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.73%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-2.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`53.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.4% / -5.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-09-10 10:00` | `2026-09-11 21:00` | 35.0h | `$0.0128` | `$0.0139` | **+8.70%** | **+8.34%** | +10.7% | -4.7% | `target_reclaim` |
| 2 | Book 3 | `2026-09-16 08:00` | `2026-09-19 08:00` | 72.0h | `$0.0136` | `$0.0133` | **-2.83%** | **-2.87%** | +2.1% | -5.6% | `time_expiry` |
| 3 | Book 3 | `2026-10-04 10:00` | `_Open Live_` | 64.7h | `$0.0141` | `$0.0147` | **+4.45%** | **+4.36%** | +6.6% | -1.9% | `open_at_end` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |
| `time_expiry` | `1` | `0.0%` | **`-2.9%`** |

---

## 4. Counterfactual Risk Gate Audit for `TRUTH`

* **Total Candidate Breakouts Filtered (Vetoed):** `37`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `29` (78.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `18`
* **Saved Capital Losses Avoided:** `+630.7%`
* **Missed Upside Forgone:** `-1,169.3%`
* **Net Veto Alpha:** `+-538.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `33` | `89.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `10.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*