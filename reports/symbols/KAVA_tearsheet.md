# Kronos V12: Institutional Symbol Tear Sheet — `KAVA`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`10.584`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+32.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.38x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+10.75%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-3.4%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`141.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+28.7% / -5.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-03-28 01:00` | `2022-04-01 02:00` | 97.0h | `$4.2305` | `$4.2411` | **+0.25%** | **+0.25%** | +16.5% | -1.5% | `breakeven_ratchet` |
| 2 | Book 2 | `2023-11-06 00:00` | `2023-11-09 16:00` | 88.0h | `$0.7384` | `$0.7140` | **-3.31%** | **-3.36%** | +5.8% | -13.2% | `fast_decay_cut` |
| 3 | Book 1 | `2026-09-03 10:00` | `2026-09-13 10:00` | 240.0h | `$0.0503` | `$0.0674` | **+42.42%** | **+35.36%** | +63.9% | -2.9% | `trail_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-3.4%`** |
| `trail_stop` | `1` | `100.0%` | **`+35.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `KAVA`

* **Total Candidate Breakouts Filtered (Vetoed):** `242`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `162` (66.9% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `25`
* **Saved Capital Losses Avoided:** `+2,108.1%`
* **Missed Upside Forgone:** `-846.5%`
* **Net Veto Alpha:** `+1,261.6%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `95` | `39.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `67` | `27.7%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `67` | `27.7%` |
| `Core 4: Funding Rate Cap` | `12` | `5.0%` |
| `Core 4: Defensible Whale Dump` | `1` | `0.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*