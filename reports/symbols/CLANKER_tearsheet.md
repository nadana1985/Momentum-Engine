# Kronos V12: Institutional Symbol Tear Sheet — `CLANKER`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-25.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.77x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-8.59%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-17.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`36.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.6% / -8.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2026-08-22 21:00` | `2026-08-25 21:00` | 72.0h | `$13.4964` | `$12.3856` | **-8.23%** | **-8.59%** | +2.4% | -9.0% | `stop_loss` |
| 2 | Book 3 | `2026-09-23 13:00` | `2026-09-23 14:00` | 1.0h | `$13.7540` | `$12.6220` | **-8.23%** | **-8.59%** | +2.2% | -8.2% | `stop_loss` |
| 3 | Book 3 | `2026-09-26 20:00` | `2026-09-28 07:00` | 35.0h | `$14.8764` | `$13.6521` | **-8.23%** | **-8.59%** | +3.2% | -8.4% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `3` | `0.0%` | **`-25.8%`** |

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