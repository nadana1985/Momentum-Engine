import http.server
import socketserver
import json
import os
import pandas as pd
import numpy as np
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from momentum_v10.config import SHARD_DIR, TAPE_DIR

PORT = 8050
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

def calc_point_72(asset_name: str) -> float | None:
    try:
        p_file = SHARD_DIR / f"{asset_name}_USDT_1h.parquet"
        if not p_file.exists(): 
            return None
        d = pd.read_parquet(p_file, columns=['close'])
        if len(d) < 720: 
            return None
        d = d.tail(720).copy()
        d['ret'] = d['close'].pct_change()
        pos = d['ret'][d['ret'] > 0].dropna().values
        if len(pos) < 50: 
            return None
        X = np.sort(pos)[::-1]
        k = max(5, int(0.05 * len(X)))
        threshold = X[k]
        if threshold <= 0: 
            return None
        log_sum = np.sum(np.log(X[:k] / threshold))
        if log_sum == 0: 
            return None
        return float(k / log_sum)
    except Exception:
        return None

def build_api_response(mode: str = 'open'):
    open_df, all_df = load_data()
    
    if mode == 'closed':
        target_df = all_df[all_df['reason'] != 'open_at_end'].copy() if not all_df.empty else pd.DataFrame()
    elif mode == 'all':
        target_df = all_df.copy() if not all_df.empty else open_df.copy()
    else:
        target_df = open_df.copy() if not open_df.empty else (all_df[all_df['reason'] == 'open_at_end'].copy() if not all_df.empty else pd.DataFrame())
        
    if target_df.empty:
        return {
            "summary": {
                "total_open": 0, "open_win_pct": 0.0, "unrealized_cum_pnl": 0.0, 
                "mean_pnl": 0.0, "top_runner_asset": "N/A", "top_runner_pnl": 0.0
            },
            "trend": [],
            "engines": [],
            "durations": [],
            "open_positions": []
        }
        
    # Standardize column names
    if 'pnl_pct' not in target_df.columns and 'pnl' in target_df.columns:
        target_df['pnl_pct'] = target_df['pnl'] * 100.0
    if 'mfe_pct' not in target_df.columns and 'mfe' in target_df.columns:
        target_df['mfe_pct'] = target_df['mfe'] * 100.0
    if 'duration_hours' not in target_df.columns:
        target_df['duration_hours'] = 1.0
        
    # Calculate KPIs
    total_open = len(target_df)
    win_pct = float((target_df['pnl_pct'] > 0).mean() * 100.0) if total_open > 0 else 0.0
    cum_pnl = float(target_df['pnl_pct'].sum())
    mean_pnl = float(target_df['pnl_pct'].mean()) if total_open > 0 else 0.0
    
    sorted_open = target_df.sort_values('pnl_pct', ascending=False)
    top_runner_asset = str(sorted_open.iloc[0]['asset']) if not sorted_open.empty else "N/A"
    top_runner_pnl = float(sorted_open.iloc[0]['pnl_pct']) if not sorted_open.empty else 0.0
    
    # Engine Breakdown
    eng_counts = target_df['engine'].value_counts()
    engine_list = []
    top_4_engines = eng_counts.head(5)
    others_count = eng_counts.iloc[5:].sum() if len(eng_counts) > 5 else 0
    
    colors = ['#00f0ff', '#ffb800', '#7b61ff', '#00ff87', '#ec4899', '#8e8ea8']
    idx = 0
    for eng_name, cnt in top_4_engines.items():
        pct = float(cnt / total_open * 100.0)
        engine_list.append({
            "name": str(eng_name),
            "count": int(cnt),
            "pct": round(pct, 1),
            "color": colors[idx % len(colors)]
        })
        idx += 1
    if others_count > 0:
        pct = float(others_count / total_open * 100.0)
        engine_list.append({
            "name": "Others",
            "count": int(others_count),
            "pct": round(pct, 1),
            "color": colors[5]
        })
        
    # Duration Breakdown
    dur_h = target_df['duration_hours'].fillna(1.0)
    bin_lt6 = int((dur_h < 6).sum())
    bin_6_24 = int(((dur_h >= 6) & (dur_h < 24)).sum())
    bin_24_48 = int(((dur_h >= 24) & (dur_h < 48)).sum())
    bin_gt48 = int((dur_h >= 48).sum())
    
    durations = [
        {"label": "< 6h", "count": bin_lt6, "pct": round(bin_lt6 / total_open * 100.0, 1)},
        {"label": "6 - 24h", "count": bin_6_24, "pct": round(bin_6_24 / total_open * 100.0, 1)},
        {"label": "24 - 48h", "count": bin_24_48, "pct": round(bin_24_48 / total_open * 100.0, 1)},
        {"label": "> 48h", "count": bin_gt48, "pct": round(bin_gt48 / total_open * 100.0, 1)},
    ]
    
    # Cumulative PnL Trend series sorted by entry date
    target_df['entry_dt'] = pd.to_datetime(target_df['entry'], errors='coerce')
    trend_df = target_df.sort_values('entry_dt').dropna(subset=['entry_dt']).copy()
    trend_df['cum_pnl'] = trend_df['pnl_pct'].cumsum()
    
    trend_series = []
    # Sample down long series for smooth chart rendering
    step = max(1, len(trend_df) // 200)
    sampled_trend = trend_df.iloc[::step]
    for _, r in sampled_trend.iterrows():
        trend_series.append({
            "time": r['entry_dt'].strftime('%b %d %H:%M') if pd.notna(r['entry_dt']) else "",
            "cum_pnl": round(float(r['cum_pnl']), 2)
        })
        
    # Positions Table
    positions = []
    for i, r in sorted_open.iterrows():
        dur_hrs = float(r.get('duration_hours', 1.0))
        dur_str = f"{int(dur_hrs)}h" if not np.isnan(dur_hrs) else "1h"
        
        entry_px = float(r.get('entry_price', r.get('entry_px', 0.0)))
        current_px = float(r.get('exit_price', r.get('exit_px', entry_px)))
        pnl_v = float(r.get('pnl_pct', 0.0))
        mfe_v = float(r.get('mfe_pct', r.get('mfe', 0.0)))
        
        positions.append({
            "id": int(i + 1000),
            "asset": str(r['asset']),
            "engine": str(r['engine']),
            "entry_time": str(r['entry']).replace('T', ' ')[:16],
            "entry_px": entry_px,
            "current_px": current_px,
            "duration": dur_str,
            "duration_hours": dur_hrs,
            "mfe": round(mfe_v, 4),
            "pnl_pct": round(pnl_v, 4)
        })
        
    return {
        "summary": {
            "total_open": total_open,
            "open_win_pct": round(win_pct, 1),
            "unrealized_cum_pnl": round(cum_pnl, 1),
            "mean_pnl": round(mean_pnl, 2),
            "top_runner_asset": top_runner_asset,
            "top_runner_pnl": round(top_runner_pnl, 1)
        },
        "trend": trend_series,
        "engines": engine_list,
        "durations": durations,
        "open_positions": positions
    }

class TradoorHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/api/data':
            query = parse_qs(parsed.query)
            mode = query.get('mode', ['open'])[0]
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            data = build_api_response(mode)
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif parsed.path == '/api/asset_dna':
            query = parse_qs(parsed.query)
            asset = query.get('asset', [''])[0]
            alpha = calc_point_72(asset) if asset else None
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"asset": asset, "alpha": alpha}).encode('utf-8'))
        elif parsed.path == '/' or parsed.path == '/index.html':
            html_file = Path(__file__).parent / 'dashboard_v10.html'
            if html_file.exists():
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                with open(html_file, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "dashboard_v10.html not found")
        else:
            super().do_GET()

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def run_server():
    print(f"[TRADOOR] Command Center Server running on http://localhost:{PORT}")
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), TradoorHandler) as httpd:
        httpd.serve_forever()

if __name__ == '__main__':
    run_server()
