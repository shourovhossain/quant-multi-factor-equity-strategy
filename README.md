# Quantitative Multi-Factor Equity Strategy

This project develops and backtests a systematic equity investment strategy using Momentum, Value, and Quality factors.

The model ranks stocks monthly, constructs a portfolio of the top signals, and evaluates performance using walk-forward backtesting.

## Strategy Overview

Factors used:
- Momentum
- Value
- Quality

Portfolio construction:
- Top 10 stocks selected each month
- Risk-adjusted allocation using inverse volatility weighting
- Walk-forward simulation

## Results

Strategy Performance:

Annual Return: 11.98%  
Volatility: 13.16%  
Sharpe Ratio: 0.91  

Market Benchmark:

Annual Return: 7.96%  
Sharpe Ratio: 0.79  

The strategy outperformed the market on a risk-adjusted basis.

## Key Features

- Multi-factor investing model
- Portfolio optimization
- Transaction cost simulation
- Walk-forward backtesting
- Factor contribution analysis
- Benchmark comparison

## Tech Stack

Python  
Pandas  
NumPy  
Matplotlib  
Seaborn

## Project Structure
