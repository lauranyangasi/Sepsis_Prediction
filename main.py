from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import List



# Load the pipeline and encoder
pipeline = joblib.load('./Model/pipeline.joblib')

encoder = joblib.load('./Model/encoder.joblib')

app = FastAPI(title="Sepsis Analysis API")

class SepsisFeatures(BaseModel):
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    
training_data = pd.read_csv('./Paitients_Files_Train.csv')  # Replace with the actual path to your training data
encoder.fit(training_data['Sepsis'])

@app.get('/')
def home():
    return "Sepsis Analysis"

@app.get('/info')
def appinfo():
    return 'Sepsis Analysis API'


@app.post('/predict_sepsis')
def predict_sepsis(sepsis_features: SepsisFeatures):

    df = pd.DataFrame([sepsis_features.model_dump()])

    prediction = pipeline.predict(df)

    encoder_prediction = encoder.inverse_transform([prediction])[0]

    return {'prediction' : encoder_prediction}

