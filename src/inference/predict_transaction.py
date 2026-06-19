from src.ocr.easyocr_processor import ReceiptOCR
from src.nlp.entity_extractor import EntityExtractor
from src.models.classifier import ExpenseClassifier


class TransactionPredictor:

    def __init__(self):

        self.ocr = ReceiptOCR()

        self.extractor = EntityExtractor()

        self.classifier = ExpenseClassifier()

        self.classifier.load()

    def predict(self, image_path):

        text = self.ocr.extract_text(image_path)

        extracted = self.extractor.extract(text)

        category = self.classifier.predict(text)

        return {
            "ocr_text": text,
            "merchant": extracted["merchant"],
            "amount": extracted["amount"],
            "predicted_category": category
        }