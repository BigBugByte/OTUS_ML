# First HW - Financial Data Processing

This project is for the first homework assignment in ML course, focusing on collecting, processing, and visualizing financial data.

## 📋 Project Overview

The project demonstrates:
- **Data Collection**: Downloading financial data via Yahoo Finance API
- **Data Processing**: Cleaning and analyzing stock/crypto data
- **Data Visualization**: Creating charts with technical indicators
- **Data Analysis**: Statistical analysis and outlier detection

## 🎯 Features

- Downloads stock and cryptocurrency data automatically
- Supports multiple visualization modes:
  - PNG files with technical indicators (SMA, EMA, RSI, MACD)
  - ASCII charts in terminal
  - Interactive charts in separate windows
- Performs data quality analysis (missing values, outliers)
- Caches data locally for faster subsequent runs

## 🔧 Requirements

- Python 3.7+
- Internet connection (for data download)
- Operating System: macOS, Linux, or Windows

## 🚀 Quick Start

### Option 1: Easy Setup (Recommended)
```bash
# Make script executable and run
chmod +x run.sh
./run.sh
```

### Option 2: Manual Setup
1. Create virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # Or on Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the project:
   ```bash
   python main.py
   ```

## 📊 Usage Examples

When you run the project, you'll be prompted to:
1. **Choose additional stock**: Base assets (AAPL, BTC-USD) are loaded by default
2. **Select visualization mode**: PNG files, ASCII charts, or interactive windows

Example interaction:
```
Базовые активы для загрузки: AAPL (Apple) и BTC-USD (Bitcoin)
Вы можете добавить третью акцию к анализу.
Введите тикер дополнительной акции (например, MSFT, GOOGL, TSLA) или нажмите Enter для пропуска: TSLA

Выберите тип отображения графиков:
1. Сохранить в файлы PNG (по умолчанию)
2. Простые ASCII графики в консоли
3. Открыть в отдельных окнах
Ваш выбор (1-3): 1
```

## 🗂️ Project Structure

```
first hw/
├── main.py              # Main entry point
├── data_loader.py       # Data download functionality
├── plotter.py          # Chart creation with technical indicators
├── analyzer.py         # Data analysis and statistics
├── simple_plotter.py   # ASCII chart creation
├── requirements.txt    # Python dependencies
├── run.sh             # Quick start script
├── README.md          # This file
├── LICENSE            # MIT License
└── materials/         # Course materials
```

## 🔍 Individual Components

You can also run components separately:

```bash
# Download data only
python data_loader.py

# Create chart for specific ticker
python plotter.py AAPL

# Analyze specific ticker data
python analyzer.py BTC-USD
```

## 📈 Supported Assets

- **Stocks**: Any ticker from Yahoo Finance (AAPL, MSFT, GOOGL, TSLA, etc.)
- **Crypto**: Bitcoin (BTC-USD), Ethereum (ETH-USD), and others

## 🛠️ Technical Details

- **Data Source**: Yahoo Finance API via `yfinance`
- **Visualization**: `matplotlib` and `mplchart` for advanced charts
- **Analysis**: `pandas` for data manipulation, `scipy` for statistics
- **Caching**: Data automatically saved to `data/` folder as CSV files

## 📄 License

MIT License - see LICENSE file for details.

## 🎓 Course Information

This project fulfills the requirements for ML course homework #1, demonstrating:
1. Git repository creation and management
2. Data collection from external APIs
3. Data visualization and analysis
4. Code organization and documentation 