
import pandas as pd
import numpy as np

from xgboost import XGBRegressor


class SpendingForecaster:

    def __init__(self):

        self.model = XGBRegressor(
            n_estimators=100,
            learning_rate=0.1,
            random_state=42
        )

    def train(self, csv_path):

        df = pd.read_csv(csv_path)

        df["month_index"] = np.arange(
            len(df)
        )

        X = df[["month_index"]]

        y = df["amount"]

        self.model.fit(X, y)

        self.last_index = len(df) - 1

    def predict_next_month(self):

        next_month = np.array(
            [[self.last_index + 1]]
        )

        prediction = self.model.predict(
            next_month
        )[0]

        return round(
            float(prediction),
            2
        )

