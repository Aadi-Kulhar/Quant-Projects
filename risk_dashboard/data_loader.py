import yfinance as yf
import pandas as pd

def get_stock_returns(ticker='AAPL', period='1y'):
    data = yf.download(ticker, period=period)
    data['Returns'] = data['Adj Close'].pct_change().dropna()
    return data.dropna()
