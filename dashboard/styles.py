import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* -----------------------------
       Hide Streamlit Default Items
    ------------------------------*/

    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    header {visibility:hidden;}

    /* -----------------------------
       Main Background
    ------------------------------*/

    .stApp{
        background:#F4F7FC;
    }

    /* -----------------------------
       Page Padding
    ------------------------------*/

    .block-container{
        padding-top:2rem;
        padding-left:2rem;
        padding-right:2rem;
        padding-bottom:2rem;
    }

    /* -----------------------------
       Dashboard Title
    ------------------------------*/

    .dashboard-title{
        font-size:40px;
        font-weight:700;
        color:white;
    }

    .dashboard-subtitle{
        color:white;
        font-size:18px;
        margin-top:-10px;
    }

    /* -----------------------------
       Header Gradient
    ------------------------------*/

    .header{
        background:linear-gradient(90deg,#4F46E5,#3B82F6,#06B6D4);
        padding:35px;
        border-radius:18px;
        margin-bottom:25px;
        box-shadow:0px 8px 25px rgba(0,0,0,0.15);
    }

    /* -----------------------------
       KPI Cards
    ------------------------------*/

    .card{
        background:white;
        padding:20px;
        border-radius:18px;
        box-shadow:0px 4px 18px rgba(0,0,0,0.08);
        text-align:center;
        transition:0.3s;
    }

    .card:hover{
        transform:translateY(-5px);
    }

    .card-title{
        color:#6B7280;
        font-size:15px;
    }

    .card-value{
        color:#2563EB;
        font-size:34px;
        font-weight:bold;
    }

    /* -----------------------------
       Section Title
    ------------------------------*/

    .section-title{
        font-size:28px;
        font-weight:bold;
        color:#1F2937;
        margin-top:20px;
        margin-bottom:15px;
    }

    </style>
    """, unsafe_allow_html=True)