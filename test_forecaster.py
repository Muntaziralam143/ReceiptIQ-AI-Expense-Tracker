
from src.models.forecaster import SpendingForecaster

forecaster = SpendingForecaster()

forecaster.train(
    "data/raw/monthly_spending.csv"
)

prediction = forecaster.predict_next_month()

print("\nNEXT MONTH FORECAST\n")

print(
    f"Predicted Spending: ₹{prediction}"
)

