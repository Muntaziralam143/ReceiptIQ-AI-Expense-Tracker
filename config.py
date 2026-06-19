import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RAW_DATA = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DATA = os.path.join(BASE_DIR, "data", "processed")

MODEL_DIR = os.path.join(BASE_DIR, "saved_models")

CLASSIFIER_MODEL = os.path.join(
    MODEL_DIR,
    "expense_classifier.pkl"
)

FORECAST_MODEL = os.path.join(
    MODEL_DIR,
    "forecast_model.pkl"
)

ANOMALY_MODEL = os.path.join(
    MODEL_DIR,
    "anomaly_model.pkl"
)