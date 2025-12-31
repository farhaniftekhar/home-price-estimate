# House Price Prediction Tool 🏠

A Python Streamlit web application that predicts future house prices based on Bank of Canada economic indicators and research.

## Features

- **Current Price Input**: Enter your current house price estimate
- **8 Economic Variables**: Adjust sliders for key indicators:
  - Policy Interest Rate (benchmark: 2.50%)
  - Core Inflation (CPI-trim and CPI-median average)
  - Mortgage Payment Shocks
  - Credit Conditions
  - Productivity & Competition
  - Trade Policy & Tariffs
  - Immigration/Population Growth
  - New Construction/Housing Supply

- **Customizable Weights**: Configure the impact of each variable via sidebar sliders
- **Resilience Factor**: Model accounts for market stability based on productivity and credit conditions
- **Summary of Deliberations**: Detailed breakdown of the calculation logic
- **Educational Disclaimer**: Clear notice that this is for educational purposes only

## Installation

1. Clone the repository:
```bash
git clone https://github.com/farhaniftekhar/home-price-estimate.git
cd home-price-estimate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## How It Works

The prediction model:
1. Takes your current house price estimate as a baseline
2. Applies weighted impacts from 8 economic variables
3. Considers market resilience based on productivity and credit conditions
4. Calculates a predicted price with detailed breakdown

**Key Logic:**
- Higher interest rates and mortgage shocks → decrease price projections
- Higher core inflation and productivity → increase price projections
- Strong productivity and credit conditions → provide resilience against negative factors

## Disclaimer

⚠️ **Important**: The Bank of Canada never gives financial advice. This tool is for educational purposes only. These projections are illustrative and should not be used as the basis for any financial decisions. Always consult with qualified financial professionals for advice specific to your circumstances.

## About

Based on Bank of Canada monetary policy framework, economic research, and financial stability indicators. Variables reflect factors that central banks and economists consider when assessing housing markets.

## License

MIT License
