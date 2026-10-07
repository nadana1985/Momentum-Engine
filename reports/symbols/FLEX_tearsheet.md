# Kronos V12: Institutional Symbol Tear Sheet — `FLEX`
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
| **Cumulative Net Log Return** | **`-3.6%`** | `> 0.0%` | 🛑 Drawdown |
| **Compounded Capital Growth** | **`0.97x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`-1.18%`** | `> +1.0%` | Normal |
| **Maximum Log Drawdown** | **`-3.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`47.3h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+2.9% / -2.7%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 2 | `2026-08-26 13:00` | `2026-08-28 15:00` | 50.0h | `$111.7988` | `$111.4507` | **-0.31%** | **-0.31%** | +5.4% | -3.1% | `fast_decay_cut` |
| 2 | Book 2 | `2026-09-22 13:00` | `2026-09-24 13:00` | 48.0h | `$113.2825` | `$109.9644` | **-2.93%** | **-2.97%** | +2.2% | -3.3% | `fast_decay_cut` |
| 3 | Book 2 | `2026-10-02 14:00` | `2026-10-04 10:00` | 44.0h | `$116.9116` | `$116.5978` | **-0.27%** | **-0.27%** | +1.0% | -1.7% | `stall_bailout` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `fast_decay_cut` | `2` | `0.0%` | **`-3.3%`** |
| `stall_bailout` | `1` | `0.0%` | **`-0.3%`** |

---

## 4. Counterfactual Risk Gate Audit for `FLEX`

* **Total Candidate Breakouts Filtered (Vetoed):** `7`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `6` (85.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `0`
* **Saved Capital Losses Avoided:** `+53.8%`
* **Missed Upside Forgone:** `-0.0%`
* **Net Veto Alpha:** `+53.8%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 2c: Tier 3 Book 1 Prohibition` | `4` | `57.1%` |
| `Core 1: Macro Bear Veto` | `3` | `42.9%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*