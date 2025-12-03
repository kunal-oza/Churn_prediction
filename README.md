# 📘 **Customer Churn Prediction App**

Machine Learning + FastAPI + Streamlit + Docker

## 🚀 **Overview**

This project is a full-stack **Customer Churn Prediction System** built
using:

-   **Machine Learning (Scikit-Learn)**
-   **FastAPI backend for serving predictions**
-   **Streamlit frontend for interactive UI**
-   **Docker for deployment**
-   Logistic Regression model pipeline with preprocessing using
    ColumnTransformer

The application takes customer details and predicts whether the customer
is likely to **churn** or **stay**.

## 📂 **Project Structure**

│   Dockerfile
│   main.py
│   requirements.txt
│   __init__.py
│
├───model
│       logistic_regression_model.pkl
│       model_loading.py
│       __init__.py
│
├───preprocessing
│       pydentic.py
│       __init__.py
│
└───ui
        frontend.py
        __init__.py

## ⚙️ **How It Works**

### 🔹 **1. Streamlit Frontend**

-   User enters customer details.
-   Streamlit sends JSON payload to FastAPI API.
-   Receives churn prediction and displays result beautifully.

### 🔹 **2. FastAPI Backend**

-   Validates the request using Pydantic schemas.
-   Preprocesses input according to model's expected features.
-   Predicts using the trained ML model pipeline.
-   Returns prediction results.

### 🔹 **3. Machine Learning Model**

-   Logistic Regression
-   ColumnTransformer-based preprocessing
-   Expects exact feature names

## 🔧 **Installation (Local Setup)**

### 1️⃣ Create Virtual Environment

``` bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 3️⃣ Start FastAPI

``` bash
uvicorn main:app --reload
```

### 4️⃣ Start Streamlit

``` bash
streamlit run frontend.py
```

## 🐳 **Run Using Docker**

### Build Image

``` bash
docker build -t churn-app .
```

### Run Container

``` bash
docker run -p 8000:8000 -p 8501:8501 --name churn-container churn-app
```

### Logs

``` bash
docker logs -f churn-container
```

## 📡 **API Usage Example**

### POST /predict

``` json
{
  "CustomerID": 1002,
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "No",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "DSL",
  "OnlineSecurity": "No",
  "OnlineBackup": "No",
  "DeviceProtection": "Yes",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 70.5,
  "total_charges": 1000.0
}
```

### Response

``` json
{
  "CustomerID": 1002,
  "Label": "Churn"
}
```

## 🎨 **Features**

✔ Professional UI\
✔ FastAPI async backend\
✔ ML model loaded efficiently\
✔ Strict Pydantic validation\
✔ Fully Dockerized\
✔ Instant churn prediction

## 📝 **Future Enhancements**

-   Probability score visualization\
-   Feature importance chart\
-   CSV upload for batch prediction\
-   PDF report generation

# Churn_prediction
