import pandas as pd


def save_results(results: dict, filepath: str) -> None:
    df = pd.DataFrame(results).T
    df.to_csv(filepath)
