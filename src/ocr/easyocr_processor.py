import easyocr


class OCRProcessor:

    def __init__(self):

        self.reader = easyocr.Reader(
            ['en'],
            gpu=False
        )

    def extract_text(self, image_path):

        result = self.reader.readtext(
            image_path
        )

        text = "\n".join(
            [item[1] for item in result]
        )

        return text