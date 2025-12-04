from pydantic import BaseModel

class PredictionOut(BaseModel):
    id: int
    customer_id: str
    label: str

    class Config:
        from_attributes = True
class UserDataOut(BaseModel):
    CustomerID: str
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    total_charges: float

    class Config:
        from_attributes = True
