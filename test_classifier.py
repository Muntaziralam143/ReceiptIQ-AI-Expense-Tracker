from src.models.classifier import ExpenseClassifier

classifier = ExpenseClassifier()

classifier.load()

samples = [
    "Amazon electronics purchase",
    "Uber airport ride",
    "Starbucks coffee",
    "Netflix monthly subscription"
]

for item in samples:
    prediction = classifier.predict(item)
    print(f"{item} --> {prediction}")