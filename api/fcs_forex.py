import requests # Library to handle HTTP requests

class FCSForex:
    def __init__(self, api_key=''):
        # Set the API key, defaulting to "API_KEY" if not provided
        self.api_key = api_key if api_key else "API_KEY"
        self.output = ''  # default is json
        self.output_type = 'JSON'  # Default output type JSON
        self.basic_url = "https://fcsapi.com/api-v3/forex"
        self.api_message = "API Key is empty, please set your API Key."


    def return_error(self, msg):
        # Returns a standardized error message in a dictionary format
        return {"status":False,"msg":msg,"Error":"Code or input data error"}
    

    def check_api_key(self):
        """Check if the API key is valid."""
        return self.api_key is not None and self.api_key != 'api_key'

    def check_symbol_id(self, txt):
        """Determine if the input is an ID or symbol."""
        cleaned_txt = txt.replace(",", "")  # Remove commas
        return 'id' if cleaned_txt.isdigit() else 'symbol'

    def response(self, url, params):
        """Make a request to the given URL and return the JSON response."""
        if not self.check_api_key():
            return self.return_error(self.api_message)
        
        if self.api_key:
            params['access_key'] = self.api_key
        if self.output:
            params['output'] = self.output

        response = requests.post(url, data=params)

        # Check if response is JSON
        try:
            response_data = response.json()
            return response_data  # Return JSON data without prettifying
        except ValueError:
            # If response is not JSON, return it as is
            return self.return_error(response.text)

    def get_symbols_list(self,type='forex'):
        """Return all symbols list of forex of ids and symbol."""
        if type != 'forex' and type != 'crypto':
            type = 'forex'
        params = {'type': type}
        link = f"{self.basic_url}/list"
        return self.response(link, params)

    def get_profile(self, symbol):
        """Get the details or profile of Currency."""
        symbol = ','.join(symbol) if isinstance(symbol, list) else symbol # convert [1,2,3] to 1,2,3

        if not symbol:
            return self.return_error("Symbol or Id not defined")

        symbol_id = self.check_symbol_id(symbol) #
        params = {symbol_id: symbol}

        link = f"{self.basic_url}/profile"
        return self.response(link, params)

    def get_converter(self, amount='200', pair_one='', pair_two=''):
        """Convert Base to quote currency."""
        if not pair_one:
            return self.return_error("Symbol not defined")

        params = {'amount': amount}

        if pair_two:
            params['pair1'] = pair_one
            params['pair2'] = pair_two
        else:
            params["symbol"] = pair_one

        link = f"{self.basic_url}/converter"
        return self.response(link, params)

    def get_latest_price(self, symbol):
        """Get Forex Latest Price By id or symbol."""
        symbol = ','.join(symbol) if isinstance(symbol, list) else symbol

        if not symbol:
            return self.return_error("Symbol or Id not defined")

        symbol_id = self.check_symbol_id(symbol)
        params = {symbol_id: symbol}

        link = f"{self.basic_url}/latest"
        return self.response(link, params)

    def get_base_prices(self, symbol, type="forex", time=False):
        """Get all quote prices."""
        symbol = ','.join(symbol) if isinstance(symbol, list) else symbol

        if not symbol:
            return self.return_error("Symbol or Id not defined")

        params = {'symbol': symbol, 'type': type}
        if time:
            params['time'] = 1

        link = f"{self.basic_url}/base_latest"
        return self.response(link, params)

    def get_last_candle(self, symbol, period='1h'):
        """Get Candle price by time period."""
        symbol = ','.join(symbol) if isinstance(symbol, list) else symbol

        if not symbol:
            return self.return_error("Symbol or Id not defined")

        symbol_id = self.check_symbol_id(symbol)
        params = {symbol_id: symbol, 'period': period}

        link = f"{self.basic_url}/candle"
        return self.response(link, params)

    def get_history(self, data):
        """Get specific currency history data."""
        id      = data.get('id', '')
        symbol  = data.get('symbol', '')

        period  = data.get('period', '1h')
        level   = data.get('level', 1)
        if (level < 1 or level > 3) : level = 1
   
        from_date = data.get('from', '')
        to_date = data.get('to', '')

        if not symbol and not id:
            return self.return_error("Symbol or Id not defined")

        params = {
            'period': period,
            'limit': level
        }
        if id: 
            params['id'] = id
        if symbol:
            params['symbol'] = symbol

        if from_date and to_date:
            params['from'] = from_date
            params['to'] = to_date

        link = f"{self.basic_url}/history"
        return self.response(link, params)

    def get_signal(self,symbol,period, url):
        if not symbol:
            return self.return_error("Symbol or Id not defined")

        result = False if isinstance(symbol, list) else False if ',' in symbol else True
        if result is not True: 
            return self.return_error("Symbol only accept single id")

        symbol_id = self.check_symbol_id(symbol)
        params = {symbol_id: symbol, 'period': period}

        link = f"{self.basic_url}/"+url
        return self.response(link, params)


    def get_pivot_points(self, symbol, period='1h'):
        """Get pivot points."""
        return self.get_signal(symbol,period,"pivot_points")

    def get_moving_averages(self, symbol, period='1h'):
        """Get moving averages forex."""
        return self.get_signal(symbol,period,"ma_avg")

    def get_technical_indicator(self, symbol, period='1h'):
        """Get top indicators signals."""
        return self.get_signal(symbol,period,"indicators")

    def get_economy_calendar(self, symbol='', country='', from_date='', to_date='', event=''):
        """Get economy calendar by symbol, country, date range, or event."""
        if not self.check_api_key():
            return self.return_error(self.api_message)

        # Prepare parameters based on the input
        params = {'access_key': self.api_key}
        if from_date:
            params['from'] = from_date
        if to_date:
            params['to'] = to_date
        if symbol:
            params['symbol'] = symbol
        if country:
            params['country'] = country
        if event:
            params['event'] = event  # Add event parameter

        # Validate that at least one of symbol, country, or event is provided
        if not symbol and not country and not event:
            return self.return_error("At least a symbol, country, or event must be defined")

        link = f"{self.basic_url}/economy_cal"
        return self.response(link, params)


    def get_search_query(self, search, strict=0):
        """Search API."""

        if not search:
            return self.return_error("Search value in empty")

        params = {'s': search, 'strict': strict}
        link = f"{self.basic_url}/search"
        return self.response(link, params)


    
