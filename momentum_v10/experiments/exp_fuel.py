# Version 10
import sys
import pandas as pd
from pathlib import Path
from momentum_v10.features import load_asset, enrich
from momentum_v10.config import CtaConfig, FeatureConfig
import argparse

def compute_features(df: pd.DataFrame, fcfg: FeatureConfig) -> pd.DataFrame:
    out = enrich(df, fcfg)
    
    out['sma_200'] = out['close'].shift(1).rolling(200, min_periods=24).mean()
    out['is_uptrend'] = out['close'] > out['sma_200']
    
    # True Dynamic Fix: Strictly Shifted for Causality
    out['avg_candle_size'] = ((out['high'] - out['low']) / out['close']).shift(1).rolling(720, min_periods=24).mean()
    out['oi_change_p90'] = out['oi_change'].shift(1).rolling(720, min_periods=24).quantile(0.90)
    
    current_candle_size = (out['high'] - out['low']) / out['low']
    
    if 'topLongShortAccountRatio' in out.columns:
        ls_p05 = out['topLongShortAccountRatio'].shift(1).rolling(720, min_periods=24).quantile(0.05)
        is_dropping = out['topLongShortAccountRatio'].diff(1) < 0
        out['whale_trap'] = (out['topLongShortAccountRatio'] < ls_p05) & is_dropping
    else:
        out['whale_trap'] = False
        
    if 'funding_rate' in out.columns:
        out['funding_p99'] = out['funding_rate'].shift(1).rolling(720, min_periods=24).quantile(0.99)
        out['is_overheated'] = (out['funding_rate'] > out['funding_p99']) & (out['funding_rate'] > 0.0001)
    else:
        out['funding_p99'] = 0.0
        out['is_overheated'] = False

    # --- Signal 1: Institutional Flow (trade count → avg trade size > P90 baseline) ---
    # Filters out retail FOMO shocks. A 25x volume spike from 12 whale blocks
    # is categorically different from 200,000 retail market orders.
    if 'count' in out.columns:
        count_safe = out['count'].replace(0, float('nan'))
        out['avg_trade_size'] = out['volume'] / count_safe
        out['avg_trade_size_p90_30d'] = (
            out['avg_trade_size'].shift(1).rolling(720, min_periods=24).quantile(0.90)
        )
        out['is_institutional_flow'] = out['avg_trade_size'] > out['avg_trade_size_p90_30d']
    else:
        out['is_institutional_flow'] = True  # count absent → gate disabled (graceful)

    # --- Signal 2: USD-denominated OI change (cross-asset normalised exhaustion) ---
    # sum_open_interest_value is in USD, making the blow-off exit comparable across
    # low-cap and high-cap assets without being distorted by contract sizing.
    if 'sum_open_interest_value' in out.columns:
        out['oi_value_change'] = out['sum_open_interest_value'].pct_change()
    else:
        out['oi_value_change'] = out.get('oi_change', pd.Series(0.0, index=out.index))

    # --- Signal 3: Quote-denominated taker aggression (USD taker flow) ---
    # taker_buy_quote_volume / quote_volume is more stable across assets of different
    # price scales than the base-token ratio. OR logic: either measure firing is enough.
    if 'taker_buy_quote_volume' in out.columns and 'quote_volume' in out.columns:
        quote_vol_safe = out['quote_volume'].replace(0, float('nan'))
        out['taker_quote_ratio'] = out['taker_buy_quote_volume'] / quote_vol_safe
        out['p50_taker_quote_30d'] = (
            out['taker_quote_ratio'].shift(1).rolling(720, min_periods=720).median()
        )
        out['is_aggressive_flow_quote'] = (
            out['taker_quote_ratio'] > (out['p50_taker_quote_30d'] + 0.01)
        )
    else:
        out['is_aggressive_flow_quote'] = out['is_aggressive_flow']

    out['continuation_long'] = (
        out['is_uptrend'] &
        out['breakout'] &
        (out['is_aggressive_flow'] | out['is_aggressive_flow_quote']) &  # Signal 3: OR (more fills)
        out['is_institutional_flow'] &                                    # Signal 1: whale confirmation
        (current_candle_size > (out['avg_candle_size'] * 2.5)) &
        (out['oi_change'] > out['oi_change_p90']) &
        (~out['whale_trap']) &
        (~out['is_overheated'])
    )

    return out

def run_cta(df: pd.DataFrame, cfg: CtaConfig, asset: str = '') -> pd.DataFrame:
    """Execute the V6 dual-engine (IGNITION + CONTINUATION) on pre-enriched features.

    Parameters
    ----------
    df : pd.DataFrame
        Output of compute_features() — must have all feature columns present.
    cfg : CtaConfig
        Execution configuration.
    asset : str
        Symbol name used to label trade records (e.g. 'BTC', 'ETH').
        Pass explicitly — never infer from df.iloc[-1] which is fragile.
    """
    completed_trades = []
    active_trades = []

    armed_countdown = 0
    armed_shock = 0.0
    armed_hard_stop = 0.0

    # Slippage assumption: 0.20% cost on aggressive entries and panic exits
    SLIPPAGE = 0.0020
    # Maximum number of concurrent open positions per asset.
    # Prevents stacking of ignition bursts / continuation chains into unbounded exposure.
    MAX_CONCURRENT = 1

    for ts, row in df.iterrows():
        curr_close = float(row['close'])
        curr_high = float(row['high'])
        curr_low = float(row['low'])
        curr_open = float(row['open'])
        curr_shock = float(row.get('shock_mult', 0.0))
        curr_taker = float(row.get('taker_ratio', 0.5))
        curr_oi_change = float(row.get('oi_change', 0.0))
        # Signal 2: USD OI change (preferred over contract OI for cross-asset exhaustion)
        curr_oi_value_change = float(row.get('oi_value_change', curr_oi_change))
        # Signal 1: institutional flow — True when avg trade size > own 30d P90
        is_institutional = bool(row.get('is_institutional_flow', True))
        
        candle_range = curr_high - curr_low
        upper_wick = curr_high - max(curr_close, curr_open)
        upper_wick_pct = upper_wick / candle_range if candle_range > 0 else 0
        
        still_active = []
        for t in active_trades:
            t['trade_max_high'] = max(t['trade_max_high'], curr_high)
            t['trade_min_low'] = min(t['trade_min_low'], curr_low)
            
            exit_triggered = False
            exit_reason = ''
            exit_price = 0.0
            
            curr_funding = float(row.get('funding_rate', 0.0))
            funding_p99 = float(row.get('funding_p99', 0.0))
            is_parabolic = curr_funding > funding_p99 and curr_funding > 0.0001
            
            # Structural Stop (Suspended during Parabolic Squeezes to avoid trap candles) + Slippage
            if curr_close < t['hard_stop'] and not is_parabolic:
                exit_price = curr_close * (1 - SLIPPAGE)
                exit_triggered = True
                exit_reason = 'structural_stop'
                
            # EXP 1: Fuel Exhaustion
            mfe_pct = (t['trade_max_high'] - t['entry_price']) / t['entry_price']
            curr_ls_ratio = float(row.get('topLongShortAccountRatio', 1.0))
            if not exit_triggered and mfe_pct > 0.80 and curr_ls_ratio > 1.2:
                # Squeeze is over, whales have flipped long, retail is bagholding/shorting
                exit_price = curr_close * (1 - SLIPPAGE)
                exit_triggered = True
                exit_reason = 'fuel_exhaustion'

            # OI Exhaustion Exit — uses USD OI change (Signal 2) for cross-asset normalised blow-off
            if not exit_triggered and curr_shock > 3.0 and (upper_wick_pct > 0.40 or curr_taker < 0.45) and curr_oi_value_change < 0.0:
                exit_price = curr_close * (1 - SLIPPAGE)
                exit_triggered = True
                exit_reason = 'exhaustion'
                
            if exit_triggered:
                pnl = (exit_price - t['entry_price']) / t['entry_price']
                completed_trades.append(dict(
                    asset=asset,  # FIXED: use explicit parameter, not df.iloc[-1]
                    side='LONG', entry=t['entry_time'], exit=ts,
                    entry_price=t['entry_price'], exit_price=exit_price,
                    pnl=pnl, shock=t['entry_shock'],
                    mae=(t['trade_min_low'] - t['entry_price']) / t['entry_price'],
                    mfe=(t['trade_max_high'] - t['entry_price']) / t['entry_price'],
                    reason=exit_reason,
                    engine=t['engine']
                ))
            else:
                still_active.append(t)

        active_trades = still_active

        if armed_countdown > 0:
            if curr_close < armed_hard_stop:
                armed_countdown = 0
            else:
                armed_countdown -= 1

        if bool(row.get('hyper_ignition', False)):
            armed_countdown = 12
            armed_shock = curr_shock
            armed_hard_stop = curr_low

        # Entry Logic (+ Slippage penalty applied to curr_close)
        entry_exec_price = curr_close * (1 + SLIPPAGE)
        is_whale_trap = bool(row.get('whale_trap', False))
        is_squeeze = float(row.get('funding_rate', 0.0)) < 0.0

        # IGNITION / SQUEEZE_IGN entry — respects MAX_CONCURRENT cap + Signal 1 institutional gate
        if (armed_countdown > 0
                and bool(row.get('is_aggressive_flow', False))
                and not is_whale_trap
                and is_institutional                            # Signal 1: only enter when avg trade size > P90
                and len(active_trades) < MAX_CONCURRENT):
            hard_stop_adj = armed_hard_stop
            if is_squeeze:
                sl_mod = -0.5  # Optimal parameter discovered via universe-wide sweep
                risk = entry_exec_price - armed_hard_stop
                hard_stop_adj = armed_hard_stop + (risk * sl_mod)

            active_trades.append({
                'entry_time': ts,
                'entry_price': entry_exec_price,
                'hard_stop': hard_stop_adj,
                'entry_shock': armed_shock,
                'trade_max_high': entry_exec_price,
                'trade_min_low': entry_exec_price,
                'engine': 'SQUEEZE_IGN' if is_squeeze else 'IGNITION'
            })
            armed_countdown = 0

        # CONTINUATION entry — respects MAX_CONCURRENT cap
        if (bool(row.get('continuation_long', False))
                and len(active_trades) < MAX_CONCURRENT):  # ADDED: position cap
            active_trades.append({
                'entry_time': ts,
                'entry_price': entry_exec_price,
                'hard_stop': curr_low,
                'entry_shock': curr_shock,
                'trade_max_high': entry_exec_price,
                'trade_min_low': entry_exec_price,
                'engine': 'CONTINUATION'
            })

    for t in active_trades:
        pnl = (curr_close - t['entry_price']) / t['entry_price']
        completed_trades.append(dict(
            asset=asset,  # FIXED: use explicit parameter, not df.iloc[-1]
            side='LONG', entry=t['entry_time'], exit=ts,
            entry_price=t['entry_price'], exit_price=curr_close,
            pnl=pnl, shock=t['entry_shock'],
            mae=(t['trade_min_low'] - t['entry_price']) / t['entry_price'],
            mfe=(t['trade_max_high'] - t['entry_price']) / t['entry_price'],
            reason='open_at_end',
            engine=t['engine']
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
        
        cols_to_join = ['sum_open_interest']
        if 'sum_open_interest_value' in metrics.columns:
            cols_to_join.append('sum_open_interest_value')
        if 'count_toptrader_long_short_ratio' in metrics.columns:
            cols_to_join.append('count_toptrader_long_short_ratio')
            
        df = df.join(metrics[cols_to_join], how='left')
        df['sum_open_interest'] = df['sum_open_interest'].ffill()
        df['oi_change'] = df['sum_open_interest'].pct_change()
        
        if 'sum_open_interest_value' in df.columns:
            df['sum_open_interest_value'] = df['sum_open_interest_value'].ffill()
        else:
            df['sum_open_interest_value'] = float('nan')

        if 'count_toptrader_long_short_ratio' in df.columns:
            df['count_toptrader_long_short_ratio'] = df['count_toptrader_long_short_ratio'].ffill()
            df['topLongShortAccountRatio'] = df['count_toptrader_long_short_ratio']
        else:
            df['count_toptrader_long_short_ratio'] = 1.0
            df['topLongShortAccountRatio'] = 1.0
    except Exception as e:
        df['oi_change'] = 0.0
        df['count_toptrader_long_short_ratio'] = 1.0
        df['topLongShortAccountRatio'] = 1.0

    try:
        funding_file = Path('data/exotic_shards') / f"{args.asset}USDT_funding.parquet"
        funding = pd.read_parquet(funding_file)
        funding['timestamp'] = pd.to_datetime(funding['timestamp'], unit='ms')
        funding.set_index('timestamp', inplace=True)
        funding = funding.resample('1h').last().ffill()
        if 'funding_rate' in funding.columns:
            df = df.join(funding[['funding_rate']], how='left')
            df['funding_rate'] = df['funding_rate'].ffill()
        else:
            df['funding_rate'] = 0.0
    except Exception:
        df['funding_rate'] = 0.0

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
    trades = run_cta(feat, cfg, asset=args.asset)
    
    if trades.empty:
        print('=== NO TRADES ===')
        return
        
    trades = trades.sort_values('entry')
    wins = trades[trades['pnl'] > 0]
    win_rate = len(wins) / len(trades) * 100
    avg_pnl = trades['pnl'].mean() * 100
    total_pnl = trades['pnl'].sum() * 100

    print(f"=== {args.asset} TRUE DYNAMIC TAPE | {len(trades)} trades | win rate {win_rate:.0f}% | avg PnL {avg_pnl:+.2f}% | total {total_pnl:+.2f}% ===")
    for _, t in trades.iterrows():
        ts_e = t['entry'].strftime('%Y-%m-%d %H:%M:%S')
        ts_x = t['exit'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"{t['engine']} {ts_e} {ts_x} {t['pnl']:.6f} {t['mfe']:.6f} {t['mae']:.6f} {t['shock']:.6f} {t['reason']}")

if __name__ == '__main__':
    main()



