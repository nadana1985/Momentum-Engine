# Kronos V12: Institutional Symbol Tear Sheet — `SUSHI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`1.681`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+3.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.03x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+1.06%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-0.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`86.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+7.7% / -2.6%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-01-09 00:00` | `2023-01-10 12:00` | 36.0h | `$1.1118` | `$1.0783` | **-4.06%** | **-4.15%** | +2.3% | -4.5% | `fast_decay_cut` |
| 2 | Book 2 | `2025-04-22 15:00` | `2025-04-29 15:00` | 168.0h | `$0.6258` | `$0.6766` | **+8.13%** | **+7.81%** | +14.4% | -1.8% | `time_cap` |
| 3 | Book 2 | `2026-05-02 02:00` | `2026-05-04 10:00` | 56.0h | `$0.2193` | `$0.2183` | **-0.50%** | **-0.50%** | +6.4% | -1.6% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-4.6%`** |
| `time_cap` | `1` | `100.0%` | **`+7.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `SUSHI`

* **Total Candidate Breakouts Filtered (Vetoed):** `258`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `156` (60.5% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `62`
* **Saved Capital Losses Avoided:** `+2,358.1%`
* **Missed Upside Forgone:** `-2,359.9%`
* **Net Veto Alpha:** `+-1.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 0: Zero-Tolerance Data Firewall` | `120` | `46.5%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `74` | `28.7%` |
| `Core 1: Macro Bear Veto` | `59` | `22.9%` |
| `Core 4: Whale Firewall` | `3` | `1.2%` |
| `Core 4: Funding Rate Cap` | `2` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*