# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import joblib
import pandas as pd


# 2. Create the app object
app = FastAPI()
pickle_in = open("logistic_regression_model.pkl","rb")
# Chargement du modèle avec joblib
classifier = joblib.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere


# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.get('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    BMI = data['BMI']
    Smoking = data['Smoking']
    AlcoholDrinking = data['AlcoholDrinking']
    Stroke = data['Stroke']
    PhysicalHealth = data['PhysicalHealth']
    MentalHealth = data['MentalHealth']
    DiffWalking = data['DiffWalking']
    Sex = data['Sex']
    AgeCategory = data['AgeCategory']
    Race = data['Race']
    Diabetic = data['Diabetic']
    PhysicalActivity = data['PhysicalActivity']
    GenHealth = data['GenHealth']
    SleepTime = data['SleepTime']
    Asthma = data['Asthma']
    KidneyDisease = data['KidneyDisease']
    SkinCancer = data['SkinCancer']

    # Préparez les données dans le format attendu par le modèle
    prediction = classifier.predict([[BMI, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth,
                 DiffWalking, Sex, AgeCategory, Race, Diabetic, PhysicalActivity,
                 GenHealth, SleepTime, Asthma, KidneyDisease, SkinCancer]])
    if(prediction[0]>0.5):
        prediction="Malade"
    else:
        prediction="Non malade"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload