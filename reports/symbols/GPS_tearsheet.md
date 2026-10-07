# Kronos V12: Institutional Symbol Tear Sheet — `GPS`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 2` | **Total Recorded Trades:** `2` (`2` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `2` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`0.0%`** | `> 40.0%` | ⚠️ Watch |
| **Profit Factor (Log-Space)** | **`0.000`** | `> 1.50` | 🛑 Negative Drag |
| **Cumulative Net Log Return** | **`-17.2%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.84x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-8.59%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`14.0h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+4.5% / -9.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-09-02 17:00` | `2026-09-03 16:00` | 23.0h | `$0.0107` | `$0.0099` | **-8.23%** | **-8.59%** | +5.9% | -11.2% | `initial_stop` |
| 2 | Book 2 | `2026-09-09 14:00` | `2026-09-09 19:00` | 5.0h | `$0.0124` | `$0.0114` | **-8.23%** | **-8.59%** | +3.1% | -8.2% | `initial_stop` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `initial_stop` | `2` | `0.0%` | **`-17.2%`** |

---

## 4. Counterfactual Risk Gate Audit for `GPS`

* **Total Candidate Breakouts Filtered (Vetoed):** `107`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `66` (61.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `12`
* **Saved Capital Losses Avoided:** `+1,225.6%`
* **Missed Upside Forgone:** `-430.9%`
* **Net Veto Alpha:** `+794.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 4: Defensible Whale Dump` | `52` | `48.6%` |
| `Core 1: Macro Bear Veto` | `46` | `43.0%` |
| `Core 1: ATH Tier-2 Protection Clamp` | `9` | `8.4%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*