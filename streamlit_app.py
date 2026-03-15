
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="GIS Stock Predictor", page_icon="🌾")

st.title("🌾 General Mills (GIS) Stock Direction Predictor")
st.markdown("""
Predict whether GIS stock will go **UP** or **DOWN** next quarter  
based on SEC EDGAR fundamentals + BLS CPI inflation data.
""")

st.divider()

st.subheader("Enter Current Quarter Data")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**SEC EDGAR Fundamentals**")
    revenue_growth = st.number_input("Revenue Growth QoQ (%)", -50.0, 50.0, 2.5)
    net_margin = st.number_input("Net Profit Margin (%)", -30.0, 30.0, 8.5)
    op_margin = st.number_input("Operating Margin (%)", -20.0, 30.0, 14.0)
    debt_to_assets = st.number_input("Debt-to-Assets Ratio", 0.0, 1.0, 0.35)

with col2:
    st.markdown("**BLS CPI Macro Data**")
    revenue_surprise = st.number_input("Revenue Surprise (%)", -30.0, 30.0, 1.0)
    asset_turnover = st.number_input("Asset Turnover", 0.0, 2.0, 0.45)
    cpi_yoy = st.number_input("CPI YoY Change (%)", -5.0, 20.0, 3.2)
    cpi_qoq = st.number_input("CPI QoQ Change (%)", -3.0, 5.0, 0.8)

st.divider()

if st.button("🔮 Predict Stock Direction", type="primary", use_container_width=True):
    
    # Simple rule-based model for demo
    score = 0
    if revenue_growth > 0: score += 1
    if net_margin > 8: score += 1
    if op_margin > 12: score += 1
    if debt_to_assets < 0.4: score += 1
    if revenue_surprise > 0: score += 1
    if cpi_yoy < 4: score += 1
    
    if score >= 4:
        st.success("## 📈 Prediction: UP")
        confidence = 50 + score * 7
    else:
        st.error("## 📉 Prediction: DOWN")
        confidence = 50 + (6 - score) * 7
    
    st.metric("Confidence Score", f"{confidence}%")
    
    st.subheader("Input Summary")
    summary = pd.DataFrame({
        "Feature": ["Revenue Growth", "Net Margin", "Operating Margin",
                   "Debt-to-Assets", "Revenue Surprise", "Asset Turnover",
                   "CPI YoY", "CPI QoQ"],
        "Value": [f"{revenue_growth:.1f}%", f"{net_margin:.1f}%", 
                 f"{op_margin:.1f}%", f"{debt_to_assets:.2f}",
                 f"{revenue_surprise:.1f}%", f"{asset_turnover:.2f}",
                 f"{cpi_yoy:.1f}%", f"{cpi_qoq:.1f}%"],
        "Source": ["SEC EDGAR", "SEC EDGAR", "SEC EDGAR", "SEC EDGAR",
                  "SEC EDGAR", "SEC EDGAR", "BLS CPI", "BLS CPI"]
    })
    st.dataframe(summary, hide_index=True, use_container_width=True)

st.divider()
st.caption("⚠️ For educational purposes only. Not financial advice.")
