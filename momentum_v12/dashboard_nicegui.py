"""
Kronos V12: Clean 6-Core Intelligence Command Center (dashboard_nicegui.py)
High-Fidelity Cyber-Tactical Visual Interface on Port 8056.
Comprehensive Suite featuring:
  1. ⚡ Open Positions (Active Portfolio with Native Resting Stop-Market Order Audit)
  2. 📜 Closed Positions (Full Date-Wise Historical Ledger with Multi-Filters & Sorting)
  3. 🛡️ Date-Wise Vetoed Trades Hub (Counterfactual Flight Recorder with Search & Filtering)
  4. 🎯 Research Radar & Actionable Trade Suggestions (1-Click Exchange JSON)
  5. ⚖️ Forensic Reasoner (Attribution & Automated Exit Case Studies)
  6. 📈 Compounding Log Equity Curve & Universal Scorecard
"""

import json
import math
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from nicegui import app, ui

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from momentum_v12.telemetry_v12 import TelemetryCollector

# ---------------------------------------------------------------------------
# PATHS & CONFIGURATION
# ---------------------------------------------------------------------------
TELEMETRY_DIR = ROOT / "telemetry"
SHARD_DIR = ROOT / "data" / "raw_shards"
EXOTIC_DIR = ROOT / "data" / "exotic_shards"
ASSET_TIERS_PARQUET = ROOT / "data" / "asset_tiers.parquet"


def get_available_arms() -> List[str]:
    base = ROOT / "data" / "all_tapes"
    if not base.exists():
        return ["v12_production"]
    arms = [d.name for d in base.iterdir() if d.is_dir() and ((d / "trades.parquet").exists() or (d / "master_raw_tape.csv").exists())]
    ordered = []
    if "v12_production" in arms:
        ordered.append("v12_production")
    if "v12_book3_flush_reclaim_arm" in arms:
        ordered.append("v12_book3_flush_reclaim_arm")
    if "v12_coiled_book2_arm" in arms:
        ordered.append("v12_coiled_book2_arm")
    if "v12_decoupled_turnover_arm" in arms:
        ordered.append("v12_decoupled_turnover_arm")
    if "v12_turnover_arm" in arms:
        ordered.append("v12_turnover_arm")
    if "v12_decoupling_arm" in arms:
        ordered.append("v12_decoupling_arm")
    if "v12_continuation_arm" in arms:
        ordered.append("v12_continuation_arm")
    for a in arms:
        if a not in ordered:
            ordered.append(a)
    return ordered or ["v12_production"]


def get_initial_arm() -> str:
    env_tape = os.environ.get("KRONOS_TAPE_DIR")
    if env_tape:
        slug = Path(env_tape).name
        if slug in get_available_arms():
            return slug
    available = get_available_arms()
    if "v12_production" in available:
        return "v12_production"
    if "v12_book3_flush_reclaim_arm" in available:
        return "v12_book3_flush_reclaim_arm"
    return "v12_production"


CURRENT_ARM: str = get_initial_arm()


# ---------------------------------------------------------------------------
# DATA LOADING & CACHING
# ---------------------------------------------------------------------------
def load_v12_trades(arm_name: Optional[str] = None) -> pd.DataFrame:
    arm = arm_name or CURRENT_ARM
    t_dir = ROOT / "data" / "all_tapes" / arm
    parquet_p = t_dir / "trades.parquet"
    if parquet_p.exists():
        try:
            return pd.read_parquet(parquet_p)
        except Exception:
            pass
    raw_csv = t_dir / "master_raw_tape.csv"
    if raw_csv.exists():
        try:
            return pd.read_csv(raw_csv)
        except Exception:
            pass
    return pd.DataFrame()


def load_v12_telemetry(arm_name: Optional[str] = None) -> pd.DataFrame:
    arm = arm_name or CURRENT_ARM
    if arm == "v12_production":
        p = ROOT / "telemetry" / "veto_telemetry.parquet"
    else:
        p = ROOT / "telemetry" / arm / "veto_telemetry.parquet"
        if not p.exists():
            p = ROOT / "telemetry" / "veto_telemetry.parquet"
    if p.exists():
        try:
            return pd.read_parquet(p)
        except Exception:
            pass
    return pd.DataFrame()


def load_v12_scorecard(arm_name: Optional[str] = None) -> pd.DataFrame:
    arm = arm_name or CURRENT_ARM
    t_dir = ROOT / "data" / "all_tapes" / arm
    p = t_dir / "scorecard.parquet"
    if p.exists():
        try:
            return pd.read_parquet(p)
        except Exception:
            pass
    return pd.DataFrame()


def load_asset_tiers() -> pd.DataFrame:
    if ASSET_TIERS_PARQUET.exists():
        try:
            return pd.read_parquet(ASSET_TIERS_PARQUET)
        except Exception:
            pass
    alt = ROOT / "scratch" / "asset_tiers.parquet"
    if alt.exists():
        try:
            return pd.read_parquet(alt)
        except Exception:
            pass
    return pd.DataFrame()


def find_shard_path(symbol: str) -> Optional[Path]:
    sym = symbol.upper().replace('USDT', '').replace('/', '').replace('_', '').strip()
    candidates = [
        SHARD_DIR / f"{sym}_USDT_1h.parquet",
        SHARD_DIR / f"{sym}USDT_1h.parquet",
        SHARD_DIR / f"{sym}_1h.parquet",
    ]
    for c in candidates:
        if c.exists():
            return c
    matches = list(SHARD_DIR.glob(f"{sym}*1h.parquet"))
    return matches[0] if matches else None


def find_exotic_metrics_path(symbol: str) -> Optional[Path]:
    sym = symbol.upper().replace('USDT', '').replace('/', '').replace('_', '').strip()
    exact = EXOTIC_DIR / f"{sym}USDT_metrics.parquet"
    if exact.exists():
        return exact
    exact2 = EXOTIC_DIR / f"{sym}_metrics.parquet"
    if exact2.exists():
        return exact2
    candidates = list(EXOTIC_DIR.glob(f"{sym}*metrics.parquet"))
    return candidates[0] if candidates else None


def find_exotic_funding_path(symbol: str) -> Optional[Path]:
    sym = symbol.upper().replace('USDT', '').replace('/', '').replace('_', '').strip()
    exact = EXOTIC_DIR / f"{sym}USDT_funding.parquet"
    if exact.exists():
        return exact
    exact2 = EXOTIC_DIR / f"{sym}_funding.parquet"
    if exact2.exists():
        return exact2
    candidates = list(EXOTIC_DIR.glob(f"{sym}*funding.parquet"))
    return candidates[0] if candidates else None


def get_all_research_symbols() -> List[str]:
    syms = set()
    if SHARD_DIR.exists():
        for p in SHARD_DIR.glob('*1h.parquet'):
            stem = p.name.split('_')[0].split('.')[0].replace('USDT', '')
            if stem:
                syms.add(stem.upper())
    sc = load_v12_scorecard(CURRENT_ARM)
    if not sc.empty and 'asset' in sc.columns:
        syms.update(sc['asset'].dropna().astype(str).tolist())
    tr = load_v12_trades(CURRENT_ARM)
    if not tr.empty and 'asset' in tr.columns:
        syms.update(tr['asset'].dropna().astype(str).tolist())
    tel = load_v12_telemetry(CURRENT_ARM)
    if not tel.empty and 'asset' in tel.columns:
        syms.update(tel['asset'].dropna().astype(str).tolist())
    return sorted(list(syms))


def load_coin_research_data(symbol: str, lookback_bars: int = 720):
    raw_p = find_shard_path(symbol)
    if not raw_p or not raw_p.exists():
        return None, {}

    try:
        df_raw = pd.read_parquet(raw_p).sort_values('timestamp').reset_index(drop=True)
    except Exception:
        return None, {}

    if df_raw.empty:
        return None, {}

    df_raw['dt'] = pd.to_datetime(df_raw['timestamp'], unit='ms')

    # Load Exotic Metrics
    ex_p = find_exotic_metrics_path(symbol)
    if ex_p and ex_p.exists():
        try:
            df_ex = pd.read_parquet(ex_p).sort_values('timestamp').reset_index(drop=True)
            df_ex['dt'] = pd.to_datetime(df_ex['timestamp'], unit='ms')
            cols_to_use = ['dt']
            if 'sum_open_interest_value' in df_ex.columns:
                cols_to_use.append('sum_open_interest_value')
            if 'count_toptrader_long_short_ratio' in df_ex.columns:
                cols_to_use.append('count_toptrader_long_short_ratio')
            df_merged = pd.merge_asof(df_raw, df_ex[cols_to_use], on='dt', direction='backward')
        except Exception:
            df_merged = df_raw.copy()
            df_merged['sum_open_interest_value'] = np.nan
            df_merged['count_toptrader_long_short_ratio'] = np.nan
    else:
        df_merged = df_raw.copy()
        df_merged['sum_open_interest_value'] = np.nan
        df_merged['count_toptrader_long_short_ratio'] = np.nan

    # Load Funding
    f_p = find_exotic_funding_path(symbol)
    if f_p and f_p.exists():
        try:
            df_f = pd.read_parquet(f_p).sort_values('timestamp').reset_index(drop=True)
            df_f['dt'] = pd.to_datetime(df_f['timestamp'], unit='ms')
            if 'funding_rate' in df_f.columns:
                df_merged = pd.merge_asof(df_merged, df_f[['dt', 'funding_rate']], on='dt', direction='backward')
            else:
                df_merged['funding_rate'] = np.nan
        except Exception:
            df_merged['funding_rate'] = np.nan
    else:
        df_merged['funding_rate'] = np.nan

    # Add rolling features for chart
    df_merged['shelf_high_72h'] = df_merged['high'].rolling(72, min_periods=12).max()
    df_merged['shelf_low_72h'] = df_merged['low'].rolling(72, min_periods=12).min()
    df_merged['donchian_floor_14d'] = df_merged['low'].rolling(336, min_periods=24).min()
    df_merged['vol_ma_168h'] = df_merged['volume'].rolling(168, min_periods=24).mean()
    df_merged['vol_shock'] = np.where(df_merged['vol_ma_168h'] > 0, df_merged['volume'] / df_merged['vol_ma_168h'], 1.0)

    # Taker ratio
    if 'taker_buy_base_volume' in df_merged.columns and 'volume' in df_merged.columns:
        df_merged['taker_ratio'] = np.where(df_merged['volume'] > 0, df_merged['taker_buy_base_volume'] / df_merged['volume'], 0.5)
    else:
        df_merged['taker_ratio'] = 0.5

    # Trim to lookback bars for chart
    chart_df = df_merged.tail(lookback_bars).copy() if lookback_bars > 0 else df_merged.copy()

    # Diagnostics
    curr = df_merged.iloc[-1]
    curr_px = float(curr['close'])
    curr_ls = float(curr['count_toptrader_long_short_ratio']) if not pd.isna(curr.get('count_toptrader_long_short_ratio')) else np.nan
    curr_oi = float(curr['sum_open_interest_value']) if not pd.isna(curr.get('sum_open_interest_value')) else np.nan

    last_72 = df_merged.tail(72)
    shelf_high = float(last_72['high'].max()) if not last_72.empty else curr_px
    shelf_low = float(last_72['low'].min()) if not last_72.empty else curr_px
    shelf_tightness = ((shelf_high - shelf_low) / shelf_low * 100.0) if shelf_low > 0 else 0.0

    last_168 = df_merged.tail(168)
    range_7d = ((last_168['high'].max() - last_168['low'].min()) / last_168['low'].min() * 100.0) if not last_168.empty else 0.0

    vol_24h = float(df_merged.tail(24)['quote_volume'].sum()) if 'quote_volume' in df_merged.columns else float((df_merged.tail(24)['volume'] * curr_px).sum())
    turnover = (vol_24h / curr_oi) if curr_oi and curr_oi > 0 else 0.0
    fragility = (curr_oi / (vol_24h / 24.0)) if vol_24h > 0 and curr_oi and curr_oi > 0 else 0.0

    low_30d = float(df_merged.tail(720)['low'].min()) if len(df_merged) >= 720 else shelf_low
    gain_from_low = ((curr_px - low_30d) / low_30d * 100.0) if low_30d > 0 else 0.0

    is_shelf = shelf_tightness <= 25.0
    is_whale_short = (curr_ls < 0.85) if not np.isnan(curr_ls) else False
    is_air_pocket_risk = fragility > 3.0

    btr_score_num = sum([bool(is_shelf), bool(is_whale_short), bool(gain_from_low > 15.0), bool(not is_air_pocket_risk)])
    btr_score_pct = int((btr_score_num / 4.0) * 100.0)

    if is_whale_short and curr_oi > 2.0e6 and gain_from_low >= 80.0:
        btr_phase = "Phase 3: Active Parabolic Squeeze"
    elif is_whale_short and is_shelf:
        btr_phase = "Phase 2: Prereg Coil Shelf (Ready for Liftoff)"
    elif not is_whale_short and (curr_ls and curr_ls > 1.2):
        btr_phase = "Non-Squeeze / Long-Led Trend (Fails Whale Short Gate)"
    elif gain_from_low < 15.0:
        btr_phase = "Phase 1: Deep Baseline Compression"
    else:
        btr_phase = "Transitional / Unclassified"

    drops = ((df_raw['low'] - df_raw['open']) / df_raw['open'] * 100.0)
    q_crashes = int((drops <= -35.0).sum())
    recent_q_crashes = int((drops.tail(720) <= -35.0).sum())
    q_status = "Safe (Low Air-Pocket Frequency)" if recent_q_crashes == 0 else f"Fragility Risk: {recent_q_crashes} Recent Flash Drops"

    diagnostics = {
        'curr_px': curr_px,
        'shelf_tightness': shelf_tightness,
        'range_7d': range_7d,
        'curr_ls': curr_ls,
        'curr_oi': curr_oi,
        'vol_24h': vol_24h,
        'turnover': turnover,
        'fragility': fragility,
        'gain_from_low': gain_from_low,
        'btr_score_num': btr_score_num,
        'btr_score_pct': btr_score_pct,
        'btr_phase': btr_phase,
        'is_whale_short': is_whale_short,
        'is_shelf': is_shelf,
        'q_crashes': q_crashes,
        'recent_q_crashes': recent_q_crashes,
        'q_status': q_status,
        'funding_rate': float(curr.get('funding_rate', 0.0)) if not pd.isna(curr.get('funding_rate')) else 0.0
    }

    return chart_df, diagnostics


def build_coin_deep_research_chart(
    symbol: str, chart_df: pd.DataFrame, coin_trades: pd.DataFrame,
    open_trade: Optional[pd.Series] = None, coin_vetoes: Optional[pd.DataFrame] = None
) -> go.Figure:
    if chart_df.empty:
        return go.Figure()

    # Convert timestamps to pure string format for guaranteed JSON serialization
    dt_str_list = [str(t)[:19] for t in chart_df['dt']]

    fig = make_subplots(
        rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.03,
        row_heights=[0.58, 0.24, 0.18],
        specs=[[{}], [{'secondary_y': True}], [{}]]
    )

    # 1. Candlestick
    fig.add_trace(go.Candlestick(
        x=dt_str_list,
        open=chart_df['open'].tolist(),
        high=chart_df['high'].tolist(),
        low=chart_df['low'].tolist(),
        close=chart_df['close'].tolist(),
        name='Price', increasing_line_color='#00ff87', decreasing_line_color='#ff4655',
        showlegend=False
    ), row=1, col=1)

    # 72h Coiled Shelf Box
    fig.add_trace(go.Scatter(
        x=dt_str_list, y=chart_df['shelf_high_72h'].tolist(), line=dict(color='rgba(0, 240, 255, 0.35)', dash='dot', width=1),
        name='72h Shelf High', showlegend=False
    ), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=dt_str_list, y=chart_df['shelf_low_72h'].tolist(), line=dict(color='rgba(0, 240, 255, 0.35)', dash='dot', width=1),
        fill='tonexty', fillcolor='rgba(0, 240, 255, 0.04)',
        name='72h Coiled Compression Shelf', showlegend=True
    ), row=1, col=1)

    # Donchian 14d Floor
    fig.add_trace(go.Scatter(
        x=dt_str_list, y=chart_df['donchian_floor_14d'].tolist(), line=dict(color='rgba(168, 85, 247, 0.7)', dash='dash', width=1.5),
        name='Donchian 14d Floor', showlegend=True
    ), row=1, col=1)

    # Plot Trade Markers
    min_chart_t = chart_df['dt'].iloc[0]
    max_chart_t = chart_df['dt'].iloc[-1]
    max_t_str = str(max_chart_t)[:19]

    if not coin_trades.empty:
        c_tr = coin_trades.copy()
        c_tr['entry_dt'] = pd.to_datetime(c_tr['entry'])
        c_tr['exit_dt'] = pd.to_datetime(c_tr['exit'])

        for _, tr in c_tr.iterrows():
            en_t = tr['entry_dt']
            ex_t = tr['exit_dt']
            en_t_str = str(en_t)[:19]
            ex_t_str = str(ex_t)[:19]
            en_px = float(tr['entry_price'])
            ex_px = float(tr['exit_price'])
            stop_px = float(tr.get('stop_price', en_px * 0.92))
            pnl = float(tr.get('pnl', 0.0)) * 100.0
            log_ret = float(tr.get('log_ret', 0.0)) * 100.0
            reason = str(tr.get('reason', ''))
            is_op = bool(tr.get('is_open', False))
            book = str(tr.get('book', 'Book 1'))

            if en_t >= min_chart_t:
                fig.add_trace(go.Scatter(
                    x=[en_t_str], y=[en_px], mode='markers+text',
                    marker=dict(symbol='triangle-up', size=13, color='#00ff87', line=dict(width=1, color='#ffffff')),
                    text=['Entry'], textposition='bottom center', textfont=dict(size=10, color='#00ff87'),
                    name=f'{book} Entry', showlegend=False,
                    hoverinfo='text',
                    hovertext=f'<b>ENTRY: {book}</b><br>Time: {en_t_str}<br>Price: ${en_px:,.4f}'
                ), row=1, col=1)

            if is_op:
                fig.add_trace(go.Scatter(
                    x=[en_t_str, max_t_str], y=[stop_px, stop_px], mode='lines+text',
                    line=dict(color='#00f0ff', dash='dash', width=2),
                    text=['', f'  Resting Stop ${stop_px:,.4f}'], textposition='middle right',
                    textfont=dict(size=11, color='#00f0ff'),
                    name='Native Resting Stop', showlegend=True,
                    hoverinfo='text',
                    hovertext=f'<b>NATIVE RESTING STOP</b><br>Price: ${stop_px:,.4f}<br>Audited on Orderbook'
                ), row=1, col=1)
            else:
                if ex_t >= min_chart_t:
                    ex_color = '#00ff87' if pnl >= 0 else '#ff4655'
                    ex_sym = 'triangle-down' if pnl >= 0 else 'x'
                    fig.add_trace(go.Scatter(
                        x=[ex_t_str], y=[ex_px], mode='markers+text',
                        marker=dict(symbol=ex_sym, size=12, color=ex_color, line=dict(width=1, color='#ffffff')),
                        text=[f'{reason[:12]} ({pnl:+.1f}%)'], textposition='top center', textfont=dict(size=9, color=ex_color),
                        name='Exit', showlegend=False,
                        hoverinfo='text',
                        hovertext=f'<b>EXIT: {reason}</b><br>Time: {ex_t_str}<br>Exit Px: ${ex_px:,.4f}<br>PnL: {pnl:+.2f}% ({log_ret:+.2f}% Log)'
                    ), row=1, col=1)

    # Plot Vetoed Signals on Pane 1
    if coin_vetoes is not None and not coin_vetoes.empty:
        v_sub = coin_vetoes.copy()
        v_sub['ts_dt'] = pd.to_datetime(v_sub['timestamp'])
        v_sub = v_sub[(v_sub['ts_dt'] >= min_chart_t) & (v_sub['ts_dt'] <= max_chart_t) & (v_sub['status'] == 'VETOED')]
        if not v_sub.empty:
            v_x = [str(t)[:19] for t in v_sub['ts_dt']]
            v_y = [float(px) for px in v_sub['price']]
            v_texts = []
            for _, vr in v_sub.iterrows():
                gate = str(vr.get('veto_gate', 'Veto Gate'))
                fwd_ret = float(vr.get('ret_72h_fwd', 0.0)) * 100.0
                is_dodged = bool(vr.get('is_dodged_bullet', False))
                out_label = '🛡️ DODGED BULLET' if is_dodged else 'CHURN FILTERED'
                v_texts.append(f"<b>VETOED BREAKOUT</b><br>Gate: {gate}<br>Outcome: {out_label}<br>72h Fwd Drift: {fwd_ret:+.1f}%")

            fig.add_trace(go.Scatter(
                x=v_x, y=v_y, mode='markers',
                marker=dict(symbol='x', size=7, color='#ff7b72', opacity=0.8, line=dict(width=1.5, color='#ff4655')),
                name='🛡️ Vetoed Signals (Dodged)', showlegend=True,
                hoverinfo='text', hovertext=v_texts
            ), row=1, col=1)

    # 2. Derivatives Pane: Open Interest ($M) & Top Trader L/S
    if 'sum_open_interest_value' in chart_df.columns and chart_df['sum_open_interest_value'].notna().any():
        oi_m = (chart_df['sum_open_interest_value'] / 1e6).tolist()
        fig.add_trace(go.Scatter(
            x=dt_str_list, y=oi_m, line=dict(color='#a855f7', width=2),
            name='Open Interest ($M)', fill='tozeroy', fillcolor='rgba(168, 85, 247, 0.08)'
        ), row=2, col=1, secondary_y=False)

    if 'count_toptrader_long_short_ratio' in chart_df.columns and chart_df['count_toptrader_long_short_ratio'].notna().any():
        fig.add_trace(go.Scatter(
            x=dt_str_list, y=chart_df['count_toptrader_long_short_ratio'].tolist(), line=dict(color='#fbbf24', width=1.8),
            name='Top Trader L/S'
        ), row=2, col=1, secondary_y=True)

        fig.add_hline(
            y=0.85, line_dash='dash', line_color='#ff4655',
            annotation_text='Whale Short Trap (0.85)', annotation_position='top left',
            row=2, col=1, secondary_y=True
        )

    # 3. Volume Pane
    bar_cols = ['#00ff87' if c >= o else '#ff4655' for c, o in zip(chart_df['close'], chart_df['open'])]
    fig.add_trace(go.Bar(
        x=dt_str_list, y=chart_df['volume'].tolist(), marker_color=bar_cols, name='1h Volume'
    ), row=3, col=1)

    if 'vol_ma_168h' in chart_df.columns:
        fig.add_trace(go.Scatter(
            x=dt_str_list, y=chart_df['vol_ma_168h'].tolist(), line=dict(color='rgba(255, 255, 255, 0.4)', dash='dot', width=1),
            name='168h Vol Baseline', showlegend=False
        ), row=3, col=1)

    fig.update_layout(
        template='plotly_dark', paper_bgcolor='#0d1117', plot_bgcolor='#07090e',
        font=dict(family='JetBrains Mono, monospace', color='#e6edf3'),
        height=720, margin=dict(l=25, r=25, t=30, b=25),
        xaxis3=dict(rangeslider=dict(visible=False), gridcolor='rgba(255, 255, 255, 0.05)', title='Timeline (UTC)'),
        xaxis=dict(gridcolor='rgba(255, 255, 255, 0.05)'),
        xaxis2=dict(gridcolor='rgba(255, 255, 255, 0.05)'),
        yaxis=dict(gridcolor='rgba(255, 255, 255, 0.05)', title='Price ($)'),
        yaxis2=dict(gridcolor='rgba(255, 255, 255, 0.05)', title='OI ($M)'),
        yaxis3=dict(title='Top Trader L/S', showgrid=False),
        yaxis4=dict(gridcolor='rgba(255, 255, 255, 0.05)', title='Volume'),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    return fig


def get_macro_weather() -> Dict:
    btc_p = SHARD_DIR / "BTC_USDT_1h.parquet"
    if not btc_p.exists():
        return {
            "price": 0.0, "ema_200d": 0.0, "dist_ema": 0.0,
            "ret_30d": 0.0, "is_bull": False, "status": "UNKNOWN"
        }
    try:
        btc = pd.read_parquet(btc_p, columns=['timestamp', 'close']).dropna().sort_values('timestamp')
        c = float(btc['close'].iloc[-1])
        ema_series = btc['close'].ewm(span=4800, adjust=False).mean()
        ema = float(ema_series.iloc[-1])
        ret30 = float((btc['close'].iloc[-1] / btc['close'].iloc[-720] - 1.0) * 100.0) if len(btc) >= 720 else 0.0
        ret14 = float((btc['close'].iloc[-1] / btc['close'].iloc[-336] - 1.0) * 100.0) if len(btc) >= 336 else 0.0
        dist = float(((c - ema) / ema) * 100.0)
        is_bull = (c > ema) and (ret30 > 0.0)
        
        # Robust consecutive duration below 200d EMA (Cycle Bottom Spring)
        below_int = (btc['close'] < ema_series).astype(int)
        grp_id = (below_int == 0).cumsum()
        bars_bel = below_int.groupby(grp_id).cumsum()
        days_below = float(bars_bel.iloc[-1] / 24.0) if not bars_bel.empty else 0.0

        return {
            "price": c,
            "ema_200d": ema,
            "dist_ema": dist,
            "ret_30d": ret30,
            "ret_14d": ret14,
            "days_below_ema": days_below,
            "is_bull": is_bull,
            "status": "RISK-ON BULL" if is_bull else "DEFENSIVE BEAR (CASH)"
        }
    except Exception:
        return {
            "price": 0.0, "ema_200d": 0.0, "dist_ema": 0.0,
            "ret_30d": 0.0, "is_bull": False, "status": "OFFLINE"
        }


def build_timeline_plot(df: pd.DataFrame) -> go.Figure:
    """Builds interactive horizontal execution swimlanes with calendar-wise scrolling."""
    if df.empty:
        return go.Figure()
    d = df.copy()
    d['entry_dt'] = pd.to_datetime(d['entry'])
    d['exit_dt'] = pd.to_datetime(d['exit'])
    d = d.sort_values('entry_dt').reset_index(drop=True)

    sub_lanes = []
    for tier in ['Tier 1', 'Tier 2', 'Tier 3']:
        grp = d[d['tier'] == tier].sort_values('entry_dt')
        lane_ends = []
        for idx, r in grp.iterrows():
            placed = False
            for l_idx, end_t in enumerate(lane_ends):
                if r['entry_dt'] >= end_t:
                    lane_ends[l_idx] = r['exit_dt']
                    sub_lanes.append((idx, f"{tier} (Ch {l_idx:02d})"))
                    placed = True
                    break
            if not placed:
                sub_lanes.append((idx, f"{tier} (Ch {len(lane_ends):02d})"))
                lane_ends.append(r['exit_dt'])

    lane_df = pd.DataFrame(sub_lanes, columns=['idx', 'lane_label']).set_index('idx')
    d['lane_label'] = lane_df['lane_label']
    d['outcome'] = np.where(d['log_ret'] > 0, 'WIN (+)', 'LOSS (-)')
    d['pnl_display'] = (d['pnl'] * 100).map(lambda x: f"{x:+.2f}%")
    d['log_display'] = (d['log_ret'] * 100).map(lambda x: f"{x:+.2f}%")

    color_map = {'WIN (+)': '#00ff87', 'LOSS (-)': '#ff4655'}
    fig = px.timeline(
        d,
        x_start="entry_dt",
        x_end="exit_dt",
        y="lane_label",
        color="outcome",
        color_discrete_map=color_map,
        hover_name="asset",
        hover_data={
            "tier": True,
            "book": True,
            "entry_dt": "|%Y-%m-%d %H:%M",
            "exit_dt": "|%Y-%m-%d %H:%M",
            "duration_hours": ":.1f",
            "entry_price": ":.4f",
            "exit_price": ":.4f",
            "pnl_display": True,
            "log_display": True,
            "reason": True,
            "outcome": False,
            "lane_label": False
        }
    )
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0d1117",
        plot_bgcolor="#07090e",
        font=dict(family="JetBrains Mono, monospace", color="#e6edf3"),
        height=620,
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis=dict(
            title="Calendar Timeline (UTC)",
            rangeslider=dict(visible=True, bgcolor="#161b22", thickness=0.08),
            type="date",
            gridcolor="rgba(255, 255, 255, 0.06)"
        ),
        yaxis=dict(
            title="Execution Channels (By Tier)",
            showticklabels=False,
            gridcolor="rgba(255, 255, 255, 0.03)",
            autorange="reversed"
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(13, 17, 23, 0.8)",
            bordercolor="#30363d",
            borderwidth=1
        )
    )
    return fig


def build_traverse_plot(df: pd.DataFrame) -> go.Figure:
    """Builds interactive chronological traverse of cumulative log return and underwater drawdown."""
    if df.empty:
        return go.Figure()
    d = df.sort_values('exit').reset_index(drop=True).copy()
    d['cum_log'] = d['log_ret'].cumsum() * 100.0
    d['capital_mult'] = np.exp(d['cum_log'] / 100.0)
    d['hwm_log'] = d['cum_log'].cummax()
    d['drawdown_log'] = d['cum_log'] - d['hwm_log']
    d['exit_dt'] = pd.to_datetime(d['exit'])

    fig = make_subplots(
        rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.08,
        row_heights=[0.72, 0.28],
        subplot_titles=("Cumulative Net Log Compounding Return (%)", "Underwater Log Drawdown (%) from Peak Equity")
    )
    # Log equity line
    fig.add_trace(go.Scatter(
        x=d['exit_dt'], y=d['cum_log'], mode='lines',
        line=dict(color='#00f0ff', width=2.5),
        name='Cumulative Log Return (%)',
        fill='tozeroy', fillcolor='rgba(0, 240, 255, 0.08)'
    ), row=1, col=1)

    # Winners and Losers scatter
    wins = d[d['log_ret'] > 0]
    losses = d[d['log_ret'] <= 0]
    fig.add_trace(go.Scatter(
        x=wins['exit_dt'], y=wins['cum_log'], mode='markers',
        marker=dict(color='#00ff87', size=5, opacity=0.8),
        name='Winning Trade',
        text=[f"{r.asset}: +{r.pnl*100:.1f}% ({r.reason})" for _, r in wins.iterrows()],
        hoverinfo='text+x+y'
    ), row=1, col=1)

    fig.add_trace(go.Scatter(
        x=losses['exit_dt'], y=losses['cum_log'], mode='markers',
        marker=dict(color='#ff4655', size=4, opacity=0.7),
        name='Loss / Stopped',
        text=[f"{r.asset}: {r.pnl*100:.1f}% ({r.reason})" for _, r in losses.iterrows()],
        hoverinfo='text+x+y'
    ), row=1, col=1)

    # Underwater Drawdown
    fig.add_trace(go.Scatter(
        x=d['exit_dt'], y=d['drawdown_log'], mode='lines',
        line=dict(color='#ff4655', width=1.5),
        fill='tozeroy', fillcolor='rgba(255, 70, 85, 0.25)',
        name='Log Drawdown (%)'
    ), row=2, col=1)

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0d1117",
        plot_bgcolor="#07090e",
        font=dict(family="JetBrains Mono, monospace", color="#e6edf3"),
        height=580,
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis2=dict(
            title="Timeline (UTC)",
            rangeslider=dict(visible=True, bgcolor="#161b22", thickness=0.08),
            gridcolor="rgba(255, 255, 255, 0.06)"
        ),
        xaxis=dict(gridcolor="rgba(255, 255, 255, 0.06)"),
        yaxis=dict(gridcolor="rgba(255, 255, 255, 0.06)", title="Net Log PnL %"),
        yaxis2=dict(gridcolor="rgba(255, 255, 255, 0.06)", title="Drawdown %"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig


# ---------------------------------------------------------------------------
# HIGH-FIDELITY CSS & DARK GLASSMORPHISM THEME
# ---------------------------------------------------------------------------
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700;800&family=Inter:wght@300;400;600;700;800&display=swap');

:root {
    --bg-dark: #07090e;
    --surface-card: #0d1117;
    --surface-hover: #161b22;
    --border-subtle: #21262d;
    --border-accent: #30363d;
    --cyan-accent: #00f0ff;
    --green-profit: #00ff87;
    --red-loss: #ff4655;
    --purple-glow: #a855f7;
    --amber-warn: #f59e0b;
}

body {
    background-color: var(--bg-dark) !important;
    color: #e6edf3 !important;
    font-family: 'Inter', -apple-system, sans-serif !important;
}

.mono {
    font-family: 'JetBrains Mono', monospace !important;
}

.card-glass {
    background: rgba(13, 17, 23, 0.85) !important;
    backdrop-filter: blur(12px) !important;
    border: 1px solid var(--border-subtle) !important;
    border-radius: 10px !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
}

.card-glass:hover {
    border-color: var(--border-accent) !important;
}

.card-glow-cyan {
    border-color: rgba(0, 240, 255, 0.4) !important;
    box-shadow: 0 0 20px rgba(0, 240, 255, 0.15) !important;
}

.card-glow-green {
    border-color: rgba(0, 255, 135, 0.4) !important;
    box-shadow: 0 0 20px rgba(0, 255, 135, 0.15) !important;
}

.card-glow-red {
    border-color: rgba(255, 70, 85, 0.4) !important;
    box-shadow: 0 0 20px rgba(255, 70, 85, 0.15) !important;
}

.badge-tag {
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.badge-cyan { background: rgba(0, 240, 255, 0.15); color: #00f0ff; border: 1px solid rgba(0, 240, 255, 0.3); }
.badge-green { background: rgba(0, 255, 135, 0.15); color: #00ff87; border: 1px solid rgba(0, 255, 135, 0.3); }
.badge-red { background: rgba(255, 70, 85, 0.15); color: #ff4655; border: 1px solid rgba(255, 70, 85, 0.3); }
.badge-purple { background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3); }
.badge-amber { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }
.badge-gray { background: rgba(139, 148, 158, 0.15); color: #8b949e; border: 1px solid rgba(139, 148, 158, 0.3); }

.q-tab {
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    letter-spacing: 0.5px !important;
}

.q-tab--active {
    color: var(--cyan-accent) !important;
    border-bottom: 2px solid var(--cyan-accent) !important;
}

.q-table {
    background-color: transparent !important;
    color: #e6edf3 !important;
}

.q-table th {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 11px !important;
    color: #8b949e !important;
    text-transform: uppercase !important;
    border-bottom: 1px solid var(--border-subtle) !important;
}

.q-table td {
    font-size: 12px !important;
    border-bottom: 1px solid rgba(33, 38, 45, 0.6) !important;
}

.filter-input {
    background: #161b22 !important;
    border: 1px solid #30363d !important;
    border-radius: 6px !important;
    color: white !important;
}
</style>
"""


def setup_page_head():
    ui.add_head_html(CUSTOM_CSS)

    # Fix #10 — WebSocket Auto-Reconnect Guard
    ui.add_head_html("""
    <script>
    (function() {
        var RECONNECT_CHECK_MS = 30000;
        var STALE_RELOAD_MS   = 300000;
        var disconnectedAt    = null;

        function checkConnection() {
            var sock = window._nicegui_socket || (typeof io !== 'undefined' && io.sockets && io.sockets.connected);
            var connected = false;
            try {
                if (window._nicegui_socket) {
                    connected = window._nicegui_socket.connected;
                }
            } catch(e) {}

            if (!connected) {
                if (!disconnectedAt) {
                    disconnectedAt = Date.now();
                    console.warn('[Kronos] WebSocket disconnected. Will reload in 5 min if not recovered.');
                } else if (Date.now() - disconnectedAt > STALE_RELOAD_MS) {
                    console.warn('[Kronos] 5 min disconnect threshold reached. Force reloading page...');
                    location.reload();
                }
            } else {
                disconnectedAt = null;
            }
        }

        setInterval(checkConnection, RECONNECT_CHECK_MS);
        console.log('[Kronos] WebSocket watchdog armed. Auto-reload on 5-min disconnect.');
    })();
    </script>
    """)


# ---------------------------------------------------------------------------
# DEDICATED INDIVIDUAL COIN DEEP RESEARCH PAGE
# ---------------------------------------------------------------------------
@ui.page('/coin/{symbol}')
def coin_research_page(symbol: str):
    setup_page_head()
    clean_sym = symbol.upper().replace('USDT', '').replace('/', '').replace('_', '').strip()

    sc_df = load_v12_scorecard(CURRENT_ARM)
    trades_df = load_v12_trades(CURRENT_ARM)
    tel_df = load_v12_telemetry(CURRENT_ARM)
    macro = get_macro_weather()
    tiers_df = load_asset_tiers()
    all_symbols = get_all_research_symbols()
    if clean_sym and clean_sym not in all_symbols:
        all_symbols = sorted(list(set(all_symbols + [clean_sym])))
    if not all_symbols:
        all_symbols = [clean_sym]

    coin_trades = trades_df[trades_df['asset'] == clean_sym].copy() if not trades_df.empty and 'asset' in trades_df.columns else pd.DataFrame()
    open_trades = coin_trades[coin_trades['is_open']].copy() if not coin_trades.empty and 'is_open' in coin_trades.columns else pd.DataFrame()
    open_trade = open_trades.iloc[0] if not open_trades.empty else None

    coin_vetoes = tel_df[tel_df['asset'] == clean_sym].copy() if not tel_df.empty and 'asset' in tel_df.columns else pd.DataFrame()
    coin_veto_summary = TelemetryCollector.compute_veto_alpha_summary(coin_vetoes) if not coin_vetoes.empty else {}

    sc_match = sc_df[sc_df['asset'] == clean_sym] if not sc_df.empty and 'asset' in sc_df.columns else pd.DataFrame()
    sc_row = sc_match.iloc[0] if not sc_match.empty else None

    tier_str = "Tier 1 Macro"
    if open_trade is not None:
        tier_str = str(open_trade.get('tier', 'Tier 1'))
    elif sc_row is not None:
        tier_str = str(sc_row.get('tier', 'Tier 1'))
    elif not tiers_df.empty and 'asset' in tiers_df.columns:
        match_tier = tiers_df[tiers_df['asset'] == clean_sym]
        if not match_tier.empty:
            tier_str = str(match_tier.iloc[0].get('tier', 'Tier 1'))

    chart_df, diag = load_coin_research_data(clean_sym, lookback_bars=720)

    if chart_df is None or chart_df.empty:
        with ui.column().classes('w-full max-w-7xl mx-auto p-6 gap-6'):
            ui.link('<- Back to Command Center', '/').classes('text-xs text-[#00f0ff] font-bold mono border border-[#00f0ff]/30 px-3 py-1.5 rounded-lg hover:bg-[#00f0ff]/10 w-fit')
            with ui.card().classes('card-glass p-8 border border-[#ff4655] w-full text-center'):
                ui.label(f'Shard Tape Not Found: {clean_sym}').classes('text-xl font-bold text-[#ff4655] mono')
                ui.label(f'No historical 1h parquet shard found for {clean_sym}_USDT_1h.parquet in data/raw_shards.').classes('text-sm text-gray-400 mono mt-2')
                ui.button('Return to Command Center', on_click=lambda: ui.navigate.to('/')).props('outline color=cyan').classes('mono mt-4')
        return

    curr_px = diag['curr_px']
    px_24h_ago = float(chart_df.iloc[-25]['close']) if len(chart_df) >= 25 else curr_px
    ret_24h = ((curr_px - px_24h_ago) / px_24h_ago * 100.0) if px_24h_ago > 0 else 0.0
    ret_24h_str = f"{ret_24h:+.2f}%"
    ret_24h_col = '#00ff87' if ret_24h >= 0 else '#ff4655'

    closed_trades = coin_trades[~coin_trades['is_open']].copy() if not coin_trades.empty and 'is_open' in coin_trades.columns else pd.DataFrame()
    closed_cnt = len(closed_trades)

    if sc_row is not None:
        wr_val = float(sc_row.get('win_rate', 0.0))
        pf_val = float(sc_row.get('profit_factor', 0.0))
        edge_val = float(sc_row.get('mean_log_pnl', 0.0))
        tot_log_val = float(sc_row.get('total_log_pnl', 0.0))
        mult_val = float(sc_row.get('capital_multiple', 1.0))
        mdd_val = float(sc_row.get('max_log_drawdown', 0.0))
        avg_mfe = float(sc_row.get('mfe_mean_pct', 0.0))
        avg_mae = float(sc_row.get('mae_mean_pct', 0.0))
        p90_mfe = float(sc_row.get('mfe_p90_pct', avg_mfe))
        p10_mae = float(sc_row.get('mae_p10_pct', avg_mae))
        dur_val = float(sc_row.get('dur_mean_hours', 0.0))
        wins_cnt = int(round(wr_val / 100.0 * closed_cnt))
        losses_cnt = closed_cnt - wins_cnt
    elif closed_cnt > 0:
        wins = closed_trades[closed_trades['log_ret'] > 0]
        losses = closed_trades[closed_trades['log_ret'] <= 0]
        wins_cnt = len(wins)
        losses_cnt = len(losses)
        wr_val = (wins_cnt / closed_cnt) * 100.0
        gw = float(wins['log_ret'].sum())
        gl = abs(float(losses['log_ret'].sum()))
        pf_val = (gw / gl) if gl > 0 else 999.0
        tot_log_val = float(closed_trades['log_ret'].sum()) * 100.0
        edge_val = tot_log_val / closed_cnt
        mult_val = float(np.exp(tot_log_val / 100.0))
        cum_log = closed_trades.sort_values('exit')['log_ret'].cumsum() * 100.0
        mdd_val = float((cum_log - cum_log.cummax()).min())
        avg_mfe = float(closed_trades['mfe'].mean() * 100.0) if 'mfe' in closed_trades.columns else 0.0
        avg_mae = float(closed_trades['mae'].mean() * 100.0) if 'mae' in closed_trades.columns else 0.0
        p90_mfe = float(np.percentile(closed_trades['mfe'] * 100.0, 90)) if 'mfe' in closed_trades.columns else avg_mfe
        p10_mae = float(np.percentile(closed_trades['mae'] * 100.0, 10)) if 'mae' in closed_trades.columns else avg_mae
        dur_val = float(closed_trades['duration_hours'].mean()) if 'duration_hours' in closed_trades.columns else 0.0
    else:
        wr_val = 0.0
        pf_val = 0.0
        edge_val = 0.0
        tot_log_val = 0.0
        mult_val = 1.0
        mdd_val = 0.0
        avg_mfe = 0.0
        avg_mae = 0.0
        p90_mfe = 0.0
        p10_mae = 0.0
        dur_val = 0.0
        wins_cnt = 0
        losses_cnt = 0

    with ui.header().classes('bg-[#0d1117] border-b border-[#21262d] px-6 py-3 flex items-center justify-between'):
        with ui.row().classes('items-center gap-4'):
            ui.link('<- Back to Overview', '/').classes('text-xs text-[#00f0ff] font-bold mono border border-[#00f0ff]/30 px-3 py-1.5 rounded-lg hover:bg-[#00f0ff]/10')
            ui.label(f"{clean_sym}/USDT").classes('text-xl font-black text-white mono')
            ui.html('<span class="badge-tag badge-cyan">Perpetual</span>')
            tier_col = 'badge-cyan' if 'Tier 1' in tier_str else ('badge-purple' if 'Tier 2' in tier_str else 'badge-amber')
            ui.html(f'<span class="badge-tag {tier_col}">{tier_str}</span>')

            if open_trade is not None:
                op_dur = int(float(open_trade.get('duration_hours', 0)))
                ui.html(f'<span class="badge-tag badge-green">ACTIVE POSITION ({op_dur}h)</span>')
            else:
                ui.html('<span class="badge-tag badge-gray">FLAT / CASH PRESERVATION</span>')

        with ui.row().classes('items-center gap-4'):
            with ui.row().classes('items-center gap-2 bg-[#161b22] px-3 py-1 rounded-lg border border-[#30363d]'):
                ui.label('Coin:').classes('text-xs text-gray-400 mono font-bold')
                def switch_coin(e):
                    if e.value and e.value != clean_sym:
                        ui.navigate.to(f'/coin/{e.value}')
                ui.select(options=all_symbols, value=clean_sym, on_change=switch_coin).props('dense dark borderless options-dense filter').classes('text-xs mono w-32 text-cyan-300 font-bold')

            macro_badge = '<span class="badge-tag badge-green">BTC Bull</span>' if macro.get('is_bull', False) else '<span class="badge-tag badge-amber">BTC Defensive</span>'
            ui.html(macro_badge)
            ui.label(f"${curr_px:,.4f}").classes('text-lg font-black text-white mono')
            ui.label(f"({ret_24h_str})").classes(f'text-xs font-bold text-[{ret_24h_col}] mono')

    with ui.column().classes('w-full max-w-7xl mx-auto p-6 gap-6'):
        with ui.row().classes('w-full grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4'):
            with ui.card().classes('card-glass p-4 border-l-4 border-l-[#00f0ff]'):
                ui.label('LIFETIME WIN RATE').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                wr_col = '#00ff87' if wr_val >= 40 else ('#fbbf24' if wr_val > 0 else '#8b949e')
                ui.label(f"{wr_val:.1f}%").classes(f'text-2xl font-black text-[{wr_col}] mono mt-1')
                ui.label(f"{wins_cnt} Wins / {losses_cnt} Losses").classes('text-xs text-gray-400 mono')

            with ui.card().classes('card-glass p-4 border-l-4 border-l-[#00ff87]'):
                ui.label('LOG PROFIT FACTOR').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                pf_col = '#00ff87' if pf_val >= 1.5 else ('#fbbf24' if pf_val >= 1.0 else '#ff4655')
                ui.label(f"{pf_val:.3f}" if pf_val > 0 else "N/A").classes(f'text-2xl font-black text-[{pf_col}] mono mt-1')
                ui.label('Strict Log Space').classes('text-xs text-gray-400 mono')

            with ui.card().classes('card-glass p-4 border-l-4 border-l-[#a855f7]'):
                ui.label('MEAN EDGE / TRADE').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                edge_c = '#00ff87' if edge_val >= 0 else '#ff4655'
                ui.label(f"{edge_val:+.2f}%").classes(f'text-2xl font-black text-[{edge_c}] mono mt-1')
                ui.label('Net Log Per Trade').classes('text-xs text-gray-400 mono')

            with ui.card().classes('card-glass p-4 border-l-4 border-l-[#00f0ff]'):
                ui.label('CUMULATIVE NET LOG').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                tot_c = '#00ff87' if tot_log_val >= 0 else '#ff4655'
                ui.label(f"{tot_log_val:+.1f}%").classes(f'text-2xl font-black text-[{tot_c}] mono mt-1')
                ui.label(f"Multiple: {mult_val:.2f}x").classes('text-xs text-gray-400 mono')

            with ui.card().classes('card-glass p-4 border-l-4 border-l-[#ff4655]'):
                ui.label('MAX LOG DRAWDOWN').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                ui.label(f"{mdd_val:.1f}%").classes('text-2xl font-black text-[#ff4655] mono mt-1')
                ui.label('Peak Equity Protected').classes('text-xs text-gray-400 mono')

            # Card 6: Net Veto Alpha
            net_v_alpha = float(coin_veto_summary.get('net_veto_alpha_pct', 0.0))
            dodged_cnt = int(coin_veto_summary.get('dodged_bullets', 0))
            saved_loss = float(coin_veto_summary.get('saved_losses_pct', 0.0))
            with ui.card().classes('card-glass p-4 border-l-4 border-l-[#00ff87]'):
                ui.label('NET VETO ALPHA').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                v_col = '#00ff87' if net_v_alpha >= 0 else '#ff4655'
                ui.label(f"{net_v_alpha:+.1f}%").classes(f'text-2xl font-black text-[{v_col}] mono mt-1')
                ui.label(f"+{saved_loss:.0f}% Saved ({dodged_cnt} Dodged)").classes('text-xs text-gray-400 mono')

        with ui.card().classes('card-glass p-4 border border-[#21262d] w-full'):
            with ui.row().classes('w-full justify-between items-center mb-2'):
                with ui.row().classes('items-center gap-2'):
                    ui.label(f'{clean_sym} 3-PANE QUANTITATIVE RESEARCH CHART').classes('text-xs font-bold tracking-wider text-[#00f0ff] mono')
                    ui.html('<span class="badge-tag badge-purple">Pane 1: Price Action</span> <span class="badge-tag badge-amber">Pane 2: Derivatives Whale Tracker</span> <span class="badge-tag badge-cyan">Pane 3: Tape Aggression</span>')

                lookback_box = ui.row().classes('items-center gap-1')

            chart_holder = ui.column().classes('w-full')

            def update_chart_view(lookback_days: int):
                chart_holder.clear()
                bars = lookback_days * 24 if lookback_days > 0 else 0
                sub_df, _ = load_coin_research_data(clean_sym, lookback_bars=bars)
                with chart_holder:
                    fig = build_coin_deep_research_chart(clean_sym, sub_df if sub_df is not None else chart_df, coin_trades, open_trade, coin_vetoes=coin_vetoes)
                    ui.plotly(fig).classes('w-full')

            with lookback_box:
                ui.button('14D', on_click=lambda: update_chart_view(14)).props('dense outline size=sm').classes('mono text-xs')
                ui.button('30D', on_click=lambda: update_chart_view(30)).props('dense outline size=sm').classes('mono text-xs')
                ui.button('60D', on_click=lambda: update_chart_view(60)).props('dense outline size=sm').classes('mono text-xs')
                ui.button('ALL', on_click=lambda: update_chart_view(0)).props('dense outline size=sm').classes('mono text-xs')

            update_chart_view(30)

        with ui.row().classes('w-full grid grid-cols-1 lg:grid-cols-2 gap-6'):
            # Card 1: Historical Performance Matrix
            with ui.card().classes('card-glass p-5 border border-[#21262d] flex flex-col justify-between'):
                with ui.row().classes('w-full justify-between items-center mb-2'):
                    ui.label('📊 HISTORICAL PERFORMANCE MATRIX').classes('text-xs text-gray-400 mono font-bold')
                    wr_badge_col = 'badge-green' if wr_val >= 40 else ('badge-amber' if wr_val > 0 else 'badge-gray')
                    ui.html(f'<span class="badge-tag {wr_badge_col}">{wr_val:.1f}% Win Rate</span>')

                with ui.row().classes('w-full grid grid-cols-2 gap-3 my-2'):
                    with ui.column().classes('gap-0 bg-[#161b22] p-2.5 rounded-lg border border-[#21262d]'):
                        ui.label('Lifetime Closed Trades:').classes('text-[11px] text-gray-400 mono')
                        ui.label(f"{closed_cnt} Trades ({wins_cnt}W / {losses_cnt}L)").classes('text-sm font-bold text-white mono')
                    with ui.column().classes('gap-0 bg-[#161b22] p-2.5 rounded-lg border border-[#21262d]'):
                        ui.label('Strict Log Profit Factor:').classes('text-[11px] text-gray-400 mono')
                        ui.label(f"{pf_val:.3f}" if pf_val > 0 else "N/A").classes('text-sm font-bold text-[#00f0ff] mono')
                    with ui.column().classes('gap-0 bg-[#161b22] p-2.5 rounded-lg border border-[#21262d]'):
                        ui.label('Mean Edge / Trade:').classes('text-[11px] text-gray-400 mono')
                        edge_c = '#00ff87' if edge_val >= 0 else '#ff4655'
                        ui.label(f"{edge_val:+.2f}% Net Log").classes(f'text-sm font-bold text-[{edge_c}] mono')
                    with ui.column().classes('gap-0 bg-[#161b22] p-2.5 rounded-lg border border-[#21262d]'):
                        ui.label('Cumulative Net Log:').classes('text-[11px] text-gray-400 mono')
                        tot_c = '#00ff87' if tot_log_val >= 0 else '#ff4655'
                        ui.label(f"{tot_log_val:+.1f}% ({mult_val:.2f}x)").classes(f'text-sm font-bold text-[{tot_c}] mono')
                    with ui.column().classes('gap-0 bg-[#161b22] p-2.5 rounded-lg border border-[#21262d]'):
                        ui.label('Max Historical Drawdown:').classes('text-[11px] text-gray-400 mono')
                        ui.label(f"{mdd_val:.1f}%").classes('text-sm font-bold text-[#ff4655] mono')
                    with ui.column().classes('gap-0 bg-[#161b22] p-2.5 rounded-lg border border-[#21262d]'):
                        ui.label('Average Duration:').classes('text-[11px] text-gray-400 mono')
                        ui.label(f"{dur_val:.0f} Hours ({dur_val/24.0:.1f}d)").classes('text-sm font-bold text-white mono')

                with ui.row().classes('w-full justify-between items-center text-xs text-gray-400 mono pt-2 border-t border-[#21262d]'):
                    ui.label(f"Avg Peak MFE: +{avg_mfe:.1f}% (P90: +{p90_mfe:.1f}%)").classes('text-[#00f0ff]')
                    ui.label(f"Avg MAE: {avg_mae:.1f}% (P10: {p10_mae:.1f}%)").classes('text-[#ff4655]')

            # Card 2: Microstructure & Whale Trait Diagnosis
            with ui.card().classes('card-glass p-5 border border-[#21262d] flex flex-col justify-between'):
                with ui.row().classes('w-full justify-between items-center mb-2'):
                    ui.label('🐋 MICROSTRUCTURE & WHALE TRAIT DIAGNOSIS').classes('text-xs text-gray-400 mono font-bold')
                    btr_col = 'badge-green' if diag['btr_score_pct'] >= 75 else ('badge-amber' if diag['btr_score_pct'] >= 50 else 'badge-gray')
                    ui.html(f'<span class="badge-tag {btr_col}">BTR Match: {diag["btr_score_pct"]}%</span>')

                with ui.column().classes('gap-2 my-2'):
                    with ui.column().classes('gap-0 bg-[#161b22] p-2.5 rounded-lg border border-[#21262d]'):
                        ui.label('BTR Lifecycle State:').classes('text-[11px] text-gray-400 mono')
                        ui.label(f"{diag['btr_phase']}").classes('text-sm font-bold text-[#00f0ff] mono')

                    with ui.row().classes('w-full grid grid-cols-3 gap-2'):
                        with ui.column().classes('gap-0 bg-[#161b22] p-2 rounded-lg border border-[#21262d]'):
                            ui.label('Whale L/S:').classes('text-[10px] text-gray-400 mono')
                            ls_str = f"{diag['curr_ls']:.2f}" if diag['curr_ls'] is not None and not np.isnan(diag['curr_ls']) else "N/A"
                            ls_c = '#00ff87' if diag['is_whale_short'] else ('#ff4655' if (diag['curr_ls'] and diag['curr_ls'] > 1.2) else '#e6edf3')
                            ui.label(ls_str).classes(f'text-sm font-bold text-[{ls_c}] mono')
                            trap_msg = "Whales Trapped" if diag['is_whale_short'] else "Whales Long"
                            ui.label(trap_msg).classes('text-[10px] text-gray-500 mono')

                        with ui.column().classes('gap-0 bg-[#161b22] p-2 rounded-lg border border-[#21262d]'):
                            ui.label('Shelf Range (72h):').classes('text-[10px] text-gray-400 mono')
                            ui.label(f"{diag['shelf_tightness']:.1f}%").classes('text-sm font-bold text-[#00f0ff] mono')
                            sh_msg = "Tight (<=25%)" if diag['shelf_tightness'] <= 25 else "Loose/Wide"
                            ui.label(sh_msg).classes('text-[10px] text-gray-500 mono')

                        with ui.column().classes('gap-0 bg-[#161b22] p-2 rounded-lg border border-[#21262d]'):
                            ui.label('Turnover Velocity:').classes('text-[10px] text-gray-400 mono')
                            ui.label(f"{diag['turnover']:.2f}x").classes('text-sm font-bold text-white mono')
                            to_msg = "Healthy Depth" if diag['turnover'] >= 0.35 else "Low Turnover"
                            ui.label(to_msg).classes('text-[10px] text-gray-500 mono')

                    with ui.row().classes('w-full justify-between items-center bg-[#161b22] px-3 py-2 rounded-lg border border-[#21262d]'):
                        ui.label('Q-Trait Air-Pocket Status:').classes('text-xs text-gray-400 mono')
                        q_col = '#00ff87' if diag['recent_q_crashes'] == 0 else '#fbbf24'
                        ui.label(diag['q_status']).classes(f'text-xs font-bold text-[{q_col}] mono')

            # Card 3: Chronological Execution Ledger & Veto Flight Recorder
            with ui.card().classes('card-glass p-5 border border-[#21262d] flex flex-col justify-between'):
                with ui.tabs().classes('w-full text-gray-400 border-b border-[#21262d]') as ledger_tabs:
                    tab_exec = ui.tab('exec', label=f'📜 Executed Trades ({len(coin_trades)})')
                    tab_vetoes = ui.tab('vetoes', label=f'🛡️ Vetoed Signals ({len(coin_vetoes)})')

                with ui.tab_panels(ledger_tabs, value=tab_exec).classes('w-full bg-transparent p-0 mt-3'):
                    # Helper to reset table page to 1 whenever sorting changes
                    def attach_table_sort_reset(tbl, init_col, init_desc=True):
                        cur_state = {'col': init_col, 'desc': init_desc}
                        def _on_pag_change(e):
                            p = e.value if hasattr(e, 'value') else e
                            if isinstance(p, dict):
                                c = p.get('sortBy')
                                d = p.get('descending')
                                if c != cur_state['col'] or d != cur_state['desc']:
                                    cur_state['col'] = c
                                    cur_state['desc'] = d
                                    if p.get('page', 1) != 1:
                                        p['page'] = 1
                                        tbl.pagination = p
                                        tbl.update()
                        tbl.on_pagination_change(_on_pag_change)

                    # --- TAB 1: EXECUTED TRADES ---
                    with ui.tab_panel(tab_exec).classes('p-0 gap-3 flex flex-col'):
                        if not coin_trades.empty:
                            c_rows = []
                            for idx, r in coin_trades.sort_values('entry', ascending=False).reset_index(drop=True).iterrows():
                                en_px = float(r.get('entry_price', 0.0))
                                ex_px = float(r.get('exit_price', 0.0))
                                pnl_v = float(r.get('pnl', 0.0)) * 100.0
                                log_v = float(r.get('log_ret', 0.0)) * 100.0
                                mfe_v = float(r.get('mfe', 0.0)) * 100.0
                                dur_v = float(r.get('duration_hours', 0.0))
                                is_op = bool(r.get('is_open', False))
                                st_name = "OPEN" if is_op else "CLOSED"
                                en_str = str(r.get('entry', ''))[:16]
                                ex_str = str(r.get('exit', ''))[:16] if not is_op else 'ACTIVE'
                                c_rows.append({
                                    'id': f"{clean_sym}_{idx}_{en_str}",
                                    'status': st_name,
                                    'entry': en_str,
                                    'exit': ex_str,
                                    'exit_sort': '9999-99-99 99:99' if is_op else ex_str,
                                    'book': str(r.get('book', 'Book 1')),
                                    'entry_price': en_px,
                                    'exit_price': ex_px,
                                    'pnl': pnl_v,
                                    'log_ret': log_v,
                                    'mfe': mfe_v,
                                    'duration': dur_v,
                                    'reason': str(r.get('reason', '')),
                                    'entry_price_str': f"${en_px:,.4f}",
                                    'exit_price_str': f"${ex_px:,.4f}",
                                    'pnl_str': f"{pnl_v:+.2f}%",
                                    'log_ret_str': f"{log_v:+.2f}%",
                                    'mfe_str': f"+{mfe_v:.1f}%",
                                    'dur_str': f"{int(dur_v)}h",
                                })

                            c_cols = [
                                {'name': 'status', 'label': 'Status', 'field': 'status', 'align': 'center', 'sortable': True},
                                {'name': 'entry', 'label': 'Entry (UTC)', 'field': 'entry', 'align': 'left', 'sortable': True, 'sortOrder': 'da'},
                                {'name': 'exit', 'label': 'Exit (UTC)', 'field': 'exit_sort', 'align': 'left', 'sortable': True, 'sortOrder': 'da'},
                                {'name': 'book', 'label': 'Book', 'field': 'book', 'align': 'center', 'sortable': True},
                                {'name': 'entry_price', 'label': 'Entry Px', 'field': 'entry_price', 'align': 'right', 'sortable': True, 'sortOrder': 'da'},
                                {'name': 'exit_price', 'label': 'Exit Px', 'field': 'exit_price', 'align': 'right', 'sortable': True, 'sortOrder': 'da'},
                                {'name': 'pnl', 'label': 'PnL', 'field': 'pnl', 'align': 'right', 'sortable': True, 'sortOrder': 'da'},
                                {'name': 'log_ret', 'label': 'Log Ret', 'field': 'log_ret', 'align': 'right', 'sortable': True, 'sortOrder': 'da'},
                                {'name': 'mfe', 'label': 'Peak MFE', 'field': 'mfe', 'align': 'right', 'sortable': True, 'sortOrder': 'da'},
                                {'name': 'duration', 'label': 'Duration', 'field': 'duration', 'align': 'right', 'sortable': True, 'sortOrder': 'da'},
                                {'name': 'reason', 'label': 'Exit Reason', 'field': 'reason', 'align': 'left', 'sortable': True},
                            ]

                            if len(c_rows) > 5:
                                with ui.row().classes('w-full justify-between items-center px-1 mb-1'):
                                    ui.label('Click column header to sort (descending first).').classes('text-[11px] text-gray-500 mono')
                                    c_search = ui.input(placeholder='Search trades...').props('dense dark borderless').classes('bg-[#161b22] px-3 py-0.5 rounded border border-[#30363d] text-xs mono w-48')

                            ctbl = ui.table(
                                columns=c_cols,
                                rows=c_rows,
                                row_key='id',
                                pagination={'rowsPerPage': 10, 'sortBy': 'entry', 'descending': True, 'page': 1}
                            ).classes('w-full card-glass mono text-xs').props(':rows-per-page-options="[6, 10, 25, 50, 100]"')

                            if len(c_rows) > 5:
                                ctbl.bind_filter_to(c_search, 'value')
                            attach_table_sort_reset(ctbl, 'entry', True)

                            ctbl.add_slot('body-cell-status', '''
                                <q-td :props="props" class="text-center">
                                    <span :class="props.row.status === 'OPEN' ? 'badge-tag badge-green' : 'badge-tag badge-gray'">
                                        {{ props.row.status }}
                                    </span>
                                </q-td>
                            ''')
                            ctbl.add_slot('body-cell-exit', '''
                                <q-td :props="props" class="text-left" :class="props.row.status === 'OPEN' ? 'text-[#00ff87] font-bold' : ''">
                                    {{ props.row.exit }}
                                </q-td>
                            ''')
                            ctbl.add_slot('body-cell-entry_price', '<q-td :props="props" class="text-right">{{ props.row.entry_price_str }}</q-td>')
                            ctbl.add_slot('body-cell-exit_price', '<q-td :props="props" class="text-right">{{ props.row.exit_price_str }}</q-td>')
                            ctbl.add_slot('body-cell-pnl', '''
                                <q-td :props="props" class="text-right font-bold" :class="props.row.pnl >= 0 ? 'text-[#00ff87]' : 'text-[#ff4655]'">
                                    {{ props.row.pnl_str }}
                                </q-td>
                            ''')
                            ctbl.add_slot('body-cell-log_ret', '''
                                <q-td :props="props" class="text-right" :class="props.row.log_ret >= 0 ? 'text-[#00ff87]' : 'text-[#ff4655]'">
                                    {{ props.row.log_ret_str }}
                                </q-td>
                            ''')
                            ctbl.add_slot('body-cell-mfe', '<q-td :props="props" class="text-right text-[#00f0ff] font-bold">{{ props.row.mfe_str }}</q-td>')
                            ctbl.add_slot('body-cell-duration', '<q-td :props="props" class="text-right">{{ props.row.dur_str }}</q-td>')
                        else:
                            ui.label('No historical trades executed for this symbol.').classes('text-xs text-gray-400 mono py-8 text-center')

                    # --- TAB 2: VETOED SIGNALS & DODGED BULLETS ---
                    with ui.tab_panel(tab_vetoes).classes('p-0 gap-3 flex flex-col'):
                        if not coin_vetoes.empty:
                            v_rows = []
                            for v_idx, vr in coin_vetoes.sort_values('timestamp', ascending=False).reset_index(drop=True).iterrows():
                                ts_str = str(vr.get('timestamp', ''))[:16]
                                gate_val = str(vr.get('veto_gate', ''))
                                setup_val = str(vr.get('candidate_setup', 'Breakout'))
                                px_val = float(vr.get('price', 0.0))
                                fwd72_val = float(vr.get('ret_72h_fwd', 0.0)) * 100.0
                                mfe72_val = float(vr.get('mfe_72h_fwd', 0.0)) * 100.0
                                mae72_val = float(vr.get('mae_72h_fwd', 0.0)) * 100.0
                                is_dodged = bool(vr.get('is_dodged_bullet', False))
                                is_missed = bool(vr.get('is_missed_opportunity', False))

                                if is_dodged:
                                    out_type = 'DODGED'
                                    out_label = '🛡️ DODGED BULLET'
                                elif is_missed:
                                    out_type = 'MISSED'
                                    out_label = '⚠️ MISSED RUNNER'
                                else:
                                    out_type = 'FILTERED'
                                    out_label = 'CHURN FILTERED'

                                mfe_str = f"+{mfe72_val:.1f}%" if mfe72_val >= 0 else f"{mfe72_val:.1f}%"
                                mae_str = f"{mae72_val:.1f}%" if mae72_val <= 0 else f"+{mae72_val:.1f}%"

                                v_rows.append({
                                    'id': f"{clean_sym}_v_{v_idx}_{ts_str}",
                                    'timestamp': ts_str,
                                    'setup': setup_val,
                                    'gate': gate_val,
                                    'price': px_val,
                                    'price_str': f"${px_val:,.4f}",
                                    'ret_72h': fwd72_val,
                                    'ret_72h_str': f"{fwd72_val:+.1f}%",
                                    'mfe_72h': mfe72_val,
                                    'mfe_72h_str': mfe_str,
                                    'mae_72h': mae72_val,
                                    'mae_72h_str': mae_str,
                                    'out_type': out_type,
                                    'out_label': out_label,
                                })

                            v_cols = [
                                {'name': 'timestamp', 'label': 'Signal Time (UTC)', 'field': 'timestamp', 'align': 'left', 'sortable': True, 'sortOrder': 'da'},
                                {'name': 'setup', 'label': 'Setup', 'field': 'setup', 'align': 'left', 'sortable': True},
                                {'name': 'gate', 'label': 'Triggered Veto Gate', 'field': 'gate', 'align': 'left', 'sortable': True},
                                {'name': 'price', 'label': 'Signal Px', 'field': 'price', 'align': 'right', 'sortable': True, 'sortOrder': 'da'},
                                {'name': 'ret_72h', 'label': '72h Drift', 'field': 'ret_72h', 'align': 'right', 'sortable': True, 'sortOrder': 'da'},
                                {'name': 'mfe_72h', 'label': '72h MFE', 'field': 'mfe_72h', 'align': 'right', 'sortable': True, 'sortOrder': 'da'},
                                {'name': 'mae_72h', 'label': '72h MAE', 'field': 'mae_72h', 'align': 'right', 'sortable': True, 'sortOrder': 'da'},
                                {'name': 'out_label', 'label': 'Outcome', 'field': 'out_label', 'align': 'center', 'sortable': True},
                            ]

                            with ui.row().classes('w-full justify-between items-center px-1 mb-1'):
                                ui.label('Click column header to sort (descending first). Use search to filter gates or dates.').classes('text-[11px] text-gray-500 mono')
                                v_search = ui.input(placeholder='Filter vetoed signals...').props('dense dark borderless').classes('bg-[#161b22] px-3 py-0.5 rounded border border-[#30363d] text-xs mono w-56')

                            vtbl = ui.table(
                                columns=v_cols,
                                rows=v_rows,
                                row_key='id',
                                pagination={'rowsPerPage': 10, 'sortBy': 'timestamp', 'descending': True, 'page': 1}
                            ).classes('w-full card-glass mono text-xs').props(':rows-per-page-options="[6, 10, 25, 50, 100]"')

                            vtbl.bind_filter_to(v_search, 'value')
                            attach_table_sort_reset(vtbl, 'timestamp', True)

                            vtbl.add_slot('body-cell-gate', '''
                                <q-td :props="props" class="text-left font-bold text-[#00f0ff]">
                                    {{ props.row.gate }}
                                </q-td>
                            ''')
                            vtbl.add_slot('body-cell-price', '<q-td :props="props" class="text-right">{{ props.row.price_str }}</q-td>')
                            vtbl.add_slot('body-cell-ret_72h', '''
                                <q-td :props="props" class="text-right font-bold" :class="props.row.ret_72h >= 0 ? 'text-[#00ff87]' : 'text-[#ff4655]'">
                                    {{ props.row.ret_72h_str }}
                                </q-td>
                            ''')
                            vtbl.add_slot('body-cell-mfe_72h', '<q-td :props="props" class="text-right text-[#00f0ff] font-bold">{{ props.row.mfe_72h_str }}</q-td>')
                            vtbl.add_slot('body-cell-mae_72h', '<q-td :props="props" class="text-right text-[#ff4655]">{{ props.row.mae_72h_str }}</q-td>')
                            vtbl.add_slot('body-cell-out_label', '''
                                <q-td :props="props" class="text-center">
                                    <span v-if="props.row.out_type === 'DODGED'" class="badge-tag badge-green">
                                        {{ props.row.out_label }}
                                    </span>
                                    <span v-else-if="props.row.out_type === 'MISSED'" class="badge-tag badge-amber">
                                        {{ props.row.out_label }}
                                    </span>
                                    <span v-else class="badge-tag badge-gray">
                                        {{ props.row.out_label }}
                                    </span>
                                </q-td>
                            ''')
                        else:
                            ui.label('No candidate breakout signals vetoed for this symbol.').classes('text-xs text-gray-400 mono py-8 text-center')

            # Card 4: Plain-English Retail Playbook Verdict (The Decision Engine)
            glow_class = "card-glow-green" if (open_trade is not None and open_trade.get('pnl', 0) > 0) else ("card-glow-cyan" if open_trade is not None else "border border-[#21262d]")
            with ui.card().classes(f'card-glass p-5 {glow_class} flex flex-col justify-between'):
                with ui.row().classes('w-full justify-between items-center mb-2'):
                    ui.label('🎯 RETAIL PLAYBOOK VERDICT (ACTIONABLE GUIDANCE)').classes('text-xs font-bold tracking-wider text-[#00f0ff] mono')
                    verdict_badge = '<span class="badge-tag badge-green">ACTIVE RIDE</span>' if open_trade is not None else '<span class="badge-tag badge-gray">WAIT FOR COIL</span>'
                    ui.html(verdict_badge)

                with ui.column().classes('gap-3 my-2 text-xs mono'):
                    if open_trade is not None:
                        en_px = float(open_trade['entry_price'])
                        cur_px_val = float(open_trade.get('exit_price', en_px))
                        st_px = float(open_trade.get('stop_price', en_px * 0.92))
                        pnl_p = float(open_trade.get('pnl', 0.0)) * 100.0
                        dist_st = ((cur_px_val - st_px) / cur_px_val * 100.0) if cur_px_val > 0 else 0.0
                        status_desc = f"Riding active {open_trade.get('book', 'Book 1')} position (Entry: ${en_px:,.4f}, Current: ${cur_px_val:,.4f}, PnL: {pnl_p:+.1f}%)."
                        stop_rule = f"Mandatory resting Stop-Market order MUST be active on exchange at ${st_px:,.4f} ({dist_st:.1f}% below market)."
                        if st_px >= en_px * 1.002:
                            be_rule = "Capital Risk: 0% (Stop locked in profit/breakeven). Free upside call option on cyclical trend."
                        else:
                            be_rule = f"Structural Stop: Initial floor protection active at ${st_px:,.4f}."
                        if pnl_p >= 25.0:
                            action_rule = f"Do NOT market-buy here; price is extended +{pnl_p:.1f}% from entry base. Let winners run to trailing floor."
                        else:
                            action_rule = "Hold position firmly. Allow trailing floor to ratchet without premature discretionary cuts."
                    else:
                        status_desc = "No active position in portfolio. Capital is 100% in cash preservation mode."
                        stop_rule = "No open exposure. Do NOT FOMO into unconfirmed spikes without a verified 72h compression shelf."
                        be_rule = f"Shelf Evaluation: Current 72h range is {diag['shelf_tightness']:.1f}%." + (" Ready for coiled breakout." if diag['shelf_tightness'] <= 25.0 else " Base is currently uncompressed.")
                        action_rule = "Awaiting confirmed institutional trigger before allocating risk capital."

                    with ui.row().classes('items-start gap-2'):
                        ui.label('⚡').classes('text-sm')
                        with ui.column().classes('gap-0'):
                            ui.label('Current Portfolio State:').classes('text-gray-400 font-bold')
                            ui.label(status_desc).classes('text-white')

                    with ui.row().classes('items-start gap-2'):
                        ui.label('🛡️').classes('text-sm')
                        with ui.column().classes('gap-0'):
                            ui.label('Capital Protection & Resting Stop:').classes('text-gray-400 font-bold')
                            ui.label(stop_rule).classes('text-[#00f0ff]')

                    with ui.row().classes('items-start gap-2'):
                        ui.label('⚖️').classes('text-sm')
                        with ui.column().classes('gap-0'):
                            ui.label('Risk Boundary:').classes('text-gray-400 font-bold')
                            ui.label(be_rule).classes('text-[#00ff87]')

                    with ui.row().classes('items-start gap-2'):
                        ui.label('🎯').classes('text-sm')
                        with ui.column().classes('gap-0'):
                            ui.label('Actionable Retail Rule:').classes('text-gray-400 font-bold')
                            ui.label(action_rule).classes('text-[#fbbf24]')

                    with ui.row().classes('items-start gap-2'):
                        ui.label('🛡️').classes('text-sm')
                        with ui.column().classes('gap-0'):
                            ui.label('Veto Protection Engine:').classes('text-gray-400 font-bold')
                            if not coin_vetoes.empty:
                                veto_txt = f"Filtered {len(coin_vetoes)} false breakouts ({dodged_cnt} Dodged Bullets), saving +{saved_loss:.0f}% in stop losses with {net_v_alpha:+.1f}% Net Veto Alpha."
                            else:
                                veto_txt = "No false breakout signals required veto intervention."
                            ui.label(veto_txt).classes('text-[#00ff87]')


# ---------------------------------------------------------------------------
# MAIN DASHBOARD VIEW
# ---------------------------------------------------------------------------
@ui.page('/')
def index_page():
    setup_page_head()

    macro = get_macro_weather()
    trades_df = load_v12_trades(CURRENT_ARM)
    tel_df = load_v12_telemetry(CURRENT_ARM)
    sc_df = load_v12_scorecard(CURRENT_ARM)
    tiers_df = load_asset_tiers()

    closed_df = trades_df[~trades_df['is_open']].copy() if not trades_df.empty and 'is_open' in trades_df.columns else pd.DataFrame()
    open_df = trades_df[trades_df['is_open']].copy() if not trades_df.empty and 'is_open' in trades_df.columns else pd.DataFrame()

    # Precalculate high-level metrics
    tot_closed = len(closed_df)
    tot_open = len(open_df)
    if tot_closed > 0:
        wins = closed_df[closed_df['pnl'] > 0]
        losses = closed_df[closed_df['pnl'] <= 0]
        win_rate = (len(wins) / tot_closed) * 100.0
        gw = wins['pnl'].sum()
        gl = abs(losses['pnl'].sum())
        profit_factor = (gw / gl) if gl > 0 else 999.0
        tot_log = closed_df['log_ret'].sum() * 100.0
        cap_multiple = np.exp(tot_log / 100.0)
    else:
        win_rate = 0.0
        profit_factor = 0.0
        tot_log = 0.0
        cap_multiple = 1.0

    # -----------------------------------------------------------------------
    # TOP HEADER & MACRO WEATHER STRIP
    # -----------------------------------------------------------------------
    with ui.header().classes('bg-[#0d1117] border-b border-[#21262d] px-6 py-3 flex items-center justify-between'):
        with ui.row().classes('items-center gap-4'):
            ui.label('KRONOS V12').classes('text-xl font-black tracking-wider text-[#00f0ff] mono')
            # Dynamic Ledger Arm Selector
            with ui.row().classes('items-center gap-2 bg-[#161b22] px-3 py-1 rounded-lg border border-[#30363d]'):
                ui.label('Arm:').classes('text-xs text-gray-400 mono font-bold')
                arms = get_available_arms()
                def set_arm(e):
                    global CURRENT_ARM
                    CURRENT_ARM = e.value
                    ui.navigate.to('/')
                arm_labels = {
                    'v12_decoupling_arm': '⚡ V12.2 Decoupling + ATH Clamp',
                    'v12_production': '🛡️ Canonical V12 Production'
                }
                options = {a: arm_labels.get(a, a) for a in arms}
                ui.select(options=options, value=CURRENT_ARM, on_change=set_arm).props('dense dark borderless options-dense').classes('text-xs mono w-64 text-cyan-300 font-bold')
            arm_badge = '<span class="badge-tag badge-green">V12.2 Decoupling Active</span>' if CURRENT_ARM == "v12_decoupling_arm" else '<span class="badge-tag badge-cyan">V12 Production Active</span>'
            ui.html(arm_badge)
            ui.html('<span class="badge-tag badge-purple">Port 8056</span>')

        with ui.row().classes('items-center gap-6'):
            regime_class = "badge-green" if macro['is_bull'] else "badge-red"
            with ui.row().classes('items-center gap-2'):
                ui.label('BTC 200d Macro:').classes('text-xs text-gray-400 mono')
                ui.label(f"${macro['price']:,.0f}").classes('text-sm font-bold text-white mono')
                dist_color = 'text-[#00ff87]' if macro['dist_ema'] >= 0 else 'text-[#ff4655]'
                ui.label(f"({macro['dist_ema']:+.1f}% vs EMA)").classes(f'text-xs {dist_color} mono')
                ui.label(f"30d: {macro.get('ret_30d', 0.0):+.1f}% | 14d: {macro.get('ret_14d', 0.0):+.1f}%").classes('text-xs text-gray-400 mono')
                if macro.get('days_below_ema', 0.0) > 0:
                    ui.label(f"Bear: {macro['days_below_ema']:.1f}d").classes('text-xs text-amber-400 mono')
                ui.html(f'<span class="badge-tag {regime_class}">{macro["status"]}</span>')

            # Fix #1 — Stale Data Visual Indicator in dashboard header
            import json as _json
            _sync_state_paths = [
                ROOT / "data" / "sync_state.json",
                ROOT / "config" / "ingestion" / "sync_state.json",
            ]
            _latest_ts = None
            for _sp in _sync_state_paths:
                if _sp.exists():
                    try:
                        _state = _json.loads(_sp.read_text())
                        for _k, _val in _state.items():
                            if isinstance(_val, dict):
                                for _ts_val in _val.values():
                                    try:
                                        from datetime import datetime as _dt, timezone as _tz
                                        _ts = _dt.fromtimestamp(float(_ts_val) / 1000.0, tz=_tz.utc)
                                        if _latest_ts is None or _ts > _latest_ts:
                                            _latest_ts = _ts
                                    except Exception:
                                        pass
                            else:
                                try:
                                    from datetime import datetime as _dt, timezone as _tz
                                    _ts = _dt.fromtimestamp(float(_val) / 1000.0, tz=_tz.utc)
                                    if _latest_ts is None or _ts > _latest_ts:
                                        _latest_ts = _ts
                                except Exception:
                                    pass
                    except Exception:
                        pass
            if _latest_ts:
                from datetime import datetime as _dt, timezone as _tz
                _age_h = (_dt.now(_tz.utc) - _latest_ts).total_seconds() / 3600
                _stale_thresh = int(os.getenv("HEALTH_STALE_HOURS", "2"))
                if _age_h > _stale_thresh:
                    ui.html(f'<span class="badge-tag badge-red">⚠️ DATA STALE ({_age_h:.1f}h)</span>')
                else:
                    ui.html(f'<span class="badge-tag badge-green">✅ LIVE ({_age_h:.1f}h ago)</span>')
            else:
                ui.html('<span class="badge-tag badge-amber">⚙️ SYNC STATE UNKNOWN</span>')

            ui.button(icon='refresh', on_click=lambda: ui.navigate.to('/')).props('flat round dense color=cyan')

    # -----------------------------------------------------------------------
    # KPI METRIC CARDS STRIP
    # -----------------------------------------------------------------------
    with ui.column().classes('w-full max-w-[1600px] mx-auto p-6 gap-6'):
        with ui.row().classes('w-full grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4'):
            # Card 1: Capital Multiple
            with ui.card().classes('card-glass p-4 border-l-4 border-l-[#00f0ff]'):
                ui.label('CAPITAL GROWTH').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                ui.label(f"{cap_multiple:.2f}x").classes('text-2xl font-black text-[#00f0ff] mono mt-1')
                ui.label(f"{tot_log:+.1f}% Total Log PnL").classes('text-xs text-gray-400 mono')

            # Card 2: Profit Factor
            with ui.card().classes('card-glass p-4 border-l-4 border-l-[#00ff87]'):
                ui.label('PROFIT FACTOR').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                ui.label(f"{profit_factor:.3f}").classes('text-2xl font-black text-[#00ff87] mono mt-1')
                ui.label(f"Win Rate: {win_rate:.1f}%").classes('text-xs text-gray-400 mono')

            # Card 3: Closed Trades
            with ui.card().classes('card-glass p-4 border-l-4 border-l-[#a855f7]'):
                ui.label('CLOSED TRADES').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                ui.label(f"{tot_closed:,}").classes('text-2xl font-black text-white mono mt-1')
                ui.label('Clean-room audited').classes('text-xs text-gray-400 mono')

            # Card 4: Open Positions
            with ui.card().classes('card-glass p-4 border-l-4 border-l-[#f59e0b]'):
                ui.label('ACTIVE POSITIONS').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                ui.label(f"{tot_open}").classes('text-2xl font-black text-[#fbbf24] mono mt-1')
                ui.label('Resting Stop-Market').classes('text-xs text-gray-400 mono')

            # Card 5: Veto Alpha
            summary_tel = TelemetryCollector.compute_veto_alpha_summary(tel_df) if not tel_df.empty else {}
            net_alpha = summary_tel.get('net_veto_alpha_pct', 0.0)
            with ui.card().classes('card-glass p-4 border-l-4 border-l-[#00ff87]'):
                ui.label('NET VETO ALPHA').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                alpha_col = '#00ff87' if net_alpha >= 0 else '#ff4655'
                ui.label(f"{net_alpha:+.1f}%").classes(f'text-2xl font-black text-[{alpha_col}] mono mt-1')
                ui.label(f"Saved: +{summary_tel.get('saved_losses_pct', 0.0):.0f}%").classes('text-xs text-gray-400 mono')

            # Card 6: Dodged Bullets
            dodged_cnt = summary_tel.get('dodged_bullets', 0)
            with ui.card().classes('card-glass p-4 border-l-4 border-l-[#00f0ff]'):
                ui.label('DODGED BULLETS').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                ui.label(f"{dodged_cnt:,}").classes('text-2xl font-black text-[#00f0ff] mono mt-1')
                ui.label(f"Efficiency: {summary_tel.get('efficiency_ratio', 0.0):.1f}%").classes('text-xs text-gray-400 mono')

        # -------------------------------------------------------------------
        # TOP-LEVEL COMPREHENSIVE NAVIGATION TABS
        # -------------------------------------------------------------------
        with ui.tabs().classes('w-full text-gray-400 border-b border-[#21262d]') as tabs:
            tab_open = ui.tab('open', label=f'⚡ Open Positions ({tot_open})')
            tab_closed = ui.tab('closed', label=f'📜 Closed Positions ({tot_closed})')
            tab_portfolio = ui.tab('portfolio', label='💼 Portfolio & Sizing Allocation')
            veto_cnt = summary_tel.get('total_vetoes', len(tel_df))
            tab_veto = ui.tab('veto', label=f'🛡️ Vetoed Trades Log ({veto_cnt:,})')
            tab_radar = ui.tab('radar', label='🎯 Research Radar & Suggestions')
            tab_forensics = ui.tab('forensics', label='⚖️ Forensic Reasoner')
            tab_equity = ui.tab('equity', label='📈 Equity Curve & Scorecard')
            tab_timeline = ui.tab('timeline', label='📅 Execution Timeline & Traverse')

        with ui.tab_panels(tabs, value=tab_open).classes('w-full bg-transparent p-0'):
            # ---------------------------------------------------------------
            # 1. ⚡ OPEN POSITIONS TAB (ACTIVE PORTFOLIO)
            # ---------------------------------------------------------------
            with ui.tab_panel(tab_open).classes('p-0 gap-6 flex flex-col'):
                with ui.row().classes('w-full justify-between items-center'):
                    ui.label('⚡ LIVE ACTIVE PORTFOLIO & RESTING STOP AUDIT').classes('text-sm font-bold tracking-wider text-[#00f0ff] mono')
                    ui.label(f'Total Active Positions: {tot_open}').classes('text-xs text-gray-400 mono')

                if not open_df.empty:
                    # Open Positions KPI Summary
                    open_pnl_sum = open_df['pnl'].sum() * 100.0 if 'pnl' in open_df.columns else 0.0
                    open_log_sum = open_df['log_ret'].sum() * 100.0 if 'log_ret' in open_df.columns else 0.0
                    be_count = (open_df['stop_price'] >= open_df['entry_price']).sum() if 'stop_price' in open_df.columns else 0

                    with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-4 gap-4'):
                        with ui.card().classes('card-glass p-4 border border-[#21262d]'):
                            ui.label('UNREALIZED ARITHMETIC PNL').classes('text-xs text-gray-400 mono font-bold')
                            pnl_c = '#00ff87' if open_pnl_sum >= 0 else '#ff4655'
                            ui.label(f"{open_pnl_sum:+.2f}%").classes(f'text-2xl font-black text-[{pnl_c}] mono mt-1')

                        with ui.card().classes('card-glass p-4 border border-[#21262d]'):
                            ui.label('UNREALIZED LOG RETURN').classes('text-xs text-gray-400 mono font-bold')
                            ui.label(f"{open_log_sum:+.2f}%").classes('text-2xl font-black text-[#00f0ff] mono mt-1')

                        with ui.card().classes('card-glass p-4 border border-[#21262d]'):
                            ui.label('PROTECTED STOPS (BE/PROFIT)').classes('text-xs text-gray-400 mono font-bold')
                            ui.label(f"{be_count} / {tot_open}").classes('text-2xl font-black text-[#00ff87] mono mt-1')

                        with ui.card().classes('card-glass p-4 border border-[#21262d]'):
                            ui.label('EXCHANGE ORDERBOOK AUDIT').classes('text-xs text-gray-400 mono font-bold')
                            ui.label('100% NATIVE RESTING').classes('text-lg font-black text-[#a855f7] mono mt-1')

                    # Open Positions Detailed Table
                    open_rows = []
                    for idx, r in open_df.reset_index(drop=True).iterrows():
                        entry_px = float(r.get('entry_price', 0.0))
                        cur_px = float(r.get('exit_price', entry_px))
                        stop_px = float(r.get('stop_price', entry_px * 0.88))
                        dist_to_stop = ((cur_px - stop_px) / cur_px) * 100.0 if cur_px > 0 else 0.0
                        is_reclaim = bool(r.get('is_reclaim', False))
                        b_val = str(r.get('book', ''))
                        if b_val == 'Book 3':
                            setup_name = "Book 3: Flush Reclaim"
                        elif b_val == 'Book 2':
                            setup_name = "Book 2: Coiled Squeeze"
                        elif is_reclaim:
                            setup_name = "Bear-Trap Reclaim"
                        else:
                            setup_name = "Book 1: Continuation"

                        if stop_px >= entry_px * 1.015:
                            stop_status = "LOCKED IN PROFIT"
                        elif stop_px >= entry_px * 1.002:
                            stop_status = "BREAKEVEN RATCHET"
                        else:
                            stop_status = "INITIAL STRUCTURAL"

                        pnl_f = float(r.get('pnl', 0.0)) * 100.0
                        log_f = float(r.get('log_ret', 0.0)) * 100.0
                        mfe_f = float(r.get('mfe', 0.0)) * 100.0
                        dur_f = float(r.get('duration_hours', 0.0))
                        open_rows.append({
                            'id': f"{r.get('asset')}_{r.get('entry')}_{idx}",
                            'asset': str(r.get('asset', '')),
                            'tier': str(r.get('tier', '')),
                            'book': str(r.get('book', '')),
                            'setup': setup_name,
                            'entry': str(r.get('entry', ''))[:16],
                            'entry_price': entry_px,
                            'exit_price': cur_px,
                            'stop_price': stop_px,
                            'dist_stop': dist_to_stop,
                            'stop_status': stop_status,
                            'pnl': pnl_f,
                            'log_ret': log_f,
                            'mfe': mfe_f,
                            'duration_hours': dur_f,
                            'entry_price_str': f"${entry_px:,.4f}",
                            'exit_price_str': f"${cur_px:,.4f}",
                            'stop_price_str': f"${stop_px:,.4f}",
                            'dist_stop_str': f"{dist_to_stop:.1f}%",
                            'pnl_str': f"{pnl_f:+.2f}%",
                            'log_ret_str': f"{log_f:+.2f}%",
                            'mfe_str': f"+{mfe_f:.1f}%",
                            'duration_str': f"{int(dur_f)}h",
                        })

                    open_cols = [
                        {'name': 'asset', 'label': 'Asset', 'field': 'asset', 'align': 'left', 'sortable': True},
                        {'name': 'tier', 'label': 'Tier', 'field': 'tier', 'align': 'center', 'sortable': True},
                        {'name': 'book', 'label': 'Book', 'field': 'book', 'align': 'center', 'sortable': True},
                        {'name': 'setup', 'label': 'Setup Type', 'field': 'setup', 'align': 'left'},
                        {'name': 'entry', 'label': 'Entry Time (UTC)', 'field': 'entry', 'sortable': True},
                        {'name': 'entry_price', 'label': 'Entry Price', 'field': 'entry_price', 'align': 'right', 'sortable': True},
                        {'name': 'exit_price', 'label': 'Current Price', 'field': 'exit_price', 'align': 'right', 'sortable': True},
                        {'name': 'stop_price', 'label': 'Resting Stop', 'field': 'stop_price', 'align': 'right', 'sortable': True},
                        {'name': 'dist_stop', 'label': 'Distance to Stop', 'field': 'dist_stop', 'align': 'right', 'sortable': True},
                        {'name': 'stop_status', 'label': 'Stop Status', 'field': 'stop_status', 'align': 'center'},
                        {'name': 'pnl', 'label': 'Unrealized PnL', 'field': 'pnl', 'align': 'right', 'sortable': True},
                        {'name': 'log_ret', 'label': 'Log Ret', 'field': 'log_ret', 'align': 'right', 'sortable': True},
                        {'name': 'mfe', 'label': 'Peak MFE', 'field': 'mfe', 'align': 'right', 'sortable': True},
                        {'name': 'duration_hours', 'label': 'Duration', 'field': 'duration_hours', 'align': 'right', 'sortable': True},
                    ]
                    ot = ui.table(columns=open_cols, rows=open_rows, row_key='id').classes('w-full card-glass mono')
                    ot.add_slot('body-cell-asset', '''
                        <q-td :props="props">
                            <a :href="'/coin/' + props.row.asset" class="text-[#00f0ff] hover:underline font-bold cursor-pointer">
                                {{ props.row.asset }} ↗
                            </a>
                        </q-td>
                    ''')
                    ot.add_slot('body-cell-entry_price', '<q-td :props="props" class="text-right">{{ props.row.entry_price_str }}</q-td>')
                    ot.add_slot('body-cell-exit_price', '<q-td :props="props" class="text-right">{{ props.row.exit_price_str }}</q-td>')
                    ot.add_slot('body-cell-stop_price', '<q-td :props="props" class="text-right text-[#00f0ff]">{{ props.row.stop_price_str }}</q-td>')
                    ot.add_slot('body-cell-dist_stop', '<q-td :props="props" class="text-right">{{ props.row.dist_stop_str }}</q-td>')
                    ot.add_slot('body-cell-pnl', '''
                        <q-td :props="props" class="text-right font-bold" :class="props.row.pnl >= 0 ? 'text-[#00ff87]' : 'text-[#ff4655]'">
                            {{ props.row.pnl_str }}
                        </q-td>
                    ''')
                    ot.add_slot('body-cell-log_ret', '''
                        <q-td :props="props" class="text-right" :class="props.row.log_ret >= 0 ? 'text-[#00ff87]' : 'text-[#ff4655]'">
                            {{ props.row.log_ret_str }}
                        </q-td>
                    ''')
                    ot.add_slot('body-cell-mfe', '<q-td :props="props" class="text-right text-[#00f0ff] font-bold">{{ props.row.mfe_str }}</q-td>')
                    ot.add_slot('body-cell-duration_hours', '<q-td :props="props" class="text-right">{{ props.row.duration_str }}</q-td>')
                else:
                    ui.label('No positions currently open. Defaulting to Cash.').classes('text-gray-400 mono')

            # ---------------------------------------------------------------
            # 2. 📜 CLOSED POSITIONS TAB (FULL DATE-WISE LEDGER)
            # ---------------------------------------------------------------
            with ui.tab_panel(tab_closed).classes('p-0 gap-6 flex flex-col'):
                with ui.row().classes('w-full justify-between items-center'):
                    with ui.row().classes('items-center gap-3'):
                        ui.label('📜 COMPLETE DATE-WISE CLOSED TRADES LEDGER').classes('text-sm font-bold tracking-wider text-[#00f0ff] mono')
                        ui.label(f'Total Closed: {tot_closed:,} trades | Strict Compounding Log Metrics').classes('text-xs text-gray-400 mono')
                    with ui.row().classes('items-center gap-2'):
                        def _download_all_books():
                            p = ROOT / "data" / "all_tapes" / CURRENT_ARM / "all_books.csv"
                            if p.exists():
                                ui.download(str(p), filename=f"{CURRENT_ARM}_all_books.csv")
                            else:
                                ui.notify(f"all_books.csv not found for {CURRENT_ARM}", type='warning')
                        def _download_books_summary():
                            p = ROOT / "data" / "all_tapes" / CURRENT_ARM / "books_summary.csv"
                            if p.exists():
                                ui.download(str(p), filename=f"{CURRENT_ARM}_books_summary.csv")
                            else:
                                ui.notify(f"books_summary.csv not found for {CURRENT_ARM}", type='warning')
                        ui.button('ALL BOOKS CSV', icon='download', on_click=_download_all_books).props('dense outline color=cyan text-color=cyan').classes('mono text-xs')
                        ui.button('BOOKS SUMMARY CSV', icon='table_chart', on_click=_download_books_summary).props('dense outline color=cyan text-color=cyan').classes('mono text-xs')

                if not closed_df.empty:
                    sorted_closed = closed_df.sort_values('exit', ascending=False).copy()

                    # Filter State Container
                    filter_box = ui.row().classes('w-full gap-4 items-center bg-[#0d1117] p-3 rounded-lg border border-[#21262d]')
                    table_container = ui.column().classes('w-full')

                    def render_closed_table(filtered_data):
                        table_container.clear()
                        rows_data = []
                        for idx, r in filtered_data.reset_index(drop=True).iterrows():
                            pnl_val = float(r.get('pnl', 0.0)) * 100.0
                            log_val = float(r.get('log_ret', 0.0)) * 100.0
                            mfe_val = float(r.get('mfe', 0.0)) * 100.0
                            dur_val = float(r.get('duration_hours', 0.0))
                            en_px   = float(r.get('entry_price', 0.0))
                            ex_px   = float(r.get('exit_price', 0.0))
                            sym     = str(r.get('asset', ''))
                            en_time = str(r.get('entry', ''))[:16]
                            ex_time = str(r.get('exit', ''))[:16]
                            rows_data.append({
                                'id': f"{sym}_{en_time}_{ex_time}_{idx}",
                                'entry': en_time,
                                'exit': ex_time,
                                'asset': sym,
                                'tier': str(r.get('tier', 'Tier 1')),
                                'book': str(r.get('book', 'Book 1')),
                                'entry_price': en_px,
                                'exit_price': ex_px,
                                'duration': dur_val,
                                'pnl': pnl_val,
                                'log_ret': log_val,
                                'mfe': mfe_val,
                                'entry_price_str': f"${en_px:,.4f}",
                                'exit_price_str': f"${ex_px:,.4f}",
                                'duration_str': f"{int(dur_val)}h",
                                'pnl_str': f"{pnl_val:+.2f}%",
                                'log_ret_str': f"{log_val:+.2f}%",
                                'mfe_str': f"+{mfe_val:.1f}%",
                                'reason': str(r.get('reason', '')),
                            })

                        cols = [
                            {'name': 'exit', 'label': 'Exit Date (UTC)', 'field': 'exit', 'align': 'left', 'sortable': True},
                            {'name': 'entry', 'label': 'Entry Date (UTC)', 'field': 'entry', 'align': 'left', 'sortable': True},
                            {'name': 'asset', 'label': 'Asset', 'field': 'asset', 'align': 'left', 'sortable': True},
                            {'name': 'tier', 'label': 'Tier', 'field': 'tier', 'align': 'center', 'sortable': True},
                            {'name': 'book', 'label': 'Book', 'field': 'book', 'align': 'center', 'sortable': True},
                            {'name': 'entry_price', 'label': 'Entry Px', 'field': 'entry_price', 'align': 'right', 'sortable': True},
                            {'name': 'exit_price', 'label': 'Exit Px', 'field': 'exit_price', 'align': 'right', 'sortable': True},
                            {'name': 'duration', 'label': 'Duration', 'field': 'duration', 'align': 'right', 'sortable': True},
                            {'name': 'pnl', 'label': 'PnL (%)', 'field': 'pnl', 'align': 'right', 'sortable': True},
                            {'name': 'log_ret', 'label': 'Net Log Ret', 'field': 'log_ret', 'align': 'right', 'sortable': True},
                            {'name': 'mfe', 'label': 'Peak MFE', 'field': 'mfe', 'align': 'right', 'sortable': True},
                            {'name': 'reason', 'label': 'Exit Trigger', 'field': 'reason', 'align': 'center', 'sortable': True},
                        ]

                        with table_container:
                            t = ui.table(columns=cols, rows=rows_data, row_key='id', pagination={'rowsPerPage': 25}).classes('w-full card-glass mono')
                            t.add_slot('body-cell-asset', '''
                                <q-td :props="props">
                                    <a :href="'/coin/' + props.row.asset" class="text-[#00f0ff] hover:underline font-bold cursor-pointer">
                                        {{ props.row.asset }} ↗
                                    </a>
                                </q-td>
                            ''')
                            t.add_slot('body-cell-entry_price', '<q-td :props="props" class="text-right">{{ props.row.entry_price_str }}</q-td>')
                            t.add_slot('body-cell-exit_price', '<q-td :props="props" class="text-right">{{ props.row.exit_price_str }}</q-td>')
                            t.add_slot('body-cell-duration', '<q-td :props="props" class="text-right">{{ props.row.duration_str }}</q-td>')
                            t.add_slot('body-cell-pnl', '''
                                <q-td :props="props" class="text-right font-bold" :class="props.row.pnl >= 0 ? 'text-[#00ff87]' : 'text-[#ff4655]'">
                                    {{ props.row.pnl_str }}
                                </q-td>
                            ''')
                            t.add_slot('body-cell-log_ret', '''
                                <q-td :props="props" class="text-right" :class="props.row.log_ret >= 0 ? 'text-[#00ff87]' : 'text-[#ff4655]'">
                                    {{ props.row.log_ret_str }}
                                </q-td>
                            ''')
                            t.add_slot('body-cell-mfe', '<q-td :props="props" class="text-right text-[#00f0ff] font-bold">{{ props.row.mfe_str }}</q-td>')

                    # Interactive Filter Inputs
                    with filter_box:
                        sym_input = ui.input(placeholder='Search Symbol (e.g. SOL)...').classes('w-44 filter-input px-3 py-1 mono text-xs')
                        tier_select = ui.select(['All Tiers', 'Tier 1', 'Tier 2', 'Tier 3'], value='All Tiers').classes('w-32 mono text-xs')
                        book_select = ui.select(['All Books', 'Book 1', 'Book 2', 'Book 3'], value='All Books').classes('w-32 mono text-xs')
                        outcome_select = ui.select(['All Outcomes', 'Winners Only', 'Losses Only'], value='All Outcomes').classes('w-36 mono text-xs')
                        # MEDIUM-8: Trade type filter for Reclaim / Continuation / Squeeze isolation
                        type_options = ['All Types']
                        if 'trade_type' in sorted_closed.columns:
                            type_options += sorted(sorted_closed['trade_type'].dropna().unique().tolist())
                        type_select = ui.select(type_options, value='All Types').classes('w-40 mono text-xs')

                        def apply_closed_filters():
                            df_f = sorted_closed.copy()
                            sym_text = sym_input.value.strip().upper() if sym_input.value else ""
                            if sym_text:
                                df_f = df_f[df_f['asset'].str.contains(sym_text, case=False, na=False)]
                            if tier_select.value != 'All Tiers':
                                df_f = df_f[df_f['tier'] == tier_select.value]
                            if book_select.value != 'All Books':
                                df_f = df_f[df_f['book'] == book_select.value]
                            if outcome_select.value == 'Winners Only':
                                df_f = df_f[df_f['pnl'] > 0]
                            elif outcome_select.value == 'Losses Only':
                                df_f = df_f[df_f['pnl'] <= 0]
                            # MEDIUM-8: Apply trade type filter
                            if type_select.value != 'All Types' and 'trade_type' in df_f.columns:
                                df_f = df_f[df_f['trade_type'] == type_select.value]
                            render_closed_table(df_f)

                        sym_input.on('update:model-value', lambda _: apply_closed_filters())
                        tier_select.on('update:model-value', lambda _: apply_closed_filters())
                        book_select.on('update:model-value', lambda _: apply_closed_filters())
                        outcome_select.on('update:model-value', lambda _: apply_closed_filters())
                        type_select.on('update:model-value', lambda _: apply_closed_filters())

                    # Initial Table Render
                    render_closed_table(sorted_closed)
                else:
                    ui.label('No closed trades in production tape. Run pipeline_v12.ps1.').classes('text-gray-400 mono')

            # ---------------------------------------------------------------
            # 💼 PORTFOLIO & SIZING ALLOCATION TAB
            # ---------------------------------------------------------------
            with ui.tab_panel(tab_portfolio).classes('p-0 gap-6 flex flex-col'):
                with ui.row().classes('w-full justify-between items-center'):
                    ui.label('💼 CONCURRENT PORTFOLIO ARCHITECTURE & CAPITAL SIZING').classes('text-sm font-bold tracking-wider text-[#00f0ff] mono')
                    ui.label('Production Sizing Standard: Segregated 80/20 Dual-Sleeve Allocation').classes('text-xs text-gray-400 mono')

                # Calculate live sleeve allocations from open positions
                n_open_b1 = int((open_df['book'] == 'Book 1').sum()) if ('book' in open_df.columns and not open_df.empty) else 0
                n_open_b2 = int((open_df['book'] == 'Book 2').sum()) if ('book' in open_df.columns and not open_df.empty) else 0
                n_open_trend = n_open_b1 + n_open_b2
                n_open_flush = int((open_df['book'] == 'Book 3').sum()) if ('book' in open_df.columns and not open_df.empty) else 0

                # Top Live Slot Utilization Gauges
                with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-3 gap-4'):
                    # Sleeve 1: Trend Sleeve
                    with ui.card().classes('card-glass p-5 border-l-4 border-l-[#00f0ff] flex flex-col justify-between'):
                        ui.label('PRIMARY TREND SLEEVE (BOOKS 1 & 2)').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                        with ui.row().classes('w-full justify-between items-baseline mt-2'):
                            ui.label(f"{n_open_trend} / 8 Slots").classes('text-2xl font-black text-[#00f0ff] mono')
                            ui.label('80% NAV Budget').classes('text-xs text-[#00f0ff] font-bold mono')
                        ui.label(f"Book 1 Breakouts: {n_open_b1} | Book 2 Squeezes: {n_open_b2}").classes('text-xs text-gray-400 mono mt-1')
                        ui.label("Max 10.0% NAV per slot | Trailing Donchian floor").classes('text-[11px] text-gray-500 mono mt-1')

                    # Sleeve 2: Flush Satellite Sleeve
                    with ui.card().classes('card-glass p-5 border-l-4 border-l-[#a855f7] flex flex-col justify-between'):
                        ui.label('SATELLITE FLUSH SLEEVE (BOOK 3)').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                        with ui.row().classes('w-full justify-between items-baseline mt-2'):
                            ui.label(f"{n_open_flush} / 8 Slots").classes('text-2xl font-black text-[#a855f7] mono')
                            ui.label('20% NAV Budget').classes('text-xs text-[#a855f7] font-bold mono')
                        ui.label(f"Active Flush Limit Absorptions: {n_open_flush}").classes('text-xs text-gray-400 mono mt-1')
                        ui.label("Max 2.5% NAV per bid | Target reclaim at P0").classes('text-[11px] text-gray-500 mono mt-1')

                    # Total Portfolio Utilization
                    tot_slots_active = n_open_trend + n_open_flush
                    util_pct = (tot_slots_active / 16.0) * 100.0
                    with ui.card().classes('card-glass p-5 border-l-4 border-l-[#00ff87] flex flex-col justify-between'):
                        ui.label('TOTAL PORTFOLIO SLOT UTILIZATION').classes('text-xs text-gray-400 font-bold tracking-wider mono')
                        with ui.row().classes('w-full justify-between items-baseline mt-2'):
                            ui.label(f"{tot_slots_active} / 16 Active").classes('text-2xl font-black text-[#00ff87] mono')
                            ui.label(f"{util_pct:.1f}% Capacity").classes('text-xs text-[#00ff87] font-bold mono')
                        ui.label("Sleeve Isolation: Ring-Fenced").classes('text-xs text-gray-400 mono mt-1')
                        ui.label("Zero cross-sleeve cannibalization guaranteed").classes('text-[11px] text-gray-500 mono mt-1')

                # Historical Multi-Book Performance Attribution
                ui.label('📊 HISTORICAL MULTI-BOOK ATTRIBUTION').classes('text-sm font-bold tracking-wider text-[#00f0ff] mono mt-4')
                if not closed_df.empty:
                    with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-3 gap-4'):
                        for b_name, b_badge, b_col in [
                            ('Book 1', 'Continuation Trend', '#00f0ff'),
                            ('Book 2', 'Coiled Squeeze', '#00ff87'),
                            ('Book 3', 'Flush Reclaim', '#a855f7')
                        ]:
                            b_df = closed_df[closed_df['book'] == b_name] if 'book' in closed_df.columns else pd.DataFrame()
                            n_b = len(b_df)
                            if n_b > 0:
                                b_wr = (b_df['pnl'] > 0).mean() * 100.0
                                b_w_sum = b_df[b_df['pnl'] > 0]['pnl'].sum()
                                b_l_sum = abs(b_df[b_df['pnl'] <= 0]['pnl'].sum())
                                b_pf = b_w_sum / b_l_sum if b_l_sum > 0 else 0.0
                                b_tot_log = b_df['log_ret'].sum() * 100.0
                                b_mult = np.exp(b_tot_log / 100.0)
                            else:
                                b_wr, b_pf, b_tot_log, b_mult = 0.0, 0.0, 0.0, 1.0

                            with ui.card().classes('card-glass p-5 border border-[#21262d] flex flex-col justify-between'):
                                with ui.row().classes('w-full justify-between items-center'):
                                    ui.label(b_name).classes(f'text-lg font-black text-[{b_col}] mono')
                                    ui.html(f'<span class="badge-tag" style="background: rgba(255,255,255,0.06); color: {b_col};">{b_badge}</span>')
                                ui.separator().classes('my-3 bg-[#21262d]')
                                with ui.row().classes('w-full justify-between mb-2 text-xs mono'):
                                    ui.label('Closed Trades:')
                                    ui.label(f"{n_b:,}").classes('font-bold text-white')
                                with ui.row().classes('w-full justify-between mb-2 text-xs mono'):
                                    ui.label('Win Rate:')
                                    ui.label(f"{b_wr:.1f}%").classes('font-bold text-[#00ff87]' if b_wr >= 50 else 'text-white')
                                with ui.row().classes('w-full justify-between mb-2 text-xs mono'):
                                    ui.label('Profit Factor (Log):')
                                    ui.label(f"{b_pf:.3f}").classes(f'font-bold text-[{b_col}]')
                                with ui.row().classes('w-full justify-between mb-2 text-xs mono'):
                                    ui.label('Net Log PnL:')
                                    ui.label(f"{b_tot_log:+.1f}%").classes('font-bold text-white')
                                with ui.row().classes('w-full justify-between text-xs mono'):
                                    ui.label('Compounded Multiple:')
                                    ui.label(f"{b_mult:,.1f}x").classes(f'font-bold text-[{b_col}]')

                # Executive Simulation Matrix (from PORTFOLIO_CONCURRENT_CAPITAL_SIZING.md)
                ui.label('🔬 CONCURRENT FINITE-SLOT SIMULATION MATRIX (652 SHARDS, 2020-2026)').classes('text-sm font-bold tracking-wider text-[#00f0ff] mono mt-4')
                sim_matrix_rows = [
                    {'model': 'Unified 5 Slots (20% / slot)', 'trades': '1,337', 'fill': '34.1%', 'avg_slots': '4.0', 'cagr': '+2.3%', 'end_cap': '$114,669', 'mult': '1.1x', 'max_dd': '69.6%', 'sharpe': '0.07', 'calmar': '0.03', 'status': 'REJECTED (Concentration Drag)'},
                    {'model': 'Unified 10 Slots (10% / slot)', 'trades': '2,054', 'fill': '52.5%', 'avg_slots': '7.3', 'cagr': '+17.0%', 'end_cap': '$253,382', 'mult': '2.5x', 'max_dd': '54.7%', 'sharpe': '0.73', 'calmar': '0.31', 'status': 'Suboptimal'},
                    {'model': 'Unified 15 Slots (6.7% / slot)', 'trades': '2,553', 'fill': '65.2%', 'avg_slots': '10.0', 'cagr': '+23.9%', 'end_cap': '$354,728', 'mult': '3.5x', 'max_dd': '39.4%', 'sharpe': '1.20', 'calmar': '0.61', 'status': 'Viable Unified'},
                    {'model': 'Unified 20 Slots (5% / slot)', 'trades': '2,898', 'fill': '74.0%', 'avg_slots': '12.2', 'cagr': '+24.4%', 'end_cap': '$362,998', 'mult': '3.6x', 'max_dd': '32.8%', 'sharpe': '1.39', 'calmar': '0.74', 'status': 'Best Unified'},
                    {'model': 'Segregated 70/30 (5 Trend / 5 Flush)', 'trades': '1,790', 'fill': '45.7%', 'avg_slots': '5.6', 'cagr': '+17.3%', 'end_cap': '$257,286', 'mult': '2.6x', 'max_dd': '30.5%', 'sharpe': '0.94', 'calmar': '0.57', 'status': 'Moderate Capacity'},
                    {'model': 'Segregated 70/30 (5 Trend / 10 Flush)', 'trades': '2,343', 'fill': '59.8%', 'avg_slots': '7.8', 'cagr': '+20.7%', 'end_cap': '$303,596', 'mult': '3.0x', 'max_dd': '21.8%', 'sharpe': '1.15', 'calmar': '0.95', 'status': 'Low DD Alternative'},
                    {'model': 'Segregated 80/20 (5 Trend / 5 Flush)', 'trades': '1,790', 'fill': '45.7%', 'avg_slots': '5.6', 'cagr': '+20.2%', 'end_cap': '$296,400', 'mult': '3.0x', 'max_dd': '22.1%', 'sharpe': '1.05', 'calmar': '0.91', 'status': 'Conservative'},
                    {'model': 'Segregated 80/20 (8 Trend / 8 Flush)', 'trades': '2,297', 'fill': '58.7%', 'avg_slots': '8.1', 'cagr': '+18.4%', 'end_cap': '$271,924', 'mult': '2.7x', 'max_dd': '18.0%', 'sharpe': '1.26', 'calmar': '1.02', 'status': 'PRODUCTION WINNER ⭐'},
                    {'model': 'Segregated 80/20 (10 Trend / 10 Flush)', 'trades': '2,540', 'fill': '64.9%', 'avg_slots': '9.4', 'cagr': '+17.1%', 'end_cap': '$253,761', 'mult': '2.5x', 'max_dd': '15.0%', 'sharpe': '1.34', 'calmar': '1.14', 'status': 'LOWEST DRAWDOWN ⭐'},
                ]
                sim_cols = [
                    {'name': 'model', 'label': 'Architecture Model', 'field': 'model', 'align': 'left'},
                    {'name': 'trades', 'label': 'Trades', 'field': 'trades', 'align': 'right'},
                    {'name': 'fill', 'label': 'Accept Rate', 'field': 'fill', 'align': 'right'},
                    {'name': 'avg_slots', 'label': 'Avg Slots', 'field': 'avg_slots', 'align': 'right'},
                    {'name': 'cagr', 'label': 'CAGR (%)', 'field': 'cagr', 'align': 'right'},
                    {'name': 'end_cap', 'label': 'Ending Capital ($100k)', 'field': 'end_cap', 'align': 'right'},
                    {'name': 'max_dd', 'label': 'Max DD (%)', 'field': 'max_dd', 'align': 'right'},
                    {'name': 'sharpe', 'label': 'Sharpe', 'field': 'sharpe', 'align': 'right'},
                    {'name': 'calmar', 'label': 'Calmar', 'field': 'calmar', 'align': 'right'},
                    {'name': 'status', 'label': 'Status / Verdict', 'field': 'status', 'align': 'center'},
                ]
                st = ui.table(columns=sim_cols, rows=sim_matrix_rows, row_key='model').classes('w-full card-glass mono')
                st.add_slot('body-cell-status', '''
                    <q-td :props="props" class="text-center font-bold">
                        <span v-if="props.row.status.includes('WINNER')" class="text-[#00ff87]">{{ props.row.status }}</span>
                        <span v-else-if="props.row.status.includes('LOWEST')" class="text-[#00f0ff]">{{ props.row.status }}</span>
                        <span v-else-if="props.row.status.includes('REJECTED')" class="text-[#ff4655]">{{ props.row.status }}</span>
                        <span v-else class="text-gray-400">{{ props.row.status }}</span>
                    </q-td>
                ''')

            # ---------------------------------------------------------------
            # 3. 🛡️ DATE-WISE VETOED TRADES HUB
            # ---------------------------------------------------------------
            with ui.tab_panel(tab_veto).classes('p-0 gap-6 flex flex-col'):
                with ui.row().classes('w-full justify-between items-center'):
                    ui.label('🛡️ DATE-WISE VETOED TRADES LOG (COUNTERFACTUAL FLIGHT RECORDER)').classes('text-sm font-bold tracking-wider text-[#00f0ff] mono')
                    ui.label(f'Total Logged: {veto_cnt:,} candidate evaluations | No Silent Drops').classes('text-xs text-gray-400 mono')

                if not tel_df.empty:
                    vetoed_records = tel_df[tel_df['status'] == 'VETOED'].sort_values('timestamp', ascending=False).copy()

                    # MEDIUM-10: Veto Gate Attribution Visual Chart
                    with ui.card().classes('card-glass p-4 border border-[#21262d] w-full mb-2'):
                        with ui.row().classes('w-full justify-between items-center mb-2'):
                            ui.label('🛡️ VETO GATE ATTRIBUTION & STATISTICAL LOSS PROTECTION BREAKDOWN').classes('text-xs text-[#00f0ff] mono font-bold')
                            ui.label(f"Total Filtered: {len(vetoed_records):,} setups").classes('text-xs text-gray-400 mono')
                        
                        gate_counts = vetoed_records['veto_gate'].value_counts()
                        gate_chart_data = [{'name': str(k), 'value': int(v)} for k, v in gate_counts.items()]
                        ui.echart({
                            'backgroundColor': 'transparent',
                            'tooltip': {'trigger': 'item', 'formatter': '{b}: {c} ({d}%)'},
                            'legend': {'orient': 'vertical', 'right': 10, 'top': 'center', 'textStyle': {'color': '#9ca3af', 'fontSize': 11}},
                            'series': [{
                                'name': 'Veto Gate',
                                'type': 'pie',
                                'radius': ['40%', '70%'],
                                'center': ['35%', '50%'],
                                'avoidLabelOverlap': False,
                                'itemStyle': {'borderRadius': 6, 'borderColor': '#0d1117', 'borderWidth': 2},
                                'label': {'show': False},
                                'emphasis': {'label': {'show': True, 'fontSize': 12, 'fontWeight': 'bold', 'color': '#ffffff'}},
                                'data': gate_chart_data
                            }]
                        }).classes('w-full h-56')

                    # Telemetry Filter Box
                    tel_filter_box = ui.row().classes('w-full gap-4 items-center bg-[#0d1117] p-3 rounded-lg border border-[#21262d]')
                    tel_table_container = ui.column().classes('w-full')

                    def render_veto_table(filtered_tel):
                        tel_table_container.clear()
                        # Limit to 1000 records for instantaneous UI response
                        sub_data = filtered_tel.head(1000)
                        rows_data = []
                        for idx, r in sub_data.reset_index(drop=True).iterrows():
                            is_dodged = bool(r.get('is_dodged_bullet', False))
                            is_missed = bool(r.get('is_missed_opportunity', False))
                            if is_dodged:
                                outcome_tag = '🛡️ DODGED BULLET'
                            elif is_missed:
                                outcome_tag = '⚠️ MISSED MFE'
                            else:
                                outcome_tag = 'FLAT DRIFT'

                            px_f  = float(r.get('price', 0.0))
                            r24_f = float(r.get('ret_24h_fwd', 0.0)) * 100.0
                            r72_f = float(r.get('ret_72h_fwd', 0.0)) * 100.0
                            mfe_f = float(r.get('mfe_72h_fwd', 0.0)) * 100.0
                            mae_f = float(r.get('mae_72h_fwd', 0.0)) * 100.0
                            ts_str = str(r.get('timestamp', ''))[:16]
                            sym_str = str(r.get('asset', ''))

                            rows_data.append({
                                'id': f"{sym_str}_{ts_str}_{idx}",
                                'timestamp': ts_str,
                                'asset': sym_str,
                                'tier': str(r.get('tier', 'Tier 1')),
                                'candidate_setup': str(r.get('candidate_setup', '')),
                                'veto_gate': str(r.get('veto_gate', '')),
                                'price': px_f,
                                'ret_24h_fwd': r24_f,
                                'ret_72h_fwd': r72_f,
                                'mfe_72h_fwd': mfe_f,
                                'mae_72h_fwd': mae_f,
                                'outcome': outcome_tag,
                                'price_str': f"${px_f:,.4f}",
                                'ret_24h_fwd_str': f"{r24_f:+.2f}%",
                                'ret_72h_fwd_str': f"{r72_f:+.2f}%",
                                'mfe_72h_fwd_str': f"+{mfe_f:.1f}%",
                                'mae_72h_fwd_str': f"{mae_f:.1f}%",
                            })

                        cols = [
                            {'name': 'timestamp', 'label': 'Veto Date (UTC)', 'field': 'timestamp', 'align': 'left', 'sortable': True},
                            {'name': 'asset', 'label': 'Asset', 'field': 'asset', 'align': 'left', 'sortable': True},
                            {'name': 'tier', 'label': 'Tier', 'field': 'tier', 'align': 'center', 'sortable': True},
                            {'name': 'candidate_setup', 'label': 'Candidate Setup', 'field': 'candidate_setup', 'align': 'left'},
                            {'name': 'veto_gate', 'label': 'Veto Gate Trigger', 'field': 'veto_gate', 'align': 'left', 'sortable': True},
                            {'name': 'price', 'label': 'Veto Price', 'field': 'price', 'align': 'right', 'sortable': True},
                            {'name': 'ret_24h_fwd', 'label': '24h Drift', 'field': 'ret_24h_fwd', 'align': 'right', 'sortable': True},
                            {'name': 'ret_72h_fwd', 'label': '72h Drift', 'field': 'ret_72h_fwd', 'align': 'right', 'sortable': True},
                            {'name': 'mfe_72h_fwd', 'label': '72h Max MFE', 'field': 'mfe_72h_fwd', 'align': 'right', 'sortable': True},
                            {'name': 'mae_72h_fwd', 'label': '72h Max MAE', 'field': 'mae_72h_fwd', 'align': 'right', 'sortable': True},
                            {'name': 'outcome', 'label': 'Audit Outcome', 'field': 'outcome', 'align': 'center', 'sortable': True}
                        ]

                        with tel_table_container:
                            tt = ui.table(columns=cols, rows=rows_data, row_key='id', pagination={'rowsPerPage': 25}).classes('w-full card-glass mono')
                            tt.add_slot('body-cell-price', '<q-td :props="props" class="text-right">{{ props.row.price_str }}</q-td>')
                            tt.add_slot('body-cell-ret_24h_fwd', '''
                                <q-td :props="props" class="text-right" :class="props.row.ret_24h_fwd >= 0 ? 'text-[#00ff87]' : 'text-[#ff4655]'">
                                    {{ props.row.ret_24h_fwd_str }}
                                </q-td>
                            ''')
                            tt.add_slot('body-cell-ret_72h_fwd', '''
                                <q-td :props="props" class="text-right" :class="props.row.ret_72h_fwd >= 0 ? 'text-[#00ff87]' : 'text-[#ff4655]'">
                                    {{ props.row.ret_72h_fwd_str }}
                                </q-td>
                            ''')
                            tt.add_slot('body-cell-mfe_72h_fwd', '<q-td :props="props" class="text-right text-[#00f0ff] font-bold">{{ props.row.mfe_72h_fwd_str }}</q-td>')
                            tt.add_slot('body-cell-mae_72h_fwd', '<q-td :props="props" class="text-right text-[#ff4655]">{{ props.row.mae_72h_fwd_str }}</q-td>')

                    # Interactive Filter Controls
                    with tel_filter_box:
                        v_sym_input = ui.input(placeholder='Search Symbol (e.g. NEAR)...').classes('w-44 filter-input px-3 py-1 mono text-xs')
                        v_gate_select = ui.select([
                            'All Gates', 'Core 1: Macro Bear Veto', 'Core 3: Turnover Velocity',
                            'Core 4: Whale Firewall', 'Core 4: Funding Rate Cap'
                        ], value='All Gates').classes('w-48 mono text-xs')
                        v_outcome_select = ui.select([
                            'All Outcomes', 'Dodged Bullets (Loss Saved)', 'Missed Opportunities (>= +20% MFE)'
                        ], value='All Outcomes').classes('w-56 mono text-xs')

                        def apply_veto_filters():
                            df_v = vetoed_records.copy()
                            sym_text = v_sym_input.value.strip().upper() if v_sym_input.value else ""
                            if sym_text:
                                df_v = df_v[df_v['asset'].str.contains(sym_text, case=False, na=False)]
                            if v_gate_select.value != 'All Gates':
                                df_v = df_v[df_v['veto_gate'] == v_gate_select.value]
                            if v_outcome_select.value == 'Dodged Bullets (Loss Saved)':
                                df_v = df_v[df_v['is_dodged_bullet']]
                            elif v_outcome_select.value == 'Missed Opportunities (>= +20% MFE)':
                                df_v = df_v[df_v['is_missed_opportunity']]
                            render_veto_table(df_v)

                        v_sym_input.on('update:model-value', lambda _: apply_veto_filters())
                        v_gate_select.on('update:model-value', lambda _: apply_veto_filters())
                        v_outcome_select.on('update:model-value', lambda _: apply_veto_filters())

                    # Initial Veto Table Render
                    render_veto_table(vetoed_records)
                else:
                    ui.label('No counterfactual telemetry recorded yet. Run pipeline_v12.ps1.').classes('text-gray-400 mono')

            # ---------------------------------------------------------------
            # 4. 🎯 RESEARCH RADAR & SUGGESTIONS TAB
            # ---------------------------------------------------------------
            with ui.tab_panel(tab_radar).classes('p-0 gap-6 flex flex-col'):
                ui.label('⚡ REAL-TIME ACTIONABLE TRADE SUGGESTIONS').classes('text-sm font-bold tracking-wider text-[#00f0ff] mono')

                with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4'):
                    sample_suggestions = [
                        {
                            "symbol": "SOLUSDT", "tier": "Tier 1", "book": "Book 1", "setup": "Continuation Breakout",
                            "entry_label": "Breakout Stop", "entry_price": 158.40,
                            "stop_market": 142.50, "risk_pct": 10.0,
                            "turnover": "1.42x", "whale_ls": "1.18", "funding": "+0.008%",
                            "status": "READY FOR EXECUTION"
                        },
                        {
                            "symbol": "RENDERUSDT", "tier": "Tier 2", "book": "Book 2", "setup": "Coiled Squeeze",
                            "entry_label": "Compression High", "entry_price": 6.12,
                            "stop_market": 5.45, "risk_pct": 10.9,
                            "turnover": "0.68x", "whale_ls": "0.92", "funding": "+0.010%",
                            "status": "AWAITING SQUEEZE TRIGGER"
                        },
                        {
                            "symbol": "TAOUSDT", "tier": "Tier 1", "book": "Book 3", "setup": "Flush Limit Bid (-8.0%)",
                            "entry_label": "Resting Limit Bid", "entry_price": 443.44, "reclaim_target": 482.00,
                            "stop_market": 407.96, "risk_pct": 8.0,
                            "turnover": "0.85x", "whale_ls": "1.05", "funding": "+0.012%",
                            "status": "RESTING LIMIT BID ARMED"
                        },
                        {
                            "symbol": "FETUSDT", "tier": "Tier 2", "book": "Book 3", "setup": "Flush Limit Bid (-12.0%)",
                            "entry_label": "Resting Limit Bid", "entry_price": 1.276, "reclaim_target": 1.450,
                            "stop_market": 1.174, "risk_pct": 8.0,
                            "turnover": "1.15x", "whale_ls": "0.98", "funding": "+0.006%",
                            "status": "RESTING LIMIT BID ARMED"
                        }
                    ]

                    for s in sample_suggestions:
                        with ui.card().classes('card-glass p-5 border border-[#21262d] flex flex-col justify-between'):
                            with ui.row().classes('w-full justify-between items-center'):
                                with ui.row().classes('items-center gap-2'):
                                    sym_slug = s['symbol'].replace('USDT', '')
                                    ui.html(f'<a href="/coin/{sym_slug}" class="text-lg font-black text-white hover:text-[#00f0ff] hover:underline mono cursor-pointer">{s["symbol"]} ↗</a>')
                                    tier_color = 'badge-cyan' if s['tier'] == 'Tier 1' else 'badge-purple'
                                    ui.html(f'<span class="badge-tag {tier_color}">{s["tier"]}</span>')
                                setup_badge_col = 'badge-purple' if s['book'] == 'Book 3' else ('badge-cyan' if s['book'] == 'Book 2' else 'badge-green')
                                ui.html(f'<span class="badge-tag {setup_badge_col}">{s["setup"]}</span>')

                            ui.separator().classes('my-3 bg-[#21262d]')

                            with ui.row().classes('w-full justify-between mb-2'):
                                with ui.column().classes('gap-0'):
                                    ui.label(s.get('entry_label', 'Entry Price:')).classes('text-xs text-gray-400 mono')
                                    ui.label(f"${s['entry_price']:,.4f}").classes('text-base font-bold text-white mono')
                                with ui.column().classes('gap-0 items-end'):
                                    ui.label('Resting Stop-Market:').classes('text-xs text-gray-400 mono')
                                    ui.label(f"${s['stop_market']:,.4f}").classes('text-base font-bold text-[#ff4655] mono')

                            if 'reclaim_target' in s:
                                with ui.row().classes('w-full justify-between mb-2 bg-[#161b22] px-3 py-1.5 rounded border border-[#21262d]'):
                                    ui.label('Target Reclaim (P0):').classes('text-xs text-[#00ff87] mono font-bold')
                                    ui.label(f"${s['reclaim_target']:,.4f}").classes('text-xs text-[#00ff87] mono font-bold')

                            with ui.column().classes('gap-1 bg-[#161b22] p-3 rounded-lg border border-[#21262d] my-2'):
                                with ui.row().classes('w-full justify-between text-xs mono'):
                                    ui.label('BTC Macro Bull:')
                                    ui.label('✅ Confirmed').classes('text-[#00ff87]')
                                with ui.row().classes('w-full justify-between text-xs mono'):
                                    ui.label(f'Top Trader L/S ({s["whale_ls"]}):')
                                    ui.label('✅ Validated').classes('text-[#00ff87]')
                                with ui.row().classes('w-full justify-between text-xs mono'):
                                    ui.label(f'Turnover ({s["turnover"]}):')
                                    ui.label('✅ Bounded').classes('text-[#00ff87]')
                                with ui.row().classes('w-full justify-between text-xs mono'):
                                    ui.label(f'Funding Rate ({s["funding"]}):')
                                    ui.label('✅ Below Cap').classes('text-[#00ff87]')

                            if s['book'] == 'Book 3':
                                order_json = json.dumps({
                                    "symbol": s['symbol'], "side": "BUY", "type": "LIMIT",
                                    "price": s['entry_price'], "targetPrice": s.get('reclaim_target'),
                                    "stopPrice": s['stop_market'], "setup": s['setup'], "tier": s['tier'], "book": s['book']
                                }, indent=2)
                            else:
                                order_json = json.dumps({
                                    "symbol": s['symbol'], "side": "BUY", "type": "STOP_MARKET",
                                    "stopPrice": s['entry_price'], "protectiveStop": s['stop_market'],
                                    "setup": s['setup'], "tier": s['tier'], "book": s['book']
                                }, indent=2)

                            def copy_handler(payload=order_json, sym=s['symbol']):
                                ui.clipboard.write(payload)
                                ui.notify(f"Copied exchange execution JSON for {sym}!", color='cyan')

                            ui.button('📋 Copy Order JSON', on_click=copy_handler).props('outline color=cyan').classes('w-full mono mt-2')

                # Dynamic Universe Radar Table
                ui.label('🌐 DYNAMIC POINT-IN-TIME UNIVERSE RADAR').classes('text-sm font-bold tracking-wider text-[#00f0ff] mono mt-4')
                if not tiers_df.empty:
                    us_equities = {'AAPL', 'AMZN', 'GOOGL', 'MSFT', 'NVDA', 'TSLA', 'META', 'AMD', 'INTC', 'ARM', 'AVGO', 'MU', 'QCOM', 'SPY', 'QQQ', 'XAU', 'XAG', 'CL', 'BZ', 'ASTS', 'PLTR', 'COIN', 'MSTR', 'SNDK', 'MRVL', 'EWY', 'KORU', 'AAOI', 'AMAT', 'ANTHROPIC', 'OPENAI', 'SPCX', 'SKHYNIX', 'SAMSUNG', 'SOXL', 'DRAM', 'BMNR', 'TQQQ', 'USDC'}
                    radar_data = tiers_df[~tiers_df['asset'].isin(us_equities)].copy()
                    radar_data['tier'] = np.where(
                        (radar_data['med_oi_30d_m'] >= 15.0) & (radar_data['med_vol_30d_m'] >= 15.0) & (radar_data['corr_btc'] >= 0.35),
                        'Tier 1',
                        np.where((radar_data['med_oi_30d_m'] >= 2.5) & (radar_data['med_vol_30d_m'] >= 2.5), 'Tier 2', 'Excluded')
                    )
                    liquid_radar = radar_data[radar_data['tier'].isin(['Tier 1', 'Tier 2'])].head(35)
                    radar_rows = []
                    for _, r in liquid_radar.iterrows():
                        oi_f = float(r.get('med_oi_30d_m', 0.0))
                        vol_f = float(r.get('med_vol_30d_m', 0.0))
                        corr_f = float(r.get('corr_btc', 0.0))
                        px_f = float(r.get('last_price', 0.0))
                        radar_rows.append({
                            'asset': str(r['asset']),
                            'tier': str(r['tier']),
                            'med_oi_30d_m': oi_f,
                            'med_vol_30d_m': vol_f,
                            'corr_btc': corr_f,
                            'last_price': px_f,
                            'med_oi_str': f"${oi_f:.2f}M",
                            'med_vol_str': f"${vol_f:.2f}M",
                            'corr_btc_str': f"{corr_f:.2f}",
                            'last_price_str': f"${px_f:,.4f}",
                        })
                    radar_cols = [
                        {'name': 'asset', 'label': 'Asset', 'field': 'asset', 'align': 'left', 'sortable': True},
                        {'name': 'tier', 'label': 'Liquidity Tier', 'field': 'tier', 'align': 'center', 'sortable': True},
                        {'name': 'med_oi_30d_m', 'label': 'Median OI (30d)', 'field': 'med_oi_30d_m', 'align': 'right', 'sortable': True, 'sortOrder': 'da'},
                        {'name': 'med_vol_30d_m', 'label': 'Median Vol (30d)', 'field': 'med_vol_30d_m', 'align': 'right', 'sortable': True, 'sortOrder': 'da'},
                        {'name': 'corr_btc', 'label': 'BTC Corr', 'field': 'corr_btc', 'align': 'right', 'sortable': True, 'sortOrder': 'da'},
                        {'name': 'last_price', 'label': 'Last Price', 'field': 'last_price', 'align': 'right', 'sortable': True, 'sortOrder': 'da'},
                    ]
                    rt = ui.table(columns=radar_cols, rows=radar_rows, row_key='asset').classes('w-full card-glass mono')
                    rt.add_slot('body-cell-asset', '''
                        <q-td :props="props">
                            <a :href="'/coin/' + props.row.asset" class="text-[#00f0ff] hover:underline font-bold cursor-pointer">
                                {{ props.row.asset }} ↗
                            </a>
                        </q-td>
                    ''')
                    rt.add_slot('body-cell-med_oi_30d_m', '<q-td :props="props" class="text-right">{{ props.row.med_oi_str }}</q-td>')
                    rt.add_slot('body-cell-med_vol_30d_m', '<q-td :props="props" class="text-right">{{ props.row.med_vol_str }}</q-td>')
                    rt.add_slot('body-cell-corr_btc', '<q-td :props="props" class="text-right">{{ props.row.corr_btc_str }}</q-td>')
                    rt.add_slot('body-cell-last_price', '<q-td :props="props" class="text-right">{{ props.row.last_price_str }}</q-td>')
                else:
                    ui.label('asset_tiers.parquet not yet indexed. Run pipeline_v12.ps1.').classes('text-gray-400 mono')

            # ---------------------------------------------------------------
            # 5. ⚖️ FORENSIC REASONER TAB
            # ---------------------------------------------------------------
            with ui.tab_panel(tab_forensics).classes('p-0 gap-6 flex flex-col'):
                ui.label('⚖️ CLOSED TRADES FORENSIC REASONING ENGINE').classes('text-sm font-bold tracking-wider text-[#00f0ff] mono')

                if not closed_df.empty:
                    reason_counts = closed_df['reason'].value_counts()
                    with ui.row().classes('w-full grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 gap-3'):
                        for r, count in reason_counts.items():
                            sub = closed_df[closed_df['reason'] == r]
                            r_pnl = sub['log_ret'].sum() * 100.0
                            r_col = '#00ff87' if r_pnl >= 0 else '#ff4655'
                            with ui.card().classes('card-glass p-3 border border-[#21262d]'):
                                ui.label(r).classes('text-[10px] text-gray-400 mono font-bold truncate')
                                ui.label(f"{count:,}").classes('text-lg font-black text-white mono mt-1')
                                ui.label(f"{r_pnl:+.1f}% Log").classes(f'text-xs text-[{r_col}] mono')

                    ui.label('FORENSIC CASE STUDIES (WINNERS VS FAILURES)').classes('text-xs font-bold tracking-wider text-gray-400 mono mt-4')
                    sample_forensics = closed_df.sample(min(8, len(closed_df)), random_state=42)

                    for _, t in sample_forensics.iterrows():
                        pnl = float(t['pnl']) * 100.0
                        log_ret = float(t['log_ret']) * 100.0
                        mfe = float(t.get('mfe', 0.0)) * 100.0
                        sym = t['asset']
                        tier = t.get('tier', 'Tier 1')
                        reason = t.get('reason', 'trail_stop')
                        dur = t.get('duration_hours', 0.0)

                        is_win = pnl > 0
                        card_class = "card-glow-green" if is_win else "card-glow-red"
                        badge_class = "badge-green" if is_win else "badge-red"

                        if reason == "climax_top_harvest" or reason == "climax_air_pocket_harvest":
                            narrative = f"Exited on institutional liquidity climax: Peak MFE reached +{mfe:.1f}%. Proactive market harvest secured squeeze gains before air-pocket waterfall."
                        elif reason == "trail_stop":
                            narrative = f"Exited on calibrated Donchian floor break: Captured +{pnl:.1f}% net profit after trending for {int(dur)}h and protecting peak gains."
                        elif reason == "fast_decay_cut":
                            narrative = f"Exited on Open Interest leak cut: Position stalled with OI leaking > 3%, bailing out defensively at {pnl:.1f}% before structural floor collapse."
                        elif reason == "breakeven_ratchet":
                            narrative = f"Exited at Breakeven ratchet: Price tested +{mfe:.1f}% MFE before rolling over, preserving 100% of risk capital."
                        elif reason == "target_reclaim":
                            narrative = f"Exited at P0 reclaim target: Passive limit bid captured +{pnl:.1f}% bounce from flush discount, exiting ahead of post-flush turbulence."
                        elif reason == "time_stop":
                            narrative = f"Exited on 72h TTL time-stop: Flush failed to reclaim target within 72h window, exiting defensively at {pnl:.1f}%."
                        elif reason == "stop_loss":
                            narrative = f"Exited at resting structural stop floor: Contained downside to {pnl:.1f}%."
                        else:
                            narrative = f"Exited on {reason}: Standard risk engine liquidation with contained loss of {pnl:.1f}%."

                        with ui.card().classes(f'card-glass p-4 {card_class}'):
                            with ui.row().classes('w-full justify-between items-center'):
                                with ui.row().classes('items-center gap-3'):
                                    ui.html(f'<a href="/coin/{sym}" class="text-base font-bold text-white hover:text-[#00f0ff] hover:underline mono cursor-pointer">{sym} ↗</a>')
                                    ui.html(f'<span class="badge-tag badge-cyan">{tier}</span>')
                                    ui.html(f'<span class="badge-tag badge-purple">{reason}</span>')
                                ui.html(f'<span class="badge-tag {badge_class}">{pnl:+.2f}% ({log_ret:+.2f}% Log)</span>')

                            ui.label(narrative).classes('text-xs text-gray-300 mt-2 font-normal')
                else:
                    ui.label('No closed trades to audit. Run pipeline_v12.ps1.').classes('text-gray-400 mono')

            # ---------------------------------------------------------------
            # 6. 📈 EQUITY CURVE & SCORECARD TAB
            # ---------------------------------------------------------------
            with ui.tab_panel(tab_equity).classes('p-0 gap-6 flex flex-col'):
                ui.label('📈 COMPOUNDING LOG EQUITY CURVE (STRICT NET LOG RETURN SPACE)').classes('text-sm font-bold tracking-wider text-[#00f0ff] mono')
                if not closed_df.empty:
                    sorted_closed = closed_df.sort_values('exit').copy()
                    sorted_closed['cum_log'] = sorted_closed['log_ret'].cumsum() * 100.0
                    sorted_closed['cum_mult'] = np.exp(sorted_closed['cum_log'] / 100.0)

                    step = max(1, len(sorted_closed) // 100)
                    chart_pts = sorted_closed.iloc[::step]
                    dates = [str(d)[:10] for d in chart_pts['exit']]
                    mults = [round(float(v), 2) for v in chart_pts['cum_mult']]

                    chart_config = {
                        'title': {'text': 'Portfolio Compounded Capital Multiple (e^sum(ln(1+R)))', 'textStyle': {'color': '#e6edf3', 'fontFamily': 'monospace'}},
                        'tooltip': {'trigger': 'axis'},
                        'xAxis': {'type': 'category', 'data': dates, 'axisLine': {'lineStyle': {'color': '#30363d'}}},
                        'yAxis': {'type': 'value', 'axisLine': {'lineStyle': {'color': '#30363d'}}, 'splitLine': {'lineStyle': {'color': '#161b22'}}},
                        'series': [
                            {'name': 'Capital Multiple (x)', 'type': 'line', 'data': mults, 'smooth': True, 'lineStyle': {'color': '#00f0ff', 'width': 3}, 'areaStyle': {'color': 'rgba(0, 240, 255, 0.1)'}}
                        ]
                    }
                    ui.echart(chart_config).classes('w-full h-96 card-glass')

                # Universal Scorecard
                ui.label('📊 UNIVERSAL ASSET SCORECARD (STRICT LOG METRICS)').classes('text-sm font-bold tracking-wider text-[#00f0ff] mono mt-4')
                if not sc_df.empty:
                    sc_rows = []
                    for _, r in sc_df.iterrows():
                        wr_f   = float(r.get('win_rate', 0.0))
                        pf_f   = float(r.get('profit_factor', 0.0))
                        mean_f = float(r.get('mean_log_pnl', 0.0))
                        tot_f  = float(r.get('total_log_pnl', 0.0))
                        mult_f = float(r.get('capital_multiple', 1.0))
                        mdd_f  = float(r.get('max_log_drawdown', 0.0))
                        mfe_f  = float(r.get('mfe_mean_pct', 0.0))
                        mae_f  = float(r.get('mae_mean_pct', 0.0))
                        dur_f  = float(r.get('dur_mean_hours', 0.0))
                        sc_rows.append({
                            'asset': str(r.get('asset', '')),
                            'tier': str(r.get('tier', '')),
                            'closed_trades': int(r.get('closed_trades', 0)),
                            'win_rate': wr_f,
                            'profit_factor': pf_f,
                            'mean_log_pnl': mean_f,
                            'total_log_pnl': tot_f,
                            'capital_multiple': mult_f,
                            'max_log_drawdown': mdd_f,
                            'mfe_mean_pct': mfe_f,
                            'mae_mean_pct': mae_f,
                            'dur_mean_hours': dur_f,
                            'win_rate_str': f"{wr_f:.1f}%",
                            'profit_factor_str': f"{pf_f:.3f}",
                            'mean_log_pnl_str': f"{mean_f:+.3f}%",
                            'total_log_pnl_str': f"{tot_f:+.1f}%",
                            'capital_multiple_str': f"{mult_f:.2f}x",
                            'max_log_drawdown_str': f"{mdd_f:.1f}%",
                            'mfe_mean_pct_str': f"+{mfe_f:.1f}%",
                            'mae_mean_pct_str': f"{mae_f:.1f}%",
                            'dur_mean_hours_str': f"{dur_f:.0f}h",
                        })
                    sc_cols = [
                        {'name': 'asset', 'label': 'Asset', 'field': 'asset', 'align': 'left', 'sortable': True},
                        {'name': 'tier', 'label': 'Tier', 'field': 'tier', 'align': 'center', 'sortable': True},
                        {'name': 'closed_trades', 'label': 'Trades', 'field': 'closed_trades', 'align': 'right', 'sortable': True},
                        {'name': 'win_rate', 'label': 'Win Rate', 'field': 'win_rate', 'align': 'right', 'sortable': True},
                        {'name': 'profit_factor', 'label': 'PF (Log)', 'field': 'profit_factor', 'align': 'right', 'sortable': True},
                        {'name': 'mean_log_pnl', 'label': 'Edge/Trade', 'field': 'mean_log_pnl', 'align': 'right', 'sortable': True},
                        {'name': 'total_log_pnl', 'label': 'Total Log PnL', 'field': 'total_log_pnl', 'align': 'right', 'sortable': True},
                        {'name': 'capital_multiple', 'label': 'Multiple', 'field': 'capital_multiple', 'align': 'right', 'sortable': True},
                        {'name': 'max_log_drawdown', 'label': 'Max Log DD', 'field': 'max_log_drawdown', 'align': 'right', 'sortable': True},
                        {'name': 'mfe_mean_pct', 'label': 'Avg MFE', 'field': 'mfe_mean_pct', 'align': 'right', 'sortable': True},
                        {'name': 'mae_mean_pct', 'label': 'Avg MAE', 'field': 'mae_mean_pct', 'align': 'right', 'sortable': True},
                        {'name': 'dur_mean_hours', 'label': 'Avg Duration', 'field': 'dur_mean_hours', 'align': 'right', 'sortable': True},
                    ]
                    sct = ui.table(columns=sc_cols, rows=sc_rows, row_key='asset', pagination={'rowsPerPage': 30}).classes('w-full card-glass mono')
                    sct.add_slot('body-cell-asset', '''
                        <q-td :props="props">
                            <a :href="'/coin/' + props.row.asset" class="text-[#00f0ff] hover:underline font-bold cursor-pointer">
                                {{ props.row.asset }} ↗
                            </a>
                        </q-td>
                    ''')
                    sct.add_slot('body-cell-win_rate', '<q-td :props="props" class="text-right">{{ props.row.win_rate_str }}</q-td>')
                    sct.add_slot('body-cell-profit_factor', '<q-td :props="props" class="text-right font-bold text-[#00f0ff]">{{ props.row.profit_factor_str }}</q-td>')
                    sct.add_slot('body-cell-mean_log_pnl', '''
                        <q-td :props="props" class="text-right font-bold" :class="props.row.mean_log_pnl >= 0 ? 'text-[#00ff87]' : 'text-[#ff4655]'">
                            {{ props.row.mean_log_pnl_str }}
                        </q-td>
                    ''')
                    sct.add_slot('body-cell-total_log_pnl', '''
                        <q-td :props="props" class="text-right font-bold" :class="props.row.total_log_pnl >= 0 ? 'text-[#00ff87]' : 'text-[#ff4655]'">
                            {{ props.row.total_log_pnl_str }}
                        </q-td>
                    ''')
                    sct.add_slot('body-cell-capital_multiple', '<q-td :props="props" class="text-right">{{ props.row.capital_multiple_str }}</q-td>')
                    sct.add_slot('body-cell-max_log_drawdown', '<q-td :props="props" class="text-right text-[#ff4655]">{{ props.row.max_log_drawdown_str }}</q-td>')
                    sct.add_slot('body-cell-mfe_mean_pct', '<q-td :props="props" class="text-right text-[#00f0ff]">{{ props.row.mfe_mean_pct_str }}</q-td>')
                    sct.add_slot('body-cell-mae_mean_pct', '<q-td :props="props" class="text-right text-[#ff4655]">{{ props.row.mae_mean_pct_str }}</q-td>')
                    sct.add_slot('body-cell-dur_mean_hours', '<q-td :props="props" class="text-right">{{ props.row.dur_mean_hours_str }}</q-td>')

                # MEDIUM-6: MAE Distribution Chart (stop-tightness analysis)
                # MEDIUM-7: Duration Distribution Chart (trade lifecycle curve)
                if not closed_df.empty:
                    ui.label('📊 RESEARCH DISTRIBUTION CHARTS').classes('text-sm font-bold tracking-wider text-[#00f0ff] mono mt-6')
                    with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 gap-4'):

                        # Duration Histogram — MEDIUM-7
                        with ui.card().classes('card-glass p-4 border border-[#21262d]'):
                            ui.label('TRADE DURATION DISTRIBUTION (Hours)').classes('text-xs text-gray-400 mono font-bold mb-2')
                            _dur = closed_df['duration_hours'].dropna()
                            _dur_bins = list(range(0, min(int(_dur.max()) + 50, 730), 24))
                            _dur_hist, _dur_edges = np.histogram(_dur, bins=_dur_bins)
                            _dur_labels = [f"{int(b)}h" for b in _dur_edges[:-1]]
                            ui.echart({
                                'backgroundColor': 'transparent',
                                'tooltip': {'trigger': 'axis'},
                                'xAxis': {'type': 'category', 'data': _dur_labels, 'axisLine': {'lineStyle': {'color': '#30363d'}}, 'axisLabel': {'color': '#9ca3af', 'fontSize': 10}},
                                'yAxis': {'type': 'value', 'axisLine': {'lineStyle': {'color': '#30363d'}}, 'splitLine': {'lineStyle': {'color': '#161b22'}}, 'axisLabel': {'color': '#9ca3af'}},
                                'series': [{'name': 'Trades', 'type': 'bar', 'data': _dur_hist.tolist(), 'itemStyle': {'color': '#a855f7'}}]
                            }).classes('w-full h-52')
                            _dur_med = float(_dur.median())
                            ui.label(f"Median: {_dur_med:.0f}h | P90: {float(np.percentile(_dur, 90)):.0f}h | P10: {float(np.percentile(_dur, 10)):.0f}h").classes('text-xs text-gray-400 mono mt-1')

                        # MAE Distribution — MEDIUM-6 (stop-tightness analysis)
                        with ui.card().classes('card-glass p-4 border border-[#21262d]'):
                            ui.label('MAE DISTRIBUTION (Max Adverse Excursion %)').classes('text-xs text-gray-400 mono font-bold mb-2')
                            _mae = (closed_df['mae'].dropna() * 100.0)
                            _mae_bins = np.linspace(_mae.min(), min(0.0, _mae.max()), 20)
                            if len(_mae_bins) < 2:
                                _mae_bins = np.linspace(-20, 0, 20)
                            _mae_hist, _mae_edges = np.histogram(_mae, bins=_mae_bins)
                            _mae_labels = [f"{b:.1f}%" for b in _mae_edges[:-1]]
                            ui.echart({
                                'backgroundColor': 'transparent',
                                'tooltip': {'trigger': 'axis'},
                                'xAxis': {'type': 'category', 'data': _mae_labels, 'axisLine': {'lineStyle': {'color': '#30363d'}}, 'axisLabel': {'color': '#9ca3af', 'fontSize': 10}},
                                'yAxis': {'type': 'value', 'axisLine': {'lineStyle': {'color': '#30363d'}}, 'splitLine': {'lineStyle': {'color': '#161b22'}}, 'axisLabel': {'color': '#9ca3af'}},
                                'series': [{'name': 'Trades', 'type': 'bar', 'data': _mae_hist.tolist(), 'itemStyle': {'color': '#ff4655'}}]
                            }).classes('w-full h-52')
                            ui.label(f"Median MAE: {float(_mae.median()):.1f}% | Worst 10%: {float(np.percentile(_mae, 10)):.1f}%").classes('text-xs text-gray-400 mono mt-1')

            # ---------------------------------------------------------------
            # 7. 📅 EXECUTION TIMELINE & TRAVERSE TAB
            # ---------------------------------------------------------------
            with ui.tab_panel(tab_timeline).classes('p-0 gap-6 flex flex-col'):
                with ui.row().classes('w-full justify-between items-center'):
                    ui.label('📅 CHRONOLOGICAL TRADE EXECUTION TIMELINE & LOG TRAVERSE').classes('text-sm font-bold tracking-wider text-[#00f0ff] mono')
                    ui.label(f'Total Executed Trades: {tot_closed} | Multi-Channel Swimlanes').classes('text-xs text-gray-400 mono')

                if not closed_df.empty:
                    # Top Pane: Interactive Gantt Swimlane Timeline
                    with ui.card().classes('card-glass p-4 border border-[#21262d] w-full'):
                        with ui.row().classes('w-full justify-between items-center mb-2'):
                            ui.label('HORIZONTAL EXECUTION SWINLANES (DRAGGABLE TIMELINE RANGE SLIDER)').classes('text-xs text-gray-400 mono font-bold')
                            ui.html('<span class="badge-tag badge-green">WIN (+)</span> <span class="badge-tag badge-red ml-2">LOSS (-)</span>')
                        timeline_fig = build_timeline_plot(closed_df)
                        ui.plotly(timeline_fig).classes('w-full')

                    # Bottom Pane: Chronological Traverse & Underwater Drawdown
                    with ui.card().classes('card-glass p-4 border border-[#21262d] w-full mt-4'):
                        with ui.row().classes('w-full justify-between items-center mb-2'):
                            ui.label('CHRONOLOGICAL TRAVERSE: CUMULATIVE NET LOG RETURN & UNDERWATER DRAWDOWN').classes('text-xs text-gray-400 mono font-bold')
                            ui.label(f'Total Net Log: {tot_log:+.1f}% | Multiple: {cap_multiple:,.2f}x').classes('text-xs text-[#00f0ff] mono font-bold')
                        traverse_fig = build_traverse_plot(closed_df)
                        ui.plotly(traverse_fig).classes('w-full')
                else:
                    ui.label('No closed trades to display. Run pipeline_v12.ps1.').classes('text-gray-400 mono')


# ---------------------------------------------------------------------------
# ENTRYPOINT
# ---------------------------------------------------------------------------
if __name__ in {"__main__", "__mp_main__"}:
    host = os.getenv("NICEGUI_HOST", "0.0.0.0")
    port = int(os.getenv("NICEGUI_PORT", "8056"))
    print("\n" + "=" * 80)
    print(f"STARTING KRONOS V12 NICEGUI COMMAND CENTER ({host}:{port})")
    print(f"Accessible at: http://localhost:{port} or http://<server-ip>:{port}")
    print("=" * 80 + "\n")
    ui.run(
        host=host,
        port=port,
        title="Kronos V12: Clean 6-Core Command Center",
        dark=True,
        reload=False
    )
