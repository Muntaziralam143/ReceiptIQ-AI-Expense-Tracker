
import re


class EntityExtractor:

    def extract_merchant(self, text):

        lines = text.split("\n")

        for line in lines:

            line = line.strip()

            if (
                len(line) > 3
                and not any(c.isdigit() for c in line)
                and "cashier" not in line.lower()
                and "server" not in line.lower()
                and "subtotal" not in line.lower()
                and "total" not in line.lower()
                and "tax" not in line.lower()
            ):

                return line

        return "Unknown"

    def extract_amount(self, text):

        # Try Total Amount First
        total_match = re.search(
            r"total\s*[\:\-]?\s*([\d,]+)",
            text,
            re.IGNORECASE
        )

        if total_match:

            try:

                return int(
                    total_match.group(1).replace(",", "")
                )

            except:
                pass

        amounts = re.findall(
            r"[\d,]+",
            text
        )

        cleaned = []

        for amount in amounts:

            try:

                value = int(
                    amount.replace(",", "")
                )

                if value > 100:

                    cleaned.append(value)

            except:
                pass

        if not cleaned:

            return None

        return max(cleaned)

    def extract_date(self, text):

        patterns = [

            r"[A-Za-z]{3}\s+\d{1,2},\s+\d{4}",

            r"\d{1,2}[/-]\d{1,2}[/-]\d{2,4}",

            r"\d{1,2}\s*,\s*\d{4}"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:

                return match.group()

        return "Not Found"

    def extract_item_count(self, text):

        patterns = [

            r"total\s*item\s*[:\-]?\s*(\d+)",

            r"total\s*qty\s*[:\-]?\s*(\d+)",

            r"qty\s*[:\-]?\s*(\d+)",

            r"pax\s*[:\-]?\s*(\d+)"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:

                return int(
                    match.group(1)
                )

        return "-"

    def extract_category(self, text):

        food_keywords = [
            "sushi",
            "ramen",
            "salmon",
            "katsu",
            "teriyaki",
            "pizza",
            "burger",
            "coffee",
            "chicken",
            "paneer",
            "mojito"
        ]

        shopping_keywords = [
            "amazon",
            "flipkart",
            "shopping"
        ]

        transport_keywords = [
            "uber",
            "ola",
            "taxi",
            "fuel"
        ]

        text = text.lower()

        for word in food_keywords:

            if word in text:
                return "Food"

        for word in shopping_keywords:

            if word in text:
                return "Shopping"

        for word in transport_keywords:

            if word in text:
                return "Transport"

        return "Unknown"

    def extract(self, text):

        return {

            "merchant":
            self.extract_merchant(text),

            "amount":
            self.extract_amount(text),

            "date":
            self.extract_date(text),

            "items":
            self.extract_item_count(text),

            "category":
            self.extract_category(text)
        }

