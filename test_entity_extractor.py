from src.ocr.easyocr_processor import ReceiptOCR
from src.nlp.entity_extractor import EntityExtractor


ocr = ReceiptOCR()

text = ocr.extract_text(
    "sample_receipt.jpg"
)

extractor = EntityExtractor()

result = extractor.extract(text)

print("\nOCR TEXT:\n")
print(text)

print("\nEXTRACTED DATA:\n")
print(result)