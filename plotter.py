import yfinance as yf
import pandas as pd
from mplchart.chart import Chart
from mplchart.primitives import Candlesticks, Volume
from mplchart.indicators import SMA, EMA, RSI, MACD
import sys

def plot_ticker(ticker, period='1y', max_bars=250):
    prices = yf.Ticker(ticker).history(period=period)
    if prices.empty:
        print(f'No data for {ticker}')
        return
    
    indicators = [
        Candlesticks(),
        Volume(),
        SMA(50),
        EMA(20),
        SMA(200),
        RSI(),
        MACD(),
    ]
    
    chart = Chart(title=ticker, max_bars=max_bars)
    chart.plot(prices, indicators)
    chart.show()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        plot_ticker(sys.argv[1])
    else:
        print('Please provide a ticker symbol.') 