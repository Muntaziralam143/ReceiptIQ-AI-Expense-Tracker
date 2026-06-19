import pandas as pd
import random

food = [
    ("Starbucks", "Coffee purchase"),
    ("Dominos", "Pizza order"),
    ("Zomato", "Food delivery"),
    ("Swiggy", "Lunch order"),
    ("KFC", "Chicken meal")
]

transport = [
    ("Uber", "Airport ride"),
    ("Ola", "City travel"),
    ("Metro", "Metro ticket"),
    ("Rapido", "Bike ride")
]

shopping = [
    ("Amazon", "Electronics purchase"),
    ("Flipkart", "Online shopping"),
    ("Myntra", "Clothing order"),
    ("Ajio", "Fashion shopping")
]

entertainment = [
    ("Netflix", "Monthly subscription"),
    ("Spotify", "Music subscription"),
    ("BookMyShow", "Movie ticket")
]

categories = {
    "Food": food,
    "Transport": transport,
    "Shopping": shopping,
    "Entertainment": entertainment
}

rows = []

for _ in range(1000):

    category = random.choice(
        list(categories.keys())
    )

    merchant, description = random.choice(
        categories[category]
    )

    amount = random.randint(100, 5000)

    rows.append(
        [
            merchant,
            description,
            amount,
            category
        ]
    )

df = pd.DataFrame(
    rows,
    columns=[
        "merchant",
        "description",
        "amount",
        "category"
    ]
)

df.to_csv(
    "data/raw/expenses_large.csv",
    index=False
)

print(df.head())
print("Rows:", len(df))