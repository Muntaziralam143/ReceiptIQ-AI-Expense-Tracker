class FinancialAdvisor:

    def generate_recommendations(
        self,
        food_growth,
        shopping_growth,
        transport_growth
    ):

        recommendations = []

        if food_growth > 20:

            recommendations.append(
                "Food spending increased significantly. "
                "Reducing restaurant visits may save money."
            )

        if shopping_growth > 20:

            recommendations.append(
                "Shopping expenses are rising. "
                "Consider setting a monthly budget."
            )

        if transport_growth < 0:

            recommendations.append(
                "Transport spending decreased. "
                "Good job maintaining lower travel costs."
            )

        if not recommendations:

            recommendations.append(
                "Spending patterns appear stable."
            )

        return recommendations