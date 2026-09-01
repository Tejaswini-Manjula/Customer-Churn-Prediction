import streamlit as st
import pandas as pd
import os
import plotly.express as px


RESULTS_PATH = "data/model_comparison_results.csv"
CONFUSION_MATRIX_PATH = "images/confusion_matrix.png"


def show():

    st.markdown(
        "<div class='section-title'>📈 Model Performance</div>",
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # LOAD MODEL RESULTS
    # -------------------------------------------------

    try:
        results = pd.read_csv(RESULTS_PATH)
    except FileNotFoundError:
        st.error(
            "Model comparison results not found. "
            "Run src/model_comparison.py first."
        )
        return

    # -------------------------------------------------
    # BEST MODEL
    # -------------------------------------------------

    best_model_row = results.loc[
        results["F1 Score"].idxmax()
    ]

    best_model = best_model_row["Model"]

    accuracy = best_model_row["Accuracy"]
    precision = best_model_row["Precision"]
    recall = best_model_row["Recall"]
    f1 = best_model_row["F1 Score"]

    # -------------------------------------------------
    # KPI CARDS
    # -------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Accuracy",
        f"{accuracy * 100:.2f}%"
    )

    c2.metric(
        "Precision",
        f"{precision * 100:.2f}%"
    )

    c3.metric(
        "Recall",
        f"{recall * 100:.2f}%"
    )

    c4.metric(
        "F1 Score",
        f"{f1 * 100:.2f}%"
    )

    st.divider()

    st.success(
        f"🏆 Best performing model based on F1 Score: **{best_model}**"
    )

    # -------------------------------------------------
    # MODEL COMPARISON TABLE
    # -------------------------------------------------

    st.subheader("🤖 Model Comparison")

    display_results = results.copy()

    for column in [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]:
        display_results[column] = (
            display_results[column] * 100
        ).round(2)

    st.dataframe(
        display_results,
        width="stretch"
    )

    st.divider()

    # -------------------------------------------------
    # ACCURACY CHART
    # -------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(
            results,
            x="Model",
            y="Accuracy",
            text="Accuracy",
            title="📊 Accuracy Comparison"
        )

        fig.update_yaxes(
            range=[0, 1]
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # -------------------------------------------------
    # F1 SCORE
    # -------------------------------------------------

    with col2:

        fig = px.bar(
            results,
            x="Model",
            y="F1 Score",
            text="F1 Score",
            title="🎯 F1 Score Comparison"
        )

        fig.update_yaxes(
            range=[0, 1]
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # -------------------------------------------------
    # ALL METRICS
    # -------------------------------------------------

    st.subheader("📊 Complete Performance Comparison")

    melted = results.melt(
        id_vars="Model",
        value_vars=[
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score"
        ],
        var_name="Metric",
        value_name="Score"
    )

    fig = px.bar(
        melted,
        x="Model",
        y="Score",
        color="Metric",
        barmode="group",
        title="Machine Learning Model Performance"
    )

    fig.update_yaxes(
        range=[0, 1]
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # -------------------------------------------------
    # CONFUSION MATRIX
    # -------------------------------------------------

    st.subheader("🔲 Confusion Matrix")

    if os.path.exists(CONFUSION_MATRIX_PATH):

        st.image(
            CONFUSION_MATRIX_PATH,
            width="stretch"
        )

    else:

        st.warning(
            "Confusion matrix image not found."
        )

    # -------------------------------------------------
    # INTERPRETATION
    # -------------------------------------------------

    st.subheader("📝 Model Interpretation")

    st.write(
        f"""
        **{best_model}** achieved the highest F1 Score among the
        evaluated models.

        - **Accuracy:** {accuracy:.4f}
        - **Precision:** {precision:.4f}
        - **Recall:** {recall:.4f}
        - **F1 Score:** {f1:.4f}

        The F1 Score provides a balance between precision and recall,
        which is useful for evaluating customer churn prediction.
        """
    )