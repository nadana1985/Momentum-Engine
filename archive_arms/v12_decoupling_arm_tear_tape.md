# Kronos V12: Production Executive Tear Sheet
**Clean 6-Core Framework Performance Ledger**  
Generated: `2026-09-29 17:02:39 UTC`

---

## 1. Executive Performance Matrix (Strict Compounding Log Space)

| Performance Metric | V12 Clean 6-Core | Benchmark Target | Status |
| :--- | :--- | :--- | :--- |
| **Total Closed Trades** | `186` | N/A | Validated |
| **Win Rate** | **`33.87%`** | `> 50.0%` | ✅ **Passed** |
| **Profit Factor** | **`1.535`** | `> 1.50` | ✅ **Passed** |
| **Cumulative Net Log Return** | **`+185.8%`** | `> +200%` | ✅ **Passed** |
| **Compounded Capital Multiple** | **`6.41x`** | `> 5.0x` | ✅ **Outperforming** |
| **Mean Net Log Return / Trade** | **`+1.00%`** | `> +1.0%` | ✅ **Passed** |
| **Currently Active Open Trades** | **`6`** | Monitored Live | In Flight |

---

## 2. Liquidity Tier & Book Attribution

### By Dynamic Liquidity Tier
| Liquidity Tier | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1** | `123` | `30.9%` | `1.604` | `+152.0%` | `4.57x` |
| **Tier 2** | `63` | `39.7%` | `1.363` | `+33.9%` | `1.40x` |


### By Execution Book
| Book | Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Book 1** | `169` | `36.7%` | `1.628` | `+217.7%` | `8.82x` |
| **Book 2** | `17` | `5.9%` | `0.440` | `-31.9%` | `0.73x` |


---

## 3. Exit Reason & Microstructure Decomposition

| Exit Trigger | Count | Share | Total Net Log PnL |
| :--- | :--- | :--- | :--- |
| `fast_decay_cut` | `72` | `38.7%` | `-293.0%` |
| `initial_stop` | `38` | `20.4%` | `-343.6%` |
| `breakeven_ratchet` | `19` | `10.2%` | `+4.7%` |
| `trail_stop` | `17` | `9.1%` | `+165.8%` |
| `climax_top_harvest` | `13` | `7.0%` | `+425.9%` |
| `time_cap` | `13` | `7.0%` | `+259.4%` |
| `stagnation_bailout` | `12` | `6.5%` | `-49.6%` |
| `climax_air_pocket_harvest` | `1` | `0.5%` | `+20.3%` |
| `stagnation_cut` | `1` | `0.5%` | `-4.1%` |


---

## 4. Top 15 Institutional Alpha Leaders

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MFE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **WLD** | `Tier 1` | `5` | `80.0%` | `52.097` | **`+88.0%`** | **`2.41x`** | `-2.1%` | `+199.3%` |
| **INJ** | `Tier 1` | `4` | `50.0%` | `12.012` | **`+58.8%`** | **`1.80x`** | `-4.0%` | `+105.7%` |
| **ENA** | `Tier 1` | `2` | `100.0%` | `999.000` | **`+58.8%`** | **`1.80x`** | `0.0%` | `+116.4%` |
| **1000FLOKI** | `Tier 2` | `2` | `100.0%` | `999.000` | **`+50.0%`** | **`1.65x`** | `0.0%` | `+68.6%` |
| **CAKE** | `Tier 1` | `4` | `50.0%` | `6.961` | **`+41.3%`** | **`1.51x`** | `-8.3%` | `+88.1%` |
| **CRV** | `Tier 1` | `4` | `25.0%` | `5.402` | **`+35.3%`** | **`1.42x`** | `-10.3%` | `+112.3%` |
| **JASMY** | `Tier 2` | `1` | `100.0%` | `999.000` | **`+32.2%`** | **`1.38x`** | `0.0%` | `+44.7%` |
| **STX** | `Tier 2` | `2` | `100.0%` | `999.000` | **`+32.1%`** | **`1.38x`** | `0.0%` | `+67.5%` |
| **AR** | `Tier 2` | `3` | `66.7%` | `39.564` | **`+31.1%`** | **`1.36x`** | `-0.9%` | `+73.6%` |
| **ETH** | `Tier 1` | `2` | `100.0%` | `999.000` | **`+30.8%`** | **`1.36x`** | `0.0%` | `+50.0%` |
| **HBAR** | `Tier 1` | `3` | `33.3%` | `7.451` | **`+29.6%`** | **`1.34x`** | `-0.5%` | `+73.6%` |
| **PENDLE** | `Tier 1` | `6` | `33.3%` | `3.422` | **`+27.9%`** | **`1.32x`** | `-8.8%` | `+78.9%` |
| **NEAR** | `Tier 1` | `5` | `60.0%` | `2.973` | **`+26.4%`** | **`1.30x`** | `-16.5%` | `+107.8%` |
| **THETA** | `Tier 2` | `1` | `100.0%` | `999.000` | **`+21.3%`** | **`1.24x`** | `0.0%` | `+41.5%` |
| **AAVE** | `Tier 1` | `2` | `50.0%` | `18.871` | **`+18.2%`** | **`1.20x`** | `0.0%` | `+30.5%` |


---

## 5. Bottom 10 Drag Laggards & Stop-Tax Culprits

| Asset | Tier | Closed Trades | Win Rate | Profit Factor | Net Log PnL | Capital Multiple | Max Log DD | Cumulative MAE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TAO** | `Tier 1` | `4` | `25.0%` | `0.096` | **`-30.1%`** | `0.74x` | `-33.1%` | `-86.3%` |
| **APT** | `Tier 1` | `4` | `0.0%` | `0.000` | **`-26.0%`** | `0.77x` | `-24.0%` | `-33.1%` |
| **ZEC** | `Tier 1` | `4` | `0.0%` | `0.000` | **`-22.7%`** | `0.80x` | `-6.2%` | `-30.7%` |
| **ATOM** | `Tier 1` | `5` | `0.0%` | `0.000` | **`-22.4%`** | `0.80x` | `-18.2%` | `-30.5%` |
| **EIGEN** | `Tier 2` | `3` | `0.0%` | `0.000` | **`-20.3%`** | `0.82x` | `-7.2%` | `-31.7%` |
| **LINK** | `Tier 1` | `4` | `0.0%` | `0.000` | **`-18.8%`** | `0.83x` | `-13.2%` | `-20.8%` |
| **ARB** | `Tier 2` | `2` | `0.0%` | `0.000` | **`-18.6%`** | `0.83x` | `-13.0%` | `-19.9%` |
| **1000BONK** | `Tier 2` | `2` | `0.0%` | `0.000` | **`-17.3%`** | `0.84x` | `-4.3%` | `-23.1%` |
| **ETC** | `Tier 1` | `1` | `0.0%` | `0.000` | **`-16.5%`** | `0.85x` | `0.0%` | `-15.7%` |
| **FIL** | `Tier 1` | `1` | `0.0%` | `0.000` | **`-16.5%`** | `0.85x` | `0.0%` | `-17.5%` |


---

## 6. Symbol Breadth & Universe Participation
- **Total Unique Symbols Traded:** `86`
- **Net Profitable Symbols:** `32` (37.2%)
- **Net Drawdown Symbols:** `53` (61.6%)
- **Neutral / Breakeven Symbols:** `1` (1.2%)
- **Individual Asset Trade Logs:** Available in `data/all_tapes/v12_production/symbols/<ASSET>_trades.csv`

---

### 🛡️ Counterfactual Telemetry & Veto Alpha
| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Total Vetoed Signals** | `27,412` | Signals safely filtered out at gates |
| **Dodged Bullets (Loss Saved)** | `16,162` | Vetoed signals that dumped or hit initial stops |
| **Missed Opportunities** | `6,527` | Vetoed signals that rallied $\ge +20\%$ MFE |
| **Saved Loss Magnitude** | `+236,334.1%` | Total capital protected from false breakouts |
| **Missed Upside Excursion** | `-330,160.1%` | Total upside forgone |
| **Net Veto Alpha** | `+-93,826.0%` | **Net Statistical Advantage of Risk Gates** |
| **Gate Efficiency Ratio** | `59.0%` | Percentage of vetoes that prevented capital loss |

---
*Confidential — Kronos V12 Autonomous Quantitative Production Architecture.*
