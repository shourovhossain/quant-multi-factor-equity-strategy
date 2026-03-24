# src/data_loader.py
import pandas as pd

def load_data(path="data/all_stocks_5yr.csv"):
    """
    Load stock data and pivot it into a clean price matrix.
    """
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    prices = df.pivot(index='date', columns='Name', values='close').sort_index()
    prices = prices[~prices.index.duplicated(keep='first')]
    prices = prices.dropna(axis=1, thresh=1000)  # remove incomplete tickers
    return prices

def calculate_monthly_returns(prices):
    monthly_prices = prices.resample('M').last()
    monthly_returns = monthly_prices.pct_change().dropna()
    return monthly_returns
# src/factors.py
import pandas as pd

def calculate_factors(prices, monthly_returns):
    """
    Calculate Momentum, Value, and Quality factors.
    """
    # Momentum (6-month rolling return)
    momentum = (1 + monthly_returns).rolling(6).apply(lambda x: x.prod() - 1).shift(1)
    
    # Value (inverse lagged price)
    value = 1 / prices.shift(1)
    
    # Quality (negative 12-month rolling volatility)
    quality = -monthly_returns.rolling(12).std()
    
    return momentum, value, quality

# src/portfolio.py
import pandas as pd
import numpy as np

def long_short_factor(factor, returns, quantile=0.2):
    """
    Calculate long-short factor returns.
    """
    ls_returns = []
    for date in factor.index:
        scores = factor.loc[date].dropna()
        if len(scores) == 0:
            ls_returns.append(np.nan)
            continue

        q_low = scores.quantile(quantile)
        q_high = scores.quantile(1 - quantile)

        long = scores[scores >= q_high].index
        short = scores[scores <= q_low].index

        if date in returns.index:
            r = returns.loc[date]
            ls_returns.append(r[long].mean() - r[short].mean())
        else:
            ls_returns.append(np.nan)

    return pd.Series(ls_returns, index=factor.index)

def multi_factor_portfolio(factors):
    """
    Combine multiple factor portfolios by averaging.
    """
    return factors.mean(axis=1)

# src/backtest.py
import numpy as np
import pandas as pd

def performance_summary(returns):
    """
    Compute key metrics: Annual Return, Volatility, Sharpe, Max Drawdown.
    """
    annual_return = returns.mean() * 12
    volatility = returns.std() * np.sqrt(12)
    sharpe_ratio = annual_return / volatility
    cumulative = returns.cumsum()
    max_drawdown = (cumulative - cumulative.cummax()).min()
    
    # Annual returns by year
    annual_returns = returns.resample("Y").sum()
    best_year = annual_returns.max()
    worst_year = annual_returns.min()
    
    # Last 12-month rolling Sharpe & Volatility
    rolling_sharpe = returns.rolling(12).apply(lambda x: np.sqrt(12) * x.mean() / x.std()).dropna()
    rolling_vol = returns.rolling(12).std().dropna()
    
    return {
        "annual_return": annual_return,
        "volatility": volatility,
        "sharpe": sharpe_ratio,
        "max_drawdown": max_drawdown,
        "best_year": best_year,
        "worst_year": worst_year,
        "annual_returns_by_year": annual_returns,
        "rolling_sharpe": rolling_sharpe,
        "rolling_vol": rolling_vol
    }

# src/plots.py
import matplotlib.pyplot as plt

def plot_equity_curve(cumulative_returns, title="Equity Curve"):
    plt.figure(figsize=(10,5))
    plt.plot(cumulative_returns, label="Strategy")
    plt.plot(cumulative_returns.cumsum().mean() * cumulative_returns.index.to_series().dt.year, label="Benchmark", linestyle="--")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_factor_contributions(factor_contributions):
    factor_contributions.plot(kind='bar', figsize=(6,4), title="Factor Contribution (Annual Return)")
    plt.ylabel("Annual Return")
    plt.show()

