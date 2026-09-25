import os
import pandas as pd
import numpy as np
from pathlib import Path
from nicegui import ui

from momentum_v10.config import SHARD_DIR, TAPE_DIR

OPEN_CSV = TAPE_DIR / 'open_trades.csv'
ALL_CSV = TAPE_DIR / 'all_trades.csv'

_DATA_CACHE = {"open_mtime": 0, "open_df": None, "all_mtime": 0, "all_df": None}

def load_data():
    global _DATA_CACHE
    if OPEN_CSV.exists():
        mtime = os.path.getmtime(OPEN_CSV)
        if _DATA_CACHE["open_df"] is None or mtime > _DATA_CACHE["open_mtime"]:
            _DATA_CACHE["open_df"] = pd.read_csv(OPEN_CSV)
            _DATA_CACHE["open_mtime"] = mtime
    else:
        _DATA_CACHE["open_df"] = pd.DataFrame()
        
    if ALL_CSV.exists():
        mtime = os.path.getmtime(ALL_CSV)
        if _DATA_CACHE["all_df"] is None or mtime > _DATA_CACHE["all_mtime"]:
            _DATA_CACHE["all_df"] = pd.read_csv(ALL_CSV)
            _DATA_CACHE["all_mtime"] = mtime
    else:
        _DATA_CACHE["all_df"] = pd.DataFrame()
        
    return _DATA_CACHE["open_df"], _DATA_CACHE["all_df"]

def find_shard_file(asset_name: str) -> Path | None:
    if not asset_name:
        return None
    clean = asset_name.strip().upper().replace('_USDT', '').replace('USDT', '')
    if not clean:
        return None
    candidates = [
        SHARD_DIR / f"{clean}_USDT_1h.parquet",
        SHARD_DIR / f"1000{clean}_USDT_1h.parquet",
        SHARD_DIR / f"1000000{clean}_USDT_1h.parquet",
    ]
    for c in candidates:
        if c.exists():
            return c
    if SHARD_DIR.exists():
        for p in SHARD_DIR.glob('*_USDT_1h.parquet'):
            sym = p.name.replace('_USDT_1h.parquet', '')
            if clean == sym or clean == sym.replace('1000', '').replace('1000000', ''):
                return p
    return None

def calc_point_72(asset_name: str) -> float | None:
    try:
        p_file = find_shard_file(asset_name)
        if not p_file or not p_file.exists(): 
            return None
        d = pd.read_parquet(p_file, columns=['close'])
        if len(d) < 720: 
            return None
        d = d.tail(720).copy()
        d['ret'] = d['close'].pct_change()
        pos = d['ret'][d['ret'] > 0].dropna().values
        if len(pos) < 10: 
            return None
        sorted_rets = np.sort(pos)[::-1]
        k = max(3, int(0.10 * len(sorted_rets)))
        tail = sorted_rets[:k]
        u = sorted_rets[k]
        if u <= 0: 
            return None
        log_ratios = np.log(tail / u)
        if np.sum(log_ratios) == 0: 
            return None
        return float(k / np.sum(log_ratios))
    except Exception:
        return None

def get_processed_data(mode='open'):
    open_df, all_df = load_data()
    if mode == 'closed':
        target_df = all_df[all_df['reason'] != 'open_at_end'].copy() if not all_df.empty else pd.DataFrame()
    elif mode == 'all':
        target_df = all_df.copy() if not all_df.empty else open_df.copy()
    else:
        target_df = open_df.copy() if not open_df.empty else (all_df[all_df['reason'] == 'open_at_end'].copy() if not all_df.empty else pd.DataFrame())
        
    if target_df.empty:
        return {
            'total': 0, 'win_pct': 0.0, 'cum_pnl': 0.0, 'mean_pnl': 0.0,
            'top_runner': 'N/A', 'top_pnl': 0.0, 'engines': [], 'trend_x': [], 'trend_y': [], 'rows': []
        }

    if 'pnl_pct' not in target_df.columns and 'pnl' in target_df.columns:
        target_df['pnl_pct'] = target_df['pnl'] * 100.0
    if 'mfe_pct' not in target_df.columns and 'mfe' in target_df.columns:
        target_df['mfe_pct'] = target_df['mfe'] * 100.0

    total = len(target_df)
    win_pct = float((target_df['pnl_pct'] > 0).mean() * 100.0) if total > 0 else 0.0
    cum_pnl = float(target_df['pnl_pct'].sum())
    mean_pnl = float(target_df['pnl_pct'].mean()) if total > 0 else 0.0
    
    sorted_df = target_df.sort_values('pnl_pct', ascending=False)
    top_runner = str(sorted_df.iloc[0]['asset']) if not sorted_df.empty else "N/A"
    top_pnl = float(sorted_df.iloc[0]['pnl_pct']) if not sorted_df.empty else 0.0

    # Engine breakdown
    eng_counts = target_df['engine'].value_counts()
    engine_data = []
    colors = ['#00f0ff', '#ffb800', '#7b61ff', '#00ff87', '#ec4899', '#8e8ea8']
    for idx, (name, count) in enumerate(eng_counts.items()):
        engine_data.append({
            'name': str(name),
            'value': int(count),
            'itemStyle': {'color': colors[idx % len(colors)]}
        })

    # Trend line
    target_df['entry_dt'] = pd.to_datetime(target_df['entry'], errors='coerce')
    trend_df = target_df.sort_values('entry_dt').dropna(subset=['entry_dt']).copy()
    trend_df['cum_pnl'] = trend_df['pnl_pct'].cumsum()
    step = max(1, len(trend_df) // 150)
    sampled = trend_df.iloc[::step]
    trend_x = [r.strftime('%b %d') for r in sampled['entry_dt']]
    trend_y = [round(float(v), 1) for v in sampled['cum_pnl']]

    # Rows for Quasar table
    rows = []
    for idx, r in sorted_df.iterrows():
        dur_h = float(r.get('duration_hours', 1.0))
        entry_px = float(r.get('entry_price', r.get('entry_px', 0.0)))
        
        exit_px_raw = r.get('exit_price', r.get('exit_px', entry_px))
        exit_px = float(exit_px_raw) if not pd.isna(exit_px_raw) and str(exit_px_raw).lower() != 'nan' else entry_px

        pnl_v = float(r.get('pnl_pct', 0.0))
        mfe_v = float(r.get('mfe_pct', r.get('mfe', 0.0)))
        
        reason_val = r.get('reason', 'open_at_end')
        if pd.isna(reason_val) or str(reason_val).lower() == 'nan':
            reason_val = 'open_at_end'

        exit_raw = r.get('exit', '')
        if pd.isna(exit_raw) or str(exit_raw).lower() == 'nan' or not str(exit_raw).strip():
            exit_time_str = 'LIVE (OPEN)' if str(reason_val) == 'open_at_end' else 'N/A'
        else:
            exit_time_str = str(exit_raw).replace('T', ' ')[:16]

        rows.append({
            'id': int(idx + 1000),
            'asset': str(r['asset']),
            'engine': str(r['engine']),
            'entry_time': str(r['entry']).replace('T', ' ')[:16],
            'exit_time': exit_time_str,
            'entry_px': round(entry_px, 4),
            'exit_px': round(exit_px, 4),
            'duration': f"{int(dur_h)}h" if not np.isnan(dur_h) else "1h",
            'mfe': round(mfe_v, 2),
            'pnl_pct': round(pnl_v, 2),
            'reason': str(reason_val)
        })

    return {
        'total': total, 'win_pct': round(win_pct, 1), 'cum_pnl': round(cum_pnl, 1), 'mean_pnl': round(mean_pnl, 2),
        'top_runner': top_runner, 'top_pnl': round(top_pnl, 1), 'engines': engine_data,
        'trend_x': trend_x, 'trend_y': trend_y, 'rows': rows
    }

# ---------------------------------------------------------------------------
# NICEGUI PURE PYTHON INTERFACE
# ---------------------------------------------------------------------------
@ui.page('/')
def main_page():
    ui.dark_mode(True)
    
    # Custom CSS for dark glassmorphism
    ui.add_head_html('''
        <style>
            body { background-color: #07090e; font-family: 'Inter', sans-serif; }
            .kpi-card { background: rgba(16, 22, 36, 0.75); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 1rem; }
            .metric-val { font-size: 1.5rem; font-weight: bold; color: #ffffff; }
            .txt-green { color: #00ff87; }
            .txt-red { color: #ff4655; }
        </style>
    ''')

    # Asset DNA Dialog
    with ui.dialog() as dna_dialog, ui.card().style('width: 450px; background: #101624; border: 1px solid #00f0ff;'):
        ui.label('🧬 TRADOOR Asset DNA Panel').classes('text-lg font-bold text-cyan')
        asset_input = ui.input('Asset Symbol', value='LIT', placeholder='Type any symbol (e.g. ALICE, PEPE, BTC)...').classes('w-full')
        alpha_output = ui.label('Alpha: --').classes('text-md font-mono mt-2 text-white')
        alpha_status = ui.label('').classes('text-sm font-bold mt-1')

        def run_dna_calc(e=None):
            sym = str(asset_input.value or '').strip()
            val = calc_point_72(sym)
            if val is not None:
                alpha_output.set_text(f'Point 72 (α) Tail Index: {val:.2f}')
                if val <= 3.19:
                    alpha_status.set_text('VALID (Fat Tail ≤ 3.19)')
                    alpha_status.classes(remove='text-red txt-red', add='text-green txt-green')
                else:
                    alpha_status.set_text('VETO (Thin Tail > 3.19)')
                    alpha_status.classes(remove='text-green txt-green', add='text-red txt-red')
            else:
                alpha_output.set_text('Point 72 (α) Tail Index: N/A')
                alpha_status.set_text(f"No shard history for '{sym}'" if sym else "Enter a symbol")
                alpha_status.classes(remove='text-green txt-green', add='text-red txt-red')

        asset_input.on('keydown.enter', run_dna_calc)
        ui.button('Inspect Asset DNA', on_click=run_dna_calc).props('color=cyan')
        ui.button('Close', on_click=dna_dialog.close).props('flat text-color=grey')

    # Sidebar Drawer
    with ui.left_drawer(value=True).classes('bg-slate-900 border-r border-slate-800').style('width: 230px'):
        ui.label('⚡ TRADOOR').classes('text-xl font-black text-cyan tracking-widest mt-2 ml-2')
        ui.label('TRADE | MONITOR | EXECUTE').classes('text-xs text-slate-400 ml-2 mb-6')
        
        with ui.column().classes('w-full gap-1'):
            ui.button('📊 Dashboard', on_click=lambda: update_mode('open')).props('flat align=left').classes('w-full text-slate-200')
            ui.button('🔥 Open Positions', on_click=lambda: update_mode('open')).props('flat align=left').classes('w-full text-slate-200')
            ui.button('📜 Trade Ledger', on_click=lambda: update_mode('closed')).props('flat align=left').classes('w-full text-slate-200')
            ui.button('📈 Analytics', on_click=lambda: update_mode('all')).props('flat align=left').classes('w-full text-slate-200')
            ui.button('🧬 Asset DNA', on_click=dna_dialog.open).props('flat align=left').classes('w-full text-slate-200')

    # Main Header
    with ui.row().classes('w-full justify-between items-center mb-4'):
        with ui.row().classes('items-center gap-2'):
            ui.label('🔥').classes('text-2xl')
            with ui.column().classes('gap-0'):
                ui.label('Active Open Positions Command Center').classes('text-xl font-bold text-white')
                ui.label('Universal Microstructure & Donchian Ratchet Execution System').classes('text-xs text-slate-400')
        
        with ui.row().classes('items-center gap-3'):
            ui.badge('🟢 LIVE SYSTEM', color='green').classes('px-3 py-1')
            mode_toggle = ui.toggle({
                'open': '🔥 Open Trades',
                'closed': '📜 Closed Book',
                'all': '🌐 All Trades'
            }, value='open', on_change=lambda e: update_mode(e.value)).props('toggle-color=cyan')

    # KPI Strip
    data = get_processed_data('open')

    with ui.grid(columns=5).classes('w-full gap-4 mb-4'):
        with ui.card().classes('kpi-card'):
            kpi_title_lbl = ui.label('Total Open Trades').classes('text-xs text-slate-400')
            kpi_total_val = ui.label(str(data['total'])).classes('metric-val')
        with ui.card().classes('kpi-card'):
            kpi_win_title = ui.label('Open Win %').classes('text-xs text-slate-400')
            kpi_win_val = ui.label(f"{data['win_pct']}%").classes('metric-val txt-green')
        with ui.card().classes('kpi-card'):
            kpi_cum_title = ui.label('Unrealized Cum PnL').classes('text-xs text-slate-400')
            kpi_cum_val = ui.label(f"+{data['cum_pnl']}%").classes('metric-val txt-green')
        with ui.card().classes('kpi-card'):
            kpi_mean_title = ui.label('Mean Open PnL').classes('text-xs text-slate-400')
            kpi_mean_val = ui.label(f"+{data['mean_pnl']}%").classes('metric-val txt-green')
        with ui.card().classes('kpi-card'):
            ui.label('Top Runner').classes('text-xs text-slate-400')
            kpi_top_val = ui.label(f"{data['top_runner']} (+{data['top_pnl']}%)").classes('metric-val text-yellow-400')

    # Middle Charts Row
    with ui.row().classes('w-full gap-4 mb-4'):
        # Trend Line Chart
        with ui.card().classes('kpi-card flex-grow').style('height: 280px;'):
            ui.label('Unrealized PnL Trend').classes('text-sm font-bold text-white mb-2')
            trend_chart = ui.echart({
                'xAxis': {'type': 'category', 'data': data['trend_x']},
                'yAxis': {'type': 'value'},
                'series': [{'data': data['trend_y'], 'type': 'line', 'smooth': True, 'color': '#00ff87', 'areaStyle': {}}]
            }).classes('w-full h-48')

        # Engine Donut Chart
        with ui.card().classes('kpi-card').style('width: 320px; height: 280px;'):
            ui.label('Positions by Engine').classes('text-sm font-bold text-white mb-2')
            donut_chart = ui.echart({
                'series': [{'type': 'pie', 'radius': ['50%', '75%'], 'data': data['engines']}]
            }).classes('w-full h-48')

    # Table Controls & Search Input
    with ui.row().classes('w-full justify-between items-center mb-2'):
        table_title_lbl = ui.label(f"Live Open Positions ({data['total']} Trades)").classes('text-lg font-bold text-white')
        search_input = ui.input(placeholder='Search asset, engine, ID...').classes('w-64')

    # High Performance Quasar Table
    columns = [
        {'name': 'id', 'label': '#', 'field': 'id', 'sortable': True},
        {'name': 'asset', 'label': 'Asset', 'field': 'asset', 'sortable': True},
        {'name': 'engine', 'label': 'Engine', 'field': 'engine', 'sortable': True},
        {'name': 'entry_time', 'label': 'Entry Time', 'field': 'entry_time', 'sortable': True},
        {'name': 'exit_time', 'label': 'Exit Time', 'field': 'exit_time', 'sortable': True},
        {'name': 'entry_px', 'label': 'Entry Px', 'field': 'entry_px'},
        {'name': 'exit_px', 'label': 'Exit Px', 'field': 'exit_px'},
        {'name': 'duration', 'label': 'Duration', 'field': 'duration'},
        {'name': 'mfe', 'label': 'MFE %', 'field': 'mfe', 'sortable': True},
        {'name': 'pnl_pct', 'label': 'PnL %', 'field': 'pnl_pct', 'sortable': True},
        {'name': 'reason', 'label': 'Closure Reason', 'field': 'reason', 'sortable': True},
    ]

    positions_table = ui.table(
        columns=columns,
        rows=data['rows'],
        row_key='id',
        pagination=10
    ).classes('w-full bg-slate-900 text-white').bind_filter(search_input, 'value')

    def update_mode(mode):
        mode_toggle.set_value(mode)
        d = get_processed_data(mode)

        if mode == 'closed':
            kpi_title_lbl.set_text('Total Closed Trades')
            kpi_win_title.set_text('Closed Win %')
            kpi_cum_title.set_text('Realized Cum PnL')
            kpi_mean_title.set_text('Mean Trade PnL')
            table_title_lbl.set_text(f"Harvested Trade Ledger ({d['total']} Trades)")
        elif mode == 'all':
            kpi_title_lbl.set_text('Total Portfolio Trades')
            kpi_win_title.set_text('Overall Win %')
            kpi_cum_title.set_text('Mark-to-Market PnL')
            kpi_mean_title.set_text('Mean Expectancy / Trade')
            table_title_lbl.set_text(f"All Portfolio Executions ({d['total']} Trades)")
        else:
            kpi_title_lbl.set_text('Total Open Trades')
            kpi_win_title.set_text('Open Win %')
            kpi_cum_title.set_text('Unrealized Cum PnL')
            kpi_mean_title.set_text('Mean Open PnL')
            table_title_lbl.set_text(f"Live Open Positions ({d['total']} Trades)")

        kpi_total_val.set_text(str(d['total']))
        kpi_win_val.set_text(f"{d['win_pct']}%")
        kpi_cum_val.set_text(f"+{d['cum_pnl']}%")
        kpi_mean_val.set_text(f"+{d['mean_pnl']}%")
        kpi_top_val.set_text(f"{d['top_runner']} (+{d['top_pnl']}%)")

        trend_chart.options['xAxis']['data'] = d['trend_x']
        trend_chart.options['series'][0]['data'] = d['trend_y']
        trend_chart.update()

        donut_chart.options['series'][0]['data'] = d['engines']
        donut_chart.update()

        positions_table.rows = d['rows']

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(port=8055, title='TRADOOR — Pure Python NiceGUI Dashboard', reload=False)
