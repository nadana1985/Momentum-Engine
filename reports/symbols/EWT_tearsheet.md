# Kronos V12: Institutional Symbol Tear Sheet — `EWT`
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
| **Cumulative Net Log Return** | **`-3.0%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.01%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-0.7%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`32.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+0.9% / -1.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-08 00:00` | `2026-09-08 08:00` | 8.0h | `$113.0419` | `$110.3959` | **-2.34%** | **-2.37%** | +0.1% | -2.2% | `initial_stop` |
| 2 | Book 2 | `2026-09-21 07:00` | `2026-09-23 12:00` | 53.0h | `$113.8539` | `$113.4158` | **-0.38%** | **-0.39%** | +2.2% | -0.7% | `fast_decay_cut` |
| 3 | Book 2 | `2026-10-02 13:00` | `2026-10-04 01:00` | 36.0h | `$116.6810` | `$116.3684` | **-0.27%** | **-0.27%** | +0.4% | -1.0% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `1` | `0.0%` | **`-0.4%`** |
| `initial_stop` | `1` | `0.0%` | **`-2.4%`** |
| `stall_bailout` | `1` | `0.0%` | **`-0.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `EWT`

* **Total Candidate Breakouts Filtered (Vetoed):** `28`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `22` (78.6% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+78.6%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+78.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `17` | `60.7%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `11` | `39.3%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*