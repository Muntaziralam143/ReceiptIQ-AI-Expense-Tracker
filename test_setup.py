from src.utils.data_loader import load_expense_data


df = load_expense_data(
    "data/raw/expenses.csv"
)

print(df.head())
print(df.shape)