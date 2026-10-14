# Kronos V12: Institutional Symbol Tear Sheet — `NOT`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `7` (`7` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `7` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`42.9%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.026`** | `> 1.50` | 🟢 Viable |
| **Cumulative Net Log Return** | **`+0.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.01x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+0.11%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`32.6h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.4% / -5.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2024-11-14 14:00` | `2024-11-17 14:00` | 72.0h | `$0.0076` | `$0.0074` | **-3.38%** | **-3.44%** | +7.0% | -7.8% | `time_expiry` |
| 2 | Book 3 | `2024-11-24 18:00` | `2024-11-26 18:00` | 48.0h | `$0.0087` | `$0.0080` | **-8.23%** | **-8.59%** | +10.2% | -8.7% | `stop_loss` |
| 3 | Book 3 | `2025-05-15 06:00` | `2025-05-15 23:00` | 17.0h | `$0.0030` | `$0.0028` | **-8.23%** | **-8.59%** | +2.6% | -8.3% | `stop_loss` |
| 4 | Book 3 | `2025-07-19 00:00` | `2025-07-19 04:00` | 4.0h | `$0.0022` | `$0.0023` | **+4.81%** | **+4.70%** | +5.5% | -1.5% | `target_reclaim` |
| 5 | Book 3 | `2026-08-22 05:00` | `2026-08-22 06:00` | 1.0h | `$0.0004` | `$0.0005` | **+18.00%** | **+16.55%** | +30.4% | -0.2% | `climax_whale_euphoria_harvest` |
| 6 | Book 3 | `2026-09-01 07:00` | `2026-09-01 21:00` | 14.0h | `$0.0005` | `$0.0004` | **-8.23%** | **-8.59%** | +0.6% | -8.1% | `stop_loss` |
| 7 | Book 3 | `2026-09-23 15:00` | `2026-09-26 15:00` | 72.0h | `$0.0005` | `$0.0005` | **+9.10%** | **+8.71%** | +9.7% | -1.9% | `time_expiry` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |
| `time_expiry` | `2` | `50.0%` | **`+5.3%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+16.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+4.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `NOT`

* **Total Candidate Breakouts Filtered (Vetoed):** `112`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `82` (73.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `20`
* **Saved Capital Losses Avoided:** `+1,152.9%`
* **Missed Upside Forgone:** `-1,201.0%`
* **Net Veto Alpha:** `+-48.1%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `53` | `47.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `47` | `42.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `11` | `9.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `1` | `0.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*