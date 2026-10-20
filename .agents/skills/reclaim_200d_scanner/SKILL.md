---
name: reclaim_200d_scanner
description: Instructions and standard procedure for screening the cryptocurrency universe for 200-day EMA Higher-Low Retest and Reclaim setups (Book 4 Engine), identifying active reclaim triggers, armed pullback stages, and Bitcoin macro regime confluence.
---

# 200-Day EMA Retest & Reclaim Scanner Skill (Book 4 Engine)

This skill teaches the AI agent how to detect, analyze, and screen for **200-Day EMA Retest & Reclaim setups** (the Kronos V12.6 Book 4 Engine) using the deterministic production tool [`scripts/scan_200d_reclaim_setups.py`](file:///f:/kronos_v1_alt/scripts/scan_200d_reclaim_setups.py).

---

## 1. When to Use This Skill
Activate this skill whenever the user asks to:
- Screen the universe for tokens breaking out, touching, or reclaiming their **200-day EMA** ($1\text{D EMA}_{200}$ / 4,800 1h bars).
- Evaluate tokens that experienced a $-10\%$ to $-20\%$ pullback after hitting their 200d EMA (e.g. `CTSI`, `MAGIC`, `OGN`, `C98`, `ERA`, `ARKM`).
- Check whether an asset is in an **`ARMED_IN_RETEST`** state (holding Higher Low above pre-pump base) or **`RECLAIM_TRIGGER_NOW`** state.
- Check the **Bitcoin Macro Regime Confluence** (`BTC_BULL_CONVERGENCE` vs `BTC_BEAR_ISOLATED`) and position sizing multipliers ($1.0\times$ vs $0.50\times$).
- Request a trade architecture tear sheet for a specific symbol (Entry, Resting Stop at Retest Low, Two-Tier Target Cap, Risk/Reward).

---

## 2. Deterministic Command-Line Execution
Agents must **NEVER** write ad-hoc scanning scripts or loops. Always use the canonical tool:

```bash
# 1. Full universe scan across all liquid shards:
python scripts/scan_200d_reclaim_setups.py --scan

# 2. Inspect a specific symbol tear sheet (e.g. MAGIC, CTSI, OGN, C98):
python scripts/scan_200d_reclaim_setups.py --symbol MAGIC
python scripts/scan_200d_reclaim_setups.py --symbol CTSI
python scripts/scan_200d_reclaim_setups.py --symbol C98

# 3. Filter universe scan by asset tier (Tier 1, Tier 2, Tier 3):
python scripts/scan_200d_reclaim_setups.py --scan --tier "Tier 2"

# 4. Historical point-in-time verification:
python scripts/scan_200d_reclaim_setups.py --symbol MAGIC --as-of "2026-10-09 06:00:00"

# 5. Machine-readable JSON output:
python scripts/scan_200d_reclaim_setups.py --symbol MAGIC --json
python scripts/scan_200d_reclaim_setups.py --scan --json
```

---

## 3. The 4 Setup Stages & Trading Rules

1. **`🚀 RECLAIM_TRIGGER_NOW` (Stage 1 - Long Entry Signal):**
   - **Criteria:** Token touched 200d EMA after $\ge 30$ days below, absorbed a $-10\%$ to $-20\%$ retest dip holding above the base low, and the current 1-hour candle is closing **ABOVE** the 200-day EMA.
   - **Historical Performance:** **83.2% Win Rate**, Mean MFE **+72.7%**, Log PF **4.809**.
   - **Execution (Study S-BE Two-Tranche Architecture):** Enter Long at market close. Stop at Retest Low.
     * **Tranche 1 (50% Position):** Limit exit at $+20\%$ target cap ($\min(1.20 \times \text{entry}, \text{nov25\_low})$).
     * **Tranche 2 (50% Position):** Once Tranche 1 executes, ratchet stop to Breakeven ($\text{Entry} \times 1.00$) and trail with rolling Donchian floor (unlocks $+995\%$ Net Log Alpha Lift, surging Log PF to 5.648 and PnL PF to 7.113).

2. **`⏳ ARMED_IN_RETEST` (Stage 2 - Pre-Pump Watchlist):**
   - **Criteria:** Touched 200d EMA in the last 14 days, currently in healthy pullback ($-8\%$ to $-20\%$) holding Higher Low above base.
   - **Execution:** DO NOT ENTER YET. Place on high-priority watchlist. Prepare resting stop level at the retest dip low.

3. **`⚠️ FIRST_TOUCH_CANARY` (Stage 3 - Do Not Enter):**
   - **Criteria:** Asset just touched the 200-day EMA within the last 24 hours after $\ge 30$ days below.
   - **The Naive Touch Law:** First touches have a **45.9% failure rate**. DO NOT ENTER. Wait for the 48h to 96h retest pullback.

4. **`❌ FAILED_REJECTION` (Dead Bull Trap):**
   - **Criteria:** Retest dip collapsed $> -25\%$, breached the pre-pump base low, or took $> 120$ hours to bottom.
   - **Execution:** Reject / Default to Cash. 81.4% of these tokens are falling knives that bleed out.

---

## 4. Bitcoin Macro Regime Sizing Overlay

- **`BTC_BULL_CONVERGENCE` ($\text{BTC} > \text{EMA}_{200\text{d}}$):**
  - Allocate **$100\%$ Full Position Size ($1.0\times$)**.
  - Historical failure rate on confluence reclaims is just **$5.8\% - 16.8\%$**.
- **`BTC_BEAR_ISOLATED` ($\text{BTC} \le \text{EMA}_{200\text{d}}$):**
  - Allocate **$50\%$ Defensive Position Size ($0.50\times$)**.
  - Enforce strict Two-Tier target cap ($\approx +15\%$ to $+20\%$) to capture idiosyncratic short squeezes (`TRB`, `LPT`, `OGN`) while protecting against macro beta air-pockets.
