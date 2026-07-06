import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# Main Title
st.title("📊 Customer Churn Prediction System")

st.markdown("""
Welcome to the **Customer Churn Prediction System**.

This application predicts whether a telecom customer is likely to **Churn** or **Stay** using Machine Learning.

---

### Application Modules

- 🏠 Home
- 📊 Dataset Overview
- 🤖 Customer Churn Prediction
- 📈 Model Performance

Use the **sidebar** to navigate between the pages.
""")

st.info("Select a page from the sidebar to get started.")