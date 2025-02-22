import streamlit as st
import numpy as np
import numpy_financial as npf

# Title of the app
st.title("Time Value of Money (TVM) Calculators - SRM")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio(
    "Choose a Calculator:",
    [
        "Present Value (PV)",
        "Future Value (FV)",
        "PV Factor (Annuity & Annuity Due)",
        "FV Factor (Annuity & Annuity Due)",
        "Net Present Value (NPV)",
        "Internal Rate of Return (IRR)",
    ],
)

# Present Value (PV) Calculator
if options == "Present Value (PV)":
    st.header("Present Value (PV) Calculator")
    fv = st.number_input("Future Value (FV):", min_value=0.0, value=1000.0)
    rate = st.number_input("Interest Rate (%):", min_value=0.0, value=5.0) / 100
    periods = st.number_input("Number of Periods:", min_value=1, value=10)
    pv = fv / ((1 + rate) ** periods)
    st.write(f"**Present Value (PV):** {pv:.2f}")

# Future Value (FV) Calculator
elif options == "Future Value (FV)":
    st.header("Future Value (FV) Calculator")
    pv = st.number_input("Present Value (PV):", min_value=0.0, value=1000.0)
    rate = st.number_input("Interest Rate (%):", min_value=0.0, value=5.0) / 100
    periods = st.number_input("Number of Periods:", min_value=1, value=10)
    fv = pv * ((1 + rate) ** periods)
    st.write(f"**Future Value (FV):** {fv:.2f}")

# PV Factor (Annuity & Annuity Due) Calculator
elif options == "PV Factor (Annuity & Annuity Due)":
    st.header("PV Factor (Annuity & Annuity Due) Calculator")
    rate = st.number_input("Interest Rate (%):", min_value=0.0, value=5.0) / 100
    periods = st.number_input("Number of Periods:", min_value=1, value=10)
    pv_factor_annuity = (1 - (1 + rate) ** -periods) / rate
    pv_factor_annuity_due = pv_factor_annuity * (1 + rate)
    st.write(f"**PV Factor (Annuity):** {pv_factor_annuity:.4f}")
    st.write(f"**PV Factor (Annuity Due):** {pv_factor_annuity_due:.4f}")

# FV Factor (Annuity & Annuity Due) Calculator
elif options == "FV Factor (Annuity & Annuity Due)":
    st.header("FV Factor (Annuity & Annuity Due) Calculator")
    rate = st.number_input("Interest Rate (%):", min_value=0.0, value=5.0) / 100
    periods = st.number_input("Number of Periods:", min_value=1, value=10)
    fv_factor_annuity = ((1 + rate) ** periods - 1) / rate
    fv_factor_annuity_due = fv_factor_annuity * (1 + rate)
    st.write(f"**FV Factor (Annuity):** {fv_factor_annuity:.4f}")
    st.write(f"**FV Factor (Annuity Due):** {fv_factor_annuity_due:.4f}")

# Net Present Value (NPV) Calculator
elif options == "Net Present Value (NPV)":
    st.header("Net Present Value (NPV) Calculator")
    rate = st.number_input("Discount Rate (%):", min_value=0.0, value=5.0) / 100
    cash_flows = st.text_input("Cash Flows (comma-separated):", value="-1000,200,300,400,500")
    cash_flows = [float(x) for x in cash_flows.split(",")]
    npv = npf.npv(rate, cash_flows)
    st.write(f"**Net Present Value (NPV):** {npv:.2f}")

# Internal Rate of Return (IRR) Calculator
elif options == "Internal Rate of Return (IRR)":
    st.header("Internal Rate of Return (IRR) Calculator")
    cash_flows = st.text_input("Cash Flows (comma-separated):", value="-1000,200,300,400,500")
    cash_flows = [float(x) for x in cash_flows.split(",")]
    irr = npf.irr(cash_flows)
    st.write(f"**Internal Rate of Return (IRR):** {irr * 100:.2f}%")
