# Kronos V12: Institutional Symbol Tear Sheet — `RESOLV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.327`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-17.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.84x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-5.72%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-16.9%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`8.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.1% / -12.2%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-11 08:00` | `2025-07-11 09:00` | 1.0h | `$0.2284` | `$0.2096` | **-8.23%** | **-8.59%** | +14.5% | -8.5% | `stop_loss` |
| 2 | Book 3 | `2026-10-02 07:00` | `2026-10-03 05:00` | 22.0h | `$0.0204` | `$0.0222` | **+8.70%** | **+8.34%** | +28.7% | -6.7% | `target_reclaim` |
| 3 | Book 3 | `2026-10-03 08:00` | `2026-10-03 09:00` | 1.0h | `$0.0236` | `$0.0200` | **-15.56%** | **-16.91%** | +5.1% | -21.3% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-25.5%`** |
| `target_reclaim` | `1` | `100.0%` | **`+8.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `RESOLV`

* **Total Candidate Breakouts Filtered (Vetoed):** `55`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `39` (70.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `27`
* **Saved Capital Losses Avoided:** `+795.4%`
* **Missed Upside Forgone:** `-1,053.7%`
* **Net Veto Alpha:** `+-258.3%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `47` | `85.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `7.3%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `2` | `3.6%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `3.6%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*