"""
House Price Prediction App
Based on Bank of Canada economic indicators and research
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Title
st.title("🏠 House Price Prediction Tool")
st.markdown("*Based on Bank of Canada Economic Indicators*")

# Disclaimer
st.warning("""
**⚠️ Important Disclaimer**

The Bank of Canada never gives financial advice. This tool is for educational purposes only. 
These projections are illustrative and should not be used as the basis for any financial decisions. 
Always consult with qualified financial professionals for advice specific to your circumstances.
""")

# Current House Price Input
st.header("Current House Price Estimate")
current_price = st.number_input(
    "Enter the current house price estimate ($CAD)",
    min_value=0.0,
    value=500000.0,
    step=10000.0,
    format="%.2f"
)

# Sidebar for weights configuration
st.sidebar.header("⚙️ Weight Configuration")
st.sidebar.markdown("Adjust the impact (weight) of each economic variable on the price prediction.")

# Weight sliders in sidebar
st.sidebar.subheader("Variable Weights")
weight_interest = st.sidebar.slider(
    "Policy Interest Rate Weight",
    min_value=0.0,
    max_value=2.0,
    value=1.0,
    step=0.1,
    help="Impact of policy interest rate changes"
)
st.sidebar.text(f"Current weight: {weight_interest}")

weight_inflation = st.sidebar.slider(
    "Core Inflation Weight",
    min_value=0.0,
    max_value=2.0,
    value=1.0,
    step=0.1,
    help="Impact of underlying inflation"
)
st.sidebar.text(f"Current weight: {weight_inflation}")

weight_mortgage = st.sidebar.slider(
    "Mortgage Payment Shocks Weight",
    min_value=0.0,
    max_value=2.0,
    value=1.0,
    step=0.1,
    help="Impact of mortgage payment changes on renewals"
)
st.sidebar.text(f"Current weight: {weight_mortgage}")

weight_credit = st.sidebar.slider(
    "Credit Conditions Weight",
    min_value=0.0,
    max_value=2.0,
    value=1.0,
    step=0.1,
    help="Impact of credit availability"
)
st.sidebar.text(f"Current weight: {weight_credit}")

weight_productivity = st.sidebar.slider(
    "Productivity & Competition Weight",
    min_value=0.0,
    max_value=2.0,
    value=1.0,
    step=0.1,
    help="Impact of economic productivity"
)
st.sidebar.text(f"Current weight: {weight_productivity}")

weight_trade = st.sidebar.slider(
    "Trade Policy & Tariffs Weight",
    min_value=0.0,
    max_value=2.0,
    value=1.0,
    step=0.1,
    help="Impact of trade policy changes"
)
st.sidebar.text(f"Current weight: {weight_trade}")

weight_immigration = st.sidebar.slider(
    "Immigration/Population Growth Weight",
    min_value=0.0,
    max_value=2.0,
    value=1.0,
    step=0.1,
    help="Impact of population growth on demand"
)
st.sidebar.text(f"Current weight: {weight_immigration}")

weight_supply = st.sidebar.slider(
    "New Construction/Housing Supply Weight",
    min_value=0.0,
    max_value=2.0,
    value=1.0,
    step=0.1,
    help="Impact of housing supply changes"
)
st.sidebar.text(f"Current weight: {weight_supply}")

# Main content - Economic Variables
st.header("Economic Variables")
st.markdown("Adjust the following indicators based on Bank of Canada research:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Monetary Policy & Inflation")
    
    # Policy Interest Rate
    policy_rate = st.slider(
        "Policy Interest Rate (%)",
        min_value=0.0,
        max_value=8.0,
        value=2.5,
        step=0.25,
        help="Current benchmark: 2.50%"
    )
    st.caption(f"Current: {policy_rate}% (Benchmark: 2.50%)")
    
    # Core Inflation (average of CPI-trim and CPI-median)
    cpi_trim = st.slider(
        "CPI-trim (%)",
        min_value=0.0,
        max_value=10.0,
        value=3.0,
        step=0.1,
        help="One measure to 'separate the signal from the noise'"
    )
    
    cpi_median = st.slider(
        "CPI-median (%)",
        min_value=0.0,
        max_value=10.0,
        value=3.1,
        step=0.1,
        help="Another measure to 'separate the signal from the noise'"
    )
    
    core_inflation = (cpi_trim + cpi_median) / 2
    st.info(f"**Core Inflation (Average):** {core_inflation:.2f}%")
    
    # Mortgage Payment Shocks
    mortgage_shock = st.slider(
        "Mortgage Payment Shocks (%)",
        min_value=-10.0,
        max_value=50.0,
        value=0.0,
        step=1.0,
        help="Impact on household balance sheets when renewing at different rates"
    )
    st.caption(f"Current shock: {mortgage_shock:+.1f}%")

with col2:
    st.subheader("Market Conditions & External Factors")
    
    # Credit Conditions
    credit_conditions = st.slider(
        "Credit Conditions (Ease of Financing)",
        min_value=0.0,
        max_value=10.0,
        value=5.0,
        step=0.5,
        help="0 = Very Difficult, 10 = Very Easy"
    )
    st.caption(f"Current: {credit_conditions:.1f}/10")
    
    # Productivity and Competition
    productivity = st.slider(
        "Productivity & Competition",
        min_value=0.0,
        max_value=10.0,
        value=5.0,
        step=0.5,
        help="Reflecting long-term economic prosperity"
    )
    st.caption(f"Current: {productivity:.1f}/10")
    
    # Trade Policy & Tariffs
    trade_policy = st.slider(
        "Trade Policy & Tariffs Impact",
        min_value=-10.0,
        max_value=10.0,
        value=0.0,
        step=0.5,
        help="External 'megatrends' - extremely difficult to predict"
    )
    st.caption(f"Current: {trade_policy:+.1f}")
    
    # Immigration/Population Growth
    immigration = st.slider(
        "Immigration/Population Growth (%)",
        min_value=0.0,
        max_value=5.0,
        value=1.5,
        step=0.1,
        help="Driver of housing demand"
    )
    st.caption(f"Current: {immigration:.1f}% annual growth")
    
    # New Construction/Housing Supply
    housing_supply = st.slider(
        "New Construction/Housing Supply Growth (%)",
        min_value=-5.0,
        max_value=10.0,
        value=2.0,
        step=0.5,
        help="Counter-balance to demand"
    )
    st.caption(f"Current: {housing_supply:+.1f}%")

# Calculation Logic
st.header("Price Prediction")

# Calculate resilience factor based on productivity and credit conditions
# Higher productivity and credit conditions provide resilience against interest rate increases
resilience_factor = ((productivity / 10.0) + (credit_conditions / 10.0)) / 2

# Normalize variables to percentage impacts
# Negative impacts (decrease price)
interest_impact = -(policy_rate - 2.5) * 2.0 * weight_interest  # Deviation from benchmark
mortgage_impact = -(mortgage_shock * 0.5) * weight_mortgage
supply_impact = -(housing_supply - 2.0) * 1.0 * weight_supply  # Above average supply reduces prices

# Positive impacts (increase price)
inflation_impact = (core_inflation - 2.0) * 1.5 * weight_inflation  # Target is ~2%
credit_impact = (credit_conditions - 5.0) * 1.0 * weight_credit
productivity_impact = (productivity - 5.0) * 1.2 * weight_productivity
trade_impact = trade_policy * 0.5 * weight_trade
immigration_impact = (immigration - 1.0) * 3.0 * weight_immigration  # Strong demand driver

# Apply resilience - if resilience is high, reduce negative impacts
adjusted_interest_impact = interest_impact * (1.0 - resilience_factor * 0.3)
adjusted_mortgage_impact = mortgage_impact * (1.0 - resilience_factor * 0.3)

# Total impact percentage
total_impact = (
    adjusted_interest_impact +
    adjusted_mortgage_impact +
    supply_impact +
    inflation_impact +
    credit_impact +
    productivity_impact +
    trade_impact +
    immigration_impact
)

# Calculate predicted price
predicted_price = current_price * (1 + total_impact / 100.0)
price_change = predicted_price - current_price
price_change_pct = (price_change / current_price) * 100

# Display results
col_res1, col_res2, col_res3 = st.columns(3)

with col_res1:
    st.metric(
        label="Current Price",
        value=f"${current_price:,.2f}"
    )

with col_res2:
    st.metric(
        label="Predicted Price",
        value=f"${predicted_price:,.2f}",
        delta=f"{price_change_pct:+.2f}%"
    )

with col_res3:
    st.metric(
        label="Price Change",
        value=f"${price_change:+,.2f}"
    )

# Resilience indicator
st.info(f"🛡️ **Market Resilience Factor:** {resilience_factor:.2%} - "
        f"{'High' if resilience_factor > 0.6 else 'Medium' if resilience_factor > 0.4 else 'Low'} resilience "
        f"{'reduces' if resilience_factor > 0.5 else 'provides limited reduction to'} negative impacts from interest rates and mortgage shocks.")

# Summary of Deliberations
st.header("📋 Summary of Deliberations")

summary_text = f"""
**Economic Analysis and Logic:**

**Negative Price Factors:**
- **Policy Interest Rate Impact:** {adjusted_interest_impact:.2f}% 
  - Current rate: {policy_rate}% vs. benchmark 2.50%
  - Higher interest rates typically decrease housing affordability and demand
  - Impact moderated by {resilience_factor:.1%} resilience factor

- **Mortgage Payment Shocks:** {adjusted_mortgage_impact:.2f}%
  - Shock level: {mortgage_shock:+.1f}%
  - Represents impact on household balance sheets when mortgages renew at different rates
  - Impact moderated by {resilience_factor:.1%} resilience factor

- **Housing Supply Changes:** {supply_impact:.2f}%
  - Current supply growth: {housing_supply:+.1f}%
  - Higher supply relative to baseline reduces price pressure

**Positive Price Factors:**
- **Core Inflation (Underlying):** {inflation_impact:.2f}%
  - Average of CPI-trim ({cpi_trim}%) and CPI-median ({cpi_median}%) = {core_inflation:.2f}%
  - These measures help 'separate the signal from the noise'
  - Inflation above target (~2%) typically supports nominal price growth

- **Credit Conditions:** {credit_impact:.2f}%
  - Current ease of financing: {credit_conditions:.1f}/10
  - Better credit conditions increase buyer access to financing

- **Productivity & Competition:** {productivity_impact:.2f}%
  - Current level: {productivity:.1f}/10
  - Reflects long-term economic prosperity and income growth potential

- **Trade Policy & Tariffs:** {trade_impact:.2f}%
  - Current impact: {trade_policy:+.1f}
  - External 'megatrends' that are 'extremely difficult to predict'

- **Immigration/Population Growth:** {immigration_impact:.2f}%
  - Current growth: {immigration:.1f}% annually
  - Strong driver of housing demand

**Resilience Assessment:**
The model incorporates resilience based on productivity ({productivity:.1f}/10) and credit conditions ({credit_conditions:.1f}/10).
When these factors are strong, the housing market shows more stability despite higher interest rates and mortgage shocks.
Current resilience factor: {resilience_factor:.1%}

**Net Impact:** {total_impact:+.2f}% → Predicted price change from ${current_price:,.2f} to ${predicted_price:,.2f}
"""

st.text_area("Detailed Breakdown", summary_text, height=500)

# Additional context
st.markdown("---")
st.subheader("About This Tool")
st.markdown("""
This educational tool is inspired by the Bank of Canada's monetary policy framework and economic research. 
The variables reflect factors that central banks and economists consider when assessing housing markets:

- **Monetary Policy Tools:** Interest rates directly affect borrowing costs
- **Inflation Measures:** Core inflation metrics (CPI-trim, CPI-median) filter out volatile components
- **Financial Stability:** Mortgage shocks and credit conditions affect household balance sheets
- **Supply and Demand:** Immigration drives demand while new construction affects supply
- **Economic Fundamentals:** Productivity reflects long-term economic health
- **External Factors:** Trade policies represent unpredictable global influences

**Sources:** Bank of Canada research, monetary policy reports, and financial stability frameworks.
""")
