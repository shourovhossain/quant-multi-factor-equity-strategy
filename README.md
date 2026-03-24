# Quantitative Multi-Factor Equity Strategy

This project develops and backtests a systematic equity investment strategy using Momentum, Value, and Quality factors on a large universe of U.S. equities.

The model ranks stocks monthly, constructs a portfolio of the top signals, and evaluates performance using walk-forward backtesting to simulate realistic trading conditions.

---

## Strategy Overview

Factors used:
- Momentum (6-month return signal)
- Value (inverse price proxy)
- Quality (low volatility factor)

Portfolio construction:
- Top 10 stocks selected each month from the investment universe
- Risk-adjusted allocation using inverse volatility weighting
- Monthly rebalancing
- Transaction cost simulation included

---

## Results

Strategy Performance

Annual Return: **11.98%**  
Volatility: **13.16%**  
Sharpe Ratio: **0.91**

Market Benchmark

Annual Return: **7.96%**  
Sharpe Ratio: **0.79**

Result:
The strategy outperformed the market on a risk-adjusted basis.

---

## Factor Contribution

Quality: **8.39%**  
Momentum: **7.74%**  
Value: **1.04%**

This indicates the strategy is primarily driven by Quality and Momentum factors.

---

## Key Features

- Multi-factor investing model
- Portfolio optimization
- Transaction cost simulation
- Walk-forward backtesting
- Factor contribution analysis
- Benchmark comparison

---

## Tech Stack

Python  
Pandas  
NumPy  
Matplotlib  
Seaborn  

---

## Project Structure
