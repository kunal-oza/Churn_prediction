📘 Customer Churn Prediction System

Machine Learning + FastAPI API + Streamlit UI + Supabase PostgreSQL + Docker

🚀 Overview

This project is a complete end-to-end churn prediction platform, combining:

Machine Learning Model (Logistic Regression + ColumnTransformer pipeline)

FastAPI Backend for prediction & data storage

Supabase PostgreSQL Database with connected tables

Streamlit Frontend for user input & results

Docker for deployment

The system:

Accepts customer information

Saves customer data in UserData table

Runs churn prediction

Stores prediction in Prediction table

Returns results to Streamlit instant UI

🗄️ Database Integration (Supabase)

The system now uses Supabase PostgreSQL as the central database with two relational tables, fully connected.

📌 1. UserData Table

Stores all customer profile information.

Column	Type	Description
CustomerID	String (PK)	Unique customer identifier
gender	String	Male / Female
SeniorCitizen	Integer	0 or 1
Partner	String	Yes / No
Dependents	String	Yes / No
tenure	Integer	Months with company
PhoneService	String	Yes / No
...	...	All remaining churn-related fields

SQLAlchemy model:

class UserData(Base):
    __tablename__ = "UserData"
    CustomerID = Column(String, primary_key=True, index=True)
    gender = Column(String)
    SeniorCitizen = Column(Integer)
    Partner = Column(String)
    Dependents = Column(String)
    tenure = Column(Integer)
    PhoneService = Column(String)
    MultipleLines = Column(String)
    InternetService = Column(String)
    OnlineSecurity = Column(String)
    OnlineBackup = Column(String)
    DeviceProtection = Column(String)
    TechSupport = Column(String)
    StreamingTV = Column(String)
    StreamingMovies = Column(String)
    Contract = Column(String)
    PaperlessBilling = Column(String)
    PaymentMethod = Column(String)
    MonthlyCharges = Column(Float)
    total_charges = Column(Float)

    # Relationship to predictions
    predictions = relationship("Prediction", back_populates="user")

📌 2. Prediction Table

Stores the churn prediction result for each customer.

Column	Type	Description
id	Integer (PK)	Auto-increment
customer_id	String (FK → UserData.CustomerID)	Linked customer
label	String	Churn / Not Churn

SQLAlchemy model:

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String, ForeignKey("UserData.CustomerID"))
    label = Column(String)

    # Relationship link to customer
    user = relationship("UserData", back_populates="predictions")

🔗 Database Relationship
UserData.CustomerID   1  ─────────>  many  Prediction.customer_id


This means:

Each customer can have multiple predictions

Each prediction is tied to only one customer

⚙️ FastAPI Workflow (Updated)
✔ 1. Receive input

FastAPI receives customer info validated by Pydantic.

✔ 2. Save / Update UserData

If the customer exists → update row
If new → insert row

✔ 3. Run ML Model

Prediction is generated using the pre-trained Scikit model.

✔ 4. Save prediction

Result is stored in predictions table with FK.

✔ 5. Respond to Streamlit

Response contains:

{
  "CustomerID": 1001,
  "Label": "Churn",
}

🖥️ Project Structure
│   Dockerfile
│   main.py
│   .env
│   requirements.txt
│   __init__.py
│   .env   ← Supabase DATABASE_URL stored here
│
├── model
│     ├── logistic_regression_model.pkl
│     └── model_loading.py
│
├── preprocessing
│     └── pydentic.py
│
├── ui
│     └── frontend.py  (Streamlit UI)
│
└── database
      ├── db.py        (SQLAlchemy engine + Supabase connection)
      ├── models.py    (UserData + Prediction)
      └── __init__.py

🔧 Local Setup
1️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Start FastAPI
uvicorn main:app --reload

4️⃣ Start Streamlit
streamlit run ui/frontend.py

🐳 Docker Deployment
Build image:
docker build -t churn-app .

Run container:
docker run -p 8000:8000 -p 8501:8501 \
  --env-file .env \
  --name churn-container churn-app


.env contains:

DATABASE_URL=postgresql+psycopg2://postgres:PASSWORD@db.xyz.supabase.co:5432/postgres

📡 API Example
Request
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

Response
{
  "CustomerID": 1002,
  "Label": "Churn",
}

🎨 Key Features

✔ Linked database tables (UserData ↔ Prediction)
✔ FastAPI backend with validation & DB persistence
✔ Streamlit modern frontend UI
✔ ML model loading + preprocessing
✔ Dockerized for easy deployment
✔ Production-grade PostgreSQL using Supabase

🚀 Future Enhancements

Add prediction probability

Add timestamps

Add user history endpoint

Display predictions history in Streamlit

Admin dashboard

Batch CSV prediction

🏁 Final Notes

Your application is now fully integrated with Supabase PostgreSQL, with:

Clean relational structure

Primary → Foreign key mapping

Consistent FastAPI transaction flow

ML + UI + API + DB working end-to-end