from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal
from pathlib import Path
import pandas as pd
import joblib
 
app = FastAPI(title="PaySim Fraud Detection API")
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
 
BASE_DIR = Path(__file__).resolve().parent
 
model = joblib.load(BASE_DIR / "fraud_detection_model.pkl")
 
 
class Transaction(BaseModel):
    step: int = Field(ge=1)
    amount: float = Field(ge=0)
    oldbalanceOrg: float = Field(ge=0)
    newbalanceOrig: float = Field(ge=0)
    oldbalanceDest: float = Field(ge=0)
    newbalanceDest: float = Field(ge=0)
    type: Literal[
        "CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"
    ]
 
 
@app.get("/")
def home():
    return FileResponse(BASE_DIR / "index.html")
 
 
@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": True}
 
 
@app.post("/predict")
def predict(transaction: Transaction):
    data = pd.DataFrame([transaction.model_dump()])
 
    data = pd.get_dummies(data, columns=["type"], dtype=int)
 
    expected_columns = [
        "step", "amount", "oldbalanceOrg", "newbalanceOrig",
        "oldbalanceDest", "newbalanceDest",
        "type_CASH_IN", "type_CASH_OUT", "type_DEBIT",
        "type_PAYMENT", "type_TRANSFER"
    ]
 
    data = data.reindex(columns=expected_columns, fill_value=0)
 
    prediction = int(model.predict(data)[0])
    probability = float(model.predict_proba(data)[0][1])
 
    return {
        "prediction": prediction,
        "result": "Fraud" if prediction == 1 else "Legitimate",
        "fraud_probability": round(probability, 6)
    }