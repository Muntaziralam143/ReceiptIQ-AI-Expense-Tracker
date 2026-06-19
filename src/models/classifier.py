import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from config import CLASSIFIER_MODEL


class ExpenseClassifier:

    def __init__(self):

        self.pipeline = Pipeline([
            (
                "tfidf",
                TfidfVectorizer()
            ),
            (
                "model",
                LogisticRegression(
                    max_iter=1000
                )
            )
        ])

        self.reverse_map = None

    def train(self, df):

        X = (
            df["merchant"]
            + " "
            + df["description"]
        )

        y = df["category"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        self.pipeline.fit(
            X_train,
            y_train
        )

        predictions = self.pipeline.predict(
            X_test
        )

        print(
            classification_report(
                y_test,
                predictions
            )
        )

    def save(self):

        joblib.dump(
            self.pipeline,
            CLASSIFIER_MODEL
        )

        print(
            f"Model saved at {CLASSIFIER_MODEL}"
        )

    def load(self):

        data = joblib.load(
            CLASSIFIER_MODEL
        )

        if isinstance(data, dict):

            self.pipeline = data["pipeline"]

            self.reverse_map = data.get(
                "reverse_map",
                None
            )

        else:

            self.pipeline = data

            self.reverse_map = None

    def predict(self, text):

        prediction = self.pipeline.predict(
            [text]
        )[0]

        if self.reverse_map:

            return self.reverse_map[
                prediction
            ]

        return prediction