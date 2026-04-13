import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model
model = pickle.load(open("Churn_prediction.sav", "rb"))

st.set_page_config(page_title="Churn Prediction", layout="wide")

st.title("📊 Customer Churn Prediction Dashboard")

st.markdown("Predict whether a customer will churn based on input features.")

# Sidebar Inputs
st.sidebar.header("Customer Details")

tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)
monthly_charges = st.sidebar.number_input("Monthly Charges", 0, 200, 50)
total_charges = st.sidebar.number_input("Total Charges", 0, 10000, 1000)
InternetService_Fiber=st.sidebar.number_input("InternetService_Fiber optic", 0, 1, 1)
OnlineSecurity=st.sidebar.number_input("OnlineSecurity_Yes", 0, 1, 1)
PaperlessBilling=st.sidebar.number_input("PaperlessBilling_Yes", 0, 1, 1)
PaymentMethod_Electronic=st.sidebar.number_input("PaymentMethod_Electronic check", 0, 1, 1)


# Prepare input
input_data = np.array([[tenure, monthly_charges, total_charges, InternetService_Fiber,OnlineSecurity,PaperlessBilling,PaymentMethod_Electronic]])

# Prediction
if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]
    #prob = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer likely to churn")
    else:
        st.success("✅ Customer likely to stay ")

    # Insights
    st.markdown("### 💡 Insights")
    st.write("- Customers with low tenure have higher churn risk")
    st.write("- Month-to-month contracts show higher churn")

