# Kronos V12: Institutional Symbol Tear Sheet — `OP`
**Classification:** Clean 6-Core Universal Multi-Tier Architecture  
**Liquidity Tier:** `Tier 1` | **Total Recorded Trades:** `18` (`18` Closed, `0` Open)  
**Database Source:** `data/all_tapes/v12_production/trades.parquet`

---

## 1. Executive Performance Matrix (Strict Log Compounding Space)

| Metric | Performance | Benchmark Target | Verdict |
| :--- | :---: | :---: | :---: |
| **Total Closed Trades** | `18` | $\ge 1$ | ✅ Validated |
| **Win Rate** | **`55.6%`** | `> 40.0%` | ✅ Passed |
| **Profit Factor (Log-Space)** | **`1.683`** | `> 1.50` | ✅ Outperforming |
| **Cumulative Net Log Return** | **`+56.0%`** | `> 0.0%` | ✅ Profitable |
| **Compounded Capital Growth** | **`1.75x`** | `> 1.0x` | 🚀 Alpha Driver |
| **Mean Net Log Return / Trade** | **`+3.11%`** | `> +1.0%` | ✅ Strong Edge |
| **Maximum Log Drawdown** | **`-28.0%`** | `< -30%` | ✅ Contained |
| **Average Trade Duration** | **`74.7h`** | `24h - 336h` | Normal Lifecycle |
| **Mean Peak MFE / Max MAE** | **`+9.4% / -11.3%`** | MFE > 2x MAE | High Asymmetry |

---

## 2. Chronological Trade History Ledger

| # | Book | Entry (UTC) | Exit (UTC) | Duration | Entry Px | Exit Px | Realized PnL | Net Log Ret | Peak MFE | Max MAE | Exit Trigger |
| :-: | :-: | :---: | :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | Book 5 (Shelf Absorption Squeeze) | `2022-06-02 15:00` | `2022-06-06 15:00` | Live | `$1.4204` | `$1.3039` | **-8.20%** | **-8.56%** | +-11.9% | -74.4% | `shelf_stop_loss` |
| 2 | Book 5 (Shelf Absorption Squeeze) | `2023-02-23 02:00` | `2023-02-27 02:00` | Live | `$2.5927` | `$2.8130` | **+8.50%** | **+8.16%** | +10.0% | -30.7% | `shelf_target_reclaim` |
| 3 | Book 4 | `2023-07-31 00:00` | `2023-08-15 19:00` | 379.0h | `$1.6479` | `$1.4228` | **-16.51%** | **-17.76%** | +10.9% | -15.1% | `structural_stop` |
| 4 | Book 4 | `2023-11-04 20:00` | `2023-11-10 00:00` | 124.0h | `$1.4771` | `$1.7725` | **+23.45%** | **+21.42%** | +20.5% | -8.3% | `target_reclaim` |
| 5 | Book 3 | `2023-11-14 18:00` | `2023-11-15 07:00` | 13.0h | `$1.7054` | `$1.8537` | **+8.70%** | **+8.34%** | +9.1% | -3.6% | `target_reclaim` |
| 6 | Book 3 | `2023-12-09 17:00` | `2023-12-10 12:00` | 19.0h | `$2.0336` | `$2.2104` | **+8.70%** | **+8.34%** | +9.3% | -1.1% | `target_reclaim` |
| 7 | Book 3 | `2024-02-20 09:00` | `2024-02-20 13:00` | 4.0h | `$3.7425` | `$3.9862` | **+6.51%** | **+6.31%** | +12.2% | -0.8% | `target_reclaim` |
| 8 | Book 3 | `2024-03-03 07:00` | `2024-03-05 04:00` | 45.0h | `$3.7549` | `$4.3122` | **+14.84%** | **+13.84%** | +17.7% | -2.6% | `target_reclaim` |
| 9 | Book 3 | `2024-03-05 19:00` | `2024-03-05 21:00` | 2.0h | `$3.8094` | `$4.4023` | **+15.57%** | **+14.47%** | +16.3% | -4.7% | `target_reclaim` |
| 10 | Book 3 | `2024-11-12 10:00` | `2024-11-13 03:00` | 17.0h | `$1.7145` | `$1.5734` | **-8.23%** | **-8.59%** | +3.8% | -8.2% | `stop_loss` |
| 11 | Book 4 | `2024-11-21 13:00` | `2024-11-27 23:00` | 154.0h | `$2.0903` | `$2.4666` | **+9.00%** | **+8.28%** | +20.2% | -4.0% | `climax_whale_euphoria_harvest` |
| 12 | Book 3 | `2024-12-09 06:00` | `2024-12-09 20:00` | 14.0h | `$2.5387` | `$2.3298` | **-8.23%** | **-8.59%** | +2.1% | -10.0% | `stop_loss` |
| 13 | Book 2 | `2025-06-29 22:00` | `2025-06-30 14:00` | 16.0h | `$0.6155` | `$0.5649` | **-10.08%** | **-10.52%** | +1.1% | -8.2% | `initial_stop` |
| 14 | Book 1 | `2025-07-10 20:00` | `2025-07-18 01:00` | 173.0h | `$0.6244` | `$0.7492` | **+31.10%** | **+27.20%** | +20.8% | -1.7% | `target_reclaim` |
| 15 | Book 1 | `2025-09-18 18:00` | `2025-09-20 18:00` | 48.0h | `$0.8387` | `$0.8037` | **-7.12%** | **-7.36%** | +2.1% | -6.5% | `fast_decay_cut` |
| 16 | Book 2 | `2025-10-26 22:00` | `2025-10-28 20:00` | 46.0h | `$0.4683` | `$0.4297` | **-10.08%** | **-10.52%** | +1.6% | -8.2% | `initial_stop` |
| 17 | Book 2 | `2026-09-14 17:00` | `2026-09-15 18:00` | 25.0h | `$0.1040` | `$0.0954` | **-9.66%** | **-10.08%** | +1.4% | -9.4% | `initial_stop` |
| 18 | Book 1 | `2026-09-18 03:00` | `2026-09-22 23:00` | 116.0h | `$0.1128` | `$0.1353` | **+24.01%** | **+21.58%** | +22.5% | -5.9% | `target_reclaim` |

---

## 3. Microstructure Exit Reason Decomposition

| Exit Trigger | Trade Count | Win Rate % | Total Net Log PnL |
| :--- | :-: | :-: | :-: |
| `target_reclaim` | `8` | `100.0%` | **`+121.5%`** |
| `initial_stop` | `3` | `0.0%` | **`-31.1%`** |
| `stop_loss` | `2` | `0.0%` | **`-17.2%`** |
| `climax_whale_euphoria_harvest` | `1` | `100.0%` | **`+8.3%`** |
| `shelf_stop_loss` | `1` | `0.0%` | **`-8.6%`** |
| `fast_decay_cut` | `1` | `0.0%` | **`-7.4%`** |
| `shelf_target_reclaim` | `1` | `100.0%` | **`+8.2%`** |
| `structural_stop` | `1` | `0.0%` | **`-17.8%`** |

---

## 4. Counterfactual Risk Gate Audit for `OP`

* **Total Candidate Breakouts Filtered (Vetoed):** `673`
* **Dodged Bullets (Lethal False Breakouts Avoided):** `444` (66.0% Efficiency)
* **Missed Opportunities (Runners $\ge +20\%$ MFE):** `140`
* **Saved Capital Losses Avoided:** `+5,785.0%`
* **Missed Upside Forgone:** `-6,022.5%`
* **Net Veto Alpha:** `+-237.5%`

### Veto Gate Breakdown for this Asset:
| Risk Gate | Veto Count | Share % |
| :--- | :-: | :-: |
| `Core 1: Macro Bear Veto` | `629` | `93.5%` |
| `Core 4: Funding Rate Cap` | `21` | `3.1%` |
| `Core 4: Defensible Whale Dump` | `17` | `2.5%` |
| `Core 4: Whale Firewall` | `5` | `0.7%` |
| `Core 4: Book 2 Above-200d Squeeze Stall` | `1` | `0.1%` |

---

*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*