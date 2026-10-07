# Kronos V12: Institutional Symbol Tear Sheet — `CELR`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-4.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.96x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-2.29%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-4.3%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`48.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.2% / -4.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2022-10-25 17:00` | `2022-10-27 17:00` | 48.0h | `$0.0153` | `$0.0152` | **-0.30%** | **-0.30%** | +4.1% | -3.4% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-13 01:00` | `2026-09-15 01:00` | 48.0h | `$0.0022` | `$0.0021` | **-4.18%** | **-4.27%** | +4.4% | -6.0% | `fast_decay_cut` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-4.6%`** |

---

## 4. Counterfactual Risk Gate Audit for `CELR`

* **Total Candidate Breakouts Filtered (Vetoed):** `298`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `167` (56.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `51`
* **Saved Capital Losses Avoided:** `+2,303.7%`
* **Missed Upside Forgone:** `-1,628.6%`
* **Net Veto Alpha:** `+675.2%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `71` | `23.8%` |
| `Core 1: Macro Bear Veto` | `68` | `22.8%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `67` | `22.5%` |
| `Core 0: Zero-Tolerance Data Firewall` | `50` | `16.8%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `42` | `14.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*