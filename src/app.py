import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Customer Churn Predictor", layout="wide")

st.title("Customer Churn Predictor - Live Demo")
st.write("Enter customer details to see churn risk update instantly")

# Sidebar inputs
st.sidebar.header("Customer Information")
tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.sidebar.number_input("Monthly Charges ($)", 18.0, 120.0, 70.0)
contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment = st.sidebar.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

def predict_churn_demo(tenure, charges, contract_type, internet_type):
    """Simple rule-based model for demo. Replace with real model later."""
    risk_score = 0
    if contract_type == "Month-to-month": 
        risk_score += 40
    if charges > 70: 
        risk_score += 25
    if tenure < 12: 
        risk_score += 20
    if internet_type == "Fiber optic": 
        risk_score += 15
    if payment == "Electronic check":
        risk_score += 10
        
    risk_score = min(risk_score, 95)
    prediction = "Churn" if risk_score > 50 else "No Churn"
    return prediction, risk_score

# Calculate prediction - runs automatically when sliders change
prediction, risk = predict_churn_demo(tenure, monthly_charges, contract, internet)

# Show results
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Prediction", prediction)
with col2:
    st.metric("Churn Risk", f"{risk}%")
with col3:
    if prediction == "Churn":
        st.error("High Risk")
    else:
        st.success("Low Risk")

# Live graph - this updates when user moves sliders
fig = px.pie(values=[risk, 100-risk], 
             names=['Likely to Churn', 'Likely to Stay'],
             title='Churn Probability',
             color_discrete_sequence=['#ff4b4b','#09ab3b'],
             hole=0.4)
fig.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig, use_container_width=True)

# Info section
st.divider()
col_a, col_b = st.columns(2)
with col_a:
    st.info("**Demo Mode**: Uses rule-based logic for instant predictions")
with col_b:
    st.write("**Full Model**: XGBoost | Accuracy: 85% | F1-Score: 87%")
    st.write("See GitHub for notebook with full model training")

st.caption("Built by Benedict Omondi | Data Analyst")