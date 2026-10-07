# Kronos V12: Institutional Symbol Tear Sheet — `DUSK`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`33.3%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.032`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-8.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.92x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.94%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-4.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`80.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+6.9% / -4.5%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2023-01-09 16:00` | `2023-01-11 04:00` | 36.0h | `$0.0945` | `$0.0913` | **-4.67%** | **-4.78%** | +0.5% | -4.7% | `stall_bailout` |
| 2 | Book 2 | `2024-02-13 11:00` | `2024-02-15 11:00` | 48.0h | `$0.3431` | `$0.3286` | **-4.23%** | **-4.32%** | +4.6% | -4.7% | `fast_decay_cut` |
| 3 | Book 1 | `2025-04-21 12:00` | `2025-04-28 01:00` | 157.0h | `$0.0819` | `$0.0821` | **+0.29%** | **+0.29%** | +15.5% | -4.1% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-4.3%`** |
| `stall_bailout` | `1` | `0.0%` | **`-4.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `DUSK`

* **Total Candidate Breakouts Filtered (Vetoed):** `190`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `105` (55.3% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `38`
* **Saved Capital Losses Avoided:** `+1,325.4%`
* **Missed Upside Forgone:** `-2,467.8%`
* **Net Veto Alpha:** `+-1,142.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `93` | `48.9%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `76` | `40.0%` |
| `Core 4: Funding Rate Cap` | `10` | `5.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `9` | `4.7%` |
| `Core 4: Whale Firewall` | `2` | `1.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*