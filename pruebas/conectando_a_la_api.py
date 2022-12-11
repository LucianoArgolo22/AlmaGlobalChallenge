#%%
import time
import yfinance as yf
import pyRofex
import datetime
from ClientLogger import ClientLogger

user = 'lucianoagustinargolo7681'
password = 'zoeqhH5!'
account = 'REM7681'
# Set the the parameter for the REMARKET environment
pyRofex.initialize(user=user,
                   password=password,
                   account=account,
                   environment=pyRofex.Environment.REMARKET)

class FinanceValues:
    def __init__ (self, TickerName:str, TickerNameFuture:str, future_date_contract:str = 'YYYY-MM-DD'):
        self.TickerName = TickerName
        self.future_date_contract = future_date_contract
        self.TickerNameFuture = TickerNameFuture
        self.TickerInfo = self.get_ticker_info()
        self.future_price = self.get_future_value()['marketData']['LA']['price']
        self.spot_price = self.get_spot_value()
        self.bid_price = self.get_bid_value()
        self.ask_price = self.get_ask_value()
    
    def get_future_value(self) -> dict:
        return pyRofex.get_market_data(ticker=self.TickerNameFuture,
                                        entries=[pyRofex.MarketDataEntry.LAST])
    
    def get_ticker_info(self) -> dict:
        return yf.Ticker(self.TickerName).info

    def get_spot_value(self) -> float:
        return self.TickerInfo['regularMarketPrice']

    def get_bid_value(self) -> float:
        return self.TickerInfo['bid']

    def get_ask_value(self) -> float:
        return self.TickerInfo['ask']

class Metrics:
    def __init__(self, finance_object:FinanceValues):
        self.object = finance_object

    def implicit_yearly_rate(self) -> float:
        future_price_date = datetime.datetime.strptime(self.object.future_date_contract ,"%Y-%m-%d")
        now = datetime.datetime.now()
        days = (future_price_date - now).days
        return ( (self.object.future_price/self.object.spot_price)**(days/360) - 1) * 100

    def get_implicit_taker_rate(self) -> float:
        pass

    def get_implicit_maker_rate(self) -> float:
        pass

class TaskHandler:
    def __init__(self):
        self.implicit_taker_value = ''
        self.implicit_maker_value = ''
    
    @staticmethod
    def compare_values(previous_value , new_value) -> float: 
        return previous_value != new_value

    def implicit_maker_setter(self, new_value) -> None:
        if TaskHandler.compare_values(previous_value=self.implicit_maker_value, \
                                    new_value=new_value):
            self.implicit_maker_value = new_value                          

    def implicit_taker_setter(self, new_value) -> None:
        if TaskHandler.compare_values(previous_value=self.implicit_taker_value, \
                                    new_value=new_value):
            self.implicit_taker_value = new_value      

# %%
#job
log = ClientLogger(filename='./app_prueba.log', app_name='FinanceBot') 
while True:    
    finance_object = FinanceValues(TickerName='DLR', TickerNameFuture='DLR/MAR23', future_date_contract='2023-03-31', log=log)
    metrics_object = Metrics(finance_object=finance_object, log=log)
    last_value = metrics_object.implicit_yearly_rate()
    
    time.sleep(10)