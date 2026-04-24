import streamlit as st
import joblib 
import numpy as np

model = joblib.load("house_price_predictor_model.pkl")
st.title("House Price Prediction App")

st.divider()

st.write("This app uses machine learining for predicting house prices with given features of the house. For using this app you can enter the inputs from this UI and them use predict button :")

st.divider()
living_area = st.number_input("Living Area (in sqft)", min_value=0,value=2000)
grade_of_the_house = st.number_input("Grade of the House", min_value=0,value=3)
Area_of_the_house = st.number_input("Area of the House (in sqft)", min_value=0,value=2000)
living_area_renov = st.number_input("Living Area (in sqft) - Renovated", min_value=0,value=0)
bathrooms = st.number_input("Number of Bathrooms", min_value=0,value=0)

st.divider()

x =[[living_area, grade_of_the_house, Area_of_the_house, living_area_renov, bathrooms]]

predict_button = st.button("Predict")

if predict_button:
    x_array = np.array(x)
    prediction= model.predict(x_array)

    st.write(f"The predicted price of the house is: {prediction[0]:,.2f} USD")
else:
    st.write("Please enter the features and click on the predict button to see the predicted price of the house.")

