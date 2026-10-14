# Kronos V12: Institutional Symbol Tear Sheet — `SPORTFUN`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 3` | **Total Recorded Trades:** `3` (`3` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `3` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`66.7%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`2.405`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+12.1%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.13x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+4.02%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-8.6%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`60.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+15.7% / -5.0%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-05-08 04:00` | `2026-05-08 15:00` | 11.0h | `$0.0695` | `$0.0820` | **+10.80%** | **+9.93%** | +23.5% | -4.4% | `climax_whale_euphoria_harvest` |
| 2 | Book 2 | `2026-09-18 20:00` | `2026-09-25 20:00` | 168.0h | `$0.0180` | `$0.0196` | **+11.20%** | **+10.72%** | +16.8% | -2.3% | `time_cap` |
| 3 | Book 3 | `2026-10-03 18:00` | `2026-10-03 21:00` | 3.0h | `$0.0218` | `$0.0200` | **-8.23%** | **-8.59%** | +6.7% | -8.3% | `stop_loss` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+9.9%`** |
| `stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `time_cap` | `1` | `100.0%` | **`+10.7%`** |

---

## 4. Counterfactual Risk Gate Audit for `SPORTFUN`

* **Total Candidate Breakouts Filtered (Vetoed):** `127`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `111` (87.4% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `14`
* **Saved Capital Losses Avoided:** `+2,384.7%`
* **Missed Upside Forgone:** `-442.0%`
* **Net Veto Alpha:** `+1,942.7%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `116` | `91.3%` |
| `Core 4: RS_BTC Over-Extension Climax Clamp` | `10` | `7.9%` |
| `Core 2c: Tier 3 Book 1 Prohibition` | `1` | `0.8%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*