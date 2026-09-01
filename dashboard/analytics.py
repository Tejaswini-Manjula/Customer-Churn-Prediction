import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


DATA_PATH = "data/cleaned_telco_churn.csv"


def show():

    st.markdown(
        "<div class='section-title'>📊 Customer Analytics</div>",
        unsafe_allow_html=True
    )

    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        st.error("Dataset file not found.")
        return

    # -------------------------------------------------
    # FILTERS
    # -------------------------------------------------

    st.subheader("🔎 Analytics Filters")

    col1, col2, col3 = st.columns(3)

    with col1:

        contract_filter = st.multiselect(
            "Contract",
            options=df["Contract"].unique(),
            default=list(df["Contract"].unique())
        )

    with col2:

        internet_filter = st.multiselect(
            "Internet Service",
            options=df["InternetService"].unique(),
            default=list(df["InternetService"].unique())
        )

    with col3:

        gender_filter = st.multiselect(
            "Gender",
            options=df["gender"].unique(),
            default=list(df["gender"].unique())
        )

    filtered_df = df[
        df["Contract"].isin(contract_filter)
        & df["InternetService"].isin(internet_filter)
        & df["gender"].isin(gender_filter)
    ]

    st.caption(
        f"Showing {len(filtered_df):,} customers"
    )

    st.divider()

    # =================================================
    # ROW 1
    # =================================================

    col1, col2 = st.columns(2)

    # -------------------------------------------------
    # CHURN PIE
    # -------------------------------------------------

    with col1:

        churn_data = (
            filtered_df["Churn"]
            .value_counts()
            .reset_index()
        )

        churn_data.columns = ["Churn", "Customers"]

        fig = px.pie(
            churn_data,
            names="Churn",
            values="Customers",
            hole=0.45,
            title="🥧 Customer Churn Distribution"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # -------------------------------------------------
    # CONTRACT BAR
    # -------------------------------------------------

    with col2:

        contract_churn = pd.crosstab(
            filtered_df["Contract"],
            filtered_df["Churn"]
        ).reset_index()

        fig = px.bar(
            contract_churn,
            x="Contract",
            y=["No", "Yes"],
            barmode="group",
            title="📊 Contract Type vs Churn"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # =================================================
    # ROW 2
    # =================================================

    col1, col2 = st.columns(2)

    # -------------------------------------------------
    # INTERNET SERVICE
    # -------------------------------------------------

    with col1:

        internet_data = (
            filtered_df["InternetService"]
            .value_counts()
            .reset_index()
        )

        internet_data.columns = [
            "InternetService",
            "Customers"
        ]

        fig = px.pie(
            internet_data,
            names="InternetService",
            values="Customers",
            hole=0.45,
            title="🌐 Internet Service Distribution"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # -------------------------------------------------
    # PAYMENT METHOD
    # -------------------------------------------------

    with col2:

        payment_data = (
            filtered_df["PaymentMethod"]
            .value_counts()
            .reset_index()
        )

        payment_data.columns = [
            "PaymentMethod",
            "Customers"
        ]

        fig = px.bar(
            payment_data,
            x="Customers",
            y="PaymentMethod",
            orientation="h",
            title="💳 Payment Method Distribution"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # =================================================
    # ROW 3
    # =================================================

    col1, col2 = st.columns(2)

    # -------------------------------------------------
    # MONTHLY CHARGES
    # -------------------------------------------------

    with col1:

        fig = px.histogram(
            filtered_df,
            x="MonthlyCharges",
            color="Churn",
            nbins=30,
            title="💰 Monthly Charges Distribution"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # -------------------------------------------------
    # TENURE
    # -------------------------------------------------

    with col2:

        fig = px.histogram(
            filtered_df,
            x="tenure",
            color="Churn",
            nbins=30,
            title="📅 Customer Tenure Distribution"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # =================================================
    # ROW 4
    # =================================================

    col1, col2 = st.columns(2)

    # -------------------------------------------------
    # TENURE VS MONTHLY CHARGES
    # -------------------------------------------------

    with col1:

        fig = px.scatter(
            filtered_df,
            x="tenure",
            y="MonthlyCharges",
            color="Churn",
            opacity=0.6,
            title="📈 Tenure vs Monthly Charges"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # -------------------------------------------------
    # BOX PLOT
    # -------------------------------------------------

    with col2:

        fig = px.box(
            filtered_df,
            x="Churn",
            y="MonthlyCharges",
            color="Churn",
            title="📦 Monthly Charges by Churn"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # =================================================
    # ROW 5
    # =================================================

    st.subheader("🔥 Correlation Analysis")

    numeric_df = filtered_df.select_dtypes(
        include=["int64", "float64"]
    )

    correlation = numeric_df.corr()

    fig = px.imshow(
        correlation,
        text_auto=True,
        aspect="auto",
        title="Feature Correlation Heatmap"
    )

    fig.update_layout(
        height=650
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # =================================================
    # ROW 6
    # =================================================

    st.subheader("👥 Customer Demographics")

    col1, col2 = st.columns(2)

    with col1:

        gender_churn = pd.crosstab(
            filtered_df["gender"],
            filtered_df["Churn"]
        ).reset_index()

        fig = px.bar(
            gender_churn,
            x="gender",
            y=["No", "Yes"],
            barmode="group",
            title="Gender vs Churn"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    with col2:

        senior_churn = pd.crosstab(
            filtered_df["SeniorCitizen"],
            filtered_df["Churn"]
        ).reset_index()

        senior_churn["SeniorCitizen"] = (
            senior_churn["SeniorCitizen"]
            .map({
                0: "Non-Senior",
                1: "Senior"
            })
        )

        fig = px.bar(
            senior_churn,
            x="SeniorCitizen",
            y=["No", "Yes"],
            barmode="group",
            title="Senior Citizen vs Churn"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )