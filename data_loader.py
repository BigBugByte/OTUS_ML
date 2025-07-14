import yfinance as yf
import pandas as pd
import os

def download_data():
    # Create data directory if not exists
    os.makedirs('data', exist_ok=True)
    
    # Get S&P500 tickers
    sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500 = pd.read_html(sp500_url)[0]['Symbol'].tolist()
    
    # Crypto tickers
    cryptos = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'XRP-USD']
    
    # All tickers
    all_tickers = sp500 + cryptos
    
    for ticker in all_tickers:
        try:
            data = yf.Ticker(ticker).history(period='max')
            if not data.empty:
                data.to_csv(f'data/{ticker}.csv')
                print(f'Downloaded data for {ticker}')
            else:
                print(f'No data for {ticker}')
        except Exception as e:
            print(f'Error downloading {ticker}: {e}')

if __name__ == '__main__':
    download_data() 