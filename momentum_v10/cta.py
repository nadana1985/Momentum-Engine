# Version 10
"""
DEPRECATED: This is an old/archived file.
Use the V3 Dynamic Architecture (cta_dual.py, universe_generator.py).
"""
import sys
import pandas as pd
from pathlib import Path
from momentum_v10.features import load_asset, enrich
from momentum_v10.config import CtaConfig, FeatureConfig
import argparse

def compute_features(df: pd.DataFrame, fcfg: FeatureConfig) -> pd.DataFrame:
    out = enrich(df, fcfg)
    
    # Map strict_ignition to raw_long
    out['raw_long'] = out['strict_ignition']
    out['raw_short'] = False # The original engine only did longs
    return out

def run_cta(df: pd.DataFrame, cfg: CtaConfig) -> pd.DataFrame:
    in_trade = False
    side = None
    entry_price = 0.0
    entry_time = None
    entry_shock = 0.0
    hard_stop = 0.0
    trade_max_high = 0.0
    trade_min_low = 0.0

    trades = []
    
    for ts, row in df.iterrows():
        curr_close = float(row['close'])
        curr_high = float(row['high'])
        curr_low = float(row['low'])
        curr_open = float(row['open'])
        curr_shock = float(row.get('shock_mult', 0.0))
        curr_taker = float(row.get('taker_ratio', 0.5))
        
        candle_range = curr_high - curr_low
        upper_wick = curr_high - max(curr_close, curr_open)
        upper_wick_pct = upper_wick / candle_range if candle_range > 0 else 0
        
        if not in_trade:
            if bool(row.get('raw_long', False)):
                in_trade, side = True, 'long'
                entry_price = curr_close
                hard_stop = curr_low
                entry_time = ts
                entry_shock = curr_shock
                trade_max_high = curr_high
                trade_min_low = curr_low
        else:
            trade_max_high = max(trade_max_high, curr_high)
            trade_min_low = min(trade_min_low, curr_low)
            
            exit_triggered = False
            exit_reason = ''
            exit_price = 0.0
            
            if side == 'long':
                if curr_close < hard_stop:
                    exit_price = curr_close
                    exit_triggered = True
                    exit_reason = 'structural_stop'
                
                curr_oi_change = float(row.get('oi_change', 0.0))
                if curr_shock > 3.0 and (upper_wick_pct > 0.40 or curr_taker < 0.45) and curr_oi_change < 0.0:
                    exit_price = curr_close
                    exit_triggered = True
                    exit_reason = 'exhaustion'
            
            if exit_triggered:
                pnl = (exit_price - entry_price) / entry_price
                trades.append(dict(asset=str(df.iloc[-1].get('asset', '')),
                                   side='LONG', entry=entry_time, exit=ts,
                                   entry_price=entry_price, exit_price=exit_price,
                                   pnl=pnl, shock=entry_shock,
                                   mae=(trade_min_low - entry_price) / entry_price,
                                   mfe=(trade_max_high - entry_price) / entry_price,
                                   reason=exit_reason))
                in_trade = False

    if in_trade:
        pnl = (curr_close - entry_price) / entry_price
        trades.append(dict(asset=str(df.iloc[-1].get('asset', '')),
                           side='LONG', entry=entry_time, exit=ts,
                           entry_price=entry_price, exit_price=curr_close,
                           pnl=pnl, shock=entry_shock,
                           mae=(trade_min_low - entry_price) / entry_price,
                           mfe=(trade_max_high - entry_price) / entry_price,
                           reason='open_at_end'))
                           
    return pd.DataFrame(trades)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--asset', type=str, required=True)
    parser.add_argument('--data-dir', type=str, default='data/raw_shards')
    args = parser.parse_args()

    file = Path(args.data_dir) / f"{args.asset}_USDT_1h.parquet"
    df = load_asset(file)
    
    try:
        metrics_file = Path('data/exotic_shards') / f"{args.asset}USDT_metrics.parquet"
        metrics = pd.read_parquet(metrics_file)
        metrics['timestamp'] = pd.to_datetime(metrics['timestamp'], unit='ms')
        metrics.set_index('timestamp', inplace=True)
        metrics = metrics.resample('1h').last().ffill()
        df = df.join(metrics[['sum_open_interest']], how='left')
        df['sum_open_interest'] = df['sum_open_interest'].ffill()
        df['oi_change'] = df['sum_open_interest'].pct_change()
    except Exception as e:
        df['oi_change'] = 0.0

    # Original Engine Features
    fcfg = FeatureConfig(
        shock_percentile=99.0,
        shock_mult=None,
        year_min_periods=720,  # lax year for early ignitions
        dormant_mode='relative',
        max_notional_usd=150000.0,
        require_taker=True,
        taker_buffer=0.01,
        first_of_run=True
    )
    
    cfg = CtaConfig() # unused mostly but passed

    feat = compute_features(df, fcfg)
    trades = run_cta(feat, cfg)
    
    if trades.empty:
        print('=== NO TRADES ===')
        return
        
    wins = trades[trades['pnl'] > 0]
    win_rate = len(wins) / len(trades) * 100
    avg_pnl = trades['pnl'].mean() * 100
    total_pnl = trades['pnl'].sum() * 100

    print(f"=== {args.asset} PURE DYNAMIC CTA | {len(trades)} trades | win rate {win_rate:.0f}% | avg PnL {avg_pnl:+.2f}% | total {total_pnl:+.2f}% ===")
    for _, t in trades.iterrows():
        ts_e = t['entry'].strftime('%Y-%m-%d %H:%M:%S')
        ts_x = t['exit'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"LONG {ts_e} {ts_x} {t['pnl']:.6f} {t['mfe']:.6f} {t['mae']:.6f} {t['shock']:.6f} {t['reason']}")

if __name__ == '__main__':
    main()




