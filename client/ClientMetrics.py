import datetime

class Metrics:
    """
    Metrics class receives an FinanceValue object for begin 
    and then it start doing calculations with the information inside the 
    FinanceValue object
    """
    def __init__(self, finance_object:object, log:object):
        self.log = log
        self.object = finance_object

    def implicit_yearly_rate(self, value:str) -> float:
        future_price_date = datetime.datetime.strptime(self.object.future_date_contract ,"%Y-%m-%d")
        now = datetime.datetime.now()
        days = (future_price_date - now).days
        rate =  ( (self.object.future_price/self.object.TickerInfo[value])**(360/days) - 1) * 100
        self.log.info(f'Implicit Yearly rate: {rate}')
        return rate

    def get_implicit_rate(self) -> float:
        implicit_rate = self.implicit_yearly_rate(value = "regularMarketPrice" )
        self.log.info(f'Implicit Spot Yearly rate: {implicit_rate}')
        return implicit_rate


    
    # def get_implicit_taker_rate(self) -> float:
    #     implicit_taker_rate = self.implicit_yearly_rate(value = "ask" )
    #     self.log.info(f'Implicit Taker Yearly rate: {implicit_taker_rate}')
    #     return implicit_taker_rate

    # def get_implicit_maker_rate(self) -> float:
    #     implicit_maker_rate = self.implicit_yearly_rate(value = "bid" )
    #     self.log.info(f'Implicit Maker Yearly rate: {implicit_maker_rate}')
    #     return implicit_maker_rate

    @staticmethod
    def arbitration_chance(value1, value2):
        return True

