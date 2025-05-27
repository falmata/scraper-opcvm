import requests
import pandas as pd


def get_yahoo_history_data(symbol: str,
                           period: str,
                           interval: str) -> pd.DataFrame:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    url = f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}'
    params = {
        'range': period,
        'interval': interval,
        'events': 'history'
    }

    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    result = data['chart']['result'][0]

    timestamps = result['timestamp']
    indicators = result['indicators']['quote'][0]

    df = pd.DataFrame({
        'Date': pd.to_datetime(timestamps, unit='s'),
        'Open': indicators['open'],
        'High': indicators['high'],
        'Low': indicators['low'],
        'Close': indicators['close'],
        'Volume': indicators['volume']
    })

    return df
