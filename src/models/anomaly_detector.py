import pandas as pd
from sklearn.ensemble import IsolationForest


class ExpenseAnomalyDetector:

    def __init__(self):

        self.model = IsolationForest(
            contamination=0.05,
            random_state=42
        )

    def train(self, expenses):

        df = pd.DataFrame(
            expenses,
            columns=["amount"]
        )

        self.model.fit(df)

    def detect(self, amount):

        prediction = self.model.predict(
            [[amount]]
        )[0]

        if prediction == -1:
            return "Anomaly Detected"

        return "Normal Transaction"