# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    BMI: float
    Smoking: int
    AlcoholDrinking: int
    Stroke: int
    PhysicalHealth: float
    MentalHealth: float
    DiffWalking: int
    Sex: int
    AgeCategory: int
    Race: int
    Diabetic: int
    PhysicalActivity: int
    GenHealth: int
    SleepTime: float
    Asthma: int
    KidneyDisease: int
    SkinCancer: int