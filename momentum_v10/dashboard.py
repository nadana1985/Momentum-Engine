import streamlit as st
import pandas as pd
import numpy as np
import os

from momentum_v10.config import SHARD_DIR, TAPE_DIR

st.set_page_config(layout="wide", page_title="Kronos V10 Production Engine Dashboard")

st.title("⚡ KRONOS V10: Production Engine Dashboard")
st.info("🔥 **TRADOOR Command Center (Pure HTML5 Interface)** is available at [http://localhost:8050](http://localhost:8050). Launch via `python -m momentum_v10.dashboard_server`")
st.caption("Universal Microstructure & Donchian Ratchet Execution System")

@st.cache_data
def load_trades():
    file_path = str(TAPE_DIR / 'all_trades.csv')
    if not os.path.exists(file_path):
        return pd.DataFrame()
    df = pd.read_csv(file_path)
    
    if 'pnl_pct' in df.columns:
        df['PnL'] = pd.to_numeric(df['pnl_pct'], errors='coerce')
        df['MFE'] = pd.to_numeric(df['mfe_pct'], errors='coerce')
        df['MAE'] = pd.to_numeric(df['mae_pct'], errors='coerce')
        df['Asset'] = df['asset']
        df['Engine'] = df['engine']
        df['EntryTime'] = df['entry']
        df['ExitTime'] = df['exit']
        df['EntryPx'] = pd.to_numeric(df['entry_price'], errors='coerce')
        df['ExitPx'] = pd.to_numeric(df['exit_price'], errors='coerce')
        df['HeldHrs'] = pd.to_numeric(df['duration_hours'], errors='coerce')
        df['ExitReason'] = df['reason']
        df['Status'] = df.get('status', 'CLOSED')
    else:
        df = df.iloc[:, :12]
        df.columns = ['Asset', 'Engine', 'EntryTime', 'EntryPx', 'ExitTime', 'ExitPx', 'HeldStr', 'HeldHrs', 'PnL', 'MFE', 'MAE', 'ExitReason']
        df['PnL'] = pd.to_numeric(df['PnL'], errors='coerce')
        df['MFE'] = pd.to_numeric(df['MFE'], errors='coerce')
        df['MAE'] = pd.to_numeric(df['MAE'], errors='coerce')
        df['HeldHrs'] = pd.to_numeric(df['HeldHrs'], errors='coerce')
        df['EntryPx'] = pd.to_numeric(df['EntryPx'], errors='coerce')
        df['ExitPx'] = pd.to_numeric(df['ExitPx'], errors='coerce')
        df['Status'] = 'CLOSED'
    return df

raw_df = load_trades()

if raw_df.empty:
    st.error("Trades file not found at data/all_tapes/v10_production/all_trades.csv. Run pipeline_v10.ps1 first.")
    st.stop()

# Sidebar Control
st.sidebar.header("🎯 Dashboard Controls")
book_mode = st.sidebar.radio(
    "Expectancy Mode", 
    ["Closed Book Only (True Expectancy)", "Open Trades Only", "All Trades (Mark-to-Market)"],
    index=1
)

open_df_all = raw_df[raw_df['ExitReason'] == 'open_at_end'].copy()
closed_df_all = raw_df[raw_df['ExitReason'] != 'open_at_end'].copy()

if book_mode == "Closed Book Only (True Expectancy)":
    df = closed_df_all.copy()
elif book_mode == "Open Trades Only":
    df = open_df_all.copy()
else:
    df = raw_df.copy()

# ----------------------------------------------------
# DEDICATED OPEN TRADES VIEW WHEN "Open Trades Only"
# ----------------------------------------------------
if book_mode == "Open Trades Only":
    st.header(f"🔥 Active Open Positions Command Center ({len(df)} Live Trades)")
    
    k1, k2, k3, k4, k5 = st.columns(5)
    with k1:
        st.metric("Total Open Trades", f"{len(df):,}")
    with k2:
        win_pct = (df['PnL'] > 0).mean() * 100 if not df.empty else 0
        st.metric("Open Win %", f"{win_pct:.1f}%")
    with k3:
        st.metric("Unrealized Cum PnL", f"{df['PnL'].sum():+,.1f}%")
    with k4:
        st.metric("Mean Open PnL", f"{df['PnL'].mean():+.2f}%")
    with k5:
        top_runner = df.sort_values('PnL', ascending=False).iloc[0] if not df.empty else None
        st.metric("Top Runner", f"{top_runner['Asset']} ({top_runner['PnL']:+.1f}%)" if top_runner is not None else "N/A")

    st.divider()

    # Engine Filter for Open Trades
    engines = sorted(df['Engine'].dropna().unique().tolist())
    selected_eng = st.selectbox("Filter Open Positions by Engine", ["ALL ENGINES"] + engines, index=0)
    
    display_open = df if selected_eng == "ALL ENGINES" else df[df['Engine'] == selected_eng]
    
    st.subheader(f"📋 Live Open Positions Ledger ({len(display_open)} Positions)")
    
    open_cols = ['Asset', 'Engine', 'EntryTime', 'EntryPx', 'ExitPx', 'HeldHrs', 'MFE', 'PnL']
    display_table = display_open[[c for c in open_cols if c in display_open.columns]].copy()
    display_table = display_table.rename(columns={'ExitPx': 'CurrentPx', 'HeldHrs': 'DurationHours', 'PnL': 'UnrealizedPnL%'})
    display_table = display_table.sort_values('UnrealizedPnL%', ascending=False)
    
    st.dataframe(display_table, use_container_width=True, height=500)

    st.divider()

else:
    # ----------------------------------------------------
    # CLOSED / ALL TRADES VIEW
    # ----------------------------------------------------
    st.header("📊 Cross-Engine Portfolio Scorecard")

    engine_stats = []
    for eng in sorted(df['Engine'].dropna().unique()):
        sub = df[df['Engine'] == eng]
        total = len(sub)
        wins = len(sub[sub['PnL'] > 0])
        wr = (wins / total * 100) if total > 0 else 0
        cum_pnl = sub['PnL'].sum()
        avg_mfe = sub['MFE'].mean()
        donchian_exits = len(sub[sub['ExitReason'] == 'donchian_trail'])
        
        engine_stats.append({
            "Engine": eng,
            "Total Trades": total,
            "Wins": wins,
            "Win Rate %": round(wr, 2),
            "Cumulative PnL %": round(cum_pnl, 1),
            "Mean MFE %": round(avg_mfe, 1),
            "Donchian Ratchets": donchian_exits
        })

    scorecard_df = pd.DataFrame(engine_stats)
    st.dataframe(scorecard_df, use_container_width=True)

    st.divider()

    # Single Engine Filter
    engines = sorted(df['Engine'].dropna().unique().tolist())
    selected_engine = st.selectbox("Filter Detailed Analysis by Engine", ["ALL ENGINES"] + engines, index=0)

    if selected_engine != "ALL ENGINES":
        filtered_df = df[df['Engine'] == selected_engine].copy()
    else:
        filtered_df = df.copy()

    # KPI Row
    st.header(f"📈 {selected_engine} Performance Overview")

    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

    total_trades = len(filtered_df)
    winners = filtered_df[filtered_df['PnL'] > 0]
    win_rate = len(winners) / total_trades * 100 if total_trades > 0 else 0
    cum_pnl = filtered_df['PnL'].sum()
    donchian_count = len(filtered_df[filtered_df['ExitReason'] == 'donchian_trail'])

    with kpi1:
        st.metric("Total Trades", f"{total_trades:,}")
    with kpi2:
        st.metric("Win Rate", f"{win_rate:.1f}%")
    with kpi3:
        st.metric("Cumulative PnL", f"{cum_pnl:+,.1f}%")
    with kpi4:
        st.metric("EV / Trade", f"{filtered_df['PnL'].mean():+.2f}%")
    with kpi5:
        st.metric("Donchian Ratchets", f"{donchian_count:,}")

    st.divider()

# ----------------------------------------------------
# TRADOOR Asset DNA Panel (Common to all modes)
# ----------------------------------------------------
st.header("🔍 TRADOOR Asset DNA Panel")
st.caption("Deep-dive asset tail indices and execution histories.")

col1, col2 = st.columns([1, 3])

assets = sorted(df['Asset'].unique().tolist())
with col1:
    selected_asset = st.selectbox("Select Asset", assets if assets else ["None"])

asset_trades = df[df['Asset'] == selected_asset]

@st.cache_data(ttl=300)
def calc_point_72(asset_name: str) -> float | None:
    try:
        p_file = SHARD_DIR / f"{asset_name}_USDT_1h.parquet"
        if not p_file.exists(): return None
        d = pd.read_parquet(p_file, columns=['close'])
        if len(d) < 720: return None
        d = d.tail(720).copy()
        d['ret'] = d['close'].pct_change()
        pos = d['ret'][d['ret'] > 0].dropna().values
        if len(pos) < 50: return None
        X = np.sort(pos)[::-1]
        k = max(5, int(0.05 * len(X)))
        threshold = X[k]
        if threshold <= 0: return None
        log_sum = np.sum(np.log(X[:k] / threshold))
        if log_sum == 0: return None
        return k / log_sum
    except:
        return None

alpha = calc_point_72(selected_asset)

with col1:
    st.subheader(f"DNA Metrics: {selected_asset}")
    st.metric("Trades on Asset", len(asset_trades))
    asset_wr = len(asset_trades[asset_trades['PnL'] > 0]) / len(asset_trades) * 100 if len(asset_trades) > 0 else 0
    st.metric("Asset Win Rate", f"{asset_wr:.1f}%")
    st.metric("Asset Cum PnL", f"{asset_trades['PnL'].sum():+.1f}%")
    
    if alpha is not None:
        color = "normal" if alpha <= 3.19 else "inverse"
        status = "VALID (Fat Tail)" if alpha <= 3.19 else "VETO (Thin Tail)"
        st.metric("Point 72 (α) Tail Index", f"{alpha:.2f}", delta=status, delta_color=color)
    else:
        st.metric("Point 72 (α) Tail Index", "N/A")

with col2:
    st.subheader(f"Execution History: {selected_asset}")
    if not asset_trades.empty:
        cols_to_show = ['EntryTime', 'ExitTime', 'Engine', 'EntryPx', 'ExitPx', 'HeldHrs', 'MFE', 'PnL', 'ExitReason']
        display_df = asset_trades[[c for c in cols_to_show if c in asset_trades.columns]].copy()
        display_df = display_df.sort_values('EntryTime', ascending=False)
        st.dataframe(display_df, use_container_width=True)
    else:
        st.write("No trades recorded for selected asset.")

if book_mode != "Open Trades Only":
    st.divider()
    st.subheader("🏆 Top 50 Harvested Winners")
    top_winners = df.sort_values('PnL', ascending=False).head(50)
    cols_winners = ['Asset', 'Engine', 'EntryTime', 'ExitTime', 'EntryPx', 'ExitPx', 'HeldHrs', 'MFE', 'PnL', 'ExitReason']
    st.dataframe(top_winners[[c for c in cols_winners if c in top_winners.columns]], use_container_width=True)
