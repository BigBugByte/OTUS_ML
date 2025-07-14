import pandas as pd
import os
from scipy import stats
import numpy as np
import sys

def analyze_ticker(ticker):
    file_path = f'data/{ticker}.csv'
    if not os.path.exists(file_path):
        print(f'No data file for {ticker}')
        return
    
    df = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    
    print(f'Analysis for {ticker}:')
    
    # Check for missing values
    missing = df.isnull().sum()
    print('Missing values:\n', missing)
    
    # Basic statistics
    print('\nDescriptive statistics:\n', df.describe())
    
    # Check for outliers using Z-score
    z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
    outliers = (z_scores > 3).any(axis=1)
    print('\nNumber of potential outliers:', outliers.sum())
    print('Sample outliers:\n', df[outliers].head())
    
    # Assessment: In financial data, 'outliers' might be real events like market crashes or booms.
    print('\nNote: In financial time series, apparent outliers are often real market events and should be retained unless proven erroneous.')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        analyze_ticker(sys.argv[1])
    else:
        print('Please provide a ticker symbol.') 