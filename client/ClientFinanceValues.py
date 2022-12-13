import yfinance as yf
import pyRofex
user = 'lucianoagustinargolo7681'
password = 'zoeqhH5!'
account = 'REM7681'
# Set the the parameter for the REMARKET environment
pyRofex.initialize(user=user,
                   password=password,
                   account=account,
                   environment=pyRofex.Environment.REMARKET)


class FinanceValues:
    """
    Class that generates an object that gets all Financial information needed
    """
    def __init__ (self, TickerName:str, TickerNameFuture:str, log:object, future_date_contract:str = 'YYYY-MM-DD'):
        self.log = log
        self.TickerName = TickerName
        self.future_date_contract = future_date_contract
        self.TickerNameFuture = TickerNameFuture
        self.TickerInfo = self.get_ticker_info()
        self.future_price = self.get_future_value()['marketData']['LA']['price']
    
    def get_future_value(self) -> dict:
        self.log.info(f'Getting info from Rofex for {self.TickerNameFuture}')
        return pyRofex.get_market_data(ticker=self.TickerNameFuture,
                                        entries=[pyRofex.MarketDataEntry.LAST])
    
    def get_ticker_info(self) -> dict:
        self.log.info(f'Getting info from Yfinance for {self.TickerName}')
        return yf.Ticker(self.TickerName).info
