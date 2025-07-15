import sys
import os
import subprocess

import data_loader
import plotter
import analyzer
import simple_plotter

def run_project(example_ticker='AAPL', chart_type='file'):
    try:
        # Пункт 1: Git-репозиторий
        print('Пункт 1: Создание git-репозитория.')
        print('Репозиторий уже инициализирован. Проверяем статус...')
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception('Ошибка: Git не инициализирован или проблема с репозиторием.')
        print(result.stdout)
        print('Пункт 1 выполнен успешно.\n')

        # Пункт 2: Файл лицензии
        print('Пункт 2: Добавление файла лицензии.')
        if not os.path.exists('LICENSE'):
            raise Exception('Ошибка: Файл LICENSE не найден.')
        print('Файл LICENSE существует. Содержимое:')
        with open('LICENSE', 'r') as f:
            print(f.read())
        print('Пункт 2 выполнен успешно.\n')

        # Пункт 3: Загрузка данных
        print('Пункт 3: Загрузка данных для базовых активов и дополнительного тикера.')
        print('Запускаем загрузку...')
        data_loader.download_data(example_ticker)
        print('Пункт 3 выполнен успешно.\n')

        # Пункт 4: Автоматическое отображение графиков
        print(f'Пункт 4: Автоматическое отображение графиков.')
        
        # Определяем какие тикеры были загружены
        base_tickers = ['BTC-USD', 'AAPL']
        if example_ticker and example_ticker.upper() not in [t.upper() for t in base_tickers]:
            all_tickers = base_tickers + [example_ticker.upper()]
        else:
            all_tickers = base_tickers
        
        if chart_type == 'ascii':
            print('Создаём простые ASCII графики в консоли...')
            simple_plotter.show_simple_charts(all_tickers)
            print('Пункт 4 выполнен успешно (ASCII графики показаны).\n')
        elif chart_type == 'window':
            print('Создаём графики в отдельных окнах...')
            plotter.plot_multiple_tickers(all_tickers, save_to_file=False, show_window=True)
            print('Пункт 4 выполнен успешно (графики показаны в окнах).\n')
        else:  # chart_type == 'file'
            print('Создаём графики и сохраняем в файлы...')
            plotter.plot_multiple_tickers(all_tickers, save_to_file=True, show_window=False)
            print('Пункт 4 выполнен успешно (графики сохранены в файлы).\n')

        # Пункт 5: Проверка данных на пропуски, ошибки и выбросы
        analysis_ticker = example_ticker if example_ticker else 'AAPL'
        print(f'Пункт 5: Анализ данных для тикера {analysis_ticker}.')
        analyzer.analyze_ticker(analysis_ticker)
        print('Пункт 5 выполнен успешно.\n')

        print('Все пункты задания выполнены успешно!')
    except Exception as e:
        print(f'Ошибка во время выполнения: {str(e)}')
        print('Процесс прерван.')
        sys.exit(1)

if __name__ == '__main__':
    print('Базовые активы для загрузки: AAPL (Apple) и BTC-USD (Bitcoin)')
    print('Вы можете добавить третью акцию к анализу.')
    ticker = input('Введите тикер дополнительной акции (например, MSFT, GOOGL, TSLA) или нажмите Enter для пропуска: ') or None
    
    print('\nВыберите тип отображения графиков:')
    print('1. Сохранить в файлы PNG (по умолчанию)')
    print('2. Простые ASCII графики в консоли') 
    print('3. Открыть в отдельных окнах')
    
    chart_choice = input('Ваш выбор (1-3): ') or '1'
    
    chart_types = {'1': 'file', '2': 'ascii', '3': 'window'}
    chart_type = chart_types.get(chart_choice, 'file')
    
    run_project(ticker, chart_type) 