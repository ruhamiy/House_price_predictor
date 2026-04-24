# House Price Predictor

A machine learning web app built with **Streamlit** that predicts house prices based on key features such as living area, grade of the house, number of bathrooms, and more.

---

## Live Demo
Try the app here: [House Price Predictor](https://house-price-predictor-0.streamlit.app/)

---

## Project Structure
- `app.py` → Streamlit app script
- `house_price_predictor_model.pkl` → Trained regression model
- `requirements.txt` → Dependencies for deployment
- `House Price India.csv` → Dataset used for training
- `Notebook.ipynb` → Model training and experimentation

---

## Features
- Interactive UI for entering house details
- Predicts estimated house price in USD
- Displays results in a clean, user-friendly format

---

##  Tech Stack
- **Python**
- **Streamlit** (frontend + deployment)
- **scikit-learn** (model training)
- **pandas / numpy** (data handling)
- **joblib** (model persistence)

---

##  Model Evaluation
The model was trained using regression techniques and evaluated with:
- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**

---

##  How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/ruhamiy/House_price_predictor
   cd house-price-predictor
