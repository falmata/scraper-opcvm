from data import get_yahoo_history_data
from indicators import calculate_indicators
from export import save_results
from datetime import datetime
import pandas as pd


def main():
    # ISIN IE0002ZXSH01 represent WPEA.PA ticker
    # Data will be scraped from Yahoo Finance
    # symbol for WPEA.PA is 'WPEA.PA'
    # (source: yahoo finance https://finance.yahoo.com/quote/WPEA.PA/history/)

    symbol = 'WPEA.PA'
    today = datetime.now()
    periods = {
        'YTD': datetime(today.year, 1, 1),
        '3M': today - pd.DateOffset(months=3),
        '6M': today - pd.DateOffset(months=6),
        '1Y': today - pd.DateOffset(years=1),
        '3Y': today - pd.DateOffset(years=3)
    }

    all_data = {}
    data = get_yahoo_history_data(symbol, period='1y', interval='1d')

    for period, start in periods.items():
        filtered = data[data['Date'] >= pd.to_datetime(start)]
        if not filtered.empty:
            indicators = calculate_indicators(filtered)
            all_data[period] = indicators
        else:
            print("No data for period:", period)

    save_results(all_data, 'data/ISIN_IE0002ZXSH01_results.csv')


if __name__ == '__main__':
    main()
