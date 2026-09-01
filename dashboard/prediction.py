import streamlit as st
import pandas as pd
import joblib
import os


MODEL_PATH = "models/churn_pipeline.pkl"


def show():

    st.markdown(
        "<div class='section-title'>🤖 Customer Churn Prediction</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        Predict whether a telecom customer is likely to
        **stay** or **churn** based on their customer profile.
        """
    )

    # -------------------------------------------------
    # LOAD MODEL
    # -------------------------------------------------

    if not os.path.exists(MODEL_PATH):

        st.error(
            "Prediction pipeline not found at "
            "models/churn_pipeline.pkl"
        )

        st.info(
            "Make sure the trained pipeline has been saved "
            "by src/model.py."
        )

        return

    try:
        model = joblib.load(MODEL_PATH)

    except Exception as e:

        st.error(
            f"Unable to load prediction pipeline: {e}"
        )

        return

    # -------------------------------------------------
    # CUSTOMER INFORMATION
    # -------------------------------------------------

    st.subheader("👤 Customer Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

        senior = st.selectbox(
            "Senior Citizen",
            ["No", "Yes"]
        )

        partner = st.selectbox(
            "Partner",
            ["No", "Yes"]
        )

        dependents = st.selectbox(
            "Dependents",
            ["No", "Yes"]
        )

    with col2:

        tenure = st.number_input(
            "Tenure (months)",
            min_value=0,
            max_value=72,
            value=12
        )

        phone_service = st.selectbox(
            "Phone Service",
            ["No", "Yes"]
        )

        multiple_lines = st.selectbox(
            "Multiple Lines",
            ["No phone service", "No", "Yes"]
        )

        internet_service = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )

    with col3:

        contract = st.selectbox(
            "Contract",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ]
        )

        paperless = st.selectbox(
            "Paperless Billing",
            ["No", "Yes"]
        )

        payment = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    st.divider()

    # -------------------------------------------------
    # SERVICES
    # -------------------------------------------------

    st.subheader("🛡️ Services")

    col1, col2, col3 = st.columns(3)

    with col1:

        online_security = st.selectbox(
            "Online Security",
            ["No internet service", "No", "Yes"]
        )

        online_backup = st.selectbox(
            "Online Backup",
            ["No internet service", "No", "Yes"]
        )

    with col2:

        device_protection = st.selectbox(
            "Device Protection",
            ["No internet service", "No", "Yes"]
        )

        tech_support = st.selectbox(
            "Tech Support",
            ["No internet service", "No", "Yes"]
        )

    with col3:

        streaming_tv = st.selectbox(
            "Streaming TV",
            ["No internet service", "No", "Yes"]
        )

        streaming_movies = st.selectbox(
            "Streaming Movies",
            ["No internet service", "No", "Yes"]
        )

    st.divider()

    # -------------------------------------------------
    # CHARGES
    # -------------------------------------------------

    st.subheader("💰 Billing Information")

    col1, col2 = st.columns(2)

    with col1:

        monthly_charges = st.number_input(
            "Monthly Charges",
            min_value=0.0,
            max_value=200.0,
            value=70.0,
            step=1.0
        )

    with col2:

        total_charges = st.number_input(
            "Total Charges",
            min_value=0.0,
            max_value=10000.0,
            value=1000.0,
            step=10.0
        )

    st.divider()

    # -------------------------------------------------
    # PREDICTION BUTTON
    # -------------------------------------------------

    predict_button = st.button(
        "🔮 Predict Customer Churn",
        width="stretch"
    )

    if predict_button:

        # Build raw customer dataframe
        user_data = pd.DataFrame({
            "gender": [gender],
            "SeniorCitizen": [
                1 if senior == "Yes" else 0
            ],
            "Partner": [partner],
            "Dependents": [dependents],
            "tenure": [tenure],
            "PhoneService": [phone_service],
            "MultipleLines": [multiple_lines],
            "InternetService": [internet_service],
            "OnlineSecurity": [online_security],
            "OnlineBackup": [online_backup],
            "DeviceProtection": [device_protection],
            "TechSupport": [tech_support],
            "StreamingTV": [streaming_tv],
            "StreamingMovies": [streaming_movies],
            "Contract": [contract],
            "PaperlessBilling": [paperless],
            "PaymentMethod": [payment],
            "MonthlyCharges": [monthly_charges],
            "TotalCharges": [total_charges]
        })

        try:

            prediction = model.predict(
                user_data
            )[0]

            # Probability if supported
            if hasattr(model, "predict_proba"):

                probabilities = model.predict_proba(
                    user_data
                )[0]

                churn_probability = probabilities[1]

            else:

                churn_probability = None

            st.divider()

            st.subheader("🎯 Prediction Result")

            if prediction == 1:

                st.error(
                    "⚠️ High Churn Risk — Customer is likely to churn."
                )

            else:

                st.success(
                    "✅ Low Churn Risk — Customer is likely to stay."
                )

            # -------------------------------------------------
            # PROBABILITY
            # -------------------------------------------------

            if churn_probability is not None:

                probability_percentage = (
                    churn_probability * 100
                )

                st.markdown(
                    f"### Churn Probability: "
                    f"{probability_percentage:.2f}%"
                )

                st.progress(
                    float(churn_probability)
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Stay Probability",
                        f"{(1 - churn_probability) * 100:.2f}%"
                    )

                with col2:

                    st.metric(
                        "Churn Probability",
                        f"{churn_probability * 100:.2f}%"
                    )

        except Exception as e:

            st.error(
                "Prediction failed."
            )

            st.exception(e)