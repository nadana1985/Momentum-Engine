# Kronos V12: Institutional Symbol Tear Sheet — `TAKE`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.942`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+8.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.08x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.70%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`8.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.3% / -5.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-10-06 03:00` | `2025-10-06 17:00` | 14.0h | `$0.1978` | `$0.2150` | **+8.70%** | **+8.34%** | +14.1% | -3.0% | `target_reclaim` |
| 2 | Book 3 | `2026-09-04 14:00` | `2026-09-05 00:00` | 10.0h | `$0.0589` | `$0.0541` | **-8.23%** | **-8.59%** | +2.9% | -11.1% | `stop_loss` |
| 3 | Book 3 | `2026-09-23 15:00` | `2026-09-23 16:00` | 1.0h | `$0.0938` | `$0.1020` | **+8.70%** | **+8.34%** | +31.8% | -1.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `2` | `100.0%` | **`+16.7%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `TAKE`

* **Total Candidate Breakouts Filtered (Vetoed):** `43`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `35` (81.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `24`
* **Saved Capital Losses Avoided:** `+1,162.5%`
* **Missed Upside Forgone:** `-1,151.6%`
* **Net Veto Alpha:** `+10.9%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `34` | `79.1%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `3` | `7.0%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `7.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `3` | `7.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*