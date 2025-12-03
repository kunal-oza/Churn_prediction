from model.model_loading import predict
from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from preprocessing.pydentic import InputData
import traceback

app = FastAPI()

@app.get('/')
def read_root():
    return {"message":"Welcome to Customer Churn Prediction API"}
@app.get('/health')
def health_check(): 
    return {"status":"OK"}
@app.post("/predict")
def get_prediction(data: InputData):
    input_data = data.model_dump(exclude={'CustomerID'})
    input_df = pd.DataFrame([input_data])
    try:
        result = predict(input_df)[0] 
    except Exception as e:
        print("=== ERROR IN PREDICT FUNCTION ===")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

    label = {0: "Not Churn", 1: "Churn"}

    return JSONResponse(
        content={
            "CustomerID": data.CustomerID,
            "Label": label[result]
        }, status_code=200
    )
    