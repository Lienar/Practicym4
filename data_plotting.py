import matplotlib.pyplot as plt
import pandas as pd
import data_save as ds

def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    file_data = ds.file_name_creator(filename, period, ticker, 'Default')

    plt.savefig(file_data[0])
    print(f"График сохранен как {file_data[0]}")

def RSI_plot(data, period, ticker, name, filename=None):
    ''' Функция создания файла с графиком RSI по заданным значениям '''
    plt.figure(figsize=(24, 12))
    plt.rcParams.update({'font.size': 22})
    ''' Настройка окна графика и шрифа в нем '''
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['rsi'].values, label='RSI индекс')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['rsi'], label='RSI индекс')
    ''' Отрисовка графика по дате и значениям RSI '''
    plt.title(f"RSI {name} ({ticker}) с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("RSI индекс")
    plt.grid()
    plt.legend()
    ''' Отрисовка информации по графику '''
    file_data = ds.file_name_creator(filename, period, ticker, 'RSI')
    ''' Определение имени сохраняемого файла '''
    plt.savefig(file_data[0])
    ''' Сохранение графика '''
    print(f"График сохранен в {file_data[1]} имя файла {file_data[2]}")
    ''' Сообщение о создание файла с его данными '''