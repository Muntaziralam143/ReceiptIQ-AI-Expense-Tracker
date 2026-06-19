import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

from xgboost import XGBClassifier

from config import CLASSIFIER_MODEL

# Load dataset
df = pd.read_csv("data/raw/expenses_large.csv")

# Features
X = df["merchant"] + " " + df["description"]
y = df["category"]

# Encode target
label_map = {
    "Food": 0,
    "Transport": 1,
    "Shopping": 2,
    "Entertainment": 3
}

reverse_map = {v: k for k, v in label_map.items()}

y = y.map(label_map)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),

    "RandomForest": RandomForestClassifier(
        n_estimators=200,
        random_state=42
    ),

    "XGBoost": XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        eval_metric="mlogloss"
    )
}

best_score = 0
best_pipeline = None
best_model_name = None

for name, model in models.items():

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("model", model)
    ])

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    score = accuracy_score(
        y_test,
        predictions
    )

    print(f"{name}: {score:.4f}")

    if score > best_score:
        best_score = score
        best_pipeline = pipeline
        best_model_name = name

joblib.dump(
    {
        "pipeline": best_pipeline,
        "reverse_map": reverse_map
    },
    CLASSIFIER_MODEL
)

print("\nBest Model:", best_model_name)
print("Best Accuracy:", best_score)