import streamlit as st
import numpy as np
import numpy_financial as npf
import pandas as pd  # Add this line to import pandas

# Title of the app
st.title("Financial Calculators - SRM Analytics")

# Disclaimer
st.sidebar.markdown("### Disclaimer")
st.sidebar.markdown(
    """
    This application is intended for educational and informational purposes only. 
    The calculations and results provided by this app are not financial advice. 
    Always consult a qualified financial professional before making any financial decisions.
    """
)

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
        "PV and FV Tables",
        "Bond Yield to Maturity",
        "Bond Valuation",
        "CAGR Calculation",
        "Cost of Equity",
        "Cost of Debt",
        "Weighted Average Cost of Capital (WACC)",
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

# PV and FV Tables
elif options == "PV and FV Tables":
    st.header("Present Value (PV) and Future Value (FV) Tables")

    # Inputs for PV and FV tables
    rate = st.number_input("Interest Rate (%):", min_value=0.0, value=5.0) / 100
    periods = st.number_input("Number of Periods:", min_value=1, value=10)

    # Generate PV and FV tables
    pv_table = pd.DataFrame({
        "Period": range(1, periods + 1),
        "PV Factor": [1 / ((1 + rate) ** t) for t in range(1, periods + 1)],
        "FV Factor": [(1 + rate) ** t for t in range(1, periods + 1)]
    })

    st.write("### PV and FV Factors")
    st.dataframe(pv_table)

# Bond Yield to Maturity
elif options == "Bond Yield to Maturity":
    st.header("Bond Yield to Maturity")

    # Inputs for bond yield to maturity
    face_value = st.number_input("Face Value:", min_value=0.0, value=1000.0)
    coupon_rate = st.number_input("Coupon Rate (%):", min_value=0.0, value=5.0) / 100
    purchase_price = st.number_input("Purchase Price:", min_value=0.0, value=950.0)
    years_to_maturity = st.number_input("Years to Maturity:", min_value=1, value=10)

    # Calculate bond yield to maturity
    coupon_payment = face_value * coupon_rate
    ytm = npf.rate(
        years_to_maturity,
        coupon_payment,
        -purchase_price,
        face_value
    )

    st.write(f"**Bond Yield to Maturity (YTM):** {ytm * 100:.2f}%")

# Bond Valuation
elif options == "Bond Valuation":
    st.header("Bond Valuation")

    # Inputs for bond valuation
    face_value = st.number_input("Face Value:", min_value=0.0, value=1000.0)
    coupon_rate = st.number_input("Coupon Rate (%):", min_value=0.0, value=5.0) / 100
    discount_rate = st.number_input("Discount Rate (%):", min_value=0.0, value=6.0) / 100
    years_to_maturity = st.number_input("Years to Maturity:", min_value=1, value=10)

    # Calculate bond valuation
    coupon_payment = face_value * coupon_rate
    bond_value = npf.pv(
        discount_rate,
        years_to_maturity,
        -coupon_payment,
        -face_value
    )

    st.write(f"**Bond Value:** {bond_value:.2f}")

# CAGR Calculation
elif options == "CAGR Calculation":
    st.header("Compound Annual Growth Rate (CAGR) Calculation")

    # Inputs for CAGR
    initial_value = st.number_input("Initial Value:", min_value=0.0, value=1000.0)
    final_value = st.number_input("Final Value:", min_value=0.0, value=2000.0)
    years = st.number_input("Number of Years:", min_value=1, value=5)

    # Calculate CAGR
    cagr = (final_value / initial_value) ** (1 / years) - 1

    st.write(f"**CAGR:** {cagr * 100:.2f}%")

# Cost of Equity
elif options == "Cost of Equity":
    st.header("Cost of Equity")

    # Inputs for Dividend Discount Model (DDM)
    st.write("### Dividend Discount Model (DDM)")
    dividend = st.number_input("Dividend per Share:", min_value=0.0, value=2.0)
    growth_rate = st.number_input("Growth Rate (%):", min_value=0.0, value=5.0) / 100
    stock_price = st.number_input("Stock Price:", min_value=0.0, value=50.0)

    # Calculate cost of equity using DDM
    cost_of_equity_ddm = (dividend / stock_price) + growth_rate

    st.write(f"**Cost of Equity (DDM):** {cost_of_equity_ddm * 100:.2f}%")

    # Inputs for CAPM
    st.write("### Capital Asset Pricing Model (CAPM)")
    risk_free_rate = st.number_input("Risk-Free Rate (%):", min_value=0.0, value=3.0) / 100
    beta = st.number_input("Beta:", min_value=0.0, value=1.2)
    market_return = st.number_input("Market Return (%):", min_value=0.0, value=8.0) / 100

    # Calculate cost of equity using CAPM
    cost_of_equity_capm = risk_free_rate + beta * (market_return - risk_free_rate)

    st.write(f"**Cost of Equity (CAPM):** {cost_of_equity_capm * 100:.2f}%")

# Cost of Debt
elif options == "Cost of Debt":
    st.header("Cost of Debt")

    # Inputs for cost of debt
    interest_expense = st.number_input("Interest Expense:", min_value=0.0, value=100.0)
    total_debt = st.number_input("Total Debt:", min_value=0.0, value=1000.0)
    tax_rate = st.number_input("Tax Rate (%):", min_value=0.0, value=30.0) / 100

    # Calculate cost of debt
    cost_of_debt = (interest_expense / total_debt) * (1 - tax_rate)

    st.write(f"**Cost of Debt:** {cost_of_debt * 100:.2f}%")

# Weighted Average Cost of Capital (WACC)
elif options == "Weighted Average Cost of Capital (WACC)":
    st.header("Weighted Average Cost of Capital (WACC)")

    # Inputs for WACC
    equity_value = st.number_input("Equity Value:", min_value=0.0, value=5000.0)
    debt_value = st.number_input("Debt Value:", min_value=0.0, value=2000.0)
    cost_of_equity = st.number_input("Cost of Equity (%):", min_value=0.0, value=10.0) / 100
    cost_of_debt = st.number_input("Cost of Debt (%):", min_value=0.0, value=5.0) / 100
    tax_rate = st.number_input("Tax Rate (%):", min_value=0.0, value=30.0) / 100

    # Calculate WACC
    total_value = equity_value + debt_value
    wacc = (equity_value / total_value) * cost_of_equity + (debt_value / total_value) * cost_of_debt * (1 - tax_rate)

    st.write(f"**WACC:** {wacc * 100:.2f}%")
