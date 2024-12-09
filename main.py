import data_download as dd
import data_plotting as dplt
import dates_check as dcheck
import data_calculate as dc
import data_save as ds


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    #print("Заданы процент колебаний: от 0 до 100")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = period_choice()
    #threshold = input("Введите заданный процент колебаний (например, '5.23' для 5.23 процентов): ")
    #filename = input("Введите имя файла для сохранения данных: ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Сalculate the average
    #dc.calculate_and_display_average_price(stock_data)

    # Checking for exceeding the threshold
    #dc.notify_if_strong_fluctuations(stock_data, threshold)

    # Export data to file
    #ds.export_data_to_csv(stock_data, filename)

    # Creat data with RSI
    rsi_data = dd.data_for_RSI_calculate(stock_data)

    # Return company name by ticker
    name = dd.name_return(ticker)

    # Plot RSI
    dplt.RSI_plot(rsi_data, period, ticker, name)


def period_choice():
    ''' Функция определения периода для данных '''
    index = input("выберите способ определения временного периода. PP для предустановленых периодов или DP для вабора периода по датам: ")
    ''' Выбор способа определения периода '''
    if index == 'PP':
        print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")
        period_temp = input("Введите период для данных (например, '1mo' для одного месяца): ")
        ''' Ввод предустановленного периода  '''
        period = [index, period_temp]
        ''' Формирование данных по предустановленноу периоду '''
    elif index == 'DP':
        print("Укажите первую и вторую даты в формате гггг-мм-дд (например 2005-04-22)")
        period1_temp = input("Введите дату начала периода: ")
        period1_temp = dcheck.dates_rechandge(period1_temp)
        ''' Ввод первой даты '''
        period2_temp = input("Введите дату окончания периода: ")
        period2_temp = dcheck.dates_rechandge(period2_temp)
        period_temp = dcheck.dates_order(period1_temp, period2_temp)
        ''' Ввод второй даты '''
        period = ['DP', (f'{period_temp[0][0]}-{period_temp[0][1]}-{period_temp[0][2]}'),
                        (f'{period_temp[1][0]}-{period_temp[1][1]}-{period_temp[1][2]}')]
        ''' Формирование данных по датам '''
    else:
        period = ['DD', '1mo']
        ''' Формирование данных по умолчанию '''
    return period


if __name__ == "__main__":
    main()



