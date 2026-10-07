# Kronos V12: Institutional Symbol Tear Sheet — `C98`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`50.0%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`0.162`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-1.3%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.99x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-0.64%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-1.5%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`57.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+10.3% / -3.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-28 13:00` | `2022-10-31 08:00` | 67.0h | `$0.3206` | `$0.3214` | **+0.25%** | **+0.25%** | +16.0% | -0.9% | `breakeven_ratchet` |
| 2 | Book 2 | `2023-07-13 16:00` | `2023-07-15 16:00` | 48.0h | `$0.1557` | `$0.1533` | **-1.52%** | **-1.54%** | +4.5% | -5.1% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `100.0%` | **`+0.2%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-1.5%`** |

---

## 4. Counterfactual Risk Gate Audit for `C98`

* **Total Candidate Breakouts Filtered (Vetoed):** `203`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `120` (59.1% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `24`
* **Saved Capital Losses Avoided:** `+1,543.6%`
* **Missed Upside Forgone:** `-591.2%`
* **Net Veto Alpha:** `+952.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `66` | `32.5%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `65` | `32.0%` |
| `Core 1: Macro Bear Veto` | `42` | `20.7%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `29` | `14.3%` |
| `Core 0: Zero-Tolerance Data Firewall` | `1` | `0.5%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*