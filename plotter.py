import yfinance as yf
import pandas as pd
from mplchart.chart import Chart
from mplchart.primitives import Candlesticks, Volume
from mplchart.indicators import SMA, EMA, RSI, MACD
import matplotlib.pyplot as plt
import sys
import os

def plot_ticker(ticker, period='1y', max_bars=250, save_to_file=True, show_window=False):
    """
    Создаёт график для тикера
    
    Args:
        ticker: символ тикера
        period: период данных 
        max_bars: максимальное количество баров
        save_to_file: сохранить в файл (True/False)
        show_window: показать в окне (True/False)
    """
    # Попробуем загрузить из файла, если есть
    csv_file = f'data/{ticker}.csv'
    if os.path.exists(csv_file):
        prices = pd.read_csv(csv_file, index_col='Date', parse_dates=True)
        print(f'Загружен {ticker} из локального файла')
    else:
        prices = yf.Ticker(ticker).history(period=period)
        print(f'Загружен {ticker} через API')
    
    if prices.empty:
        print(f'Нет данных для {ticker}')
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
    
    chart = Chart(title=f'{ticker} - Financial Chart', max_bars=max_bars)
    chart.plot(prices, indicators)
    
    if save_to_file:
        # Сохраняем в файл
        os.makedirs('charts', exist_ok=True)
        filename = f'charts/{ticker}_chart.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f'📊 График сохранён: {filename}')
    
    if show_window:
        chart.show()
    else:
        plt.close()

def plot_multiple_tickers(tickers, period='1y', max_bars=250, save_to_file=True, show_window=False):
    """Создаёт графики для нескольких тикеров"""
    print(f'Создаём графики для: {", ".join(tickers)}')
    
    for ticker in tickers:
        print(f'\n--- Обработка {ticker} ---')
        plot_ticker(ticker, period, max_bars, save_to_file, show_window)
    
    if save_to_file:
        print(f'\n✅ Все графики сохранены в папке charts/')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        plot_ticker(sys.argv[1])
    else:
        print('Please provide a ticker symbol.') 