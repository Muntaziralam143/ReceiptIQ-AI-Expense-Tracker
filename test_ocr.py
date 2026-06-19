from src.ocr.easyocr_processor import ReceiptOCR

ocr = ReceiptOCR()

text = ocr.extract_text(
    "sample_receipt.jpg"
)

print(text)
