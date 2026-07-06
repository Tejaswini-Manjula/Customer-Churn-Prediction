import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset", page_icon="📊")

st.title("📊 Dataset Overview")

# Load dataset
df = pd.read_csv("data/cleaned_telco_churn.csv")

# Dataset Information
st.header("Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

with col3:
    st.metric("Missing Values", df.isnull().sum().sum())

st.divider()

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(df.head(10), use_container_width=True)

st.divider()

# Column Names
st.subheader("Columns")
st.write(list(df.columns))

st.divider()

# Statistical Summary
st.subheader("Statistical Summary")
st.dataframe(df.describe(), use_container_width=True)

st.divider()

# Churn Distribution
st.subheader("Target Variable Distribution")

if "Churn" in df.columns:
    st.bar_chart(df["Churn"].value_counts())
else:
    st.warning("Churn column not found.")