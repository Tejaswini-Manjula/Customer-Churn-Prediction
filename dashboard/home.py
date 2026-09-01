import streamlit as st

def show():

    st.markdown("""
    <div class="header">

        <div class="dashboard-title">
            📊 Customer Churn Analytics Dashboard
        </div>

        <div class="dashboard-subtitle">
            AI Powered Telecom Customer Retention System
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<div class='section-title'>Dashboard Overview</div>",
        unsafe_allow_html=True
    )

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class='card'>
            <div class='card-title'>Customers</div>
            <div class='card-value'>7032</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='card'>
            <div class='card-title'>Accuracy</div>
            <div class='card-value'>78.82%</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='card'>
            <div class='card-title'>Algorithms</div>
            <div class='card-value'>5</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class='card'>
            <div class='card-title'>Features</div>
            <div class='card-value'>30</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.info("Interactive analytics charts will appear here in the next step.")