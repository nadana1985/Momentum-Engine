# KRONOS V2 AI Agent System Skills (Consolidated)

This document compiles the core system skills and sovereign rules required to guide any AI agent (such as Claude, Gemini, or ChatGPT) when writing or modifying code in the **KRONOS V2** repository. These rules are designed to prevent code/mathematical drift, maintain strict type boundaries, and protect the core logic.

---

## 0. The Sovereign Rules (Sovereignty Paradigm)

**Description:** Dictates that the system remains purely configuration-driven and reproducible, forbidding any hardcoded constants or strategy states in active code.

### Core Rules

1. **The Zero-Literals Rule (Strict Config-Only):**
   * **Rule:** No active Python code (`.py` files) may contain hardcoded parameter values, thresholds, lookback windows, fee rates, model IDs, symbol strings (e.g., `"ETH/USDT"`), or file paths.
   * **Implementation:** All values must be dynamically loaded from configurations (via the `KRONOS_PARAMS_PATH` environment variable) and injected at runtime.
   * **Enforcement:** Checked automatically by the structural audit scanner (`scripts/v5_structural_audit.py`).

2. **Causality Barrier Enforcement:**
   * **Rule:** All rolling mathematical estimators and overrides (e.g., empirical quantiles, volatility, or regimes) must be strictly causal.
   * **Implementation:** Calculations at time index $t$ must only look at historical data strictly up to index $t-1$. No future-leakage is allowed.

3. **Dynamic Parameter Tiering (Liquidity Adapting):**
   * **Rule:** The pipeline parameters must adapt to the liquidity of the asset.
   * **Implementation:** Symbols are mapped through `liquidity_tiers.yaml` (Tier 1 to Tier 5), and the system dynamically updates lookback windows ($W$) and precision margins ($\epsilon$) based on the asset's tier.

4. **Independent Fitting (Reproducibility):**
   * **Rule:** Statistical models (like HMMs or clustering ontologies) must not share rolling states or use warm-starts that introduce path-dependent memory drift. 
   * **Implementation:** Models are refit independently from scratch at configured bar intervals to ensure clean reproducibility.

---

## 1. Interface Compliance & Validation Skill

**Description:** Enforces strict type boundaries and prevents AI agents from modifying variable names, types, or mutations across pipeline layers.

### Core Rules

1. **Strict Immutability:**
   * Every data transfer object (DTO) must be declared as a frozen dataclass: `@dataclass(frozen=True)`.
   * Under no circumstances should dictionary keys be modified in-place or passed as mutable state.

2. **Validation on Initialization:**
   * Every dataclass must define `__post_init__(self)` to assert value ranges and types immediately upon creation (e.g., confidence must be $\in [0, 1]$).
   * Use explicit Python typing (`typing.Dict`, `typing.Optional`, etc.).

3. **Zero Inline Literals:**
   * All parameters, thresholds, and limits must be loaded from configurations (via `MarketContext` or configuration files) and injected. No hardcoded magic numbers.

4. **`AlphaSignal` Must Include All 8 Missing Fields:**
   * The production parquet `ETH_USDT_historical_stream.parquet` is missing: `current_regime`, `predicted_direction`, `preclamp_confidence`, `structural_slots`, `computed_points`. These fields are computed in the legacy miner but never serialized.
   * The frozen `AlphaSignal` dataclass MUST include: `current_regime: str`, `predicted_direction: str`, `preclamp_confidence: float`, `structural_slots: Dict[str, float]`, `computed_points: Dict[str, Any]`, `is_signal_trigger: bool`, `neural_conviction: float`, `history_length: int`.

5. **`__post_init__` Must Assert `slot_39` Unit Range:**
   * If the dataclass or telemetry record contains a `mad_vol` field, assert `0.0001 < mad_vol < 0.20`. A value near 2,200 indicates the Point 48 unit bug (price MAD vs return MAD) was not fixed.

---

## 2. Adapter Pattern Integration Skill

**Description:** Guidelines for building wrappers (adapters) around legacy codebase features (like data ingestion or liquidity classifiers) to protect their internal rules from AI modification.

### Core Rules

1. **Isolation of Legacy Modules:**
   * Treat legacy files (`kronos/`, `config/`, etc.) as external third-party libraries. Do not edit their code.
   
2. **Standard Output Mapping:**
   * Every adapter must ingest legacy DataFrame/dict outputs and map them directly to the new `MarketContext` or `AlphaSignal` DTOs.
   
3. **Graceful Degradation:**
   * If a legacy module fails, the adapter must log the error and degrade gracefully (returning clean fallbacks rather than passing internal tracebacks down the clean pipeline).

4. **`InsufficientDataError` Contract:**
   * The ingestion adapter (`kronos_v2/adapters/data_adapter.py`) must raise `InsufficientDataError` if the legacy engine returns a DataFrame with fewer bars than `neural['min_history']`. Do NOT silently pass partial DataFrames downstream.

5. **Scope Adapters to 14 Tier 1 Points Only:**
   * The bridge adapter for override points must cover exactly the 14 currently executed points: `[01, 02, 06, 11, 15, 28, 48, 52, 56, 57, 64, 66, 69, 72]`. Do NOT attempt to bridge all 100 phantom columns. Points 73–100 are 100% NULL in the production database.

---

## 3. Clean-Room Math Reconstruction Skill

**Description:** Guidelines for isolating legacy mathematical kernels into pure, side-effect-free functions, verifying them with tests, and avoiding duplicate implementation.

### Core Rules

1. **Pure Functions Only:**
   * All mathematical estimators and signal normalizers must be "pure functions" (outputs depend strictly on inputs, no side effects, no database/config access).
   
2. **Golden Snapshot Testing:**
   * For every math function extracted, the agent must write a unit test inside `kronos_v2/tests/` using pre-calculated mock input/output pairs to verify mathematical equality.
   
3. **No Zero-Series Fallbacks:**
   * If a mathematical estimation node fails (e.g. Numba matrix math throws exception), the fallback must return a domain-specific conservative estimate (like standard deviation for volatility) instead of returning `0.0`.

4. **Estimator Independence — No Shared Mutation:**
   * The 4 legacy volatility estimators (Points 48, 52, 56, 57) mutate a shared `_raw_std_vol` variable sequentially. In `kronos_v2/estimators.py`, each estimator MUST compute from raw OHLCV independently with its own explicit lookback window. Do not share or mutate intermediate results across estimators.

5. **Golden Snapshot for `slot_39` Unit Bug:**
   * The mandatory golden snapshot test for Point 48 (MAD vol) must assert the output is a percentage return (not a price): `assert 0.0001 < mad_vol < 0.20`. Historical parquet shows `slot_39` mean = 2,200 (ETH price in USD) — this is the confirmed unit bug. Use `df['close'].pct_change().mad()`, not `df['close'].mad()`.

---

## 4. Counterfactual Telemetry Collector Skill

**Description:** Guidelines for building the logging, telemetry, and retrospective tracking layers to measure opportunity cost of vetoes and calculate Veto Alpha.

### Core Rules

1. **No Silent Drops:**
   * Every trade signal, whether executed, scaled down, or vetoed, must be logged with a status tag (`status="ACTIVE"` vs `status="VETOED"`).
   
2. **Retrospective Enrichment:**
   * Telemetry must support loading past vetoed signals and enriching them with forward returns (e.g. 24h asset return post-signal) to evaluate what would have happened.
   
3. **Veto Alpha Calculation:**
   * Provide built-in methods to compute Veto Alpha ($\text{Sharpe}_{\text{actual}} - \text{Sharpe}_{\text{counterfactual}}$) to statically validate the risk gate thresholds.

4. **Telemetry Path Isolation (Critical Safety Constraint):**
   * The `TelemetryCollector` must write logs to `kronos_v2/telemetry/`. Do NOT write logs to the legacy `signatures/` folder. Writing telemetry records to the signatures folder will trigger file-collision false positives in the legacy miner's shard worker resumption check (`if os.path.exists(sig_path): return {"status": "skipped"}`), causing the system to silently skip mining runs.

5. **Historical Price Source (Veto Alpha Calculations):**
   * Retrieve retrospectively evaluated price data directly from `label_forward_return_24h` and `label_forward_return_48h` columns in the historical parquet database (`ETH_USDT_historical_stream.parquet`). Do not build a live network price feed for calculating retroactive return metrics.

---

## 5. Institutional Support & Resistance Strategy (சிறந்த உத்தி) Skill

**Description:** Standard procedure for extracting institutional Support/Resistance tiers and tactical execution plans combining Volume Profile, Open Interest (OI), and Whale L/S ratios.

### Core Rules

1. **Deterministic Script Mandate:**
   * Never run ad-hoc loops or heuristic calculations.
   * Always execute `python scripts/calculate_best_sr_strategy.py --symbol <ASSET> [--days <N>]`.

2. **The Price-Action + Positioning Duality:**
   * Volume Profile determines the **"WHERE"** (Point of Control POC, Value Area VAH/VAL, High-Volume Shelves).
   * Open Interest and Top Trader Long/Short ratio determine the **"WHO & WHY"** (Who is trapped? Is this shelf an accumulation floor or an exit wall?).

3. **Classification Integrity:**
   * Support: S1 (Immediate Absorption / Flush Low), S2 (Major Structural Base), S3 (Macro Cycle Low).
   * Resistance: R1 (Primary Point of Control POC / Trapped Supply), R2 (Double-Top / Distribution Shelf), R3 (Macro Cycle Climax High).

4. **Whale Long/Short Interpretation:**
   * $L/S < 0.85$: Institutional Whale Short Trap (Parabolic squeeze potential).
   * $L/S > 2.20$: Crowded Long Euphoria (Fragile / Elevated long squeeze risk).

---

## 6. Pre-Pump Coiled Squeeze Scanner (OGN Trait at t=0) Skill

**Description:** Standard procedure for scanning the cryptocurrency universe for pre-pump coiled squeeze setups at $t=0$ before parabolic breakouts ignite.

### Core Rules

1. **Deterministic Script Mandate:**
   * Never run ad-hoc loops or heuristic queries.
   * Always execute `python scripts/scan_pre_pump_coils.py --scan` or `python scripts/scan_pre_pump_coils.py --symbol <ASSET>`.

2. **The 5 Pre-Pump Invariants (Empirically Verified on OGN):**
   * Severe Negative Funding ($\le -0.02\%$ per 8h, often $\le -0.20\%$).
   * Deep Shelf Compression ($72\text{h Range} \le 25\%$).
   * Whale L/S Contraction ($\Delta L/S < 0$ or $L/S \le 1.80$).
   * Meaningful Liquidity ($\text{OI} \ge \$1\text{M}$ USD).
   * Pre-Breakout State ($\text{Ret}_{24\text{h}} \le +8\%$, unextended).

3. **Readiness Scoring:**
   * Score $\ge 70$: `PRIME_COIL (READY FOR IGNITION)`.
   * Score $\ge 50$: `COILING (WATCHLIST)`.


