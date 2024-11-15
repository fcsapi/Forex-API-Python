# Forex API Python

**Last Updated**: 2024-11-06 (Version 3)

The most complete forex API python solution for accessing currency quotes and economic calendar. Get JSON responses for real-time rates, historical data, and technical indicators.

This python forex API  library provides comprehensive access to market data with the following features:

## Features

- Provides access to over 2,000 currency exchange rates
- Updates currency rates every 10 seconds
- Offers 25 years of historical data
- Contains moving averages (MA) and indicator signals
- Includes an economic calendar with worldwide event data

## Requirements

- Python >= Python 3.13.0
- FCS [API key](https://fcsapi.com/dashboard)

## Installation

Clone the repository and install any dependencies listed in `requirements.txt`:

```bash
git clone https://github.com/fcsapi/Forex-API-Python.git
cd FCS_Forex
pip install -r requirements.txt
```

## Getting Started with forex API python

### Setting up
1. Get your API key from the [FCS API Dashboard](https://fcsapi.com/dashboard).
2. Update the `api_key` parameter when initializing the `FCSForex` class in `main.py`, or pass it directly to the class instance.

```python
from fcs_forex import FCSForex

# Initialize with your API key
forex_api = FCSForex(api_key='YOUR_API_KEY')

latest_price = forex_api.get_latest_price("GBP/CHF")
print("Latest Price of GBP/CHF :", latest_price)
```
## API Response Format
The default response format is JSON.

```python
OIUTPUT: 
{
  "status": true,
  "code": 200,
  "msg": "Successfully",
  "response": [
    {
      "id": "41",
      "o": "1.11997",
      "h": "1.12864",
      "l": "1.12201",
      "c": "1.12425",
      "a": "1.12447",
      "b": "1.12403",
      "sp": "4.4",
      "ch": "+0.00428",
      "cp": "+0.38%",
      "t": "1730874177",
      "s": "GBP/CHF",
      "tm": "2024-11-06 06:22:57"
    }
  ],
  "info": {
    "server_time": "2024-11-06 06:23:41 UTC",
    "credit_count": 1
  }
}
```

## Complete Forex API Python Methods

1. **Fetch Symbols List**  

   Get a list of available forex or crypto symbols.
   ```python
   symbols_list = forex_api.get_symbols_list()

2. **Get Latest Price**

   Retrieve the latest pricing for designated currency pairs or by their ID. If you wish to see the latest prices for all forex currencies, simply use "all_forex" as the symbol.

   ```python
   latest_price = forex_api.get_latest_price(['EUR/USD', 'USD/JPY', 'GBP/CHF'])
   latest_price = forex_api.get_latest_price('20') 
   latest_price = forex_api.get_latest_price("all_forex")

   RESPONSE:
   {
    "id": "20",
    "o": "151.613",
    "h": "154.343",
    "l": "151.297",
    "c": "153.883",
    "a": "153.894",
    "b": "153.883",
    "sp": "1.1",
    "ch": "+2.27",
    "cp": "+1.5%",
    "t": "1730873696",
    "s": "USD/JPY",
    "tm": "2024-11-06 06:14:56"
   }
   ```

3. **Currency Conversion**

    Convert a currency to a different one. For example, you can convert 200 EUR into USD, or perform the conversion using combined currency symbols differenciate by '/'.

    ```python
    conversion_result = forex_api.get_converter(200, 'EUR', 'USD')
    conversion_result = forex_api.get_converter(200,'JPY/GBP')

    RESPONSE:
    { 
    "price_1x_EUR": "1.0212418", // 1 EUR = USD 
    "price_1x_USD": "0.9792", // 1 USD = EUR 
    "total": "195.84" // Total Price x amount (Amount * 1 USD) = Total (USD) 
    }, 
    ```

4. **Retrieve Currency Profile**

    Access information for specific currencies through either their symbols or IDs.

    ```python
    profile = forex_api.get_profile('EUR')
    profile = forex_api.get_profile('EUR,USD,JPY')
    profile = forex_api.get_profile('1,2,3')

    RESPONSE:
    {  
    "short_name" : "EUR", 
    "name" : "Euro", 
    "country" : "Belgium", 
    "code_n" : "978", 
    "subunit" : "cent", 
    "website" : "ecb.europa.eu", 
    "symbol" : "€", 
    "bank" : "European Central Bank", 
    "banknotes" : '€5, €10, €20, €50, €100'
    "coins" : '1c, 2c, 5c, 10c, 20c, 50c, €1, €2'
    "icon" : "https://fcsapi.com/assets/images/flags/eur.svg", 
    "type" : "forex", 
    }, {and more} 
    ```

5. **Fetch Base Prices**

    Get all quote prices for a specified base currency and you can also specify the type = {forex OR crypto} => default: forex

    ```python
    base_prices = forex_api.get_base_prices('EUR')
    base_prices = forex_api.get_base_prices('EUR','crypto')
    ```

6. **Retrieve Historical Candle Data**

    Access historical OHLC (Open, High, Low, Close) data using designated currency pairs or IDs, and we can additionally view all current prices of forex currencies within a specific timeframe.

    ```python
    last_candle = forex_api.get_last_candle('EUR/USD', '1d')
    last_candle = forex_api.get_last_candle("all_forex", '1h')
    last_candle = forex_api.get_last_candle('1,2,3','1d')
    ```

7. **Access Historical Data**

    Retrieve historical forex data for a specific time period.

    ```python
    history_data = forex_api.get_history({
        'symbol': 'EUR/USD',
        'period': '1d',
        'from': '2024-10-01',
        'to': '2024-10-31'
    })

     history_data = forex_api.get_history({
        'id': '3',
        'period': '1h'
    })
    ```

8. **Technical Indicators**

    Fetch moving averages, pivot points, and other top indicators.

    ```python
    moving_averages = forex_api.get_moving_averages('EUR/USD', '1d')
    pivot_points    = forex_api.get_pivot_points('EUR/USD', '1d')
    indicators      = forex_api.get_technical_indicator('EUR/USD', '1d')
    ```

9. **Economic Calendar**

    Get economic events that fall within a specified date range, whether by currency, country, event type, or any particular timeframe.

    ```python
    economy_calendar_event = forex_api.get_economy_calendar(symbol='USD', from_date='2024-11-01', to_date='2024-11-05')
    economy_calendar_event = forex_api.get_economy_calendar(event='365014')
    economy_calendar_event = forex_api.get_economy_calendar(from_date='2024-11-04', to_date='2024-11-05')
    economy_calendar_event = forex_api.get_economy_calendar(country='US')
    ```

10. **Search for Forex Symbols**

    Search for forex symbols by keyword or filter criteria, with options to set strict:

- **strict = {0,1}**
     - **0**: Search if any keyword exists
     - **1**: Search only if all keywords exist

    ```python
    search_results = forex_api.get_search_query('BTC')
    search_results = forex_api.get_search_query("BTC Dollar",1)
    search_results = forex_api.get_search_query("BTC Dollar",0)
    ```

This forex API for python implementation supports additional features through our WebSocket API for real-time data.

## Other Resources

- **WebSocket API for Real-Time Prices:** [View Documentation](https://fcsapi.com/document/socket-api)
- **PHP Library:** [Available on GitHub](https://github.com/fcsapi/Forex-API-PHP/tree/master?)
- **Node JS Library:** [Available on GitHub](https://github.com/fcsapi/forex-api-node-js/)

## Support

For support, please contact us at [support@fcsapi.com](mailto:support@fcsapi.com) or use the [live chat](https://fcsapi.com/)

## License

This project comes with the MIT License. Please check the LICENSE file for more information.