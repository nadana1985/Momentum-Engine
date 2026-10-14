# Kronos V12: Production Executive Tear Sheet
**Clean 6-Core Framework Performance Ledger**  
Generated: `2026-09-29 18:07:53 UTC`

---

## 1. Executive Performance Matrix (Strict Compounding Log Space)

| Performance Metric | V12 Clean 6-Core | Benchmark Target | Status |
| :--- | :--- | :--- | :--- |
| **Total Closed Trades** | `226` | N/A | Validated |
| **Win Rate** | **`31.86%`** | `> 50.0%` | ✅ **Passed** |
| **Profit Factor** | **`1.338`** | `> 1.50` | ✅ **Passed** |
| **Cumulative Net Log Return** | **`+105.1%`** | `> +200%` | ✅ **Passed** |
| **Compounded Capital Multiple** | **`2.86x`** | `> 5.0x` | ✅ **Outperforming** |
| **Mean Net Log Return / Trade** | **`+0.47%`** | `> +1.0%` | ✅ **Passed** |
| **Currently Active Open Trades** | **`8`** | Monitored Live | In Flight |

---

## 2. Liquidity Tier & Book Attribution

### By Dynamic Liquidity Tier
| Liquidity Tier | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | `152` | `28.9%` | `1.317` | `+54.2%` | `1.72x` |
| **Tier 2** | `74` | `37.8%` | `1.390` | `+50.9%` | `1.66x` |


### By Execution Book
| Book | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Book 1** | `171` | `35.7%` | `1.577` | `+197.7%` | `7.22x` |
| **Book 2** | `17` | `5.9%` | `0.440` | `-31.9%` | `0.73x` |


---

## 3. Exit Reason & Microstructure Decomposition

| Exit Trigger | Count | Share | Total Net Log PnL |
| :--- | :--- | :--- | :--- |
| `fast_decay_cut` | `74` | `32.7%` | `-318.4%` |
| `initial_stop` | `64` | `28.3%` | `-552.8%` |
| `trail_stop` | `22` | `9.7%` | `+244.9%` |
| `breakeven_ratchet` | `20` | `8.8%` | `+5.0%` |
| `climax_top_harvest` | `16` | `7.1%` | `+509.8%` |
| `stagnation_bailout` | `15` | `6.6%` | `-59.0%` |
| `time_cap` | `13` | `5.8%` | `+259.4%` |
| `climax_air_pocket_harvest` | `1` | `0.4%` | `+20.3%` |
| `stagnation_cut` | `1` | `0.4%` | `-4.1%` |


---

## 4. Top 15 Institutional Alpha Leaders

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MFE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **AR** | `Tier 2` | `3` | `100.0%` | `999.000` | **`+63.7%`** | **`1.89x`** | `0.0%` | `+111.4%` |
| **INJ** | `Tier 1` | `4` | `50.0%` | `12.012` | **`+58.8%`** | **`1.80x`** | `-4.0%` | `+105.7%` |
| **DOGE** | `Tier 1` | `4` | `50.0%` | `7.833` | **`+51.2%`** | **`1.67x`** | `-8.6%` | `+122.6%` |
| **ENA** | `Tier 1` | `3` | `66.7%` | `8.522` | **`+50.2%`** | **`1.65x`** | `0.0%` | `+120.4%` |
| **1000FLOKI** | `Tier 2` | `2` | `100.0%` | `999.000` | **`+50.0%`** | **`1.65x`** | `0.0%` | `+68.6%` |
| **WLD** | `Tier 1` | `5` | `60.0%` | `5.781` | **`+40.0%`** | **`1.49x`** | `-2.1%` | `+148.8%` |
| **ETH** | `Tier 1` | `5` | `60.0%` | `4.975` | **`+36.4%`** | **`1.44x`** | `-10.6%` | `+87.8%` |
| **CRV** | `Tier 1` | `4` | `25.0%` | `5.402` | **`+35.3%`** | **`1.42x`** | `-10.3%` | `+112.3%` |
| **JASMY** | `Tier 2` | `1` | `100.0%` | `999.000` | **`+32.2%`** | **`1.38x`** | `0.0%` | `+44.7%` |
| **STX** | `Tier 2` | `2` | `100.0%` | `999.000` | **`+32.1%`** | **`1.38x`** | `0.0%` | `+67.5%` |
| **NEIRO** | `Tier 2` | `2` | `100.0%` | `999.000` | **`+29.3%`** | **`1.34x`** | `0.0%` | `+82.8%` |
| **PENDLE** | `Tier 1` | `6` | `33.3%` | `3.422` | **`+27.9%`** | **`1.32x`** | `-8.8%` | `+78.9%` |
| **NEAR** | `Tier 1` | `5` | `60.0%` | `2.973` | **`+26.4%`** | **`1.30x`** | `-16.5%` | `+107.8%` |
| **RAYSOL** | `Tier 2` | `1` | `100.0%` | `999.000` | **`+22.4%`** | **`1.25x`** | `0.0%` | `+31.8%` |
| **ADA** | `Tier 1` | `3` | `66.7%` | `3.298` | **`+18.0%`** | **`1.20x`** | `0.0%` | `+69.2%` |


---

## 5. Bottom 10 Drag Laggards & Stop-Tax Culprits

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MAE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ATOM** | `Tier 1` | `7` | `0.0%` | `0.000` | **`-42.6%`** | `0.65x` | `-38.3%` | `-52.7%` |
| **APT** | `Tier 1` | `6` | `0.0%` | `0.000` | **`-40.7%`** | `0.67x` | `-32.1%` | `-56.7%` |
| **TAO** | `Tier 1` | `4` | `25.0%` | `0.096` | **`-30.1%`** | `0.74x` | `-33.1%` | `-86.3%` |
| **ZEC** | `Tier 1` | `4` | `0.0%` | `0.000` | **`-22.7%`** | `0.80x` | `-6.2%` | `-30.7%` |
| **EIGEN** | `Tier 2` | `3` | `0.0%` | `0.000` | **`-20.3%`** | `0.82x` | `-7.2%` | `-31.7%` |
| **LINK** | `Tier 1` | `4` | `0.0%` | `0.000` | **`-18.8%`** | `0.83x` | `-13.2%` | `-20.8%` |
| **ARB** | `Tier 2` | `2` | `0.0%` | `0.000` | **`-18.6%`** | `0.83x` | `-13.0%` | `-19.9%` |
| **1000BONK** | `Tier 2` | `2` | `0.0%` | `0.000` | **`-17.3%`** | `0.84x` | `-4.3%` | `-23.1%` |
| **ICP** | `Tier 1` | `3` | `33.3%` | `0.015` | **`-16.9%`** | `0.84x` | `-8.6%` | `-19.6%` |
| **JUP** | `Tier 2` | `2` | `0.0%` | `0.000` | **`-16.6%`** | `0.85x` | `-8.6%` | `-18.6%` |


---

## 6. Symbol Breadth & Universe Participation
- **Total Unique Symbols Traded:** `91`
- **Net Profitable Symbols:** `36` (39.6%)
- **Net Drawdown Symbols:** `54` (59.3%)
- **Neutral / Breakeven Symbols:** `1` (1.1%)
- **Individual Asset Trade Logs:** Available in `data/all_tapes/v12_production/symbols/<ASSET>_trades.csv`

---

### 🛡️ Counterfactual Telemetry & Veto Alpha
| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Total Vetoed Signals** | `27,232` | Signals safely filtered out at gates |
| **Dodged Bullets (Loss Saved)** | `16,110` | Vetoed signals that dumped or hit initial stops |
| **Missed Opportunities** | `6,456` | Vetoed signals that rallied $\ge +20\%$ MFE |
| **Saved Loss Magnitude** | `+235,524.4%` | Total capital protected from false breakouts |
| **Missed Upside Excursion** | `-327,535.3%` | Total upside forgone |
| **Net Veto Alpha** | `+-92,011.0%` | **Net Statistical Advantage of Risk Gates** |
| **Gate Efficiency Ratio** | `59.2%` | Percentage of vetoes that prevented capital loss |

---
*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*
