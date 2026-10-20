---
name: interface_compliance_and_validation
description: Guidelines for enforcing strict, type-safe, immutable API contracts and dataclasses in the quant pipeline to prevent AI agentic drift.
---

# Interface Compliance & Validation Skill

This skill enforces strict type boundaries and prevents AI agents from modifying variable names, types, or mutations across pipeline layers.

## Core Rules

1. **Strict Immutability:**
   * Every data transfer object (DTO) must be declared as a frozen dataclass: `@dataclass(frozen=True)`.
   * Under no circumstances should dictionary keys be modified in-place or passed as mutable state.

2. **Validation on Initialization:**
   * Every dataclass must define `__post_init__(self)` to assert value ranges and types immediately upon creation (e.g., confidence must be ∈ [0, 1]).
   * Use explicit Python typing (`typing.Dict`, `typing.Optional`, etc.).

3. **Zero Inline Literals:**
   * All parameters, thresholds, and limits must be loaded from configurations (via `MarketContext` or configuration files) and injected. No hardcoded magic numbers.

4. **`AlphaSignal` Must Include All 8 Missing Fields (Data-Verified):**
   * The production parquet `ETH_USDT_historical_stream.parquet` is missing: `current_regime`, `predicted_direction`, `preclamp_confidence`, `structural_slots`, `computed_points`. These fields are computed in the legacy miner but never serialized.
   * The frozen `AlphaSignal` dataclass MUST include: `current_regime: str`, `predicted_direction: str`, `preclamp_confidence: float`, `structural_slots: Dict[str, float]`, `computed_points: Dict[str, Any]`, `is_signal_trigger: bool`, `neural_conviction: float`, `history_length: int`.

5. **`__post_init__` Must Assert `slot_39` Unit Range:**
   * If the dataclass or telemetry record contains a `mad_vol` field, assert `0.0001 < mad_vol < 0.20`. A value near 2,200 indicates the Point 48 unit bug (price MAD vs return MAD) was not fixed.
