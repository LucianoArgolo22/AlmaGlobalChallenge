import datetime

class Metrics:
    def __init__(self, finance_object:object, log:object):
        self.log = log
        self.object = finance_object

    def implicit_yearly_rate(self) -> float:
        future_price_date = datetime.datetime.strptime(self.object.future_date_contract ,"%Y-%m-%d")
        now = datetime.datetime.now()
        days = (future_price_date - now).days
        rate =  ( (self.object.future_price/self.object.spot_price)**(days/360) - 1) * 100
        self.log.info(f'Implicit Yearly rate: {rate}')
        return rate

    def get_implicit_taker_rate(self) -> float:
        pass

    def get_implicit_maker_rate(self) -> float:
        pass
