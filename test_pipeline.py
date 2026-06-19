from src.inference.predict_transaction import TransactionPredictor

predictor = TransactionPredictor()

result = predictor.predict(
    "sample_receipt.jpg"
)

print("\nRESULT\n")

for key, value in result.items():
    print(f"{key}: {value}")