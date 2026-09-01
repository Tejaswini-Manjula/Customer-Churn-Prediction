import streamlit as st

from dashboard.styles import load_css
from dashboard.home import show as home_page
from dashboard.dataset import show as dataset_page
from dashboard.prediction import show as prediction_page
from dashboard.analytics import show as analytics_page
from dashboard.performance import show as performance_page

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Customer Churn Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------
# LOAD GLOBAL CSS
# -------------------------------------------------

load_css()

home, dataset, prediction, analytics, performance = st.tabs([
    "🏠 Dashboard",
    "📂 Dataset",
    "🤖 Prediction",
    "📊 Analytics",
    "📈 Performance"
])

with home:
    home_page()

with dataset:
    dataset_page()

with prediction:
    prediction_page()

with analytics:
    analytics_page()

with performance:
    performance_page()