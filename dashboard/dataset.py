import streamlit as st
import pandas as pd
import plotly.express as px


DATA_PATH = "data/cleaned_telco_churn.csv"


def show():

    st.markdown(
        "<div class='section-title'>📂 Dataset Explorer</div>",
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # LOAD DATA
    # -------------------------------------------------

    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        st.error("Dataset file not found.")
        return

    # -------------------------------------------------
    # KPI CARDS
    # -------------------------------------------------

    total_customers = len(df)
    total_features = len(df.columns) - 1
    missing_values = int(df.isnull().sum().sum())

    churn_count = (
        df["Churn"].value_counts().get("Yes", 0)
        if "Churn" in df.columns
        else 0
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Customers", f"{total_customers:,}")
    c2.metric("Features", total_features)
    c3.metric("Missing Values", missing_values)
    c4.metric("Churned Customers", f"{churn_count:,}")

    st.divider()

    # -------------------------------------------------
    # DATASET PREVIEW
    # -------------------------------------------------

    st.subheader("Dataset Preview")

    rows_to_show = st.slider(
        "Number of rows",
        min_value=5,
        max_value=50,
        value=10
    )

    st.dataframe(
        df.head(rows_to_show),
        width="stretch"
    )

    st.divider()

    # -------------------------------------------------
    # STATISTICAL SUMMARY
    # -------------------------------------------------

    st.subheader("Statistical Summary")

    st.dataframe(
        df.describe(include="all").T,
        width="stretch"
    )

    st.divider()

    # -------------------------------------------------
    # DATA TYPES
    # -------------------------------------------------

    st.subheader("Column Information")

    column_info = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str).values,
        "Missing Values": df.isnull().sum().values,
        "Unique Values": df.nunique().values
    })

    st.dataframe(
        column_info,
        width="stretch"
    )

    st.divider()

    # -------------------------------------------------
    # QUICK VISUALIZATION
    # -------------------------------------------------

    st.subheader("Dataset Distribution")

    col1, col2 = st.columns(2)

    with col1:

        if "Churn" in df.columns:

            churn_data = (
                df["Churn"]
                .value_counts()
                .reset_index()
            )

            churn_data.columns = ["Churn", "Customers"]

            fig = px.pie(
                churn_data,
                names="Churn",
                values="Customers",
                hole=0.45,
                title="Customer Churn Distribution"
            )

            fig.update_layout(
                height=400,
                margin=dict(l=20, r=20, t=60, b=20)
            )

            st.plotly_chart(
                fig,
                width="stretch"
            )

    with col2:

        if "Contract" in df.columns and "Churn" in df.columns:

            contract_data = (
                pd.crosstab(
                    df["Contract"],
                    df["Churn"]
                )
                .reset_index()
            )

            fig = px.bar(
                contract_data,
                x="Contract",
                y=["No", "Yes"],
                barmode="group",
                title="Contract Type vs Churn"
            )

            fig.update_layout(
                height=400,
                margin=dict(l=20, r=20, t=60, b=20)
            )

            st.plotly_chart(
                fig,
                width="stretch"
            )