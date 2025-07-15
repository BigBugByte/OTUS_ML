import pandas as pd
import os

def simple_price_chart(ticker, days=30):
    """Простой ASCII график цены закрытия"""
    csv_file = f'data/{ticker}.csv'
    if not os.path.exists(csv_file):
        print(f'Нет данных для {ticker}')
        return
    
    df = pd.read_csv(csv_file, index_col='Date', parse_dates=True)
    
    # Берём последние N дней
    recent_data = df['Close'].tail(days)
    
    print(f'\n📈 Простой график цены {ticker} (последние {days} дней):')
    print('=' * 60)
    
    # Нормализуем данные для ASCII графика
    min_price = recent_data.min()
    max_price = recent_data.max()
    height = 20  # высота графика в символах
    
    for i, (date, price) in enumerate(recent_data.items()):
        # Нормализуем цену к высоте графика
        normalized = int((price - min_price) / (max_price - min_price) * height)
        
        # Создаём строку графика
        bar = '█' * normalized + '░' * (height - normalized)
        
        # Показываем только каждый 3-й день для читаемости
        if i % 3 == 0:
            date_str = date.strftime('%m-%d')
            print(f'{date_str} │{bar}│ ${price:.2f}')
    
    print('=' * 60)
    print(f'Диапазон: ${min_price:.2f} - ${max_price:.2f}')

def show_simple_charts(tickers):
    """Показывает простые ASCII графики для списка тикеров"""
    for ticker in tickers:
        simple_price_chart(ticker) 