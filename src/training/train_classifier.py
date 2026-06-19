import pandas as pd

from src.models.classifier import ExpenseClassifier


df = pd.read_csv(
    "data/raw/expenses_large.csv"
)

classifier = ExpenseClassifier()

classifier.train(df)

classifier.save()