import pandas as pd
import numpy as np


def calculate_indicators(df: pd.DataFrame) -> dict:

    data = df.copy()
    data['Returns'] = data['Close'].pct_change()

    perf = data['Close'].iloc[-1] / data['Close'].iloc[0] - 1
    vol = data['Returns'].std() * np.sqrt(252)
    avg_return = data['Returns'].mean() * 252

    cumulative = (1 + data['Returns'].fillna(0)).cumprod()
    max_cum = cumulative.cummax()
    drawdown = cumulative / max_cum - 1
    max_dd = drawdown.min()

    indicators = {
        'Performance': f"{perf * 100:.2f}%",
        'Volatility': f"{vol * 100:.2f}%",
        'Expected Return': f"{avg_return * 100:.2f}%",
        'Max Drawdown': f"{max_dd * 100:.2f}%"
    }

    return indicators
