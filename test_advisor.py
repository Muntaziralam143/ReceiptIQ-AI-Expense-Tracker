from src.recommendation.advisor import FinancialAdvisor

advisor = FinancialAdvisor()

recommendations = (
    advisor.generate_recommendations(
        food_growth=35,
        shopping_growth=42,
        transport_growth=-10
    )
)

print("\nRECOMMENDATIONS\n")

for item in recommendations:
    print("-", item)