import streamlit as st
import joblib 
import numpy as np

model = joblib.load("house_price_predictor_model.pkl")
st.title("House Price Prediction App")

st.divider()

st.write("This app uses machine learining for predicting house prices with given features of the house. For using this app you can enter the inputs from this UI and them use predict button :")

st.divider()
bedrooms = st.number_input("Number of Bedrooms", min_value=0,value=0)
bathrooms = st.number_input("Number of Bathrooms", min_value=0,value=0)
living_area = st.number_input("Living Area (in sqft)", min_value=0,value=2000)
condition = st.number_input("Condition of the House", min_value=0,value=3)
number_of_schools = st.number_input("Number of Schools Nearby", min_value=0,value=0)

st.divider()

x =[[bedrooms, bathrooms, living_area, condition, number_of_schools]]

predict_button = st.button("Predict")

if predict_button:
    x_array = np.array(x)
    prediction= model.predict(x_array)

    st.write(f"The predicted price of the house is: {prediction[0]:,.2f} USD")
else:
    st.write("Please enter the features and click on the predict button to see the predicted price of the house.")