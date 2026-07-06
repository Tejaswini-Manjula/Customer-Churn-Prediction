import streamlit as st

st.title("🏠 Customer Churn Prediction")

st.header("Project Overview")

st.write("""
Customer churn refers to customers leaving a company or discontinuing its services.

This project predicts whether a customer is likely to churn using Machine Learning.
""")

st.header("Objectives")

st.markdown("""
- Predict customer churn
- Help businesses retain customers
- Compare multiple Machine Learning algorithms
- Visualize model performance
""")

st.header("Machine Learning Models")

st.markdown("""
- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors
- Support Vector Machine
""")

st.header("Technologies Used")

col1, col2 = st.columns(2)

with col1:
    st.success("Python")
    st.success("Pandas")
    st.success("NumPy")
    st.success("Scikit-Learn")

with col2:
    st.success("Matplotlib")
    st.success("Joblib")
    st.success("Streamlit")
    st.success("GitHub")

st.info("Use the sidebar to explore the project.")