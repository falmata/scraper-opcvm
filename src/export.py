import pandas as pd


def save_results(results: dict, filepath: str) -> None:

    # I used dataframe.T to transpose the dictionary
    # so that the keys become the columns and the values become the rows
    df = pd.DataFrame(results).T
    df.to_csv(filepath)
