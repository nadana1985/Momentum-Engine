# Kronos V12: Institutional Symbol Tear Sheet — `RESOLV`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `4` (`4` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `4` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`25.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.547`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-8.7%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.17%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-10.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`25.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.7% / -8.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-07-11 09:00` | `2025-07-11 14:00` | 5.0h | `$0.2175` | `$0.1996` | **-8.23%** | **-8.59%** | +20.2% | -8.4% | `stop_loss` |
| 2 | Book 3 | `2026-09-28 03:00` | `2026-10-01 03:00` | 72.0h | `$0.0190` | `$0.0189` | **-0.30%** | **-0.30%** | +2.6% | -5.3% | `time_expiry` |
| 3 | Book 3 | `2026-10-02 07:00` | `2026-10-03 05:00` | 22.0h | `$0.0200` | `$0.0222` | **+11.05%** | **+10.48%** | +31.5% | -4.6% | `target_reclaim` |
| 4 | Book 3 | `2026-10-03 08:00` | `2026-10-03 09:00` | 1.0h | `$0.0221` | `$0.0199` | **-9.76%** | **-10.27%** | +12.4% | -15.9% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `2` | `0.0%` | **`-18.9%`** |
| `target_reclaim` | `1` | `100.0%` | **`+10.5%`** |
| `time_expiry` | `1` | `0.0%` | **`-0.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `RESOLV`

* **Total Candidate Breakouts Filtered (Vetoed):** `209`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `180` (86.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `57`
* **Saved Capital Losses Avoided:** `+5,281.5%`
* **Missed Upside Forgone:** `-1,909.1%`
* **Net Veto Alpha:** `+3,372.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `201` | `96.2%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `1.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `2` | `1.0%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `2` | `1.0%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*