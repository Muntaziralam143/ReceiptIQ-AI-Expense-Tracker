import pandas as pd


def load_expense_data(path):
    """
    Load expense dataset
    """

    df = pd.read_csv(path)

    return df