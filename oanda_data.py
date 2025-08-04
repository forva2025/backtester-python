import oandapyV20
from oandapyV20.endpoints.instruments import InstrumentsCandles
import pandas as pd

def fetch_oanda_data(instrument="EUR_USD", granularity="M5", count=500, api_key="your_api_key"):
    client = oandapyV20.API(access_token=api_key)
    params = {
        "granularity": granularity,
        "count": count,
        "price": "M"
    }
    r = InstrumentsCandles(instrument=instrument, params=params)
    client.request(r)
    candles = r.response['candles']

    data = pd.DataFrame([{
        "datetime": c['time'],
        "open": float(c['mid']['o']),
        "high": float(c['mid']['h']),
        "low": float(c['mid']['l']),
        "close": float(c['mid']['c']),
        "volume": c['volume']
    } for c in candles])
    data['datetime'] = pd.to_datetime(data['datetime'])
    data.set_index('datetime', inplace=True)
    return data
