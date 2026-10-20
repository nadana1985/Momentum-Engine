# OGN/USDT (Oct 5 – Oct 10, 2026) Complete Lifecycle Reference: Entry, Mid-Run Retest Hold, and Climax Exit Signatures

This reference document serves as the canonical benchmark for evaluating **Book 2 Coiled Short Squeezes** from initial trap seeding through Bar 0 ignition, mid-run shakeout retests, and exact climax top exits.

---

## 1. Master Chronological Benchmark Table (`OGN/USDT`: Oct 5 – Oct 10, 2026)

| Phase & Exact Timestamp (UTC) | Price Action (O $\rightarrow$ H / C) | Upper Wick | 1h Volume (Shock) | 1h Trade Count (Shock) | Taker Buy % | Open Interest (\$ / Tokens) | Whale L/S Ratio | 8h Funding Rate | Quantitative Phase Diagnosis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **0. Dormant Base**<br>`Oct 05 06:00` | \$0.0205 $\rightarrow$ \$0.0207<br>*(+0.6%)* | 12% | \$0.01M<br>*(0.7x)* | 576<br>*(0.8x)* | 59.7% | \$1.34M<br>*(65.2M)* | **3.81**<br>*(79% Long)* | **+0.005%** | Dead baseline; zero short interest, normal positive carry. |
| **1. Trap Seeding**<br>`Oct 05 12:00–18:00` | \$0.0208 $\rightarrow$ **\$0.0232**<br>Close: \$0.0220 | **79%** | \$2.87M<br>*(100.9x)* | 51,531<br>*(68.6x)* | 48.8% | \$2.31M<br>*(**104.3M**)* | **2.88**<br>*($\Delta: -0.93$)* | **-0.266%** | Initial test spike traps 39M new short tokens at \$0.0220; funding flips deeply negative. |
| **2. 48h Coil Floor**<br>`Oct 08 07:00` *(t - 1h)* | \$0.0225 $\rightarrow$ \$0.0232<br>Close: **\$0.0225** | 91% | \$0.49M<br>*(1.6x)* | 6,931<br>*(1.2x)* | **59.6%**<br>*(`P94.4`)* | \$1.94M<br>*(85.9M)* | **1.92**<br>*(`P01.6` $\Delta$)* | **-0.148%**<br>*(`P01.8`)* | **Pre-Pump Stealth Absorption:** Aggressive 59.6% taker buying absorbs all sellers at \$0.0225. |
| **3. Bar 0 Ignition**<br>`Oct 08 08:00` *(t = 0)* | \$0.0225 $\rightarrow$ **\$0.0259**<br>Close: **\$0.0258** *(+14.7%)* | **3%** | **\$11.70M**<br>*(**37.8x**)* | **120,576**<br>*(**18.9x**)* | 50.4% | \$1.91M<br>*(**84.9M Flat**)* | **2.00** | -0.099% | **Bar 0 Ignition Shock:** `P99.7` Vol & Trade shock, 3% wick Marubozu, Flat-OI Law. |
| **4. Squeeze Ramp**<br>`Oct 08 12:00–13:00` | \$0.0362 $\rightarrow$ **\$0.0447**<br>Close: \$0.0421 | 7% $\rightarrow$ 39% | **\$116.51M**<br>*(**212.3x**)* | **967,806**<br>*(**106.9x**)* | 51.5% | **\$16.77M**<br>*(**398.1M**)* | **0.59**<br>*(63% Short)* | **-0.893%** | Whales fight the pump ($L/S: 2.00 \rightarrow 0.59$); OI explodes 4.7x; funding hits **-0.893%**. |
| **5. Retest Trap**<br>`Oct 08 15:00–16:00` | Pullback to **\$0.0376**<br>Close: \$0.0396 | 37% | \$52.33M<br>*(48.5x)* | 445,254<br>*(25.7x)* | **51.0%** | **\$18.74M**<br>*(**456.5M Peak**)* | **0.52** | **-0.893%** $\rightarrow$<br>**-0.400%** | **Mid-Run Shakeout:** Price dips -15%, but **58M MORE tokens short the dip** (456.5M OI peak!). |
| **6. CLIMAX EXIT**<br>`Oct 08 20:00` *(PEAK)* | \$0.0492 $\rightarrow$ **\$0.0536**<br>Close: **\$0.0495** *(+0.6%)* | **85%** 🚨 | **\$44.24M**<br>*(**3.1x drop**)* | **478,445**<br>*(**3.6x drop**)* | 51.7% | \$21.31M<br>*(433.0M)* | **0.45** | **-0.037%** 🚨 | **THE TOP (\$0.0536):** 85% Pinbar Wick + -62% Vol Divergence + Funding collapses 10x (-0.40% $\rightarrow$ -0.037%). |
| **7. Breakdown**<br>`Oct 08 21:00–22:00` | \$0.0495 $\rightarrow$ **\$0.0465**<br>*(Bounce wick: 80%)* | 41% $\rightarrow$ **80%** | \$26.47M<br>*(**1.2x**)* | 303,203<br>*(**1.3x**)* | **49.2%** 🚨 | **\$22.09M**<br>*(446.1M)* | **0.43**<br>*(Floor)* | -0.037% | Taker buy drops $<50\%$; failed retest of \$0.0495 prints 80% wick on dead 0.9x volume. |
| **8. Distribution**<br>`Oct 09 00:00 – Oct 10` | Bleeds to **\$0.0351**<br>*(Now: \$0.0398)* | — | \$2.5M–\$6M<br>*(**0.3x–0.6x**)* | 45k–115k<br>*(**0.3x–0.6x**)* | 47%–51% | Bleeds to<br>**\$10.49M (277M)** | Rises to<br>**0.82** | **-0.002%** | **Short Profit-Taking:** 169M tokens close out (-38% OI); Whale L/S rises $0.42 \rightarrow 0.82$ as price drops. |

---

## 2. The 4 Quantitative Entry & Hold Signatures

1. **Phase 1 — Trap Seeding Spike (48h–72h Prior to Launch):**
   - An initial volume pulse spikes price $+8\%$ to $+15\%$ and leaves a long upper wick ($\ge 65\%$), but **Token Open Interest expands $\ge +40\%$**, **Whale L/S drops $\ge -0.50$**, and **8h Funding flips deeply negative ($\le -0.10\%$ to $-0.30\%$)**.
   - *Interpretation:* Early shorts are now trapped at the floor paying negative carry.
2. **Phase 2 — Pre-Ignition Stealth Absorption ($t - 1\text{h}$):**
   - Price compresses tightly at the shelf floor ($\text{72h Range} \le 18\%$) while **Taker Market Buy Ratio surges $\ge 58\%$ ($\ge \text{P90}$)** on quiet headline volume.
3. **Phase 3 — Bar 0 Ignition Shock ($t = 0$):**
   - Instantaneous **Volume Shock $\ge 15\times - 35\times$ ($\ge \text{P99}$)** and **Trade Count Velocity $\ge 10\times - 20\times$ ($\ge \text{P99}$)**.
   - Candle closes near its absolute high (**Upper Wick $\le 10\%$**).
   - **Flat-OI Invariant:** Token Open Interest remains flat ($\pm 3\%$) on Bar 0 as aggressive market buys clear resting limit sell walls, before exploding $3\times$ to $5\times$ in Bars 1–5.
4. **Phase 4 — Mid-Run Shakeout Retest (HOLD / ADD Rule):**
   - When price pulls back $-10\%$ to $-18\%$ after the first impulse (`Oct 8 13:00–16:00`), **DO NOT EXIT** if:
     - **Token OI expands to a new high** during the dip (shorts aggressively adding at the bottom of the pullback).
     - **Whale L/S continues falling** ($\Delta L/S < 0$ during the dip).
     - **8h Funding remains extreme negative** ($\le -0.20\%$ to $-0.89\%$).
     - **Taker Buy Ratio holds $\ge 50.0\%$**.

---

## 3. The 6 Quantitative Climax EXIT Signatures (Take-Profit Rules)

When evaluating an active squeeze runner (`MFE >= +30%`), trigger a **Full Climax Market Exit** when $\ge 3$ of the following 6 exhaustion signatures fire simultaneously:

1. **Signature 1 — Climax Pinbar Upper Wick ($\ge 75\% - 85\%$):**
   - A new cycle price high is immediately rejected within the same 1h bar, leaving an **Upper Wick $\ge 75\%$** of total candle range (`OGN` printed an **85% wick** at \$0.0536 and an **80% wick** on the \$0.0495 secondary retest).
2. **Signature 2 — Bearish Volume & Trade Count Divergence ($\le -50\%$ Drop vs. Wave 1 Peak):**
   - Price makes a higher high, but 1h Volume and Trade Count are **$\ge 50\%$ lower** than the earlier impulse wave (`OGN` Wave 1 @ \$0.0447 had \$116.5M vol; Wave 3 Peak @ \$0.0536 had \$44.2M vol — a **-62% volume divergence**).
3. **Signature 3 — Token Open Interest Bearish Divergence:**
   - Price prints a higher high, but **Token Open Interest is lower than its earlier peak** (`OGN` Token OI peaked at 456.5M at `15:00 UTC` and dropped to 433.0M at the `20:00 UTC` price peak). No new shorts are entering; fuel is depleted.
4. **Signature 4 — The 10x Funding Rate Normalization Collapse:**
   - Extreme negative funding ($\le -0.40\%$ to $-0.89\%$) suddenly **collapses toward zero ($\ge -0.04\%$)** at the price high (`OGN` funding snapped from **-0.400% to -0.037%** at `20:00 UTC`). The perpetual discount basis has vanished because spot buying stopped and short liquidations finished.
5. **Signature 5 — Sub-50% Taker Buy Breakdown + Sub-1.5x Volume Velocity:**
   - Immediately following the climax wick, a red breakdown candle prints with **Taker Buy $< 49.5\%$** and **Volume Shock collapsing to $\le 1.2\times$** the 24h median.
6. **Signature 6 — Whale L/S Inflection Bottom (Rising $L/S$ + Falling OI + Falling Price):**
   - Whale L/S stops falling, hits its floor (`0.42`), and **turns upward ($0.42 \rightarrow 0.82$)** while **Token OI bleeds ($-20\%$ to $-40\%$)** and price declines. Whales who shorted the top are covering their shorts in profit into retail long liquidations.

---

## 4. Decision Matrix: Mid-Run Dip (Hold/Add) vs. Climax Top (Full Exit)

| Diagnostic Dimension | Mid-Run Shakeout (`Oct 8 15:00` @ \$0.0388) $\rightarrow$ **HOLD / ADD** | Climax Peak (`Oct 8 20:00–21:00` @ \$0.0536) $\rightarrow$ **FULL EXIT** |
| :--- | :--- | :--- |
| **Candle Upper Wick** | Moderate ($35\% - 46\%$) | **Extreme Pinbar Rejection ($80\% - 85\%$)** 🚨 |
| **Token Open Interest** | **New Highs** ($398\text{M} \rightarrow 456.5\text{M}$) | **Lower High Divergence** ($433\text{M}$) $\rightarrow$ **$-38\%$ Unwind** 🚨 |
| **Whale L/S Trajectory** | **Falling Sharply** ($0.59 \rightarrow 0.52$) | **Bottoms ($0.42$) and Turns UP** ($0.42 \rightarrow 0.82$) 🚨 |
| **8h Funding Rate** | **Extreme Negative Carry** ($-0.893\% \rightarrow -0.400\%$) | **Collapses 10x Toward Zero** ($-0.037\% \rightarrow -0.019\%$) 🚨 |
| **Volume vs. Prior Wave** | Sustained ($48\times - 71\times$ median) | **$-62\%$ Bearish Divergence** ($3.1\times \rightarrow 0.9\times$ median) 🚨 |

---

## 5. The Multi-Timeframe `200 EMA` Convergence Law (`LEADING` vs. `LAGGING` Candidate Provider)

### Why `OGN`, `MAGIC`, `GTC`, `CTSI`, `BAT`, and `ARPA` Flew While `ERA` Struggled:
1. **`LEADING` Candidates (`200-EMA Merged & Reclaimed` — True Flyers):**
   - **Rule:** `Price vs 1D EMA 200 >= -3.0%` **AND** `1h EMA 200 vs 1D EMA 200 Gap >= -15.0%`.
   - **Physics:** Assets that bottomed in June/July and formed Higher Lows in August and September (`OGN`, `GTC`, `CTSI`, `BAT`, `ARPA`, `KAIA`, `SAND`, `C98`, `MAGIC`, `RLC`, `STRK`, `LUMIA`) compressed their **`1h EMA 200`**, **`4h EMA 200`**, and **`1D EMA 200` (Daily 200 EMA)** into a tight ribbon underneath price (on `OGN` at `Oct 8 08:00`, `1h EMA 200` was `$0.02129` and `1D EMA 200` was `$0.02129` — a `0.0%` gap!). When Bar 0 ignites, price breaks above all timeframe `200 EMAs` simultaneously with zero macro moving-average resistance overhead.
2. **`LAGGING` Candidates (`Sub-1D-200-EMA Counter-Trend` — Scalp to Ceiling Only):**
   - **Rule:** `Price vs 1D EMA 200 < -3.0%` **OR** `1h EMA 200 vs 1D EMA 200 Gap < -15.0%`.
   - **Physics:** Assets that kept making new lows in August (`ERA`, `WAL`) have their `1h/4h EMA 200` stranded `-35%` to `-60%` below a descending **`1D SMA 200` and `1D EMA 200`**. Even when they print massive Bar 0 volume shocks and `-0.80%` to `-1.37%` negative funding, they slam into the overhead `1D SMA 200` / `1D EMA 200` wall (`ERA` rejected at `$0.0912` right under its `1D SMA 200` at `$0.0940`, and failed 10 out of 11 historical episodes while below `1D EMA 200`). Never bag-hold a `LAGGING` candidate; harvest profits into the `1D SMA 200` / `1D EMA 200` ceiling.

---

## 6. The Two-Stage Macro Breakdown Low Magnet Law (`Nov 2025` $\rightarrow$ `Sep 2025`)

Full-universe verification across all 652 liquid shards proves that October 2026 supernovas follow a deterministic two-stage macro price-memory roadmap:
1. **Stage 1 Gateway & Support Flip (`Nov 2025 Breakdown Low` — `[M1]`):**
   - Breaking above the **November 2025 Breakdown Low** (`$0.0325` on `OGN`, `$0.1000` on `MAGIC`, `$0.0378` on `CTSI`, `$0.0138` on `ARPA`, `$0.0230` on `C98`, `$0.0716` on `KAIA`) enters a vertical historical waterfall vacuum where almost zero horizontal volume profile exists.
   - After climaxing at the `Sep 2025 Low`, both `OGN` (`$0.0350` vs `$0.0325`) and `MAGIC` (`$0.1062` vs `$0.1000`) pulled back to flip their **Nov 2025 Breakdown Low** into structural support.
2. **Stage 2 Terminal Supernova Climax Magnet (`Sep 2025 Breakdown Low` — `[M2]`):**
   - Major October 2026 short-squeeze rallies terminated their exact blow-off tops at their **September 2025 Breakdown Low**:
     - **`OGN/USDT`:** Sep 2025 Low = **\$0.0538** | Oct 2026 Peak = **\$0.0536** (**`-0.3%` exact hit!**)
     - **`GTC/USDT`:** Sep 2025 Low = **\$0.2460** | Oct 2026 Peak = **\$0.2488** (**`+1.1%` exact hit!**)
     - **`MAGIC/USDT`:** Sep 2025 Low = **\$0.1614** | Oct 2026 Peak = **\$0.1637** (**`+1.4%` exact hit!**)
     - **`RAYSOL/USDT`:** Sep 2025 Low = **\$2.4954** | Oct 2026 Peak = **\$2.5740** (**`+3.1%` exact hit!**)
     - **`GRIFFAIN/USDT`:** Sep 2025 Low = **\$0.0279** | Oct 2026 Peak = **\$0.0291** (**`+4.2%` exact hit!**)
     - **`VELODROME/USDT`:** Sep 2025 Low = **\$0.0410** | Oct 2026 Peak = **\$0.0400** (**`-2.5%` front-run!**)
     - **`AERO/USDT`:** Sep 2025 Low = **\$0.9606** | Oct 2026 Peak = **\$0.9319** (**`-3.0%` front-run!**)
