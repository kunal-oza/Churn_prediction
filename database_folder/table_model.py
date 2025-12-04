from sqlalchemy import Column, Integer, String, Float,ForeignKey
from sqlalchemy.orm import relationship
from database_folder.db import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String, ForeignKey("UserData.CustomerID"), index=True)
    label = Column(String) 
    user = relationship("UserData", back_populates="predictions")

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
    predictions = relationship("Prediction", back_populates="user")