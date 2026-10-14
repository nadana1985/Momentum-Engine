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
| **Profit Factor (Log-Space)** | **`2.295`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+4.2%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.04x`** | `> 1.0x` | Neutral |
| **Mean Net Log Return / Trade** | **`+2.08%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-3.2%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`182.5h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+27.5% / -13.9%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 4 | `2026-04-19 06:00` | `2026-05-02 15:00` | 321.0h | `$4.6369` | `$5.5643` | **+7.61%** | **+7.38%** | +28.0% | -12.9% | `target_reclaim` |
| 2 | Book 1 | `2026-08-20 09:00` | `2026-08-22 05:00` | 44.0h | `$4.0581` | `$3.9873` | **-3.17%** | **-3.21%** | +27.0% | -14.8% | `breakeven_ratchet` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `breakeven_ratchet` | `1` | `0.0%` | **`-3.2%`** |
| `target_reclaim` | `1` | `100.0%` | **`+7.4%`** |

---

## 4. Counterfactual Risk Gate Audit for `ORDI`

* **Total Candidate Breakouts Filtered (Vetoed):** `544`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `417` (76.7% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `61`
* **Saved Capital Losses Avoided:** `+7,704.3%`
* **Missed Upside Forgone:** `-4,804.9%`
* **Net Veto Alpha:** `+2,899.4%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: ATH Tier-2 Protection Clamp` | `419` | `77.0%` |
| `Core 1: Macro Bear Veto` | `122` | `22.4%` |
| `Core 4: Whale Firewall` | `1` | `0.2%` |
| `Core 4: Funding Rate Cap` | `1` | `0.2%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.2%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*