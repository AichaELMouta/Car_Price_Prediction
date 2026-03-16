# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:41:59 2026

@author: ELITEBOOK
"""

# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import streamlit as st
import pandas as pd
import joblib
import numpy as np

#Load trained model
best_gbr = joblib.load("car_price_selling.pkl")
st.title("Predict car price")
st.write("Enter car details to predict the selling price.")
present_price = st.number_input("Present Price", min_value = 0.0)
age = st.number_input("Car Age", min_value = 0)
kms_driven = st.number_input("Kilometers Driven", min_value = 0)

fuel_type = st.selectbox(
    "Fuel type",
    ["Petrol", "Diesel", "CNG"]
    )

seller_type = st.selectbox(
    "seller type",
    ["Dealer", "Individual"]
    )

transmission = st.selectbox(
    "transmission",
    ["Manual", "Automatic"]
    )
owner = st.selectbox(
    "Number of Previous Owners",
    [0,1,2,3]
)

#Feature engineering

log_age = np.log(age)
log_kms_driven = np.log(kms_driven)

fuel_type = {"Petrol":0, "Diesel":1, "CNG":2}[fuel_type]
seller_type = {"Dealer":0, "Individual":1}[seller_type]
transmission = {"Manual":0, "Automatic":1}[transmission]

#Create dataframe
input_data = pd.DataFrame({
     "Present_Price":[present_price],
     "Fuel_Type":[fuel_type],
     "Seller_Type":[seller_type],
     "Transmission":[transmission],
     "Owner":[owner],
     "Log_Age":[np.log(age)],
     "Log_Kms_Driven":[np.log(kms_driven)]

     })
 
 #Prediction
input_data = pd.DataFrame([[present_price, fuel_type, seller_type,
                            transmission, owner, log_age, log_kms_driven]],
                          columns=['Present_Price','Fuel_Type','Seller_Type',
                                   'Transmission','Owner','Log_Age','Log_Kms_Driven'])
if st.button("Predict Price"):
     prediction = best_gbr.predict(input_data)[0]

     st.success(f"Estimated Selling Price: {prediction:.2f}")
