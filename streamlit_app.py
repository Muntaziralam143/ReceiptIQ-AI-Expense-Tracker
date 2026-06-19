
import streamlit as st
import pandas as pd
import os

from src.nlp.entity_extractor import EntityExtractor
from src.models.classifier import ExpenseClassifier
from src.models.anomaly_detector import ExpenseAnomalyDetector
from src.ocr.easyocr_processor import OCRProcessor

st.set_page_config(
    page_title="AI Financial Intelligence",
    layout="wide"
)

st.title("💰 AI Financial Intelligence System")

st.write(
    "OCR, Expense Classification and Receipt Analytics"
)

# ==================================================
# RECEIPT DASHBOARD
# ==================================================

st.header("📊 Receipt Dashboard")

if os.path.exists("data/receipts.csv"):

    history = pd.read_csv("data/receipts.csv")

    if not history.empty:

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Receipts",
                len(history)
            )

        with col2:
            st.metric(
                "Total Spending",
                f"₹{history['amount'].sum():,.0f}"
            )

        with col3:
            st.metric(
                "Average Bill",
                f"₹{history['amount'].mean():,.0f}"
            )

        st.dataframe(history)

# ==================================================
# OCR SECTION
# ==================================================

st.header("📄 Upload Receipt")

uploaded_file = st.file_uploader(
    "Upload Receipt",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    with open(
        "temp_receipt.jpg",
        "wb"
    ) as f:

        f.write(
            uploaded_file.getbuffer()
        )

    try:

        ocr = OCRProcessor()

        ocr_text = ocr.extract_text(
            "temp_receipt.jpg"
        )

        extractor = EntityExtractor()

        data = extractor.extract(
            ocr_text
        )

        classifier = ExpenseClassifier()

        classifier.load()

        category = classifier.predict(
            ocr_text
        )

        st.subheader(
            "📋 Receipt Analysis"
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "Merchant",
                data.get(
                    "merchant",
                    "Unknown"
                )
            )

        with c2:
            st.metric(
                "Amount",
                data.get(
                    "amount",
                    0
                )
            )

        with c3:
            st.metric(
                "Date",
                data.get(
                    "date",
                    "-"
                )
            )

        with c4:
            st.metric(
                "Items",
                data.get(
                    "items",
                    "-"
                )
            )

        st.success(
            f"Category: {category}"
        )

        receipt_row = pd.DataFrame([{
            "merchant": data.get("merchant"),
            "amount": data.get("amount"),
            "date": data.get("date"),
            "category": category
        }])

        if os.path.exists(
            "data/receipts.csv"
        ):

            old = pd.read_csv(
                "data/receipts.csv"
            )

            old = pd.concat(
                [old, receipt_row],
                ignore_index=True
            )

            old.to_csv(
                "data/receipts.csv",
                index=False
            )

        else:

            receipt_row.to_csv(
                "data/receipts.csv",
                index=False
            )

        with st.expander(
            "View OCR Text"
        ):

            st.text_area(
                "OCR Text",
                ocr_text,
                height=200
            )

    except Exception as e:

        st.error(
            str(e)
        )

# ==================================================
# ANOMALY DETECTION
# ==================================================

st.header("🚨 Anomaly Detection")

amount = st.number_input(
    "Enter Amount",
    min_value=0.0,
    value=1000.0
)

if st.button(
    "Check Transaction"
):

    detector = ExpenseAnomalyDetector()

    detector.train(
        [
            500,
            700,
            800,
            1200,
            650,
            900,
            1100,
            1400,
            750,
            1000
        ]
    )

    result = detector.detect(
        amount
    )

    st.write(result)

st.markdown("---")

st.caption(
    "Built by Muntazir Alam"
)

