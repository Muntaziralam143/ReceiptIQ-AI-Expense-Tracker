from src.models.anomaly_detector import (
    ExpenseAnomalyDetector
)

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

print(
    detector.detect(850)
)

print(
    detector.detect(25000)
)