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
    def __init__ (self, TickerName:str, TickerNameFuture:str, log:object, future_date_contract:str = 'YYYY-MM-DD'):
        self.log = log
        self.TickerName = TickerName
        self.future_date_contract = future_date_contract
        self.TickerNameFuture = TickerNameFuture
        self.TickerInfo = self.get_ticker_info()
        self.future_price = self.get_future_value()['marketData']['LA']['price']
        self.spot_price = self.get_spot_value()
        self.bid_price = self.get_bid_value()
        self.ask_price = self.get_ask_value()
    
    def get_future_value(self) -> dict:
        self.log.info(f'Getting info from Rofex for {self.TickerNameFuture,}')
        return pyRofex.get_market_data(ticker=self.TickerNameFuture,
                                        entries=[pyRofex.MarketDataEntry.LAST])
    
    def get_ticker_info(self) -> dict:
        self.log.info(f'Getting info from Yfinance for {self.TickerName}')
        return yf.Ticker(self.TickerName).info

    def get_spot_value(self) -> float:
        self.log.info(f'{self.TickerName} Spot Value : {self.stock_info["regularMarketPrice"]} ')
        return self.stock_info['regularMarketPrice']

    def get_bid_value(self) -> float:
        self.log.info(f'{self.TickerName} Spot Value : {self.stock_info["bid"]} ')
        return self.stock_info['bid']

    def get_ask_value(self) -> float:
        self.log.info(f'{self.TickerName} Spot Value : {self.stock_info["ask"]} ')
        return self.stock_info['ask']