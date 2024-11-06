# fcs_forex/main.py
# Import FCS API Class
from fcs_forex import FCSForex

def main():

    # An API key, you can get free at https://fcsapi.com/dashboard
    forex_api = FCSForex(api_key='XxNTqX6UlRgDaIo3N24M') 

    latest_price = forex_api.get_latest_price("GBP/CHF")
    print("Latest Price of GBP/CHF :", latest_price)
     


"""
    Implementation of all methods are listed below:

    #Example: Get symbols list, Documentation : https://fcsapi.com/document/forex-api#forexsupportedcurrency
    symbols_list = forex_api.get_symbols_list()
    print("Symbols List:", symbols_list)

    # Example: Get profile of a currency
    symbol_profile = forex_api.get_profile('1')
    print("Currency Profile of your desired country :", symbol_profile)

    symbol_profile = forex_api.get_profile('EUR')
    print("Currency Profile BY IDS:", symbol_profile)

    # Example: Convert currency
    conversion_result = forex_api.get_converter(200,'JPY/GBP')
    print("Conversion Result :", conversion_result)

    conversion_result = forex_api.get_converter(200, 'EUR','USD')
    print("Conversion Result for different countries:", conversion_result)

    # Get Latest Price
    latest_price = forex_api.get_latest_price(['EUR/USD', 'USD/JPY', 'GBP/CHF'])
    print("Latest Price for all_forex :", latest_price)

    latest_price = forex_api.get_latest_price("JPY/GBP")
    print("Latest Price for different countries:", latest_price)

    latest_price = forex_api.get_latest_price(['EUR/USD','JPY/USD'])
    print("Latest Price for multiple countries:", latest_price)

    latest_price = forex_api.get_latest_price('87') 
    print("Latest Price by ID:", latest_price) 

    
    # Get Base Prices
    base_prices = forex_api.get_base_prices("USD")
    print("Base Prices for Different countries:", base_prices)

    base_prices = forex_api.get_base_prices('EUR','crypto')
    print("Base Prices for EUR and forex:", base_prices)

    # Get Last Candle
    last_candle = forex_api.get_last_candle('1,2,3','1d')
    print("Last Candle for EURUSD:", last_candle)

    last_candle = forex_api.get_last_candle("all_forex", '1h')
    print("Last Candle for EURUSD:", last_candle)

    last_candle = forex_api.get_last_candle("all_forex", '1d')
    print("Last Candle for EURUSD:", last_candle)

    last_candle = forex_api.get_last_candle("all_forex", '1d')
    print("Last Candle for EURUSD:", last_candle)

    candle_data = forex_api.get_last_candle("1,2,3", period='1h')
    print("Candle Data for IDs:", candle_data)


    # Get Currency History
    history_data = forex_api.get_history({
        'id': '10',
        'period': '1d',
        'level': 1,
        'from': '2024-10-30',
        'to': '2024-10-31'
    })
    print("History Data for countries:", history_data)

    history_data = forex_api.get_history({
    'id': '3',
    'period': '1h'
    })
    print("History Data for countries:", history_data)


    # Get Pivot Points

    pivot_points = forex_api.get_pivot_points("10", '1d')
    print("Pivot Points for EURUSD:", pivot_points)

    pivot_points = forex_api.get_pivot_points("EUR/USD", '1d')
    print("Pivot Points for countries:", pivot_points)

    pivot_points = forex_api.get_pivot_points("JPY/CHF", '1d')
    print("Pivot Points for countries:", pivot_points)


    # Get Moving Averages
    moving_averages = forex_api.get_moving_averages("10", '1d')
    print("Moving Averages for 1:", moving_averages)

    moving_averages = forex_api.get_moving_averages("JPY/CHF", '1d')
    print("Moving Averages for different countries:", moving_averages)


    # Get Technical Indicators
    indicators = forex_api.get_technical_indicator('10', '1d')
    print("Technical Indicators for id and symbol:", indicators)

    indicators = forex_api.get_technical_indicator("JPY/CHF", period='1d')
    print("Technical Indicators for countries code:", indicators)

    #Get Economy Calendar
    economy_calendar = forex_api.get_economy_calendar(country='US,JP', from_date='2024-11-04', to_date='2024-11-05')
    print("Economy Calendar for countries  :", economy_calendar)

    economy_calendar_event = forex_api.get_economy_calendar(event='365014')
    print("Economy Calendar (Event):", economy_calendar_event)

    economy_calendar_range = forex_api.get_economy_calendar(from_date='2024-11-04', to_date='2024-11-05')
    print("Economy Calendar (Date Range with Symbol):", economy_calendar_range)

    economy_calendar = forex_api.get_economy_calendar(country='US')
    print("Economy Calendar for countries  :", economy_calendar)

    # Search API
    search_results = forex_api.get_search_query("BTC")
    print("Search Results: ", search_results)
"""


    

if __name__ == "__main__":
    main()