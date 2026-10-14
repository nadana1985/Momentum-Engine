# Kronos V12: Institutional Symbol Tear Sheet — `BAS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.761`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-2.1%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.98x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.03%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`0.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`111.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.9% / -19.1%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 3 | `2025-10-10 20:00` | `2025-10-10 21:00` | 1.0h | `$0.0220` | `$0.0202` | **-8.23%** | **-8.59%** | +10.6% | -25.5% | `stop_loss` |
| 2 | Book 4 | `2026-03-13 10:00` | `2026-03-22 16:00` | 222.0h | `$0.0093` | `$0.0112` | **+6.72%** | **+6.54%** | +21.2% | -12.7% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `target_reclaim` | `1` | `100.0%` | **`+6.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `BAS`

* **Total Candidate Breakouts Filtered (Vetoed):** `210`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `187` (89.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `94`
* **Saved Capital Losses Avoided:** `+5,191.6%`
* **Missed Upside Forgone:** `-3,743.7%`
* **Net Veto Alpha:** `+1,447.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `201` | `95.7%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `4` | `1.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `1.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `1` | `0.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*