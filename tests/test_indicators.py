import pandas as pd
import numpy as np
from src.indicators import calculate_indicators


def test_calculate_indicators_basic():

    data = pd.DataFrame({
        'Close': [100, 105, 110, 120, 130]
    })
    indicators = calculate_indicators(data)

    assert 'Performance' in indicators
    assert 'Volatility' in indicators
    assert 'Expected Return' in indicators
    assert 'Max Drawdown' in indicators

    perf_val = float(indicators['Performance'].replace('%', ''))
    assert perf_val > 0


def test_calculate_indicators_constant_prices():

    data = pd.DataFrame({
        'Close': [100, 100, 100, 100, 100]
    })
    indicators = calculate_indicators(data)
    assert indicators['Performance'] == "0.00%"
    assert indicators['Volatility'] == "0.00%"
    assert indicators['Expected Return'] == "0.00%"
    assert indicators['Max Drawdown'] == "0.00%"


def test_calculate_indicators_with_nan():

    data = pd.DataFrame({
        'Close': [100, np.nan, 110, 120, 130]
    })
    indicators = calculate_indicators(data)
    assert isinstance(indicators, dict)

    perf_val = float(indicators['Performance'].replace('%', ''))
    assert perf_val > 0


def test_calculate_indicators_drawdown():

    data = pd.DataFrame({
        'Close': [100, 120, 80, 90, 110]
    })
    indicators = calculate_indicators(data)
    max_dd = float(indicators['Max Drawdown'].replace('%', ''))
    assert max_dd < 0


def test_calculate_indicators_short_series():

    data = pd.DataFrame({
        'Close': [100, 110]
    })
    indicators = calculate_indicators(data)
    assert isinstance(indicators, dict)
    assert 'Performance' in indicators
