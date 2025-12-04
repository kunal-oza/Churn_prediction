from model.model_loading import predict
from fastapi import FastAPI,HTTPException, Depends
from fastapi.responses import JSONResponse
import pandas as pd
from preprocessing.pydentic import InputData
import traceback
from database_folder.db import get_db, engine, Base
from sqlalchemy.orm import Session
from database_folder.table_model import Prediction, UserData



app = FastAPI()
@app.on_event("startup")
def on_startup():

    # Create database tables
    Base.metadata.create_all(bind=engine)
@app.get('/')
def read_root():
    return {"message":"Welcome to Customer Churn Prediction API"}
@app.get('/health')
def health_check(): 
    return {"status":"OK"}
@app.post("/predict")
def get_prediction(data: InputData, db: Session = Depends(get_db)):

    input_data = data.model_dump(exclude={'CustomerID'})
    input_df = pd.DataFrame([input_data])
    user_record = db.query(UserData).filter(
        UserData.CustomerID == str(data.CustomerID)
    ).first()

    if user_record:
        for key, value in input_data.items():
            setattr(user_record, key, value)
    else:
        user_record = UserData(
            CustomerID=str(data.CustomerID),
            **input_data
        )
        db.add(user_record)
    db.commit()
    db.refresh(user_record)
    try:
        result = predict(input_df)[0]
    except Exception as e:
        db.rollback()
        print("=== ERROR IN PREDICT FUNCTION ===")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
    label_map = {0: "Not Churn", 1: "Churn"}
    label = label_map[result]

    prediction_record = Prediction(
        customer_id=str(data.CustomerID),
        label=label,
    )
    db.add(prediction_record)
    db.commit()
    db.refresh(prediction_record)

    return {
        "CustomerID": data.CustomerID,
        "Label": label,
    }
