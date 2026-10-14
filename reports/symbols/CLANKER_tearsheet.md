# Kronos V12: Institutional Symbol Tear Sheet — `CLANKER`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`75.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`11.250`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+19.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.22x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.95%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-1.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`72.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+22.6% / -10.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-01-28 12:00` | `2026-02-01 12:00` | Live | `$33.5524` | `$36.4044` | **+8.50%** | **+8.16%** | +61.1% | -32.9% | `shelf_target_reclaim` |
| 2 | Book 3 | `2026-08-23 04:00` | `2026-08-26 04:00` | 72.0h | `$12.8749` | `$12.6283` | **-1.91%** | **-1.93%** | +7.3% | -4.6% | `time_expiry` |
| 3 | Book 3 | `2026-09-23 14:00` | `2026-09-26 14:00` | 72.0h | `$12.7371` | `$14.3141` | **+12.38%** | **+11.67%** | +16.3% | -0.9% | `time_expiry` |
| 4 | Book 3 | `2026-09-28 05:00` | `2026-10-01 05:00` | 72.0h | `$13.8857` | `$14.1545` | **+1.94%** | **+1.92%** | +5.6% | -4.1% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `time_expiry` | `3` | `66.7%` | **`+11.7%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `CLANKER`

* **Total Candidate Breakouts Filtered (Vetoed):** `16`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `16` (100.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `2`
* **Saved Capital Losses Avoided:** `+315.1%`
* **Missed Upside Forgone:** `-58.6%`
* **Net Veto Alpha:** `+256.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `9` | `56.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `5` | `31.2%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `12.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*