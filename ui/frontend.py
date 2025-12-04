import streamlit as st
import pandas as pd
import requests

# -------------------------------
# GLOBAL CONFIG (Dark Theme)
# -------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="wide"
)
st.experimental_set_query_params()
API_URL = "http://127.0.0.1:8000/predict"

# -------------------------------
# CUSTOM CSS
# -------------------------------
st.markdown(
    """
    <style>
        .main { background-color: #0e1117; }
        label, .st-emotion-cache-q8sbsg, .stSelectbox label {
            color: #e2e2e2 !important;
        }
        .stTextInput>div>div>input, 
        .stNumberInput>div>div>input,
        .stSelectbox>div>div>select {
            background-color: #1c1f26 !important;
            color: white !important;
        }
        .title { font-size: 28px; font-weight: 600; color: white; }
        .subheader { font-size: 20px; font-weight: 500; color: #c1c1c1; }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# HEADER
# -------------------------------
st.markdown("<div class='title'> Customer Churn Prediction</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Fill in customer details to predict churn probability</div>", unsafe_allow_html=True)
st.write("---")


# -------------------------------
# USER INPUT FORM
# -------------------------------
def user_input_features():

    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            CustomerID = st.number_input("Customer ID", key="customer_id", min_value=1000, step=1, value=1001)
            gender = st.selectbox("Gender", ['Male', 'Female'], index=0)
            SeniorCitizen = st.selectbox("Senior Citizen", [0, 1], index=0)
            Partner = st.selectbox("Partner", ['Yes', 'No'], index=1)
            Dependents = st.selectbox("Dependents", ['Yes', 'No'], index=1)
            tenure = st.number_input("Tenure (Months)", min_value=0, max_value=72, step=1, value=12)
            PhoneService = st.selectbox("Phone Service", ['Yes', 'No'], index=0)
        with col2:
            MultipleLines = st.selectbox("Multiple Lines", ['No', 'Yes', 'No phone service'], index=0)
            InternetService = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'], index=0)
            OnlineSecurity = st.selectbox("Online Security", ['No', 'Yes', 'No internet service'], index=0)
            OnlineBackup = st.selectbox("Online Backup", ['No', 'Yes', 'No internet service'], index=0)
            DeviceProtection = st.selectbox("Device Protection", ['No', 'Yes', 'No internet service'], index=0)
            TechSupport = st.selectbox("Tech Support", ['No', 'Yes', 'No internet service'], index=0)
        with col3:
            StreamingTV = st.selectbox("Streaming TV", ['No', 'Yes', 'No internet service'], index=0)
            StreamingMovies = st.selectbox("Streaming Movies", ['No', 'Yes', 'No internet service'], index=0)
            Contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'], index=0)
            PaperlessBilling = st.selectbox("Paperless Billing", ['Yes', 'No'], index=0)
            PaymentMethod = st.selectbox(
                "Payment Method",
                ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'],
                index=0
            )
            MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, step=0.1, value=70.5)
            total_charges = st.number_input("Total Charges", min_value=0.0, step=0.1, value=1000.0)

    data = {
        "CustomerID": CustomerID,
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "total_charges": total_charges
    }
    return data


# ---- GET INPUT ----
input_data = user_input_features()

# ---------- PREDICT BUTTON ----------
st.write("")
if st.button(" Predict Churn", use_container_width=True):

    with st.spinner("Predicting... Please wait "):
        try:
            response = requests.post(API_URL, json=input_data)
        except Exception as e:
            st.error(f" Connection Error: {e}")
            st.stop()

    if response.status_code == 200:
        result = response.json()

        st.success(f"###  Customer ID: `{result['CustomerID']}`")

        if result["Label"] == "Churn":
            st.error("###  Churn Prediction: **Churn **")
        else:
            st.success("###  Churn Prediction: **Not Churn**")

    else:
        st.error(f" Server Error: {response.text}")
