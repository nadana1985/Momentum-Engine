# Kronos V12: Institutional Symbol Tear Sheet — `FWDI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.485`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-8.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.95%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`11.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.2% / -6.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-28 15:00` | `2026-08-28 19:00` | 4.0h | `$6.3949` | `$5.8686` | **-8.23%** | **-8.59%** | +1.7% | -8.1% | `stop_loss` |
| 2 | Book 3 | `2026-09-15 13:00` | `2026-09-15 18:00` | 5.0h | `$6.6074` | `$6.0636` | **-8.23%** | **-8.59%** | +1.9% | -8.9% | `stop_loss` |
| 3 | Book 3 | `2026-09-24 09:00` | `2026-09-25 11:00` | 26.0h | `$7.9433` | `$8.6340` | **+8.70%** | **+8.34%** | +9.1% | -0.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `FWDI`

* **Total Candidate Breakouts Filtered (Vetoed):** `18`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `8` (44.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `1`
* **Saved Capital Losses Avoided:** `+107.2%`
* **Missed Upside Forgone:** `-28.6%`
* **Net Veto Alpha:** `+78.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `8` | `44.4%` |
| `Core 1: Macro Bear Veto` | `5` | `27.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `3` | `16.7%` |
| `Core 4: Defensible Whale Dump` | `2` | `11.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*