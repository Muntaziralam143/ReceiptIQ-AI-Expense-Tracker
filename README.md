## System Architecture

<div align="center">

<pre>
                Receipt Image
                       │
                       ▼
                   EasyOCR
                       │
                       ▼
               Entity Extraction
                       │
                       ▼
              Transaction Database
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼

 Expense         Forecasting      Anomaly
Classifier         Model         Detection
       │               │               │
       └───────┬───────┴───────┬───────┘
               ▼
      Recommendation Engine
               │
               ▼
        Financial Insights
</pre>

</div>

---

## Data Processing Pipeline

<div align="center">

<pre>
Receipt Image
    ↓
EasyOCR
    ↓
Text Cleanup
    ↓
Entity Extraction
    ↓
JSON Output
</pre>

</div>

Example Output:

```json
{
  "merchant": "ICHIBAN SUSHI",
  "amount": 223000,
  "date": "Aug 19, 2024",
  "items": 6,
  "category": "Food"
}
```

---

## Machine Learning Models

### Expense Classification

* Logistic Regression
* Random Forest
* XGBoost

### Forecasting

* Time Series Spending Forecast Model

### Anomaly Detection

* Transaction Outlier Detection

### Recommendation Engine

* Rule-Based Financial Advisor
* Expense Optimization Suggestions

---

## Features

✅ Receipt OCR using EasyOCR

✅ Merchant Extraction

✅ Amount Extraction

✅ Date Extraction

✅ Item Count Detection

✅ Expense Classification

✅ Spending Forecasting

✅ Anomaly Detection

✅ Financial Recommendation Engine

✅ Interactive Streamlit Dashboard

✅ Real-Time Receipt Analytics

---

## Screenshots

<table align="center">
<tr>
<td align="center">
<img src="assets/dashboard.png" width="450"/>
<br>
<b>Dashboard</b>
</td>

<td align="center">
<img src="assets/receipt_upload.png" width="450"/>
<br>
<b>Receipt Upload</b>
</td>
</tr>

<tr>
<td align="center">
<img src="assets/ocr_result.png" width="450"/>
<br>
<b>OCR Result</b>
</td>

<td align="center">
<img src="assets/expense_analysis.png" width="450"/>
<br>
<b>Expense Analysis</b>
</td>
</tr>
</table>

---

## Tech Stack

**Frontend**

* Streamlit
* Plotly

**Backend**

* Python

**Machine Learning**

* Scikit-Learn
* XGBoost

**Data Processing**

* Pandas
* NumPy

**OCR & NLP**

* EasyOCR
* Regex Based Entity Extraction

---

## Project Author

**Muntazir Alam**

B.Tech CSE | AI & Data Science Enthusiast

GitHub: https://github.com/Muntaziralam143
