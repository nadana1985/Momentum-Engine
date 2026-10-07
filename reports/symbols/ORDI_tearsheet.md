# Kronos V12: Institutional Symbol Tear Sheet — `ORDI`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.309`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-0.8%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.38%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.1%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`46.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+16.1% / -9.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 1 | `2026-08-20 09:00` | `2026-08-22 05:00` | 44.0h | `$4.0581` | `$4.0682` | **+0.34%** | **+0.34%** | +27.0% | -14.8% | `breakeven_ratchet` |
| 2 | Book 2 | `2026-09-18 23:00` | `2026-09-20 23:00` | 48.0h | `$4.6115` | `$4.5606` | **-1.10%** | **-1.11%** | +5.2% | -4.9% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.3%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.1%`** |

---

## 4. Counterfactual Risk Gate Audit for `ORDI`

* **Total Candidate Breakouts Filtered (Vetoed):** `128`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `78` (60.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `32`
* **Saved Capital Losses Avoided:** `+1,279.6%`
* **Missed Upside Forgone:** `-3,689.4%`
* **Net Veto Alpha:** `+-2,409.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `68` | `53.1%` |
| `Core 1: Macro Bear Veto` | `58` | `45.3%` |
| `Core 4: Whale Firewall` | `1` | `0.8%` |
| `Core 4: Funding Rate Cap` | `1` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*