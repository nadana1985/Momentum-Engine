"""
Kronos V12: Counterfactual Telemetry & Veto Alpha Recorder (telemetry_v12.py)
Implements 'No Silent Drops' architecture to audit risk gates and quantify Veto Alpha.
Writes to isolated path: telemetry/veto_telemetry.parquet.
"""

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Optional
import numpy as np
import pandas as pd


@dataclass(frozen=True)
class TelemetryRecord:
    """Immutable data record for every candidate signal evaluation."""
    timestamp: pd.Timestamp
    asset: str
    tier: str
    status: str            # 'ACTIVE' or 'VETOED'
    veto_gate: str         # 'None', 'Macro Bear Veto', 'Turnover Velocity', 'Whale Firewall', 'Funding Cap', 'Cooldown'
    candidate_setup: str   # 'Continuation Breakout', 'Bear-Trap V-Reclaim', 'Squeeze Hunter'
    price: float
    turnover: float
    ls_ratio: float
    funding_rate: float
    btc_macro_bull: bool
    ret_24h_fwd: float = 0.0
    ret_48h_fwd: float = 0.0
    ret_72h_fwd: float = 0.0
    mfe_72h_fwd: float = 0.0
    mae_72h_fwd: float = 0.0
    fwd_hours_elapsed: int = 0
    is_complete_24h: bool = False
    is_complete_72h: bool = False
    is_in_flight: bool = False
    is_dodged_bullet: bool = False
    is_missed_opportunity: bool = False

    def __post_init__(self):
        assert self.status in ('ACTIVE', 'VETOED', 'SHADOW_ARMED'), f"Invalid status: {self.status}"
        assert self.price > 0.0, "price must be positive"


class TelemetryCollector:
    """Collector and forensic analyzer for candidate and counterfactual signals."""

    def __init__(self, storage_dir: Optional[Path] = None):
        if storage_dir is None:
            storage_dir = Path(__file__).resolve().parent.parent / "telemetry"
        self.storage_dir = storage_dir
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.telemetry_file = self.storage_dir / "veto_telemetry.parquet"
        self.records: List[TelemetryRecord] = []

    def log_signal(self, record: TelemetryRecord):
        """Append an immutable telemetry record."""
        self.records.append(record)

    def to_dataframe(self) -> pd.DataFrame:
        """Converts collected records into a pandas DataFrame."""
        if not self.records:
            return pd.DataFrame()
        return pd.DataFrame([asdict(r) for r in self.records])

    def load_from_disk(self) -> pd.DataFrame:
        """Loads persisted telemetry from isolated parquet storage."""
        if self.telemetry_file.exists():
            return pd.read_parquet(self.telemetry_file)
        return pd.DataFrame()

    def save(self):
        """Persists telemetry to isolated parquet storage."""
        df = self.to_dataframe()
        if not df.empty:
            df.to_parquet(self.telemetry_file, index=False)

    @staticmethod
    def enrich_forward_returns(df_telemetry: pd.DataFrame, shard_df: pd.DataFrame) -> pd.DataFrame:
        """
        Retrospectively enriches vetoed signals with 24h/48h/72h forward returns
        and forward MFE/MAE from the shard price series.
        Properly flags in-flight observation windows where < 72 hours have elapsed.
        """
        if df_telemetry.empty or shard_df.empty:
            return df_telemetry

        enriched = df_telemetry.copy()
        c = shard_df['close']
        h = shard_df['high']
        l = shard_df['low']

        for idx, row in enriched.iterrows():
            ts = row['timestamp']
            if ts not in shard_df.index:
                continue

            loc = shard_df.index.get_loc(ts)
            entry_px = row['price']
            total_bars = len(shard_df)
            n_fwd = max(0, total_bars - 1 - loc)

            is_complete_24h = (n_fwd >= 24)
            is_complete_72h = (n_fwd >= 72)
            is_in_flight = not is_complete_72h

            # Forward slices
            fwd_24 = c.iloc[loc+1 : loc+25] if is_complete_24h else (c.iloc[loc+1 :] if n_fwd > 0 else pd.Series(dtype=float))
            fwd_48 = c.iloc[loc+1 : loc+49] if (n_fwd >= 48) else (c.iloc[loc+1 :] if n_fwd > 0 else pd.Series(dtype=float))
            fwd_72 = c.iloc[loc+1 : loc+73] if is_complete_72h else (c.iloc[loc+1 :] if n_fwd > 0 else pd.Series(dtype=float))
            fwd_h72 = h.iloc[loc+1 : loc+73] if is_complete_72h else (h.iloc[loc+1 :] if n_fwd > 0 else pd.Series(dtype=float))
            fwd_l72 = l.iloc[loc+1 : loc+73] if is_complete_72h else (l.iloc[loc+1 :] if n_fwd > 0 else pd.Series(dtype=float))

            ret_24 = (fwd_24.iloc[-1] - entry_px) / entry_px if len(fwd_24) > 0 else 0.0
            ret_48 = (fwd_48.iloc[-1] - entry_px) / entry_px if len(fwd_48) > 0 else 0.0
            ret_72 = (fwd_72.iloc[-1] - entry_px) / entry_px if len(fwd_72) > 0 else 0.0

            mfe_72 = ((fwd_h72.max() - entry_px) / entry_px) if len(fwd_h72) > 0 else 0.0
            mae_72 = ((fwd_l72.min() - entry_px) / entry_px) if len(fwd_l72) > 0 else 0.0

            enriched.at[idx, 'fwd_hours_elapsed'] = int(n_fwd)
            enriched.at[idx, 'is_complete_24h'] = bool(is_complete_24h)
            enriched.at[idx, 'is_complete_72h'] = bool(is_complete_72h)
            enriched.at[idx, 'is_in_flight'] = bool(is_in_flight)

            enriched.at[idx, 'ret_24h_fwd'] = ret_24
            enriched.at[idx, 'ret_48h_fwd'] = ret_48
            enriched.at[idx, 'ret_72h_fwd'] = ret_72
            enriched.at[idx, 'mfe_72h_fwd'] = mfe_72
            enriched.at[idx, 'mae_72h_fwd'] = mae_72

            # Classification:
            # When horizon is complete:
            #   Dodged bullet: price dropped by >= 10% or forward 72h return was negative
            #   Missed opportunity: forward MFE was >= +20%
            # When in-flight (< 72h):
            #   Cannot be classified as Dodged Bullet yet because observation is incomplete.
            #   Can only be flagged as Missed Opportunity if price ALREADY spiked >= +20%.
            if is_complete_72h:
                enriched.at[idx, 'is_dodged_bullet'] = bool((mae_72 <= -0.10) or (ret_72 < 0.0))
                enriched.at[idx, 'is_missed_opportunity'] = bool(mfe_72 >= 0.20)
            else:
                enriched.at[idx, 'is_dodged_bullet'] = False
                enriched.at[idx, 'is_missed_opportunity'] = bool(mfe_72 >= 0.20)

        return enriched

    @staticmethod
    def compute_veto_alpha_summary(df: pd.DataFrame) -> Dict[str, float]:
        """
        Computes Veto Alpha strictly on COMPLETED observation windows:
        Saved Losses: Sum of negative returns avoided on dodged bullets
        Missed Upside: Sum of positive returns lost on missed opportunities
        Net Veto Alpha = Saved Losses - Missed Upside
        """
        if df.empty:
            return {
                'total_vetoes': 0,
                'completed_vetoes': 0,
                'in_flight_vetoes': 0,
                'dodged_bullets': 0,
                'missed_opportunities': 0,
                'saved_losses_pct': 0.0,
                'missed_upside_pct': 0.0,
                'net_veto_alpha_pct': 0.0,
                'efficiency_ratio': 0.0
            }

        vetoed = df[df['status'] == 'VETOED'].copy()
        if vetoed.empty:
            return {
                'total_vetoes': 0,
                'completed_vetoes': 0,
                'in_flight_vetoes': 0,
                'dodged_bullets': 0,
                'missed_opportunities': 0,
                'saved_losses_pct': 0.0,
                'missed_upside_pct': 0.0,
                'net_veto_alpha_pct': 0.0,
                'efficiency_ratio': 0.0
            }

        # Segregate completed vs in-flight
        if 'is_complete_72h' in vetoed.columns:
            completed = vetoed[vetoed['is_complete_72h'] == True]
            in_flight = vetoed[vetoed['is_complete_72h'] == False]
        else:
            completed = vetoed
            in_flight = vetoed.iloc[0:0]

        dodged = completed[completed['is_dodged_bullet']]
        missed = completed[completed['is_missed_opportunity']]

        # Saved losses: magnitude of drawdown or negative return avoided
        saved_losses = np.abs(dodged['mae_72h_fwd'].clip(upper=0.0)).sum() * 100.0
        # Missed upside: positive MFE sacrificed
        missed_upside = missed['mfe_72h_fwd'].sum() * 100.0

        net_alpha = saved_losses - missed_upside
        efficiency = (len(dodged) / len(completed) * 100.0) if len(completed) > 0 else 0.0

        return {
            'total_vetoes': len(vetoed),
            'completed_vetoes': len(completed),
            'in_flight_vetoes': len(in_flight),
            'dodged_bullets': len(dodged),
            'missed_opportunities': len(missed),
            'saved_losses_pct': round(saved_losses, 2),
            'missed_upside_pct': round(missed_upside, 2),
            'net_veto_alpha_pct': round(net_alpha, 2),
            'efficiency_ratio': round(efficiency, 2)
        }
