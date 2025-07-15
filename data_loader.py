import yfinance as yf
import pandas as pd
import os
import ssl
import urllib.request

def download_data(specific_ticker=None):
    # Create data directory if not exists
    os.makedirs('data', exist_ok=True)
    
    # Default base assets for demonstration
    base_tickers = ['BTC-USD', 'AAPL']  # Bitcoin and Apple as defaults
    
    # If specific ticker is provided, add it to the list
    if specific_ticker:
        tickers_to_download = list(set(base_tickers + [specific_ticker.upper()]))
        print(f'Загружаем базовые активы ({", ".join(base_tickers)}) + запрошенный тикер ({specific_ticker.upper()})')
    else:
        tickers_to_download = base_tickers
        print(f'Загружаем базовые активы: {", ".join(base_tickers)}')
    
    all_tickers = tickers_to_download
    
    # Configure SSL to handle certificate issues
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    
    for ticker in all_tickers:
        try:
            data = yf.Ticker(ticker).history(period='1y')  # Use 1 year instead of 'max' for faster download
            if not data.empty:
                data.to_csv(f'data/{ticker}.csv')
                print(f'Downloaded data for {ticker}')
            else:
                print(f'No data for {ticker}')
        except Exception as e:
            print(f'Error downloading {ticker}: {e}')

if __name__ == '__main__':
    download_data() 