from fastapi import FastAPI
import ccxt
import pandas as pd

app = FastAPI()

exchange = ccxt.binance()

def get_data():
    ohlcv = exchange.fetch_ohlcv('BTC/USDT', timeframe='15m', limit=100)
    df = pd.DataFrame(ohlcv, columns=['timestamp','open','high','low','close','volume'])
    return df

def simple_fibo_levels(df):
    high = df['high'].max()
    low = df['low'].min()

    level_0_618 = high - (high - low) * 0.618
    return level_0_618

def simple_volume_check(df):
    last_volume = df['volume'].iloc[-1]
    avg_volume = df['volume'].rolling(20).mean().iloc[-1]

    return last_volume > avg_volume

def generate_signal(df):
    price = df['close'].iloc[-1]
    fibo = simple_fibo_levels(df)
    volume_ok = simple_volume_check(df)

    if price < fibo and volume_ok:
        return "long", 0.75

    elif price > fibo and volume_ok:
        return "short", 0.75

    else:
        return "no_trade", 0.5

@app.get("/signal")
def signal():
    df = get_data()
    signal, confidence = generate_signal(df)

    return {
        "symbol": "BTCUSDT",
        "signal": signal,
        "confidence": confidence
    }
