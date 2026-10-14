# Kronos V12: Institutional Symbol Tear Sheet — `SKHY`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.426`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+4.8%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.05x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.40%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-3.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.7% / -18.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2026-07-14 13:00` | `2026-07-18 13:00` | Live | `$156.6392` | `$169.9535` | **+8.50%** | **+8.16%** | +4.5% | -33.0% | `shelf_target_reclaim` |
| 2 | Book 2 | `2026-08-31 13:00` | `2026-09-02 01:00` | 36.0h | `$165.1418` | `$159.6898` | **-3.31%** | **-3.36%** | +0.8% | -4.0% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `stall_bailout` | `1` | `0.0%` | **`-3.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `SKHY`

* **Total Candidate Breakouts Filtered (Vetoed):** `24`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `7` (29.2% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+64.7%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+64.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `6` | `25.0%` |
| `Core 4: Defensible Whale Dump` | `5` | `20.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `5` | `20.8%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `4` | `16.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `16.7%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*