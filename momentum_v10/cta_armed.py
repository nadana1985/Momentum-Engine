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
    return out

def run_cta(df: pd.DataFrame, cfg: CtaConfig) -> pd.DataFrame:
    completed_trades = []
    active_trades = []
    
    armed_countdown = 0
    armed_shock = 0.0
    armed_hard_stop = 0.0
    
    for ts, row in df.iterrows():
        curr_close = float(row['close'])
        curr_high = float(row['high'])
        curr_low = float(row['low'])
        curr_open = float(row['open'])
        curr_shock = float(row.get('shock_mult', 0.0))
        curr_taker = float(row.get('taker_ratio', 0.5))
        curr_oi_change = float(row.get('oi_change', 0.0))
        
        candle_range = curr_high - curr_low
        upper_wick = curr_high - max(curr_close, curr_open)
        upper_wick_pct = upper_wick / candle_range if candle_range > 0 else 0
        
        # 1. Update and Check Exits for all active trades
        still_active = []
        for t in active_trades:
            t['trade_max_high'] = max(t['trade_max_high'], curr_high)
            t['trade_min_low'] = min(t['trade_min_low'], curr_low)
            
            exit_triggered = False
            exit_reason = ''
            exit_price = 0.0
            
            if curr_close < t['hard_stop']:
                exit_price = curr_close
                exit_triggered = True
                exit_reason = 'structural_stop'
            
            if not exit_triggered and t['entry_shock'] > 3.0 and (upper_wick_pct > 0.40 or curr_taker < 0.45) and curr_oi_change < 0.0:
                exit_price = curr_close
                exit_triggered = True
                exit_reason = 'exhaustion'
                
            if exit_triggered:
                pnl = (exit_price - t['entry_price']) / t['entry_price']
                completed_trades.append(dict(
                    asset=str(df.iloc[-1].get('asset', '')),
                    side='LONG', entry=t['entry_time'], exit=ts,
                    entry_price=t['entry_price'], exit_price=exit_price,
                    pnl=pnl, shock=t['entry_shock'],
                    mae=(t['trade_min_low'] - t['entry_price']) / t['entry_price'],
                    mfe=(t['trade_max_high'] - t['entry_price']) / t['entry_price'],
                    reason=exit_reason
                ))
            else:
                still_active.append(t)
                
        active_trades = still_active

        # 2. Armed State Maintenance
        if armed_countdown > 0:
            if curr_close < armed_hard_stop:
                armed_countdown = 0 # Invalidated by structural breakdown
            else:
                armed_countdown -= 1
                
        # 3. Primer: Hyper Ignition
        if bool(row.get('hyper_ignition', False)):
            armed_countdown = 12
            armed_shock = curr_shock
            armed_hard_stop = curr_low
            
        # 4. Trigger: Taker Aggression
        if armed_countdown > 0 and bool(row.get('is_aggressive_flow', False)):
            active_trades.append({
                'entry_time': ts,
                'entry_price': curr_close,
                'hard_stop': armed_hard_stop,
                'entry_shock': armed_shock,
                'trade_max_high': curr_high,
                'trade_min_low': curr_low
            })
            armed_countdown = 0 # Consumed!

    # Close out any remaining active trades
    for t in active_trades:
        pnl = (curr_close - t['entry_price']) / t['entry_price']
        completed_trades.append(dict(
            asset=str(df.iloc[-1].get('asset', '')),
            side='LONG', entry=t['entry_time'], exit=ts,
            entry_price=t['entry_price'], exit_price=curr_close,
            pnl=pnl, shock=t['entry_shock'],
            mae=(t['trade_min_low'] - t['entry_price']) / t['entry_price'],
            mfe=(t['trade_max_high'] - t['entry_price']) / t['entry_price'],
            reason='open_at_end'
        ))
                           
    return pd.DataFrame(completed_trades)

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

    fcfg = FeatureConfig(
        shock_percentile=99.0,
        shock_mult=None,
        year_min_periods=720,
        dormant_mode='relative',
        max_notional_usd=150000.0,
        require_taker=True,
        taker_buffer=0.01,
        first_of_run=True
    )
    
    cfg = CtaConfig()
    feat = compute_features(df, fcfg)
    trades = run_cta(feat, cfg)
    
    if trades.empty:
        print('=== NO TRADES ===')
        return
        
    trades = trades.sort_values('entry')
    wins = trades[trades['pnl'] > 0]
    win_rate = len(wins) / len(trades) * 100
    avg_pnl = trades['pnl'].mean() * 100
    total_pnl = trades['pnl'].sum() * 100

    print(f"=== {args.asset} ARMED STATE TAPE | {len(trades)} trades | win rate {win_rate:.0f}% | avg PnL {avg_pnl:+.2f}% | total {total_pnl:+.2f}% ===")
    for _, t in trades.iterrows():
        ts_e = t['entry'].strftime('%Y-%m-%d %H:%M:%S')
        ts_x = t['exit'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"LONG {ts_e} {ts_x} {t['pnl']:.6f} {t['mfe']:.6f} {t['mae']:.6f} {t['shock']:.6f} {t['reason']}")

if __name__ == '__main__':
    main()




