from fastapi import FastAPI

from src.models.forecaster import SpendingForecaster
from src.models.anomaly_detector import (
    ExpenseAnomalyDetector
)
from src.recommendation.advisor import (
    FinancialAdvisor
)
from src.models.classifier import ExpenseClassifier

app = FastAPI(
    title="AI Financial Intelligence API"
)


@app.get("/")
def home():

    return {
        "message": "AI Financial Intelligence System"
    }


@app.get("/health")
def health():

    return {
        "status": "running"
    }


@app.get("/forecast")
def forecast():

    forecaster = SpendingForecaster()

    forecaster.train(
        "data/raw/monthly_spending.csv"
    )

    prediction = (
        forecaster.predict_next_month()
    )

    return {
        "predicted_spending": prediction
    }


@app.get("/anomaly")
def anomaly(amount: float):

    detector = ExpenseAnomalyDetector()

    historical_expenses = [
        500,
        700,
        800,
        1200,
        650,
        900,
        1100,
        1400,
        750,
        1000
    ]

    detector.train(
        historical_expenses
    )

    result = detector.detect(
        amount
    )

    return {
        "amount": amount,
        "result": result
    }

@app.get("/recommend")
def recommend(

    food_growth: float,
    shopping_growth: float,
    transport_growth: float

):

    advisor = FinancialAdvisor()

    recommendations = (
        advisor.generate_recommendations(
            food_growth=food_growth,
            shopping_growth=shopping_growth,
            transport_growth=transport_growth
        )
    )

    return {
        "recommendations": recommendations
    }
@app.get("/classify")
def classify(text: str):

    classifier = ExpenseClassifier()

    classifier.load()

    category = classifier.predict(
        text
    )

    return {
        "text": text,
        "category": category
    }