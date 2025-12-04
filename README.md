```markdown
# 📘 Customer Churn Prediction System

Machine Learning + FastAPI backend + Streamlit UI + Supabase (Postgres) + Docker

---

## 🚀 Overview

An end-to-end churn prediction platform that accepts customer information, persists it to a Supabase PostgreSQL database, runs a pre-trained ML model to predict churn, stores the prediction, and returns results to a Streamlit frontend.

Key components:
- Scikit-learn model (Logistic Regression + ColumnTransformer pipeline)
- FastAPI backend (prediction + data storage)
- Supabase PostgreSQL (UserData and Prediction tables)
- Streamlit frontend (user input & results)
- Docker for deployment

---

## Table of Contents

- [Architecture](#architecture)
- [Database Schema](#database-schema)
- [FastAPI Workflow](#fastapi-workflow)
- [API Example](#api-example)
- [Project Structure](#project-structure)
- [Local Setup](#local-setup)
- [Docker Deployment](#docker-deployment)
- [Environment](#environment)
- [Future Enhancements](#future-enhancements)
- [Notes](#notes)

---

## Architecture

User submits customer info via the Streamlit UI → FastAPI validates and upserts UserData → ML model runs prediction → Prediction saved to DB (FK to UserData) → Result returned to UI.

ASCII relationship:
```
UserData.CustomerID   1  ─────────>  many  Prediction.customer_id
```

---

## Database Schema

Two main tables in Supabase Postgres.

### 1) UserData (stores customer profile)
| Column | Type | Description |
|---|---:|---|
| CustomerID | String (PK) | Unique customer identifier |
| gender | String | Male / Female |
| SeniorCitizen | Integer | 0 or 1 |
| Partner | String | Yes / No |
| Dependents | String | Yes / No |
| tenure | Integer | Months with company |
| PhoneService | String | Yes / No |
| MultipleLines | String | ... |
| InternetService | String | ... |
| OnlineSecurity | String | ... |
| OnlineBackup | String | ... |
| DeviceProtection | String | ... |
| TechSupport | String | ... |
| StreamingTV | String | ... |
| StreamingMovies | String | ... |
| Contract | String | ... |
| PaperlessBilling | String | ... |
| PaymentMethod | String | ... |
| MonthlyCharges | Float | Monthly charge amount |
| total_charges | Float | Total charges to date |

SQLAlchemy model (example)
```py
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
```

### 2) Prediction (stores model outputs)
| Column | Type | Description |
|---|---:|---|
| id | Integer (PK) | Auto-increment |
| customer_id | String (FK → UserData.CustomerID) | Linked customer |
| label | String | "Churn" / "Not Churn" |

SQLAlchemy model (example)
```py
class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String, ForeignKey("UserData.CustomerID"))
    label = Column(String)

    # Relationship link to customer
    user = relationship("UserData", back_populates="predictions")
```

---

## FastAPI Workflow (summary)

1. Receive input via POST (Pydantic validation).
2. Upsert UserData row (update if exists, insert if new).
3. Load preprocessing pipeline + model and generate prediction.
4. Save prediction row (with FK to user).
5. Return JSON response to frontend.

Example Response:
```json
{
  "CustomerID": 1001,
  "Label": "Churn"
}
```

---

## API Example (request)

Request body (JSON):
```json
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

Response:
```json
{
  "CustomerID": 1002,
  "Label": "Churn"
}
```

---

## Project Structure
```
.
├── Dockerfile
├── main.py                # FastAPI app
├── requirements.txt
├── .env                   # DATABASE_URL (Supabase)
├── model
│   ├── logistic_regression_model.pkl
│   └── model_loading.py
├── preprocessing
│   └── pydentic.py
├── ui
│   └── frontend.py        # Streamlit UI
└── database
    ├── db.py              # SQLAlchemy engine + Supabase connection
    ├── models.py          # UserData + Prediction models
    └── __init__.py
```

---

## Local Setup

1. Create and activate venv
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Start FastAPI (development)
```bash
uvicorn main:app --reload
```

4. Start Streamlit UI
```bash
streamlit run ui/frontend.py
```

---

## Docker Deployment

Build:
```bash
docker build -t churn-app .
```

Run:
```bash
docker run -p 8000:8000 -p 8501:8501 \
  --env-file .env \
  --name churn-container churn-app
```

---

## Environment (.env example)

Store your Supabase/DB connection here:
```
DATABASE_URL=postgresql+psycopg2://postgres:PASSWORD@db.xyz.supabase.co:5432/postgres
```

Ensure this file is excluded from source control (add to .gitignore).

---

## Key Features

- Linked relational DB tables (UserData ↔ Prediction)
- FastAPI backend with Pydantic validation and DB persistence
- Streamlit frontend for interactive predictions
- ML model loading + preprocessing pipeline
- Dockerized for easy deployment
- Production-grade PostgreSQL using Supabase

---

## Future Enhancements

- Return prediction probability (confidence)
- Add timestamps to records (created_at, updated_at)
- Expose user history endpoints (list predictions per user)
- Display prediction history in Streamlit
- Admin dashboard
- Batch CSV prediction endpoint

---

## Notes

- The repository currently uses a logistic regression model saved in `model/logistic_regression_model.pkl`.
- Database models and example schemas are under `database/models.py`.
- Make sure `DATABASE_URL` is set correctly in `.env` before running the app.

---

Thank you — contributions, bug reports, and feature requests are welcome!
```
